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
        deadline_install_dir = "C:\\Program Files\\Thinkbox\\Deadline\\bin\\deadlinecommand.exe -SubmitCommandLineJob"
        launch_exec = " -executable "

        if self.file_path_box.text() == "":
            print "Please pass a proper file path in the file path box."
            return

        launch_bat_file = os.path.dirname(self.file_path_box.text()) + "\\render_bats\\" + os.path.basename(self.file_path_box.text())[:-3] + ".bat"
        launch_args = " -arguments "

        ren_name, ren_ver = str(self.renderer_selector_combo.currentText()).split("_")
        env_str = launch_app.set_env_vars(str(self.project_selector_combo.currentText()), self.master_app_dict, "Maya", "2014", ren_name, ren_ver, False)
        env_str_list = []
        ren_lyr_list = []

        env_str += "\"C:\\Program Files\\Autodesk\\Maya2014\\bin\\render.exe\" -s %3 -e %4 -rd %2"

        launch_args += "\""

        file_to_open = str(self.file_path_box.text())
        launch_args += "<QUOTE>%s<QUOTE>" % file_to_open

        output_dir = str(self.output_path_box.text())
        launch_args += " <QUOTE>%s<QUOTE>" % output_dir

        start_frame = str(self.start_frame_spnr.value())
        end_frame = str(self.end_frame_spnr.value())
        launch_args += " %s %s" % (start_frame, end_frame)

        flag_count = 4
        if str(self.render_cam_box.text()):
            flag_count += 1
            launch_args += " %s" % str(self.render_cam_box.text())
            env_str += " -cam %5"

        if str(self.render_layer_box.text()):
            for each in str(self.render_layer_box.text()).split(";"):
                env_str_list.append(env_str + " -rl %" + str(flag_count+1))
                ren_lyr_list.append(each)

        if len(ren_lyr_list):
            for lyr_id in xrange(0, len(ren_lyr_list)):
                bat_file_name = os.path.basename(file_to_open)[:-3]
                bat_file_name += "." + ren_lyr_list[lyr_id] + ".bat"
                launch_file = os.path.dirname(launch_bat_file) + "\\" + bat_file_name
                if not os.path.exists(os.path.dirname(launch_bat_file)):
                    os.makedirs(os.path.dirname(launch_bat_file))
                ren_bat_f = open(launch_file, "w")
                ren_bat_f.write(env_str_list[lyr_id] + " %1")
                ren_bat_f.close()

                deadline_cmd = deadline_install_dir + launch_exec + launch_file + launch_args + " " + ren_lyr_list[lyr_id] + "\""
                #deadline_cmd += " -frames %s-%s" % (start_frame, end_frame)
                deadline_cmd += " -name %s" % bat_file_name[:-4]
                if str(self.render_pool_box.text()):
                    deadline_cmd += " -pool %s" % str(self.render_pool_box.text())
                deadline_cmd += " -prop OutputDirectory0=\"%s\"" % output_dir
                subprocess.Popen(deadline_cmd)
        else:
            if not os.path.exists(os.path.dirname(launch_bat_file)):
                os.makedirs(os.path.dirname(launch_bat_file))
            ren_bat_f = open(launch_bat_file, "w")
            ren_bat_f.write(env_str + " %1")
            ren_bat_f.close()

            deadline_cmd = deadline_install_dir + launch_exec + launch_bat_file + launch_args + "\""
            deadline_cmd += " -frames %s-%s" % (start_frame, end_frame)
            deadline_cmd += " -name %s" % os.path.basename(launch_bat_file)[:-4]
            if str(self.render_pool_box.text()):
                deadline_cmd += " -pool %s" % str(self.render_pool_box.text())
            deadline_cmd += " -prop OutputDirectory0=\"%s\"" % output_dir
            subprocess.Popen(deadline_cmd)


if __name__ == "__main__":
    mApp = QtGui.QApplication(sys.argv)
    mrl = MayaRenderLauncher()
    mrl.show()
    sys.exit(mApp.exec_())
