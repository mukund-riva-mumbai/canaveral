import os
import sys
import optparse
import subprocess

import PySide.QtGui as QtGui

import canaveral.ui.canaveral_ui as canaveral_ui
import canaveral.launch_app as launch_app
import canaveral.get_proj_apps as proj_app_info
import ledger.db_connect as dbc
import ledger.db_query as dbq


class Canaveral(canaveral_ui.Ui_MayaLauncher, QtGui.QMainWindow):
    def __init__(self, app="Maya", version="2014", proj="", batch_mode=False, renderer_name="", renderer_ver=""):
        super(Canaveral, self).__init__()
        self.setupUi(self)

        self.launch_btn.clicked.connect(self.launch_app)
        self.close_btn.clicked.connect(self.close)
        self.project_selector_combo.currentIndexChanged.connect(self.fill_renderer_list)

        self.__app = app
        self.__ver = version
        self.__batch_mode = batch_mode
        self.__proj = proj
        self.__renderer_name = renderer_name
        self.__renderer_version = renderer_ver

        self.master_app_dict = {}
        self.renderer_list = []

        self.fill_project_list()

    def fill_project_list(self):
        all_projs = proj_app_info.get_proj_info()
        self.project_selector_combo.addItems(all_projs)

        self.sort_all_apps_vars()
        self.fill_renderer_list()

    def sort_all_apps_vars(self):
        # Should be called only with a project selected!!!!!
        self.master_app_dict.clear()

        if not self.__batch_mode:
            self.__proj = str(self.project_selector_combo.currentText()).lower()

        self.master_app_dict = proj_app_info.get_app_info(self.__proj)

    def fill_renderer_list(self):
        self.renderer_selector_combo.clear()
        self.sort_all_apps_vars()

        self.renderer_list = []
        for each_app in self.master_app_dict.keys():
            for each_ver in self.master_app_dict[each_app]:
                if each_ver.get("isrenderer"):
                    self.renderer_list.append(each_app + "_" + each_ver.get("version"))

        self.renderer_selector_combo.addItems(self.renderer_list)

    def launch_app(self, arg_str=""):
        # def_app = self.master_app_dict.get(self.__app)
        if not self.__batch_mode:
            self.__renderer_name, self.__renderer_version = str(self.renderer_selector_combo.currentText()).split("_")

        launch_app.launch_app(self.__proj, self.master_app_dict, self.__app, self.__ver, self.__renderer_name, self.__renderer_version, arg_str)
        self.close()


def main():
    parser = optparse.OptionParser(usage="app_launcher")
    parser.add_option("-b", "--batch", dest="batch", action="store_true", default=False, help="Start App Launcher in batch mode")
    parser.add_option("-s", "--software", dest="software", default="", help="Name of the software")
    parser.add_option("-v", "--version", dest="version", default="", help="Version of the software")
    parser.add_option("-r", "--renderer", dest="renderername", default="", help="Name of the renderer to be used")
    parser.add_option("-i", "--rendererversion", dest="rendererversion", default="", help="Version of the renderer to be used")
    parser.add_option("-a", "--argumentstring", dest="argumentstring", default="", help="App specific arguments string")
    parser.add_option("-p", "--projectname", dest="project", default="", help="Name of the project")

    opts, args = parser.parse_args()
    option_dict = vars(opts)

    if not option_dict.get("software"):
        print "Please specify a software"
        return

    if not option_dict.get("version"):
        print "Please specify a software version"
        return

    cApp = QtGui.QApplication(sys.argv)

    args = [option_dict.get("software"), option_dict.get("version"), option_dict.get("project"), option_dict.get("batch")]

    if option_dict.get("renderername"):
        args.append(option_dict.get("renderername"))

    if option_dict.get("rendererversion"):
        args.append(option_dict.get("rendererversion"))

    can = Canaveral(*args)
    if not option_dict.get("batch"):
        can.show()
        sys.exit(cApp.exec_())
    elif option_dict.get("batch"):
        if not option_dict.get("project"):
            print "Please pass a project name."
            sys.exit(0)
        can.launch_app(option_dict.get("argumentstring"))

    sys.exit(1)


if __name__ == "__main__":
    main()

