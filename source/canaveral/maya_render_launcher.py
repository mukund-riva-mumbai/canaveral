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
        # Build two deadline ".job" files; one for the basic params
        # and the other for the plugin params.
        # Basic params will have:
        # Plugin=RivaBatch
        # ForceReloadPlugin=false
        # Frames=
        # Priority=
        # Pool=
        # Name=
        # Comment=
        # OutputDirectory0=
        deadline_install_dir = "C:\\Program Files\\Thinkbox\\Deadline\\bin\\deadlinecommand.exe"


if __name__ == "__main__":
    mApp = QtGui.QApplication(sys.argv)
    mrl = MayaRenderLauncher()
    mrl.show()
    sys.exit(mApp.exec_())
