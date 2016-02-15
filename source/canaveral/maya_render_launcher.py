import os
import sys
import subprocess

import PySide.QtGui as QtGui

import canaveral.ui.canaveral_maya_deadline_ui as maya_deadline
import canaveral.get_proj_apps as proj_app_info
import canaveral.launch_app as launch_app


class MayaRenderLauncher(maya_deadline.Ui_deadline_launch_win, QtGui.QMainWindow):
    def __init__(self):
        super(MayaRenderLauncher, self).__init__()
        self.setupUi(self)

        self.master_app_dict = {}

        self.launch_btn.clicked.connect(self.build_deadline_cmd)
        self.close_btn.clicked.connect(self.close)
        self.dir_selector_btn.clicked.connect(self.get_dir)
        self.file_selector_btn.clicked.connect(self.get_file)
        self.project_selector_combo.currentIndexChanged.connect(self.fill_renderer_list)

        self.fill_project_list()

        self.end_frame_spnr.setMaximum(1000000)
        self.start_frame_spnr.setMaximum(1000000)

    def fill_project_list(self):
        all_projs = proj_app_info.get_proj_info()
        self.project_selector_combo.addItems(all_projs)

        self.sort_all_apps_vars()
        self.fill_renderer_list()

    def sort_all_apps_vars(self):
        # Should be called only with a project selected!!!!!
        self.master_app_dict.clear()
        self.master_app_dict = proj_app_info.get_app_info(str(self.project_selector_combo.currentText()).lower())

    def fill_renderer_list(self):
        self.renderer_selector_combo.clear()
        self.sort_all_apps_vars()

        self.renderer_list = []
        for each_app in self.master_app_dict.keys():
            for each_ver in self.master_app_dict[each_app]:
                if each_ver.get("isrenderer"):
                    self.renderer_list.append(each_app + "_" + each_ver.get("version"))

        self.renderer_selector_combo.addItems(self.renderer_list)

    def get_dir(self):
        f_dlg = QtGui.QFileDialog(self)
        f_dlg.setFileMode(QtGui.QFileDialog.Directory)
        f_dlg.setOption(f_dlg.ShowDirsOnly)
        f_dlg.show()

        if f_dlg.exec_():
            self.output_path_box.setText(str(f_dlg.directory().path().replace("/", "\\")))

    def get_file(self):
        fname, fltr = QtGui.QFileDialog.getOpenFileName(self)
        self.file_path_box.setText(fname.replace("/", "\\"))

    def build_deadline_cmd(self):
        # Build two deadline ".job" files; one for the basic params and the other for the plugin params.
        # Basic params will have:
        # Plugin=RivaBatch
        # ForceReloadPlugin=false
        # Frames=
        # Priority=100
        # Pool=
        # Name=
        # OutputDirectory0=
        #
        # Plugin params will have:
        # Plugin=RivaBatch
        # Project=
        # MayaVersion=
        # ArnoldVersion=
        # ApplicationArguments=-rd "\\bdc\script\tech\temp_tests\renders" \\bdc\script\tech\launchers_temp\test_render.ma

        deadline_install_dir = "C:\\Program Files\\Thinkbox\\Deadline\\bin\\deadlinecommand.exe"
        if self.file_path_box.text() == "":
            print "Please pass a proper file path in the file path box."
            return

        project = str(self.project_selector_combo.currentText())
        ren_name, ren_ver = str(self.renderer_selector_combo.currentText()).split("_")
        file_to_open = str(self.file_path_box.text())
        output_dir = str(self.output_path_box.text())
        start_frame = str(self.start_frame_spnr.value())
        end_frame = str(self.end_frame_spnr.value())
        pool = "python_script"
        if str(self.render_pool_box.text()):
            pool = str(self.render_pool_box.text())
        name = os.path.basename(self.file_path_box.text())[:-3]
        cameras = str(self.render_cam_box.text()).split(";") if str(self.render_cam_box.text()) else []
        layers = str(self.render_layer_box.text()).split(";") if str(self.render_layer_box.text()) else []

        base_job_file_loc = os.environ["TMP"].replace("\\", "/") + "/"
        plugin_job_file_loc = os.environ["TMP"].replace("\\", "/") + "/"

        # Now that we have all the info in the world, let's start writing the job files.
        # Let's create the base job and plugin file param lists, for params that will remain constant.
        bjfp_list = list()
        bjfp_list.append("Plugin=RivaBatch\n")
        bjfp_list.append("ForceReloadPlugin=false\n")
        bjfp_list.append("Priority=100\n")
        bjfp_list.append("Frames=%s-%s\n" % (start_frame, end_frame))
        bjfp_list.append("Pool=%s\n" % pool)
        bjfp_list.append("Name=/n")
        bjfp_list.append("OutputDirectory0=%s\n" % output_dir)

        pjfp_list = list()
        pjfp_list.append("Plugin=RivaBatch\n")
        pjfp_list.append("Project=%s\n" % project)
        pjfp_list.append("MayaVersion=2014\n")
        pjfp_list.append("ArnoldVersion=%s\n" % ren_ver)
        pjfp_list.append("ApplicationArguments=/n")

        # With that out of the way, we have to deal with multiple cameras and multiple render layers.
        # specifically, they affect two parts of our write operation:
        # (1) The name of the job(s) and the name of the .job files. Ideally, the name of the job(s) should be
        #     <WHATEVER>_cam_layer & the files should be <WHATEVER>_cam_layer.job and <WHATEVER>_cam_layer_rivabatch.job
        # (2) The ApplicationArguments flag in the "_rivabatch.job" file. The flag, under normal circumstances, is just
        #     -rd <OUTPUTDIR> <RENDERFILE>, but in case of a camera, becomes -cam <CAM> -rd <OUTPUTDIR> <RENDERFILE>.
        #     In case of a layer, it will be -rl <LAYER> -rd <OUTPUTDIR> <RENDERFILE>. In case of a camera and a render
        #     layer, it will be -cam <CAM> -rl <LAYER> -rd <OUTPUTDIR> <RENDERFILE>.
        # So again, as before, let's spit out the constant part first.
        app_arg_line = "-rd \"%s\" %s" % (output_dir, file_to_open)
        app_arg_line_list = list()

        # Let's define a dictionary, where the cameras are the keys. If there are no cameras, the key will be "default"
        # If there are any layers, they will be stored as values of the cameras.
        cam_lyr_dict = {}
        if not cameras:
            cam_lyr_dict["default"] = layers
        else:
            for each in cameras:
                cam_lyr_dict[each] = layers

        for each in cam_lyr_dict.keys():
            cam_line = app_arg_line
            if each != "default":
                cam_line = "-cam \"" + each + "\" " + cam_line

            if cam_lyr_dict[each]:
                for each_lyr in cam_lyr_dict[each]:
                    app_arg_line_list.append("-rl \"" + each_lyr + "\" " + cam_line)
            else:
                app_arg_line_list.append(cam_line)

        # And now, for the final loop, the one in which we add these final bits
        # to the two job files, and save said job files.
        for each_arg in app_arg_line_list:
            each_arg_parts = each_arg.split()
            cam_index = -1
            lyr_index = -1
            if "-cam" in each_arg_parts:
                cam_index = each_arg_parts.index("-cam") + 1
            if "-rl" in each_arg_parts:
                lyr_index = each_arg_parts.index("-rl") + 1

            job_name = name
            if cam_index != -1:
                job_name += "_" + each_arg_parts[cam_index].strip("\"")
            if lyr_index != -1:
                job_name += "_" + each_arg_parts[lyr_index].strip("\"")

            # Modify the job name entry to match the name of the job
            bjfp_list[5] = "Name=" + job_name + "\n"
            pjfp_list[4] = "ApplicationArguments=" + each_arg + "\n"

            # Write the job files out...
            bjf_handle = open(base_job_file_loc + job_name + ".job", "w")
            bjf_handle.writelines(bjfp_list)
            bjf_handle.close()

            pjf_handle = open(plugin_job_file_loc + job_name + "_rivabatch.job", "w")
            pjf_handle.writelines(pjfp_list)
            pjf_handle.close()

            deadline_cmd = "\"" + deadline_install_dir + "\" " + base_job_file_loc.replace("/", "\\") + job_name + ".job" + " " + plugin_job_file_loc.replace("/", "\\") + job_name + "_rivabatch.job"
            subprocess.Popen(deadline_cmd)


if __name__ == "__main__":
    mApp = QtGui.QApplication(sys.argv)
    mrl = MayaRenderLauncher()
    mrl.show()
    sys.exit(mApp.exec_())
