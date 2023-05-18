# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_error.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Error(object):
    def setupUi(self, Error):
        if not Error.objectName():
            Error.setObjectName(u"Error")
        Error.resize(250, 150)
        Error.setMinimumSize(QSize(250, 150))
        Error.setMaximumSize(QSize(250, 150))
        self.horizontalLayout = QHBoxLayout(Error)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Error)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background:qradialgradient(cx:0, cy:0, radius:1, fx:0,fy:0,\n"
"                  stop:0 #22a241, stop:1 #eacd13);")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.frame_top = QFrame(self.frame)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMinimumSize(QSize(0, 55))
        self.frame_top.setMaximumSize(QSize(16777215, 55))
        self.frame_top.setStyleSheet(u"background:#e4e9cd;")
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(15, 5, 0, 0)
        self.lab_icon = QLabel(self.frame_top)
        self.lab_icon.setObjectName(u"lab_icon")
        self.lab_icon.setMinimumSize(QSize(35, 35))
        self.lab_icon.setMaximumSize(QSize(35, 35))

        self.horizontalLayout_2.addWidget(self.lab_icon)

        self.lab_heading = QLabel(self.frame_top)
        self.lab_heading.setObjectName(u"lab_heading")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(12)
        self.lab_heading.setFont(font)
        self.lab_heading.setStyleSheet(u"color:#04130a;")
        self.lab_heading.setWordWrap(True)

        self.horizontalLayout_2.addWidget(self.lab_heading)


        self.verticalLayout.addWidget(self.frame_top)

        self.frame_bottom = QFrame(self.frame)
        self.frame_bottom.setObjectName(u"frame_bottom")
        self.frame_bottom.setStyleSheet(u"background:#e4e9cd;")
        self.frame_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_bottom.setFrameShadow(QFrame.Plain)
        self.gridLayout = QGridLayout(self.frame_bottom)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.bn_ok = QPushButton(self.frame_bottom)
        self.bn_ok.setObjectName(u"bn_ok")
        self.bn_ok.setMinimumSize(QSize(69, 25))
        self.bn_ok.setMaximumSize(QSize(69, 25))
        self.bn_ok.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid #eacd13;\n"
"	border-radius: 5px;	\n"
"	color:#04130a;\n"
"	background-color: #eacd13;\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid #f6e56a;\n"
"	background-color: #f6e56a;\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid #fbd411;\n"
"	background-color: #fbd411;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.bn_ok, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.frame_bottom)


        self.horizontalLayout.addWidget(self.frame)


        self.retranslateUi(Error)

        QMetaObject.connectSlotsByName(Error)
    # setupUi

    def retranslateUi(self, Error):
        Error.setWindowTitle(QCoreApplication.translate("Error", u"Dialog", None))
        self.lab_icon.setText("")
        self.lab_heading.setText("")
        self.bn_ok.setText("")
    # retranslateUi

