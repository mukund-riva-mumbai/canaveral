# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\riva-software\canaveral\source\canaveral\ui\canaveral_maya_deadline_ui.ui'
#
# Created: Fri Jan 29 14:27:05 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_deadline_launch_win(object):
    def setupUi(self, deadline_launch_win):
        deadline_launch_win.setObjectName("deadline_launch_win")
        deadline_launch_win.resize(668, 257)
        self.centralwidget = QtGui.QWidget(deadline_launch_win)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_5 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName("gridLayout_5")
        spacerItem = QtGui.QSpacerItem(317, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem, 0, 0, 1, 1)
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.project_selector_combo = QtGui.QComboBox(self.widget)
        self.project_selector_combo.setEditable(False)
        self.project_selector_combo.setObjectName("project_selector_combo")
        self.gridLayout.addWidget(self.project_selector_combo, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.renderer_selector_combo = QtGui.QComboBox(self.widget)
        self.renderer_selector_combo.setEditable(False)
        self.renderer_selector_combo.setObjectName("renderer_selector_combo")
        self.gridLayout.addWidget(self.renderer_selector_combo, 0, 3, 1, 1)
        self.gridLayout_5.addWidget(self.widget, 0, 2, 1, 3)
        self.widget_2 = QtGui.QWidget(self.centralwidget)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_2 = QtGui.QGridLayout(self.widget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_3 = QtGui.QLabel(self.widget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(114, 0))
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.file_path_box = QtGui.QLineEdit(self.widget_2)
        self.file_path_box.setObjectName("file_path_box")
        self.gridLayout_2.addWidget(self.file_path_box, 0, 1, 1, 1)
        self.file_selector_btn = QtGui.QToolButton(self.widget_2)
        self.file_selector_btn.setText("")
        self.file_selector_btn.setObjectName("file_selector_btn")
        self.gridLayout_2.addWidget(self.file_selector_btn, 0, 2, 1, 1)
        self.label_4 = QtGui.QLabel(self.widget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(114, 0))
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)
        self.output_path_box = QtGui.QLineEdit(self.widget_2)
        self.output_path_box.setObjectName("output_path_box")
        self.gridLayout_2.addWidget(self.output_path_box, 1, 1, 1, 1)
        self.dir_selector_btn = QtGui.QToolButton(self.widget_2)
        self.dir_selector_btn.setText("")
        self.dir_selector_btn.setObjectName("dir_selector_btn")
        self.gridLayout_2.addWidget(self.dir_selector_btn, 1, 2, 1, 1)
        self.gridLayout_5.addWidget(self.widget_2, 1, 0, 1, 5)
        self.widget_4 = QtGui.QWidget(self.centralwidget)
        self.widget_4.setObjectName("widget_4")
        self.gridLayout_4 = QtGui.QGridLayout(self.widget_4)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_7 = QtGui.QLabel(self.widget_4)
        self.label_7.setObjectName("label_7")
        self.gridLayout_4.addWidget(self.label_7, 0, 0, 1, 1)
        self.render_cam_box = QtGui.QLineEdit(self.widget_4)
        self.render_cam_box.setObjectName("render_cam_box")
        self.gridLayout_4.addWidget(self.render_cam_box, 0, 1, 1, 1)
        self.label_8 = QtGui.QLabel(self.widget_4)
        self.label_8.setObjectName("label_8")
        self.gridLayout_4.addWidget(self.label_8, 0, 2, 1, 1)
        self.render_layer_box = QtGui.QLineEdit(self.widget_4)
        self.render_layer_box.setText("")
        self.render_layer_box.setObjectName("render_layer_box")
        self.gridLayout_4.addWidget(self.render_layer_box, 0, 3, 1, 1)
        self.label_9 = QtGui.QLabel(self.widget_4)
        self.label_9.setEnabled(False)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setItalic(True)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setBold(False)
        self.label_9.setFont(font)
        self.label_9.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_9.setObjectName("label_9")
        self.gridLayout_4.addWidget(self.label_9, 1, 3, 1, 1)
        self.gridLayout_5.addWidget(self.widget_4, 3, 0, 1, 5)
        self.launch_btn = QtGui.QPushButton(self.centralwidget)
        self.launch_btn.setObjectName("launch_btn")
        self.gridLayout_5.addWidget(self.launch_btn, 4, 3, 1, 1)
        self.close_btn = QtGui.QPushButton(self.centralwidget)
        self.close_btn.setObjectName("close_btn")
        self.gridLayout_5.addWidget(self.close_btn, 4, 4, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(431, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem1, 4, 0, 1, 3)
        self.widget_3 = QtGui.QWidget(self.centralwidget)
        self.widget_3.setObjectName("widget_3")
        self.gridLayout_3 = QtGui.QGridLayout(self.widget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_10 = QtGui.QLabel(self.widget_3)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 0, 4, 1, 1)
        self.label_6 = QtGui.QLabel(self.widget_3)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 0, 2, 1, 1)
        self.end_frame_spnr = QtGui.QSpinBox(self.widget_3)
        self.end_frame_spnr.setMinimumSize(QtCore.QSize(100, 0))
        self.end_frame_spnr.setObjectName("end_frame_spnr")
        self.gridLayout_3.addWidget(self.end_frame_spnr, 0, 3, 1, 1)
        self.label_5 = QtGui.QLabel(self.widget_3)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)
        self.start_frame_spnr = QtGui.QSpinBox(self.widget_3)
        self.start_frame_spnr.setMinimumSize(QtCore.QSize(100, 0))
        self.start_frame_spnr.setObjectName("start_frame_spnr")
        self.gridLayout_3.addWidget(self.start_frame_spnr, 0, 1, 1, 1)
        self.render_pool_box = QtGui.QLineEdit(self.widget_3)
        self.render_pool_box.setObjectName("render_pool_box")
        self.gridLayout_3.addWidget(self.render_pool_box, 0, 5, 1, 1)
        self.gridLayout_5.addWidget(self.widget_3, 2, 0, 1, 4)
        deadline_launch_win.setCentralWidget(self.centralwidget)

        self.retranslateUi(deadline_launch_win)
        QtCore.QMetaObject.connectSlotsByName(deadline_launch_win)

    def retranslateUi(self, deadline_launch_win):
        deadline_launch_win.setWindowTitle(QtGui.QApplication.translate("deadline_launch_win", "Deadline Launcher", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("deadline_launch_win", "Select Project", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("deadline_launch_win", "Select Renderer", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("deadline_launch_win", "Select Render File", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("deadline_launch_win", "Select Render Directory", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("deadline_launch_win", "Render Camera", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("deadline_launch_win", "Render Layers", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("deadline_launch_win", "Enter multiple render layers separated by a \";\"", None, QtGui.QApplication.UnicodeUTF8))
        self.launch_btn.setText(QtGui.QApplication.translate("deadline_launch_win", "Launch Render", None, QtGui.QApplication.UnicodeUTF8))
        self.close_btn.setText(QtGui.QApplication.translate("deadline_launch_win", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("deadline_launch_win", "Render Pool", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("deadline_launch_win", "End Frame", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("deadline_launch_win", "Start Frame", None, QtGui.QApplication.UnicodeUTF8))
