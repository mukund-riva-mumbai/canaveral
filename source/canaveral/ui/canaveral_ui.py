# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\riva-software\canaveral\source\canaveral\ui\canaveral_ui.ui'
#
# Created: Mon Jan 25 15:13:59 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MayaLauncher(object):
    def setupUi(self, MayaLauncher):
        MayaLauncher.setObjectName("MayaLauncher")
        MayaLauncher.resize(350, 200)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MayaLauncher.sizePolicy().hasHeightForWidth())
        MayaLauncher.setSizePolicy(sizePolicy)
        MayaLauncher.setMinimumSize(QtCore.QSize(350, 200))
        MayaLauncher.setMaximumSize(QtCore.QSize(350, 200))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/mukund.d/Documents/MayaIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MayaLauncher.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MayaLauncher)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtGui.QSpacerItem(66, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.project_selector_combo = QtGui.QComboBox(self.widget)
        self.project_selector_combo.setEditable(False)
        self.project_selector_combo.setObjectName("project_selector_combo")
        self.gridLayout.addWidget(self.project_selector_combo, 0, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(72, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 3, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(66, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        self.renderer_selector_combo = QtGui.QComboBox(self.widget)
        self.renderer_selector_combo.setEditable(False)
        self.renderer_selector_combo.setObjectName("renderer_selector_combo")
        self.gridLayout.addWidget(self.renderer_selector_combo, 1, 2, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(72, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 3, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(149, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 2, 0, 1, 2)
        self.launch_btn = QtGui.QPushButton(self.widget)
        self.launch_btn.setObjectName("launch_btn")
        self.gridLayout.addWidget(self.launch_btn, 2, 2, 1, 1)
        self.close_btn = QtGui.QPushButton(self.widget)
        self.close_btn.setObjectName("close_btn")
        self.gridLayout.addWidget(self.close_btn, 2, 3, 1, 1)
        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)
        MayaLauncher.setCentralWidget(self.centralwidget)

        self.retranslateUi(MayaLauncher)
        QtCore.QMetaObject.connectSlotsByName(MayaLauncher)

    def retranslateUi(self, MayaLauncher):
        MayaLauncher.setWindowTitle(QtGui.QApplication.translate("MayaLauncher", "Launch Maya For Project", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MayaLauncher", "Select Project", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MayaLauncher", "Select Renderer", None, QtGui.QApplication.UnicodeUTF8))
        self.launch_btn.setText(QtGui.QApplication.translate("MayaLauncher", "Launch Maya", None, QtGui.QApplication.UnicodeUTF8))
        self.close_btn.setText(QtGui.QApplication.translate("MayaLauncher", "Close", None, QtGui.QApplication.UnicodeUTF8))

