# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(922, 688)
        MainWindow.setMinimumSize(QSize(800, 550))
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background:#04130a;")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_top = QFrame(self.centralwidget)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMaximumSize(QSize(16777215, 55))
        font_path = "./fonts/SmileySans.ttf"  # FONT PATH FOR THE APPLICATION
        QFontDatabase.addApplicationFont(font_path)  # ADDING THE FONT TO THE DATABASE
        font = QFont()
        font.setFamily(u"Smiley Sans")
        font.setItalic(True)
        self.frame_top.setFont(font)
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Plain)
        self.horizontalLayout = QHBoxLayout(self.frame_top)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_toodle = QFrame(self.frame_top)
        self.frame_toodle.setObjectName(u"frame_toodle")
        self.frame_toodle.setMinimumSize(QSize(80, 55))
        self.frame_toodle.setMaximumSize(QSize(80, 55))
        self.frame_toodle.setFont(font)
        self.frame_toodle.setStyleSheet(u"background:qradialgradient(cx:0, cy:0, radius:1, fx:0,fy:0,\n"
"                  stop:0 #22a241, stop:1 #eacd13);")
        self.frame_toodle.setFrameShape(QFrame.NoFrame)
        self.frame_toodle.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_toodle)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.toodle = QPushButton(self.frame_toodle)
        self.toodle.setObjectName(u"toodle")
        self.toodle.setMinimumSize(QSize(80, 55))
        self.toodle.setMaximumSize(QSize(80, 55))
        self.toodle.setFont(font)
        self.toodle.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: qradialgradient(cx:0, cy:0, radius:1, fx:0,fy:0,\n"
"                  stop:0.8 #22a241, stop:1 #eacd13);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon = QIcon()
        icon.addFile(u"icons/1x/logo-pixelicious.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toodle.setIcon(icon)
        self.toodle.setIconSize(QSize(32, 32))
        self.toodle.setFlat(True)

        self.horizontalLayout_3.addWidget(self.toodle)


        self.horizontalLayout.addWidget(self.frame_toodle)

        self.frame_top_east = QFrame(self.frame_top)
        self.frame_top_east.setObjectName(u"frame_top_east")
        self.frame_top_east.setMaximumSize(QSize(16777215, 55))
        self.frame_top_east.setFont(font)
        self.frame_top_east.setStyleSheet(u"background:#eacd13;")
        self.frame_top_east.setFrameShape(QFrame.NoFrame)
        self.frame_top_east.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_top_east)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_appname = QFrame(self.frame_top_east)
        self.frame_appname.setObjectName(u"frame_appname")
        self.frame_appname.setFont(font)
        self.frame_appname.setFrameShape(QFrame.NoFrame)
        self.frame_appname.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_appname)
        self.horizontalLayout_10.setSpacing(7)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.lab_appname = QLabel(self.frame_appname)
        self.lab_appname.setObjectName(u"lab_appname")
        font1 = QFont()
        font1.setFamily(u"Smiley Sans")
        font1.setPointSize(24)
        font1.setItalic(True)
        self.lab_appname.setFont(font1)
        self.lab_appname.setStyleSheet(u"color:rgb(255,255,255);")

        self.horizontalLayout_10.addWidget(self.lab_appname)


        self.horizontalLayout_4.addWidget(self.frame_appname)

        self.frame_user = QFrame(self.frame_top_east)
        self.frame_user.setObjectName(u"frame_user")
        self.frame_user.setFont(font)
        self.frame_user.setFrameShape(QFrame.NoFrame)
        self.frame_user.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_user)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.lab_user = QLabel(self.frame_user)
        self.lab_user.setObjectName(u"lab_user")
        self.lab_user.setFont(font1)
        self.lab_user.setStyleSheet(u"color:rgb(255,255,255);")
        self.lab_user.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.lab_user)


        self.horizontalLayout_4.addWidget(self.frame_user)

        self.frame_person = QFrame(self.frame_top_east)
        self.frame_person.setObjectName(u"frame_person")
        self.frame_person.setMinimumSize(QSize(55, 55))
        self.frame_person.setMaximumSize(QSize(55, 55))
        self.frame_person.setFont(font)
        self.frame_person.setFrameShape(QFrame.NoFrame)
        self.frame_person.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_person)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.lab_person = QLabel(self.frame_person)
        self.lab_person.setObjectName(u"lab_person")
        self.lab_person.setMaximumSize(QSize(55, 55))
        self.lab_person.setFont(font)
        self.lab_person.setPixmap(QPixmap(u"icons/1x/peple.png"))
        self.lab_person.setScaledContents(False)
        self.lab_person.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.lab_person)


        self.horizontalLayout_4.addWidget(self.frame_person)

        self.frame_min = QFrame(self.frame_top_east)
        self.frame_min.setObjectName(u"frame_min")
        self.frame_min.setMinimumSize(QSize(55, 55))
        self.frame_min.setMaximumSize(QSize(55, 55))
        self.frame_min.setFont(font)
        self.frame_min.setFrameShape(QFrame.NoFrame)
        self.frame_min.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_min)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.bn_min = QPushButton(self.frame_min)
        self.bn_min.setObjectName(u"bn_min")
        self.bn_min.setMaximumSize(QSize(55, 55))
        self.bn_min.setFont(font)
        self.bn_min.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #f6e56a;\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"icons/1x/hideAsset53.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_min.setIcon(icon1)
        self.bn_min.setIconSize(QSize(22, 22))
        self.bn_min.setFlat(True)

        self.horizontalLayout_7.addWidget(self.bn_min)


        self.horizontalLayout_4.addWidget(self.frame_min)

        self.frame_max = QFrame(self.frame_top_east)
        self.frame_max.setObjectName(u"frame_max")
        self.frame_max.setMinimumSize(QSize(55, 55))
        self.frame_max.setMaximumSize(QSize(55, 55))
        self.frame_max.setFont(font)
        self.frame_max.setFrameShape(QFrame.NoFrame)
        self.frame_max.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_max)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.bn_max = QPushButton(self.frame_max)
        self.bn_max.setObjectName(u"bn_max")
        self.bn_max.setMaximumSize(QSize(55, 55))
        self.bn_max.setFont(font)
        self.bn_max.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #f6e56a;\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"icons/1x/max.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_max.setIcon(icon2)
        self.bn_max.setIconSize(QSize(22, 22))
        self.bn_max.setFlat(True)

        self.horizontalLayout_6.addWidget(self.bn_max)


        self.horizontalLayout_4.addWidget(self.frame_max)

        self.frame_close = QFrame(self.frame_top_east)
        self.frame_close.setObjectName(u"frame_close")
        self.frame_close.setMinimumSize(QSize(55, 55))
        self.frame_close.setMaximumSize(QSize(55, 55))
        self.frame_close.setFont(font)
        self.frame_close.setFrameShape(QFrame.NoFrame)
        self.frame_close.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_close)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.bn_close = QPushButton(self.frame_close)
        self.bn_close.setObjectName(u"bn_close")
        self.bn_close.setMaximumSize(QSize(55, 55))
        self.bn_close.setFont(font)
        self.bn_close.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #f6e56a;\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"icons/1x/closeAsset43.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_close.setIcon(icon3)
        self.bn_close.setIconSize(QSize(22, 22))
        self.bn_close.setFlat(True)

        self.horizontalLayout_5.addWidget(self.bn_close)


        self.horizontalLayout_4.addWidget(self.frame_close)


        self.horizontalLayout.addWidget(self.frame_top_east)


        self.verticalLayout.addWidget(self.frame_top)

        self.frame_bottom = QFrame(self.centralwidget)
        self.frame_bottom.setObjectName(u"frame_bottom")
        self.frame_bottom.setFont(font)
        self.frame_bottom.setStyleSheet(u"background:#eacd13;")
        self.frame_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_bottom.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_bottom)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_bottom_west = QFrame(self.frame_bottom)
        self.frame_bottom_west.setObjectName(u"frame_bottom_west")
        self.frame_bottom_west.setMinimumSize(QSize(80, 0))
        self.frame_bottom_west.setMaximumSize(QSize(80, 16777215))
        self.frame_bottom_west.setFont(font)
        self.frame_bottom_west.setStyleSheet(u"background:#eacd13;")
        self.frame_bottom_west.setFrameShape(QFrame.NoFrame)
        self.frame_bottom_west.setFrameShadow(QFrame.Plain)
        self.verticalLayout_3 = QVBoxLayout(self.frame_bottom_west)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_text = QFrame(self.frame_bottom_west)
        self.frame_text.setObjectName(u"frame_text")
        self.frame_text.setMinimumSize(QSize(80, 55))
        self.frame_text.setMaximumSize(QSize(160, 55))
        self.frame_text.setFont(font)
        self.frame_text.setFrameShape(QFrame.NoFrame)
        self.frame_text.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_text)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.bn_text = QPushButton(self.frame_text)
        self.bn_text.setObjectName(u"bn_text")
        self.bn_text.setMinimumSize(QSize(80, 55))
        self.bn_text.setMaximumSize(QSize(160, 55))
        self.bn_text.setFont(font)
        self.bn_text.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: #eacd13;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #f6e56a;\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: #fbd411;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"icons/1x/icons8-align-text-left-22.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_text.setIcon(icon4)
        self.bn_text.setIconSize(QSize(32, 32))
        self.bn_text.setFlat(True)

        self.horizontalLayout_15.addWidget(self.bn_text)


        self.verticalLayout_3.addWidget(self.frame_text)

        self.frame_voice = QFrame(self.frame_bottom_west)
        self.frame_voice.setObjectName(u"frame_voice")
        self.frame_voice.setMinimumSize(QSize(80, 55))
        self.frame_voice.setMaximumSize(QSize(160, 55))
        self.frame_voice.setFont(font)
        self.frame_voice.setFrameShape(QFrame.NoFrame)
        self.frame_voice.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_voice)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.bn_voice = QPushButton(self.frame_voice)
        self.bn_voice.setObjectName(u"bn_voice")
        self.bn_voice.setMinimumSize(QSize(80, 55))
        self.bn_voice.setMaximumSize(QSize(160, 55))
        self.bn_voice.setFont(font)
        self.bn_voice.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: #eacd13;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #f6e56a;\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: #fbd411;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u"icons/1x/icons8-audio-wave-22.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_voice.setIcon(icon5)
        self.bn_voice.setIconSize(QSize(32, 32))
        self.bn_voice.setFlat(True)

        self.horizontalLayout_16.addWidget(self.bn_voice)


        self.verticalLayout_3.addWidget(self.frame_voice)

        self.frame_noise = QFrame(self.frame_bottom_west)
        self.frame_noise.setObjectName(u"frame_noise")
        self.frame_noise.setMinimumSize(QSize(80, 55))
        self.frame_noise.setMaximumSize(QSize(160, 55))
        self.frame_noise.setFont(font)
        self.frame_noise.setFrameShape(QFrame.NoFrame)
        self.frame_noise.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_noise)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.bn_noise = QPushButton(self.frame_noise)
        self.bn_noise.setObjectName(u"bn_noise")
        self.bn_noise.setMinimumSize(QSize(80, 55))
        self.bn_noise.setMaximumSize(QSize(160, 55))
        self.bn_noise.setFont(font)
        self.bn_noise.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: #eacd13;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #f6e56a;\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: #fbd411;\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u"icons/1x/icons8-sine-22.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_noise.setIcon(icon6)
        self.bn_noise.setIconSize(QSize(32, 32))
        self.bn_noise.setFlat(True)

        self.horizontalLayout_17.addWidget(self.bn_noise)


        self.verticalLayout_3.addWidget(self.frame_noise)

        self.frame_image = QFrame(self.frame_bottom_west)
        self.frame_image.setObjectName(u"frame_image")
        self.frame_image.setMinimumSize(QSize(80, 55))
        self.frame_image.setMaximumSize(QSize(160, 55))
        self.frame_image.setFont(font)
        self.frame_image.setFrameShape(QFrame.NoFrame)
        self.frame_image.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_image)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.bn_image = QPushButton(self.frame_image)
        self.bn_image.setObjectName(u"bn_image")
        self.bn_image.setMinimumSize(QSize(80, 55))
        self.bn_image.setMaximumSize(QSize(160, 55))
        self.bn_image.setFont(font)
        self.bn_image.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: #eacd13;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #f6e56a;\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: #fbd411;\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u"icons/1x/icons8-image-22.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_image.setIcon(icon7)
        self.bn_image.setIconSize(QSize(32, 32))
        self.bn_image.setFlat(True)

        self.horizontalLayout_18.addWidget(self.bn_image)


        self.verticalLayout_3.addWidget(self.frame_image)


        self.horizontalLayout_2.addWidget(self.frame_bottom_west)

        self.frame_bottom_east = QFrame(self.frame_bottom)
        self.frame_bottom_east.setObjectName(u"frame_bottom_east")
        self.frame_bottom_east.setFont(font)
        self.frame_bottom_east.setStyleSheet(u"background:#eacd13;")
        self.frame_bottom_east.setFrameShape(QFrame.NoFrame)
        self.frame_bottom_east.setFrameShadow(QFrame.Plain)
        self.verticalLayout_2 = QVBoxLayout(self.frame_bottom_east)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frame_bottom_east)
        self.frame.setObjectName(u"frame")
        self.frame.setFont(font)
        self.frame.setStyleSheet(u"background:#eacd13;")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_14 = QHBoxLayout(self.frame)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(0, 55))
        self.stackedWidget.setFont(font)
        self.stackedWidget.setLayoutDirection(Qt.LeftToRight)
        self.stackedWidget.setStyleSheet(u"background:#ffffff;")
        self.page_about_Lemon4 = QWidget()
        self.page_about_Lemon4.setObjectName(u"page_about_Lemon4")
        self.page_about_Lemon4.setFont(font)
        self.page_about_Lemon4.setStyleSheet(u"background:#e9e9cd;")
        self.verticalLayout_13 = QVBoxLayout(self.page_about_Lemon4)
        self.verticalLayout_13.setSpacing(5)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(5, 5, 5, 5)
        self.lab_about_home = QLabel(self.page_about_Lemon4)
        self.lab_about_home.setObjectName(u"lab_about_home")
        self.lab_about_home.setMinimumSize(QSize(0, 55))
        self.lab_about_home.setMaximumSize(QSize(16777215, 55))
        self.lab_about_home.setFont(font1)
        self.lab_about_home.setStyleSheet(u"color:#04130a;\n"
"background:#e4e9cd;")

        self.verticalLayout_13.addWidget(self.lab_about_home)

        self.frame_about_lemon4 = QFrame(self.page_about_Lemon4)
        self.frame_about_lemon4.setObjectName(u"frame_about_lemon4")
        self.frame_about_lemon4.setFrameShape(QFrame.StyledPanel)
        self.frame_about_lemon4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_about_lemon4)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(5, 5, 0, 5)
        self.text_about_home = QTextEdit(self.frame_about_lemon4)
        self.text_about_home.setObjectName(u"text_about_home")
        self.text_about_home.setEnabled(True)
        font2 = QFont()
        font2.setFamily(u"Smiley Sans")
        font2.setPointSize(10)
        font2.setItalic(True)
        self.text_about_home.setFont(font2)
        self.text_about_home.setStyleSheet(u"color:#04130a;")
        self.text_about_home.setFrameShape(QFrame.NoFrame)
        self.text_about_home.setFrameShadow(QFrame.Plain)
        self.text_about_home.setReadOnly(True)
        self.text_about_home.setTextInteractionFlags(Qt.TextBrowserInteraction)

        self.horizontalLayout_28.addWidget(self.text_about_home)

        self.vsb_about_home = QScrollBar(self.frame_about_lemon4)
        self.vsb_about_home.setObjectName(u"vsb_about_home")
        self.vsb_about_home.setStyleSheet(u"QScrollBar:vertical {\n"
"	background:#e4e9cd;\n"
"    width:20px;\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background:#645c0c;\n"
"}\n"
"QScrollBar::add-page:vertical {\n"
" 	background:#22a241;\n"
"}\n"
"QScrollBar::sub-page:vertical {\n"
" 	background:#fbd411;\n"
"}")
        self.vsb_about_home.setOrientation(Qt.Vertical)

        self.horizontalLayout_28.addWidget(self.vsb_about_home)


        self.verticalLayout_13.addWidget(self.frame_about_lemon4)

        self.stackedWidget.addWidget(self.page_about_Lemon4)
        self.page_about_TextToSpeech = QWidget()
        self.page_about_TextToSpeech.setObjectName(u"page_about_TextToSpeech")
        self.page_about_TextToSpeech.setAutoFillBackground(False)
        self.page_about_TextToSpeech.setStyleSheet(u"background:#e9e9cd;")
        self.verticalLayout_7 = QVBoxLayout(self.page_about_TextToSpeech)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.lab_about_home_2 = QLabel(self.page_about_TextToSpeech)
        self.lab_about_home_2.setObjectName(u"lab_about_home_2")
        self.lab_about_home_2.setMinimumSize(QSize(0, 55))
        self.lab_about_home_2.setMaximumSize(QSize(16777215, 55))
        self.lab_about_home_2.setFont(font1)
        self.lab_about_home_2.setStyleSheet(u"color:#04130a;\n"
"background:#e4e9cd;")

        self.verticalLayout_7.addWidget(self.lab_about_home_2)

        self.text_about_home_2 = QTextEdit(self.page_about_TextToSpeech)
        self.text_about_home_2.setObjectName(u"text_about_home_2")
        self.text_about_home_2.setEnabled(True)
        self.text_about_home_2.setFont(font2)
        self.text_about_home_2.setStyleSheet(u"color:#04130a;\n"
"background:#e4e9cd;")
        self.text_about_home_2.setFrameShape(QFrame.NoFrame)
        self.text_about_home_2.setFrameShadow(QFrame.Plain)
        self.text_about_home_2.setReadOnly(True)
        self.text_about_home_2.setTextInteractionFlags(Qt.TextBrowserInteraction)

        self.verticalLayout_7.addWidget(self.text_about_home_2)

        self.stackedWidget.addWidget(self.page_about_TextToSpeech)
        self.page_about_VoiceConversion = QWidget()
        self.page_about_VoiceConversion.setObjectName(u"page_about_VoiceConversion")
        self.page_about_VoiceConversion.setStyleSheet(u"background:#e9e9cd;")
        self.verticalLayout_17 = QVBoxLayout(self.page_about_VoiceConversion)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.lab_about_home_3 = QLabel(self.page_about_VoiceConversion)
        self.lab_about_home_3.setObjectName(u"lab_about_home_3")
        self.lab_about_home_3.setMinimumSize(QSize(0, 55))
        self.lab_about_home_3.setMaximumSize(QSize(16777215, 55))
        self.lab_about_home_3.setFont(font1)
        self.lab_about_home_3.setStyleSheet(u"color:#04130a;\n"
"background:#e4e9cd;")

        self.verticalLayout_17.addWidget(self.lab_about_home_3)

        self.text_about_home_3 = QTextEdit(self.page_about_VoiceConversion)
        self.text_about_home_3.setObjectName(u"text_about_home_3")
        self.text_about_home_3.setEnabled(True)
        self.text_about_home_3.setFont(font2)
        self.text_about_home_3.setStyleSheet(u"color:#04130a;\n"
"background:#e4e9cd;")
        self.text_about_home_3.setFrameShape(QFrame.NoFrame)
        self.text_about_home_3.setFrameShadow(QFrame.Plain)
        self.text_about_home_3.setReadOnly(True)
        self.text_about_home_3.setTextInteractionFlags(Qt.TextBrowserInteraction)

        self.verticalLayout_17.addWidget(self.text_about_home_3)

        self.stackedWidget.addWidget(self.page_about_VoiceConversion)
        self.page_about_Denoise = QWidget()
        self.page_about_Denoise.setObjectName(u"page_about_Denoise")
        self.page_about_Denoise.setStyleSheet(u"background:#e9e9cd;")
        self.verticalLayout_18 = QVBoxLayout(self.page_about_Denoise)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.lab_about_home_4 = QLabel(self.page_about_Denoise)
        self.lab_about_home_4.setObjectName(u"lab_about_home_4")
        self.lab_about_home_4.setMinimumSize(QSize(0, 55))
        self.lab_about_home_4.setMaximumSize(QSize(16777215, 55))
        self.lab_about_home_4.setFont(font1)
        self.lab_about_home_4.setStyleSheet(u"color:#04130a;\n"
"background:#e4e9cd;")

        self.verticalLayout_18.addWidget(self.lab_about_home_4)

        self.text_about_home_4 = QTextEdit(self.page_about_Denoise)
        self.text_about_home_4.setObjectName(u"text_about_home_4")
        self.text_about_home_4.setEnabled(True)
        self.text_about_home_4.setFont(font2)
        self.text_about_home_4.setStyleSheet(u"color:#04130a;\n"
"background:#e4e9cd;")
        self.text_about_home_4.setFrameShape(QFrame.NoFrame)
        self.text_about_home_4.setFrameShadow(QFrame.Plain)
        self.text_about_home_4.setReadOnly(True)
        self.text_about_home_4.setTextInteractionFlags(Qt.TextBrowserInteraction)

        self.verticalLayout_18.addWidget(self.text_about_home_4)

        self.stackedWidget.addWidget(self.page_about_Denoise)
        self.page_about_ImageRefinement = QWidget()
        self.page_about_ImageRefinement.setObjectName(u"page_about_ImageRefinement")
        self.page_about_ImageRefinement.setStyleSheet(u"background:#e9e9cd;")
        self.verticalLayout_20 = QVBoxLayout(self.page_about_ImageRefinement)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.lab_about_home_5 = QLabel(self.page_about_ImageRefinement)
        self.lab_about_home_5.setObjectName(u"lab_about_home_5")
        self.lab_about_home_5.setMinimumSize(QSize(0, 55))
        self.lab_about_home_5.setMaximumSize(QSize(16777215, 55))
        self.lab_about_home_5.setFont(font1)
        self.lab_about_home_5.setStyleSheet(u"color:#04130a;\n"
"background:#e4e9cd;")

        self.verticalLayout_20.addWidget(self.lab_about_home_5)

        self.text_about_home_5 = QTextEdit(self.page_about_ImageRefinement)
        self.text_about_home_5.setObjectName(u"text_about_home_5")
        self.text_about_home_5.setEnabled(True)
        self.text_about_home_5.setFont(font2)
        self.text_about_home_5.setStyleSheet(u"color:#04130a;\n"
"background:#e4e9cd;")
        self.text_about_home_5.setFrameShape(QFrame.NoFrame)
        self.text_about_home_5.setFrameShadow(QFrame.Plain)
        self.text_about_home_5.setReadOnly(True)
        self.text_about_home_5.setTextInteractionFlags(Qt.TextBrowserInteraction)

        self.verticalLayout_20.addWidget(self.text_about_home_5)

        self.stackedWidget.addWidget(self.page_about_ImageRefinement)
        self.page_Denoise = QWidget()
        self.page_Denoise.setObjectName(u"page_Denoise")
        self.page_Denoise.setFont(font)
        self.page_Denoise.setStyleSheet(u"background:#e4e9cd;")
        self.verticalLayout_16 = QVBoxLayout(self.page_Denoise)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.Denoise_label_Title = QLabel(self.page_Denoise)
        self.Denoise_label_Title.setObjectName(u"Denoise_label_Title")
        self.Denoise_label_Title.setMinimumSize(QSize(0, 55))
        self.Denoise_label_Title.setMaximumSize(QSize(16777215, 55))
        self.Denoise_label_Title.setFont(font1)

        self.verticalLayout_16.addWidget(self.Denoise_label_Title)

        self.Denoise_frame_1 = QFrame(self.page_Denoise)
        self.Denoise_frame_1.setObjectName(u"Denoise_frame_1")
        font3 = QFont()
        font3.setPointSize(10)
        self.Denoise_frame_1.setFont(font3)
        self.horizontalLayout_29 = QHBoxLayout(self.Denoise_frame_1)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.groupBox_2 = QGroupBox(self.Denoise_frame_1)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setStyleSheet(u"border: 2px;\n"
"border-radius: 5px;	\n"
"")
        self.groupBox_2.setFlat(False)
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalFrame = QFrame(self.groupBox_2)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        self.horizontalLayout_21 = QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.Denoise_pushButton_SelectFile = QPushButton(self.horizontalFrame)
        self.Denoise_pushButton_SelectFile.setObjectName(u"Denoise_pushButton_SelectFile")
        self.Denoise_pushButton_SelectFile.setMinimumSize(QSize(108, 38))
        font4 = QFont()
        font4.setFamily(u"Smiley Sans")
        font4.setPointSize(12)
        font4.setBold(False)
        font4.setItalic(True)
        font4.setWeight(50)
        self.Denoise_pushButton_SelectFile.setFont(font4)
        self.Denoise_pushButton_SelectFile.setStyleSheet(u"QPushButton {\n"
"	border-radius:1px;\n"
"	font: italic 12pt \"Smiley Sans\";\n"
"	background-color:#ddddd9;\n"
"	border-radius:17px;\n"
"	margin-left:10px;\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid #e4e4e1;\n"
"	background-color: #e4e4e1;\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid #eeeeec;\n"
"	background-color: #eeeeec;\n"
"}\n"
"")

        self.horizontalLayout_21.addWidget(self.Denoise_pushButton_SelectFile)

        self.horizontalFrame_4 = QFrame(self.horizontalFrame)
        self.horizontalFrame_4.setObjectName(u"horizontalFrame_4")
        self.horizontalFrame_4.setMinimumSize(QSize(0, 38))
        self.horizontalFrame_4.setMaximumSize(QSize(16777215, 38))
        self.horizontalFrame_4.setStyleSheet(u"background-color:#ddddd9;\n"
"height:32px;\n"
"border-radius:15px;\n"
"margin-left:14px;\n"
"margin-right:14px;")
        self.horizontalLayout_19 = QHBoxLayout(self.horizontalFrame_4)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.Denoise_pushButton_PlayAudio_before = QPushButton(self.horizontalFrame_4)
        self.Denoise_pushButton_PlayAudio_before.setObjectName(u"Denoise_pushButton_PlayAudio_before")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Denoise_pushButton_PlayAudio_before.sizePolicy().hasHeightForWidth())
        self.Denoise_pushButton_PlayAudio_before.setSizePolicy(sizePolicy)
        self.Denoise_pushButton_PlayAudio_before.setMinimumSize(QSize(20, 20))
        self.Denoise_pushButton_PlayAudio_before.setBaseSize(QSize(12, 12))
        font5 = QFont()
        font5.setFamily(u"MicrosoftJhengHei")
        self.Denoise_pushButton_PlayAudio_before.setFont(font5)
        self.Denoise_pushButton_PlayAudio_before.setStyleSheet(u"QPushButton {\n"
"	border-radius:7px;\n"
"	border:2px soild;\n"
"	margin-left:15px;\n"
"	margin-right:15px;\n"
"	margin-bottom:2px;\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid #e4e4e1;\n"
"	background-color: #e4e4e1;\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid #eeeeec;\n"
"	background-color: #eeeeec;\n"
"}\n"
"")
        icon8 = QIcon()
        icon8.addFile(u"icons/1x/play-button-circled.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Denoise_pushButton_PlayAudio_before.setIcon(icon8)
        self.Denoise_pushButton_PlayAudio_before.setIconSize(QSize(21, 21))

        self.horizontalLayout_19.addWidget(self.Denoise_pushButton_PlayAudio_before)

        self.Denoise_label_AudioTime_before = QLabel(self.horizontalFrame_4)
        self.Denoise_label_AudioTime_before.setObjectName(u"Denoise_label_AudioTime_before")
        self.Denoise_label_AudioTime_before.setFont(font4)
        self.Denoise_label_AudioTime_before.setStyleSheet(u"margin-right:0 px;\n"
"font: italic 12pt \"Smiley Sans\";")

        self.horizontalLayout_19.addWidget(self.Denoise_label_AudioTime_before)

        self.Denoise_Slider_before = QSlider(self.horizontalFrame_4)
        self.Denoise_Slider_before.setObjectName(u"Denoise_Slider_before")
        self.Denoise_Slider_before.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    height:5px;\n"
"    background: #04130a;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background:#fbd411;\n"
"    width: 10px;\n"
"margin:-8px 0\n"
"}")
        self.Denoise_Slider_before.setOrientation(Qt.Horizontal)

        self.horizontalLayout_19.addWidget(self.Denoise_Slider_before)

        self.Denoise_pushButton_VolumeAdjustment_before = QPushButton(self.horizontalFrame_4)
        self.Denoise_pushButton_VolumeAdjustment_before.setObjectName(u"Denoise_pushButton_VolumeAdjustment_before")
        self.Denoise_pushButton_VolumeAdjustment_before.setStyleSheet(u"\n"
"QPushButton {\n"
"	border-radius:7px;\n"
"	border:2px soild;\n"
"	margin-left:15px;\n"
"	margin-right:15px;\n"
"	margin-bottom:2px;\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid #e4e4e1;\n"
"	background-color: #e4e4e1;\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid #eeeeec;\n"
"	background-color: #eeeeec;\n"
"}\n"
"")
        icon9 = QIcon()
        icon9.addFile(u"icons/1x/speaker.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Denoise_pushButton_VolumeAdjustment_before.setIcon(icon9)

        self.horizontalLayout_19.addWidget(self.Denoise_pushButton_VolumeAdjustment_before)


        self.horizontalLayout_21.addWidget(self.horizontalFrame_4)


        self.verticalLayout_5.addWidget(self.horizontalFrame)

        self.frame_2 = QFrame(self.groupBox_2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.Denoise_pushButton_StartDenoising = QPushButton(self.frame_2)
        self.Denoise_pushButton_StartDenoising.setObjectName(u"Denoise_pushButton_StartDenoising")
        sizePolicy.setHeightForWidth(self.Denoise_pushButton_StartDenoising.sizePolicy().hasHeightForWidth())
        self.Denoise_pushButton_StartDenoising.setSizePolicy(sizePolicy)
        self.Denoise_pushButton_StartDenoising.setMinimumSize(QSize(44, 0))
        self.Denoise_pushButton_StartDenoising.setSizeIncrement(QSize(0, 0))
        self.Denoise_pushButton_StartDenoising.setFont(font2)
        self.Denoise_pushButton_StartDenoising.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"	height:45px;\n"
"	border-radius:20px;\n"
"	margin-left:20px;\n"
"	margin-right:25px;\n"
"	background:#dcd7d7;\n"
"	width:140px;\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid #e4e4e1;\n"
"	background-color: #e4e4e1;\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid #eeeeec;\n"
"	background-color: #eeeeec;\n"
"}")
        self.Denoise_pushButton_StartDenoising.setIcon(icon5)

        self.horizontalLayout_23.addWidget(self.Denoise_pushButton_StartDenoising)


        self.verticalLayout_5.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.groupBox_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"QWeight{\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: #000000;\n"
"}\n"
"")
        self.horizontalLayout_35 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalFrame_5 = QFrame(self.frame_3)
        self.horizontalFrame_5.setObjectName(u"horizontalFrame_5")
        self.horizontalFrame_5.setMinimumSize(QSize(0, 40))
        self.horizontalFrame_5.setMaximumSize(QSize(16777215, 40))
        self.horizontalFrame_5.setStyleSheet(u"background-color:#ddddd9;\n"
"height:35px;\n"
"border-radius:17px;\n"
"margin-left:20px;\n"
"margin-right:20px;")
        self.horizontalLayout_33 = QHBoxLayout(self.horizontalFrame_5)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.Denoise_pushButton_PlayAudio_after = QPushButton(self.horizontalFrame_5)
        self.Denoise_pushButton_PlayAudio_after.setObjectName(u"Denoise_pushButton_PlayAudio_after")
        self.Denoise_pushButton_PlayAudio_after.setMinimumSize(QSize(15, 15))
        self.Denoise_pushButton_PlayAudio_after.setBaseSize(QSize(12, 12))
        self.Denoise_pushButton_PlayAudio_after.setFont(font5)
        self.Denoise_pushButton_PlayAudio_after.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"\n"
"	border:2px soild;\n"
"	border-radius:7px;\n"
"	margin-left:25px;\n"
"	margin-right:5px;\n"
"	margin-bottom:2px;\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid #e4e4e1;\n"
"	background-color: #e4e4e1;\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid #eeeeec;\n"
"	background-color: #eeeeec;\n"
"}\n"
"")
        self.Denoise_pushButton_PlayAudio_after.setIcon(icon8)

        self.horizontalLayout_33.addWidget(self.Denoise_pushButton_PlayAudio_after)

        self.Denoise_label_AudioTime_after = QLabel(self.horizontalFrame_5)
        self.Denoise_label_AudioTime_after.setObjectName(u"Denoise_label_AudioTime_after")
        self.Denoise_label_AudioTime_after.setFont(font4)
        self.Denoise_label_AudioTime_after.setStyleSheet(u"margin-right:10px;\n"
"font: italic 12pt \"Smiley Sans\";\n"
"")

        self.horizontalLayout_33.addWidget(self.Denoise_label_AudioTime_after)

        self.Denoise_Slider_after = QSlider(self.horizontalFrame_5)
        self.Denoise_Slider_after.setObjectName(u"Denoise_Slider_after")
        self.Denoise_Slider_after.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    height:5px;\n"
"    background: #04130a;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background:#fbd411;\n"
"    width: 10px;\n"
"margin:-8px 0\n"
"}")
        self.Denoise_Slider_after.setOrientation(Qt.Horizontal)

        self.horizontalLayout_33.addWidget(self.Denoise_Slider_after)

        self.Denoise_pushButton_VolumeAdjustment_after = QPushButton(self.horizontalFrame_5)
        self.Denoise_pushButton_VolumeAdjustment_after.setObjectName(u"Denoise_pushButton_VolumeAdjustment_after")
        self.Denoise_pushButton_VolumeAdjustment_after.setStyleSheet(u"\n"
"QPushButton {\n"
"	border:2px soild;\n"
"	border-radius:8px;\n"
"	margin-right:5px;\n"
"	margin-left:10px;\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid #e4e4e1;\n"
"	background-color: #e4e4e1;\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid #eeeeec;\n"
"	background-color: #eeeeec;\n"
"}\n"
"")
        self.Denoise_pushButton_VolumeAdjustment_after.setIcon(icon9)

        self.horizontalLayout_33.addWidget(self.Denoise_pushButton_VolumeAdjustment_after)

        self.Denoise_pushButton_more = QPushButton(self.horizontalFrame_5)
        self.Denoise_pushButton_more.setObjectName(u"Denoise_pushButton_more")
        self.Denoise_pushButton_more.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"	font: italic 14pt \"Smiley Sans\";\n"
"	background-color:#ddddd9;\n"
"	border-radius:9px;\n"
"	margin-left:5px;\n"
"	margin-right:10px;\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid #e4e4e1;\n"
"	background-color: #e4e4e1;\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid #eeeeec;\n"
"	background-color: #eeeeec;\n"
"}\n"
"")
        icon10 = QIcon()
        icon10.addFile(u"icons/1x/menu-vertical.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Denoise_pushButton_more.setIcon(icon10)
        self.horizontalLayout_34 = QHBoxLayout(self.Denoise_pushButton_more)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")

        self.horizontalLayout_33.addWidget(self.Denoise_pushButton_more)


        self.horizontalLayout_35.addWidget(self.horizontalFrame_5)


        self.verticalLayout_5.addWidget(self.frame_3)

        self.Denoise_textBrowser = QTextBrowser(self.groupBox_2)
        self.Denoise_textBrowser.setObjectName(u"Denoise_textBrowser")
        self.Denoise_textBrowser.setMinimumSize(QSize(0, 165))
        self.Denoise_textBrowser.setMaximumSize(QSize(16777215, 170))
        self.Denoise_textBrowser.setFont(font)
        self.Denoise_textBrowser.setAutoFillBackground(False)
        self.Denoise_textBrowser.setStyleSheet(u"QTextBrowser{\n"
"border: 2px solid #cccccc;\n"
"border-radius: 5px;	\n"
"}\n"
"QScrollBar:vertical {\n"
"	background:#e4e9cd;\n"
"    width:20px;\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background:#645c0c;\n"
"}\n"
"QScrollBar::add-page:vertical {\n"
" 	background:#22a241;\n"
"}\n"
"QScrollBar::sub-page:vertical {\n"
" 	background:#fbd411;\n"
"}\n"
"")

        self.verticalLayout_5.addWidget(self.Denoise_textBrowser)


        self.horizontalLayout_29.addWidget(self.groupBox_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer)

        self.Denoise_frame_2 = QFrame(self.Denoise_frame_1)
        self.Denoise_frame_2.setObjectName(u"Denoise_frame_2")
        self.Denoise_frame_2.setMinimumSize(QSize(230, 0))
        self.Denoise_frame_2.setMaximumSize(QSize(230, 16777215))
        self.Denoise_frame_2.setFrameShape(QFrame.StyledPanel)
        self.Denoise_frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.Denoise_frame_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.Denoise_widget_1 = QWidget(self.Denoise_frame_2)
        self.Denoise_widget_1.setObjectName(u"Denoise_widget_1")
        self.Denoise_widget_1.setMinimumSize(QSize(181, 0))
        self.Denoise_widget_1.setFont(font)
        self.verticalLayout_26 = QVBoxLayout(self.Denoise_widget_1)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.Denoise_label_LoadtheModel = QLabel(self.Denoise_widget_1)
        self.Denoise_label_LoadtheModel.setObjectName(u"Denoise_label_LoadtheModel")
        self.Denoise_label_LoadtheModel.setEnabled(True)
        self.Denoise_label_LoadtheModel.setFont(font4)
        self.Denoise_label_LoadtheModel.setStyleSheet(u"")
        self.Denoise_label_LoadtheModel.setScaledContents(False)
        self.Denoise_label_LoadtheModel.setMargin(5)

        self.verticalLayout_26.addWidget(self.Denoise_label_LoadtheModel)

        self.Denoise_pushButton_SelectTheModel = QPushButton(self.Denoise_widget_1)
        self.Denoise_pushButton_SelectTheModel.setObjectName(u"Denoise_pushButton_SelectTheModel")
        self.Denoise_pushButton_SelectTheModel.setMinimumSize(QSize(0, 28))
        self.Denoise_pushButton_SelectTheModel.setFont(font)
        self.Denoise_pushButton_SelectTheModel.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid #eacd13;\n"
"	border-radius: 5px;	\n"
"	color:#04130a;\n"
"	background-color: #eacd13;\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid #fbd411;\n"
"	background-color: #fbd411;\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid #f6e56a;\n"
"	background-color: #f6e56a;\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")

        self.verticalLayout_26.addWidget(self.Denoise_pushButton_SelectTheModel)

        self.model_path_se_edit = QLineEdit(self.Denoise_widget_1)
        self.model_path_se_edit.setObjectName(u"model_path_se_edit")
        self.model_path_se_edit.setMinimumSize(QSize(0, 30))
        self.model_path_se_edit.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_26.addWidget(self.model_path_se_edit)

        self.Denoise_pushButton_StartLoading = QPushButton(self.Denoise_widget_1)
        self.Denoise_pushButton_StartLoading.setObjectName(u"Denoise_pushButton_StartLoading")
        self.Denoise_pushButton_StartLoading.setMinimumSize(QSize(0, 28))
        self.Denoise_pushButton_StartLoading.setFont(font)
        self.Denoise_pushButton_StartLoading.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid #eacd13;\n"
"	border-radius: 5px;	\n"
"	color:#04130a;\n"
"	background-color: #eacd13;\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid #fbd411;\n"
"	background-color: #fbd411;\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid #f6e56a;\n"
"	background-color: #f6e56a;\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")

        self.verticalLayout_26.addWidget(self.Denoise_pushButton_StartLoading)


        self.verticalLayout_6.addWidget(self.Denoise_widget_1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_6)


        self.horizontalLayout_29.addWidget(self.Denoise_frame_2)


        self.verticalLayout_16.addWidget(self.Denoise_frame_1)

        self.stackedWidget.addWidget(self.page_Denoise)
        self.page_TextToSpeech = QWidget()
        self.page_TextToSpeech.setObjectName(u"page_TextToSpeech")
        self.page_TextToSpeech.setMouseTracking(True)
        self.page_TextToSpeech.setStyleSheet(u"background:#e4e9cd;")
        self.horizontalLayout_32 = QHBoxLayout(self.page_TextToSpeech)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.frame_TextToSpeech = QFrame(self.page_TextToSpeech)
        self.frame_TextToSpeech.setObjectName(u"frame_TextToSpeech")
        self.frame_TextToSpeech.setFont(font)
        self.frame_TextToSpeech.setFrameShape(QFrame.NoFrame)
        self.frame_TextToSpeech.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_TextToSpeech)
        self.horizontalLayout_30.setSpacing(0)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.verticalFrame = QFrame(self.frame_TextToSpeech)
        self.verticalFrame.setObjectName(u"verticalFrame")
        self.verticalFrame.setFont(font)
        self.verticalFrame.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_4 = QVBoxLayout(self.verticalFrame)
        self.verticalLayout_4.setSpacing(7)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.TTS_label_Title = QLabel(self.verticalFrame)
        self.TTS_label_Title.setObjectName(u"TTS_label_Title")
        self.TTS_label_Title.setFont(font1)
        self.TTS_label_Title.setStyleSheet(u"margin-bottom:10px;")

        self.verticalLayout_4.addWidget(self.TTS_label_Title)

        self.TTS_textEdit_Text = QTextEdit(self.verticalFrame)
        self.TTS_textEdit_Text.setObjectName(u"TTS_textEdit_Text")
        self.TTS_textEdit_Text.setFont(font2)
        self.TTS_textEdit_Text.setStyleSheet(u"QTextEdit {\n"
"	color:#04130a;\n"
"	border:2px solid #f6e56a;\n"
"	border-radius:4px;\n"
"	background:#f6e56a;\n"
"\n"
"}\n"
"\n"
"QTextEdit:disabled {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid #645c0c;\n"
"	border-radius:4px;\n"
"	background:#645c0c;\n"
"}")

        self.verticalLayout_4.addWidget(self.TTS_textEdit_Text)

        self.horizontalFrame_2 = QFrame(self.verticalFrame)
        self.horizontalFrame_2.setObjectName(u"horizontalFrame_2")
        self.horizontalFrame_2.setFont(font)
        self.horizontalFrame_2.setStyleSheet(u"height:37px;\n"
"margin-bottom:7px;\n"
"margin-top:7px;")
        self.horizontalFrame_2.setFrameShape(QFrame.StyledPanel)
        self.horizontalFrame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.horizontalFrame_2)
        self.verticalLayout_24.setSpacing(7)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.pushButton_29 = QPushButton(self.horizontalFrame_2)
        self.pushButton_29.setObjectName(u"pushButton_29")
        self.pushButton_29.setMinimumSize(QSize(0, 24))
        font6 = QFont()
        font6.setFamily(u"Smiley Sans")
        font6.setPointSize(12)
        font6.setItalic(True)
        self.pushButton_29.setFont(font6)
        self.pushButton_29.setStyleSheet(u"height:50px;\n"
"margin-bottom:3px;\n"
"margin-top:3px;\n"
"border-radius:5px;")
        self.horizontalLayout_31 = QHBoxLayout(self.pushButton_29)
        self.horizontalLayout_31.setSpacing(46)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(28, -1, 28, 5)
        self.TTS_pushButton_GenerateSpeech = QPushButton(self.pushButton_29)
        self.TTS_pushButton_GenerateSpeech.setObjectName(u"TTS_pushButton_GenerateSpeech")
        self.TTS_pushButton_GenerateSpeech.setMinimumSize(QSize(0, 35))
        self.TTS_pushButton_GenerateSpeech.setFont(font6)
        self.TTS_pushButton_GenerateSpeech.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid #eacd13;\n"
"	border-radius: 15px;	\n"
"	color:#04130a;\n"
"	background-color: #eacd13;\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid #fbd411;\n"
"	background-color: #fbd411;\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid #f6e56a;\n"
"	background-color: #f6e56a;\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")

        self.horizontalLayout_31.addWidget(self.TTS_pushButton_GenerateSpeech)

        self.TTS_pushButton_FastGenerate = QPushButton(self.pushButton_29)
        self.TTS_pushButton_FastGenerate.setObjectName(u"TTS_pushButton_FastGenerate")
        self.TTS_pushButton_FastGenerate.setMinimumSize(QSize(0, 24))
        self.TTS_pushButton_FastGenerate.setFont(font6)
        self.TTS_pushButton_FastGenerate.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid #eacd13;\n"
"	border-radius: 15px;	\n"
"	color:#04130a;\n"
"	background-color: #eacd13;\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid #fbd411;\n"
"	background-color: #fbd411;\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid #f6e56a;\n"
"	background-color: #f6e56a;\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")

        self.horizontalLayout_31.addWidget(self.TTS_pushButton_FastGenerate)

        self.TTS_pushButton_Clear = QPushButton(self.pushButton_29)
        self.TTS_pushButton_Clear.setObjectName(u"TTS_pushButton_Clear")
        self.TTS_pushButton_Clear.setMinimumSize(QSize(0, 24))
        self.TTS_pushButton_Clear.setFont(font6)
        self.TTS_pushButton_Clear.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid #eacd13;\n"
"	border-radius: 15px;	\n"
"	color:#04130a;\n"
"	background-color: #eacd13;\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid #fbd411;\n"
"	background-color: #fbd411;\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid #f6e56a;\n"
"	background-color: #f6e56a;\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")

        self.horizontalLayout_31.addWidget(self.TTS_pushButton_Clear)


        self.verticalLayout_24.addWidget(self.pushButton_29)


        self.verticalLayout_4.addWidget(self.horizontalFrame_2)

        self.horizontalFrame0 = QFrame(self.verticalFrame)
        self.horizontalFrame0.setObjectName(u"horizontalFrame0")
        self.horizontalFrame0.setMinimumSize(QSize(0, 40))
        self.horizontalFrame0.setMaximumSize(QSize(16777215, 40))
        self.horizontalFrame0.setFont(font)
        self.horizontalFrame0.setStyleSheet(u"background-color:#ddddd9;\n"
"height:35px;\n"
"border-radius:17px;\n"
"margin-left:20px;\n"
"margin-right:20px;")
        self.horizontalLayout_0 = QHBoxLayout(self.horizontalFrame0)
        self.horizontalLayout_0.setObjectName(u"horizontalLayout_0")
        self.TTS_pushButton_PlayAudio = QPushButton(self.horizontalFrame0)
        self.TTS_pushButton_PlayAudio.setObjectName(u"TTS_pushButton_PlayAudio")
        self.TTS_pushButton_PlayAudio.setMinimumSize(QSize(15, 15))
        self.TTS_pushButton_PlayAudio.setBaseSize(QSize(12, 12))
        font7 = QFont()
        font7.setFamily(u"Smiley Sans")
        font7.setPointSize(11)
        font7.setItalic(True)
        self.TTS_pushButton_PlayAudio.setFont(font7)
        self.TTS_pushButton_PlayAudio.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"	border:2px soild;\n"
"	border-radius:7px;\n"
"	margin-left:25px;\n"
"	margin-right:5px;\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid #e4e4e1;\n"
"	background-color: #e4e4e1;\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid #eeeeec;\n"
"	background-color: #eeeeec;\n"
"}\n"
"")
        self.TTS_pushButton_PlayAudio.setIcon(icon8)

        self.horizontalLayout_0.addWidget(self.TTS_pushButton_PlayAudio)

        self.TTS_label_AudioTime = QLabel(self.horizontalFrame0)
        self.TTS_label_AudioTime.setObjectName(u"TTS_label_AudioTime")
        self.TTS_label_AudioTime.setFont(font4)
        self.TTS_label_AudioTime.setStyleSheet(u"margin-right:9 px;\n"
"font: italic 12pt \"Smiley Sans\";")

        self.horizontalLayout_0.addWidget(self.TTS_label_AudioTime)

        self.TTS_Slider = QSlider(self.horizontalFrame0)
        self.TTS_Slider.setObjectName(u"TTS_Slider")
        self.TTS_Slider.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    height:5px;\n"
"    background: #04130a;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background:#fbd411;\n"
"    width: 10px;\n"
"	margin:-8px 0\n"
"\n"
"\n"
"}\n"
"\n"
"QSlider::add-page:horizondal {\n"
"    background:#04130a;\n"
"}\n"
"\n"
"QSlider::sub-page:horizondal {\n"
"    background:#04130a;\n"
"}")
        self.TTS_Slider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_0.addWidget(self.TTS_Slider)

        self.TTS_pushButton_more = QPushButton(self.horizontalFrame0)
        self.TTS_pushButton_more.setObjectName(u"TTS_pushButton_more")
        self.TTS_pushButton_more.setFont(font)
        self.TTS_pushButton_more.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"	border:1px soild;\n"
"	border-radius:7px;\n"
"	margin-left:5px;\n"
"	margin-right:10px;\n"
"}\n"
"QPushButton:hover {\n"
"	border: 1px solid #e4e4e1;\n"
"	background-color: #e4e4e1;\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 1px solid #eeeeec;\n"
"	background-color: #eeeeec;\n"
"}\n"
"")
        self.TTS_pushButton_more.setIcon(icon10)
        self.horizontalLayout_20 = QHBoxLayout(self.TTS_pushButton_more)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")

        self.horizontalLayout_0.addWidget(self.TTS_pushButton_more)


        self.verticalLayout_4.addWidget(self.horizontalFrame0)

        self.TTS_textBrowser = QTextBrowser(self.verticalFrame)
        self.TTS_textBrowser.setObjectName(u"TTS_textBrowser")
        self.TTS_textBrowser.setMaximumSize(QSize(16777215, 150))
        self.TTS_textBrowser.setBaseSize(QSize(0, 0))
        self.TTS_textBrowser.setFont(font)
        self.TTS_textBrowser.setStyleSheet(u"QTextBrowser{\n"
"border: 2px solid #cccccc;\n"
"border-radius: 5px;	\n"
"}\n"
"QScrollBar:vertical {\n"
"	background:#e4e9cd;\n"
"    width:20px;\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background:#645c0c;\n"
"}\n"
"QScrollBar::add-page:vertical {\n"
" 	background:#22a241;\n"
"}\n"
"QScrollBar::sub-page:vertical {\n"
" 	background:#fbd411;\n"
"}\n"
"")
        self.TTS_textBrowser.setFrameShape(QFrame.StyledPanel)
        self.TTS_textBrowser.setLineWidth(1)

        self.verticalLayout_4.addWidget(self.TTS_textBrowser)


        self.horizontalLayout_30.addWidget(self.verticalFrame)

        self.verticalWidget_2 = QWidget(self.frame_TextToSpeech)
        self.verticalWidget_2.setObjectName(u"verticalWidget_2")
        self.verticalWidget_2.setMinimumSize(QSize(200, 0))
        self.verticalWidget_2.setMaximumSize(QSize(200, 576))
        self.verticalWidget_2.setFont(font)
        self.verticalLayout_15 = QVBoxLayout(self.verticalWidget_2)
        self.verticalLayout_15.setSpacing(11)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setSizeConstraint(QLayout.SetFixedSize)
        self.verticalLayout_15.setContentsMargins(4, 1, -1, 5)
        self.TTS_label_SelectTheModel = QLabel(self.verticalWidget_2)
        self.TTS_label_SelectTheModel.setObjectName(u"TTS_label_SelectTheModel")
        self.TTS_label_SelectTheModel.setFont(font4)
        self.TTS_label_SelectTheModel.setStyleSheet(u"")
        self.TTS_label_SelectTheModel.setScaledContents(False)
        self.TTS_label_SelectTheModel.setMargin(5)

        self.verticalLayout_15.addWidget(self.TTS_label_SelectTheModel)

        self.TTS_pushButton_SelcetTheModel = QPushButton(self.verticalWidget_2)
        self.TTS_pushButton_SelcetTheModel.setObjectName(u"TTS_pushButton_SelcetTheModel")
        self.TTS_pushButton_SelcetTheModel.setMinimumSize(QSize(0, 30))
        self.TTS_pushButton_SelcetTheModel.setFont(font)
        self.TTS_pushButton_SelcetTheModel.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid #eacd13;\n"
"	border-radius: 5px;	\n"
"	color:#04130a;\n"
"	background-color: #eacd13;\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid #fbd411;\n"
"	background-color: #fbd411;\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid #f6e56a;\n"
"	background-color: #f6e56a;\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")

        self.verticalLayout_15.addWidget(self.TTS_pushButton_SelcetTheModel)

        self.mdoel_path_tts_edit = QLineEdit(self.verticalWidget_2)
        self.mdoel_path_tts_edit.setObjectName(u"mdoel_path_tts_edit")
        self.mdoel_path_tts_edit.setMinimumSize(QSize(0, 30))
        self.mdoel_path_tts_edit.setMaximumSize(QSize(16777215, 30))
        self.mdoel_path_tts_edit.setReadOnly(False)

        self.verticalLayout_15.addWidget(self.mdoel_path_tts_edit)

        self.TTS_pushButton_StartLoading = QPushButton(self.verticalWidget_2)
        self.TTS_pushButton_StartLoading.setObjectName(u"TTS_pushButton_StartLoading")
        self.TTS_pushButton_StartLoading.setMinimumSize(QSize(0, 28))
        self.TTS_pushButton_StartLoading.setFont(font)
        self.TTS_pushButton_StartLoading.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid #eacd13;\n"
"	border-radius: 5px;	\n"
"	color:#04130a;\n"
"	background-color: #eacd13;\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid #fbd411;\n"
"	background-color: #fbd411;\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid #f6e56a;\n"
"	background-color: #f6e56a;\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")

        self.verticalLayout_15.addWidget(self.TTS_pushButton_StartLoading)

        self.frame_4 = QFrame(self.verticalWidget_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_4)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.TTS_label_SelectRole = QLabel(self.frame_4)
        self.TTS_label_SelectRole.setObjectName(u"TTS_label_SelectRole")
        self.TTS_label_SelectRole.setFont(font4)
        self.TTS_label_SelectRole.setStyleSheet(u"")
        self.TTS_label_SelectRole.setMargin(5)

        self.verticalLayout_27.addWidget(self.TTS_label_SelectRole)

        self.TTS_comboBox_SelectRole = QComboBox(self.frame_4)
        self.TTS_comboBox_SelectRole.setObjectName(u"TTS_comboBox_SelectRole")
        self.TTS_comboBox_SelectRole.setMinimumSize(QSize(0, 30))
        self.TTS_comboBox_SelectRole.setFont(font)
        self.TTS_comboBox_SelectRole.setStyleSheet(u"QComboBox {\n"
"	border: 2px solid #eacd13;\n"
"	border-radius: 5px;	\n"
"	color:#04130a;\n"
"	background-color: #eacd13;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"	border: 2px solid #f6e56a;\n"
"	border-radius: 5px;	\n"
"	color:#04130a;\n"
"	background-color: #f6e56a;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"	background: #eacd13;\n"
"}\n"
"\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background:#eacd13;\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 5px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 5px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url"
                        "(icons/1x/arrow.png);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    background:#eacd13;\n"
"}\n"
"\n"
"")

        self.verticalLayout_27.addWidget(self.TTS_comboBox_SelectRole)


        self.verticalLayout_15.addWidget(self.frame_4)

        self.TTS_label_SpeedControl = QLabel(self.verticalWidget_2)
        self.TTS_label_SpeedControl.setObjectName(u"TTS_label_SpeedControl")
        self.TTS_label_SpeedControl.setFont(font4)
        self.TTS_label_SpeedControl.setStyleSheet(u"")
        self.TTS_label_SpeedControl.setMargin(5)

        self.verticalLayout_15.addWidget(self.TTS_label_SpeedControl)

        self.TTS_Slider_SpeedControl = QSlider(self.verticalWidget_2)
        self.TTS_Slider_SpeedControl.setObjectName(u"TTS_Slider_SpeedControl")
        self.TTS_Slider_SpeedControl.setFont(font)
        self.TTS_Slider_SpeedControl.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    height:5px;\n"
"    background: #04130a;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background:#fbd411;\n"
"    width: 10px;\n"
"margin:-8px 0\n"
"}\n"
"\n"
"QSlider::add-page:horizondal {\n"
"    background:#04130a;\n"
"}\n"
"\n"
"QSlider::sub-page:horizondal {\n"
"    background:#04130a;\n"
"}")
        self.TTS_Slider_SpeedControl.setOrientation(Qt.Horizontal)

        self.verticalLayout_15.addWidget(self.TTS_Slider_SpeedControl)

        self.TTS_label_EmotionalControl = QLabel(self.verticalWidget_2)
        self.TTS_label_EmotionalControl.setObjectName(u"TTS_label_EmotionalControl")
        self.TTS_label_EmotionalControl.setFont(font4)
        self.TTS_label_EmotionalControl.setStyleSheet(u"")
        self.TTS_label_EmotionalControl.setMargin(4)

        self.verticalLayout_15.addWidget(self.TTS_label_EmotionalControl)

        self.TTS_Slider_EmotionalControl = QSlider(self.verticalWidget_2)
        self.TTS_Slider_EmotionalControl.setObjectName(u"TTS_Slider_EmotionalControl")
        self.TTS_Slider_EmotionalControl.setFont(font)
        self.TTS_Slider_EmotionalControl.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    height:5px;\n"
"    background: #04130a;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background:#fbd411;\n"
"    width: 10px;\n"
"margin:-8px 0\n"
"}\n"
"\n"
"QSlider::add-page:horizondal {\n"
"    background:#04130a;\n"
"}\n"
"\n"
"QSlider::sub-page:horizondal {\n"
"    background:#04130a;\n"
"}")
        self.TTS_Slider_EmotionalControl.setOrientation(Qt.Horizontal)

        self.verticalLayout_15.addWidget(self.TTS_Slider_EmotionalControl)

        self.TTS_label_VolumeAdjustment = QLabel(self.verticalWidget_2)
        self.TTS_label_VolumeAdjustment.setObjectName(u"TTS_label_VolumeAdjustment")
        self.TTS_label_VolumeAdjustment.setFont(font4)
        self.TTS_label_VolumeAdjustment.setStyleSheet(u"")
        self.TTS_label_VolumeAdjustment.setMargin(2)

        self.verticalLayout_15.addWidget(self.TTS_label_VolumeAdjustment)

        self.TTS_Slider_VolumeAdjustment = QSlider(self.verticalWidget_2)
        self.TTS_Slider_VolumeAdjustment.setObjectName(u"TTS_Slider_VolumeAdjustment")
        self.TTS_Slider_VolumeAdjustment.setFont(font)
        self.TTS_Slider_VolumeAdjustment.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    height:5px;\n"
"    background: #04130a;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background:#fbd411;\n"
"    width: 10px;\n"
"margin:-8px 0\n"
"}\n"
"\n"
"QSlider::add-page:horizondal {\n"
"    background:#04130a;\n"
"}\n"
"\n"
"QSlider::sub-page:horizondal {\n"
"    background:#04130a;\n"
"}")
        self.TTS_Slider_VolumeAdjustment.setOrientation(Qt.Horizontal)

        self.verticalLayout_15.addWidget(self.TTS_Slider_VolumeAdjustment)

        self.verticalLayout_15.setStretch(10, 9)

        self.horizontalLayout_30.addWidget(self.verticalWidget_2)


        self.horizontalLayout_32.addWidget(self.frame_TextToSpeech)

        self.stackedWidget.addWidget(self.page_TextToSpeech)
        self.page_ImageRefinement = QWidget()
        self.page_ImageRefinement.setObjectName(u"page_ImageRefinement")
        self.page_ImageRefinement.setStyleSheet(u"background:#e4e9cd;")
        self.horizontalLayout_38 = QHBoxLayout(self.page_ImageRefinement)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.frame_7 = QFrame(self.page_ImageRefinement)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFont(font)
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Sunken)
        self.verticalLayout_14 = QVBoxLayout(self.frame_7)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.Image_label_Title = QLabel(self.frame_7)
        self.Image_label_Title.setObjectName(u"Image_label_Title")
        self.Image_label_Title.setFont(font1)

        self.verticalLayout_14.addWidget(self.Image_label_Title)

        self.Image_widget_ImageRepaired = QWidget(self.frame_7)
        self.Image_widget_ImageRepaired.setObjectName(u"Image_widget_ImageRepaired")
        self.Image_widget_ImageRepaired.setFont(font)
        self.horizontalLayout_36 = QHBoxLayout(self.Image_widget_ImageRepaired)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.Image_graphicsView = QGraphicsView(self.Image_widget_ImageRepaired)
        self.Image_graphicsView.setObjectName(u"Image_graphicsView")
        self.Image_graphicsView.setStyleSheet(u"QGraphicsVier{\n"
"border: 2px solid;\n"
"border-radius: 5px;	\n"
"}")

        self.horizontalLayout_36.addWidget(self.Image_graphicsView)


        self.verticalLayout_14.addWidget(self.Image_widget_ImageRepaired)

        self.Image_Slider = QSlider(self.frame_7)
        self.Image_Slider.setObjectName(u"Image_Slider")
        self.Image_Slider.setFont(font)
        self.Image_Slider.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    height:5px;\n"
"    background: #04130a;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background:#fbd411;\n"
"    width: 10px;\n"
"margin:-8px 0\n"
"}\n"
"\n"
"QSlider::add-page:horizondal {\n"
"    background:#04130a;\n"
"}\n"
"\n"
"QSlider::sub-page:horizondal {\n"
"    background:#04130a;\n"
"}")
        self.Image_Slider.setOrientation(Qt.Horizontal)

        self.verticalLayout_14.addWidget(self.Image_Slider)

        self.frame_6 = QFrame(self.frame_7)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFont(font)
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_37.addItem(self.horizontalSpacer_10)

        self.Image_pushButton_StartRepairing = QPushButton(self.frame_6)
        self.Image_pushButton_StartRepairing.setObjectName(u"Image_pushButton_StartRepairing")
        self.Image_pushButton_StartRepairing.setMinimumSize(QSize(117, 33))
        self.Image_pushButton_StartRepairing.setMaximumSize(QSize(393, 16777215))
        self.Image_pushButton_StartRepairing.setFont(font7)
        self.Image_pushButton_StartRepairing.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid #eacd13;\n"
"	border-radius: 12px;	\n"
"	color:#04130a;\n"
"	background-color: #eacd13;\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid #fbd411;\n"
"	background-color: #fbd411;\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid #f6e56a;\n"
"	background-color: #f6e56a;\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 12px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")

        self.horizontalLayout_37.addWidget(self.Image_pushButton_StartRepairing)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_37.addItem(self.horizontalSpacer_11)

        self.Image_pushButton_Download = QPushButton(self.frame_6)
        self.Image_pushButton_Download.setObjectName(u"Image_pushButton_Download")
        self.Image_pushButton_Download.setMinimumSize(QSize(117, 31))
        self.Image_pushButton_Download.setFont(font2)
        self.Image_pushButton_Download.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid #eacd13;\n"
"	border-radius: 12px;	\n"
"	color:#04130a;\n"
"	background-color: #eacd13;\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid #fbd411;\n"
"	background-color: #fbd411;\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid #f6e56a;\n"
"	background-color: #f6e56a;\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 12px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")

        self.horizontalLayout_37.addWidget(self.Image_pushButton_Download)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_37.addItem(self.horizontalSpacer_13)

        self.horizontalLayout_37.setStretch(0, 1)
        self.horizontalLayout_37.setStretch(1, 1)
        self.horizontalLayout_37.setStretch(2, 1)
        self.horizontalLayout_37.setStretch(3, 1)
        self.horizontalLayout_37.setStretch(4, 1)

        self.verticalLayout_14.addWidget(self.frame_6)

        self.Image_textBrowser = QTextBrowser(self.frame_7)
        self.Image_textBrowser.setObjectName(u"Image_textBrowser")
        self.Image_textBrowser.setMinimumSize(QSize(0, 180))
        self.Image_textBrowser.setMaximumSize(QSize(16777215, 180))
        self.Image_textBrowser.setFont(font)
        self.Image_textBrowser.setStyleSheet(u"QTextBrowser{\n"
"border: 2px solid #cccccc;\n"
"border-radius: 5px;	\n"
"}\n"
"QScrollBar:vertical {\n"
"	background:#e4e9cd;\n"
"    width:20px;\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background:#645c0c;\n"
"}\n"
"QScrollBar::add-page:vertical {\n"
" 	background:#22a241;\n"
"}\n"
"QScrollBar::sub-page:vertical {\n"
" 	background:#fbd411;\n"
"}\n"
"")

        self.verticalLayout_14.addWidget(self.Image_textBrowser)

        self.verticalLayout_14.setStretch(1, 7)
        self.verticalLayout_14.setStretch(3, 2)

        self.horizontalLayout_38.addWidget(self.frame_7)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_38.addItem(self.horizontalSpacer_3)

        self.frame_5 = QFrame(self.page_ImageRefinement)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(240, 0))
        self.frame_5.setMaximumSize(QSize(240, 16777215))
        self.frame_5.setFont(font)
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Sunken)
        self.verticalLayout_23 = QVBoxLayout(self.frame_5)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.frame_8 = QFrame(self.frame_5)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFont(font)
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Sunken)
        self.verticalLayout_19 = QVBoxLayout(self.frame_8)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.Image_label_SelectTheModel = QLabel(self.frame_8)
        self.Image_label_SelectTheModel.setObjectName(u"Image_label_SelectTheModel")
        self.Image_label_SelectTheModel.setFont(font4)
        self.Image_label_SelectTheModel.setStyleSheet(u"")
        self.Image_label_SelectTheModel.setScaledContents(False)
        self.Image_label_SelectTheModel.setMargin(5)

        self.verticalLayout_19.addWidget(self.Image_label_SelectTheModel)

        self.Image_pushButton_SelectTheModel = QPushButton(self.frame_8)
        self.Image_pushButton_SelectTheModel.setObjectName(u"Image_pushButton_SelectTheModel")
        self.Image_pushButton_SelectTheModel.setMinimumSize(QSize(0, 28))
        self.Image_pushButton_SelectTheModel.setFont(font)
        self.Image_pushButton_SelectTheModel.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid #eacd13;\n"
"	border-radius: 5px;	\n"
"	color:#04130a;\n"
"	background-color: #eacd13;\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid #fbd411;\n"
"	background-color: #fbd411;\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid #f6e56a;\n"
"	background-color: #f6e56a;\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")

        self.verticalLayout_19.addWidget(self.Image_pushButton_SelectTheModel)

        self.model_path_sr_edit = QLineEdit(self.frame_8)
        self.model_path_sr_edit.setObjectName(u"model_path_sr_edit")
        self.model_path_sr_edit.setMinimumSize(QSize(0, 30))
        self.model_path_sr_edit.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_19.addWidget(self.model_path_sr_edit)

        self.Image_pushButton_StartLoading = QPushButton(self.frame_8)
        self.Image_pushButton_StartLoading.setObjectName(u"Image_pushButton_StartLoading")
        self.Image_pushButton_StartLoading.setMinimumSize(QSize(0, 27))
        self.Image_pushButton_StartLoading.setFont(font2)
        self.Image_pushButton_StartLoading.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid #eacd13;\n"
"	border-radius: 5px;	\n"
"	color:#04130a;\n"
"	background-color: #eacd13;\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid #fbd411;\n"
"	background-color: #fbd411;\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid #f6e56a;\n"
"	background-color: #f6e56a;\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")

        self.verticalLayout_19.addWidget(self.Image_pushButton_StartLoading)

        self.verticalLayout_19.setStretch(0, 2)
        self.verticalLayout_19.setStretch(3, 2)

        self.verticalLayout_23.addWidget(self.frame_8)

        self.groupBox_5 = QGroupBox(self.frame_5)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setFont(font6)
        self.groupBox_5.setStyleSheet(u"text-align:center;\n"
"margin-top:20px;")
        self.verticalLayout_22 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.Image_pushButton_Upload = QPushButton(self.groupBox_5)
        self.Image_pushButton_Upload.setObjectName(u"Image_pushButton_Upload")
        self.Image_pushButton_Upload.setMinimumSize(QSize(178, 101))
        self.Image_pushButton_Upload.setBaseSize(QSize(0, 0))
        self.Image_pushButton_Upload.setFont(font)
        self.Image_pushButton_Upload.setStyleSheet(u"border-radius:5px;\n"
"\n"
"margin-top:20px;")
        icon11 = QIcon()
        icon11.addFile(u"icons/1x/picture.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Image_pushButton_Upload.setIcon(icon11)
        self.Image_pushButton_Upload.setIconSize(QSize(101, 101))
        self.Image_pushButton_Upload.setAutoRepeat(False)
        self.Image_pushButton_Upload.setAutoExclusive(False)

        self.verticalLayout_22.addWidget(self.Image_pushButton_Upload)

        self.label_6 = QLabel(self.groupBox_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 37))
        self.label_6.setFont(font2)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.label_6)

        self.verticalSpacer_2 = QSpacerItem(20, 48, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_22.addItem(self.verticalSpacer_2)


        self.verticalLayout_23.addWidget(self.groupBox_5)

        self.verticalLayout_23.setStretch(0, 3)
        self.verticalLayout_23.setStretch(1, 7)

        self.horizontalLayout_38.addWidget(self.frame_5)

        self.horizontalLayout_38.setStretch(0, 6)
        self.horizontalLayout_38.setStretch(2, 3)
        self.stackedWidget.addWidget(self.page_ImageRefinement)
        self.page_VoiceConversion = QWidget()
        self.page_VoiceConversion.setObjectName(u"page_VoiceConversion")
        self.page_VoiceConversion.setStyleSheet(u"background:#e4e9cd;")
        self.verticalLayout_9 = QVBoxLayout(self.page_VoiceConversion)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalFrame_3 = QFrame(self.page_VoiceConversion)
        self.horizontalFrame_3.setObjectName(u"horizontalFrame_3")
        self.horizontalFrame_3.setFont(font)
        self.horizontalLayout_22 = QHBoxLayout(self.horizontalFrame_3)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.verticalFrame_2 = QFrame(self.horizontalFrame_3)
        self.verticalFrame_2.setObjectName(u"verticalFrame_2")
        self.verticalFrame_2.setMaximumSize(QSize(16777215, 16777215))
        self.verticalFrame_2.setFont(font)
        self.verticalLayout_11 = QVBoxLayout(self.verticalFrame_2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.VC_label_Title = QLabel(self.verticalFrame_2)
        self.VC_label_Title.setObjectName(u"VC_label_Title")
        self.VC_label_Title.setMinimumSize(QSize(0, 55))
        self.VC_label_Title.setMaximumSize(QSize(16777215, 55))
        self.VC_label_Title.setFont(font1)

        self.verticalLayout_11.addWidget(self.VC_label_Title)

        self.verticalFrame0 = QFrame(self.verticalFrame_2)
        self.verticalFrame0.setObjectName(u"verticalFrame0")
        self.verticalFrame0.setFont(font)
        self.verticalLayout_12 = QVBoxLayout(self.verticalFrame0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.VC_pushButton_Upload = QPushButton(self.verticalFrame0)
        self.VC_pushButton_Upload.setObjectName(u"VC_pushButton_Upload")
        self.VC_pushButton_Upload.setMinimumSize(QSize(0, 30))
        self.VC_pushButton_Upload.setFont(font2)
        self.VC_pushButton_Upload.setStyleSheet(u"height:45px;\n"
"border-radius:13px;")
        icon12 = QIcon()
        icon12.addFile(u"icons/1x/icons8-microphone-22.png", QSize(), QIcon.Normal, QIcon.Off)
        self.VC_pushButton_Upload.setIcon(icon12)

        self.verticalLayout_12.addWidget(self.VC_pushButton_Upload)

        self.frame_11 = QFrame(self.verticalFrame0)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(0, 70))
        self.frame_11.setMaximumSize(QSize(16777215, 70))
        self.frame_11.setFont(font)
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalFrame_6 = QFrame(self.frame_11)
        self.horizontalFrame_6.setObjectName(u"horizontalFrame_6")
        self.horizontalFrame_6.setMinimumSize(QSize(0, 40))
        self.horizontalFrame_6.setMaximumSize(QSize(16777215, 40))
        self.horizontalFrame_6.setFont(font)
        self.horizontalFrame_6.setStyleSheet(u"background-color:#ddddd9;\n"
"height:55px;\n"
"border-radius:20px;\n"
"margin-left:20px;\n"
"margin-right:20px;")
        self.horizontalLayout_24 = QHBoxLayout(self.horizontalFrame_6)
        self.horizontalLayout_24.setSpacing(3)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(-1, 12, 17, -1)
        self.VC_pushButton_PlayAudio_before = QPushButton(self.horizontalFrame_6)
        self.VC_pushButton_PlayAudio_before.setObjectName(u"VC_pushButton_PlayAudio_before")
        self.VC_pushButton_PlayAudio_before.setMinimumSize(QSize(15, 15))
        self.VC_pushButton_PlayAudio_before.setBaseSize(QSize(12, 12))
        self.VC_pushButton_PlayAudio_before.setFont(font7)
        self.VC_pushButton_PlayAudio_before.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"	border:2px soild;\n"
"	border-radius:7px;\n"
"	margin-left:25px;\n"
"	margin-right:5px;\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid #e4e4e1;\n"
"	background-color: #e4e4e1;\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid #eeeeec;\n"
"	background-color: #eeeeec;\n"
"}\n"
"")
        self.VC_pushButton_PlayAudio_before.setIcon(icon8)

        self.horizontalLayout_24.addWidget(self.VC_pushButton_PlayAudio_before)

        self.VC_label_AudioTime_before = QLabel(self.horizontalFrame_6)
        self.VC_label_AudioTime_before.setObjectName(u"VC_label_AudioTime_before")
        self.VC_label_AudioTime_before.setFont(font4)
        self.VC_label_AudioTime_before.setStyleSheet(u"margin-right:9 px;\n"
"font: italic 12pt \"Smiley Sans\";")

        self.horizontalLayout_24.addWidget(self.VC_label_AudioTime_before)

        self.VC_Slider_before = QSlider(self.horizontalFrame_6)
        self.VC_Slider_before.setObjectName(u"VC_Slider_before")
        self.VC_Slider_before.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    height:5px;\n"
"    background: #04130a;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background:#fbd411;\n"
"    width: 10px;\n"
"margin:-8px 0\n"
"}")
        self.VC_Slider_before.setOrientation(Qt.Horizontal)

        self.horizontalLayout_24.addWidget(self.VC_Slider_before)

        self.VC_pushButton_VolumeAdjustment_before = QPushButton(self.horizontalFrame_6)
        self.VC_pushButton_VolumeAdjustment_before.setObjectName(u"VC_pushButton_VolumeAdjustment_before")
        self.VC_pushButton_VolumeAdjustment_before.setFont(font)
        self.VC_pushButton_VolumeAdjustment_before.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"	border:2px soild;\n"
"	border-radius:7px;\n"
"	margin-right:5px;\n"
"	margin-left:10px;\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid #e4e4e1;\n"
"	background-color: #e4e4e1;\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid #eeeeec;\n"
"	background-color: #eeeeec;\n"
"}\n"
"")
        self.VC_pushButton_VolumeAdjustment_before.setIcon(icon9)

        self.horizontalLayout_24.addWidget(self.VC_pushButton_VolumeAdjustment_before)


        self.horizontalLayout_25.addWidget(self.horizontalFrame_6)


        self.verticalLayout_12.addWidget(self.frame_11)

        self.horizontalWidget = QWidget(self.verticalFrame0)
        self.horizontalWidget.setObjectName(u"horizontalWidget")
        self.horizontalWidget.setMinimumSize(QSize(0, 80))
        self.horizontalWidget.setMaximumSize(QSize(16777215, 80))
        self.horizontalWidget.setFont(font)
        self.horizontalLayout_26 = QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.VC_pushButton_StartConversion = QPushButton(self.horizontalWidget)
        self.VC_pushButton_StartConversion.setObjectName(u"VC_pushButton_StartConversion")
        sizePolicy.setHeightForWidth(self.VC_pushButton_StartConversion.sizePolicy().hasHeightForWidth())
        self.VC_pushButton_StartConversion.setSizePolicy(sizePolicy)
        self.VC_pushButton_StartConversion.setMinimumSize(QSize(44, 0))
        self.VC_pushButton_StartConversion.setSizeIncrement(QSize(0, 0))
        self.VC_pushButton_StartConversion.setFont(font2)
        self.VC_pushButton_StartConversion.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"	height:45px;\n"
"	border-radius:20px;\n"
"	margin-left:20px;\n"
"	margin-right:25px;\n"
"	background:#dcd7d7;\n"
"	width:140px;\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid #e4e4e1;\n"
"	background-color: #e4e4e1;\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid #eeeeec;\n"
"	background-color: #eeeeec;\n"
"}")
        self.VC_pushButton_StartConversion.setIcon(icon5)

        self.horizontalLayout_26.addWidget(self.VC_pushButton_StartConversion)


        self.verticalLayout_12.addWidget(self.horizontalWidget)

        self.frame_13 = QFrame(self.verticalFrame0)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(0, 64))
        self.frame_13.setMaximumSize(QSize(16777215, 70))
        self.frame_13.setFont(font)
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_13)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.horizontalFrame_8 = QFrame(self.frame_13)
        self.horizontalFrame_8.setObjectName(u"horizontalFrame_8")
        self.horizontalFrame_8.setMaximumSize(QSize(16777215, 40))
        self.horizontalFrame_8.setFont(font)
        self.horizontalFrame_8.setStyleSheet(u"background-color:#ddddd9;\n"
"height:45px;\n"
"border-radius:20px;\n"
"margin-left:20px;\n"
"margin-right:20px;")
        self.horizontalLayout_27 = QHBoxLayout(self.horizontalFrame_8)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(10, 11, 13, 10)
        self.VC_pushButton_PlayAudio_after = QPushButton(self.horizontalFrame_8)
        self.VC_pushButton_PlayAudio_after.setObjectName(u"VC_pushButton_PlayAudio_after")
        self.VC_pushButton_PlayAudio_after.setMinimumSize(QSize(15, 15))
        self.VC_pushButton_PlayAudio_after.setBaseSize(QSize(12, 12))
        self.VC_pushButton_PlayAudio_after.setFont(font7)
        self.VC_pushButton_PlayAudio_after.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"	border:2px soild;\n"
"	border-radius:7px;\n"
"	margin-left:20px;\n"
"	margin-right:5px;\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid #e4e4e1;\n"
"	background-color: #e4e4e1;\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid #eeeeec;\n"
"	background-color: #eeeeec;\n"
"}")
        self.VC_pushButton_PlayAudio_after.setIcon(icon8)

        self.horizontalLayout_27.addWidget(self.VC_pushButton_PlayAudio_after)

        self.VC_label_AudioTime_after = QLabel(self.horizontalFrame_8)
        self.VC_label_AudioTime_after.setObjectName(u"VC_label_AudioTime_after")
        self.VC_label_AudioTime_after.setFont(font4)
        self.VC_label_AudioTime_after.setStyleSheet(u"margin-right:9 px;\n"
"font: italic 12pt \"Smiley Sans\";")

        self.horizontalLayout_27.addWidget(self.VC_label_AudioTime_after)

        self.VC_Slider_after = QSlider(self.horizontalFrame_8)
        self.VC_Slider_after.setObjectName(u"VC_Slider_after")
        self.VC_Slider_after.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    height:5px;\n"
"    background: #04130a;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background:#fbd411;\n"
"    width: 10px;\n"
"margin:-8px 0\n"
"}")
        self.VC_Slider_after.setOrientation(Qt.Horizontal)

        self.horizontalLayout_27.addWidget(self.VC_Slider_after)

        self.VC_pushButton_VolumeAdjustment_after = QPushButton(self.horizontalFrame_8)
        self.VC_pushButton_VolumeAdjustment_after.setObjectName(u"VC_pushButton_VolumeAdjustment_after")
        self.VC_pushButton_VolumeAdjustment_after.setFont(font)
        self.VC_pushButton_VolumeAdjustment_after.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"	border:2px soild;\n"
"	border-radius:7px;\n"
"	margin-right:5px;\n"
"	margin-left:0px;\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid #e4e4e1;\n"
"	background-color: #e4e4e1;\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid #eeeeec;\n"
"	background-color: #eeeeec;\n"
"}\n"
"")
        self.VC_pushButton_VolumeAdjustment_after.setIcon(icon9)

        self.horizontalLayout_27.addWidget(self.VC_pushButton_VolumeAdjustment_after)

        self.VC_pushButton_more = QPushButton(self.horizontalFrame_8)
        self.VC_pushButton_more.setObjectName(u"VC_pushButton_more")
        self.VC_pushButton_more.setFont(font)
        self.VC_pushButton_more.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"	border:2px soild;\n"
"	border-radius:7px;\n"
"	margin-left:0px;\n"
"	margin-right:5px;\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid #e4e4e1;\n"
"	background-color: #e4e4e1;\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid #eeeeec;\n"
"	background-color: #eeeeec;\n"
"}\n"
"")
        self.VC_pushButton_more.setIcon(icon10)

        self.horizontalLayout_27.addWidget(self.VC_pushButton_more)


        self.verticalLayout_25.addWidget(self.horizontalFrame_8)


        self.verticalLayout_12.addWidget(self.frame_13)

        self.VC_textBrowser = QTextBrowser(self.verticalFrame0)
        self.VC_textBrowser.setObjectName(u"VC_textBrowser")
        self.VC_textBrowser.setFont(font)
        self.VC_textBrowser.setStyleSheet(u"QTextBrowser{\n"
"border: 2px solid #cccccc;\n"
"border-radius: 5px;	\n"
"}\n"
"QScrollBar:vertical {\n"
"	background:#e4e9cd;\n"
"    width:20px;\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background:#645c0c;\n"
"}\n"
"QScrollBar::add-page:vertical {\n"
" 	background:#22a241;\n"
"}\n"
"QScrollBar::sub-page:vertical {\n"
" 	background:#fbd411;\n"
"}\n"
"")

        self.verticalLayout_12.addWidget(self.VC_textBrowser)


        self.verticalLayout_11.addWidget(self.verticalFrame0)


        self.horizontalLayout_22.addWidget(self.verticalFrame_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_2)

        self.frame_10 = QFrame(self.horizontalFrame_3)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy1)
        self.frame_10.setMinimumSize(QSize(230, 0))
        self.frame_10.setMaximumSize(QSize(230, 16777215))
        self.frame_10.setSizeIncrement(QSize(1, 0))
        self.frame_10.setFont(font)
        self.frame_10.setStyleSheet(u"margin-right:5px;")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_10)
        self.verticalLayout_10.setSpacing(10)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(12, 6, 16, 29)
        self.verticalWidget_4 = QWidget(self.frame_10)
        self.verticalWidget_4.setObjectName(u"verticalWidget_4")
        self.verticalWidget_4.setMinimumSize(QSize(200, 0))
        self.verticalWidget_4.setMaximumSize(QSize(200, 320))
        self.verticalWidget_4.setFont(font)
        self.verticalLayout_21 = QVBoxLayout(self.verticalWidget_4)
        self.verticalLayout_21.setSpacing(11)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setSizeConstraint(QLayout.SetFixedSize)
        self.verticalLayout_21.setContentsMargins(4, 1, -1, 5)
        self.VC_label_SelectTheModel = QLabel(self.verticalWidget_4)
        self.VC_label_SelectTheModel.setObjectName(u"VC_label_SelectTheModel")
        self.VC_label_SelectTheModel.setMaximumSize(QSize(16777215, 30))
        self.VC_label_SelectTheModel.setFont(font4)
        self.VC_label_SelectTheModel.setStyleSheet(u"")
        self.VC_label_SelectTheModel.setScaledContents(False)
        self.VC_label_SelectTheModel.setMargin(5)

        self.verticalLayout_21.addWidget(self.VC_label_SelectTheModel)

        self.VC_pushButton_SelectTheModel = QPushButton(self.verticalWidget_4)
        self.VC_pushButton_SelectTheModel.setObjectName(u"VC_pushButton_SelectTheModel")
        self.VC_pushButton_SelectTheModel.setMinimumSize(QSize(0, 28))
        self.VC_pushButton_SelectTheModel.setFont(font)
        self.VC_pushButton_SelectTheModel.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid #eacd13;\n"
"	border-radius: 5px;	\n"
"	color:#04130a;\n"
"	background-color: #eacd13;\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid #fbd411;\n"
"	background-color: #fbd411;\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid #f6e56a;\n"
"	background-color: #f6e56a;\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")

        self.verticalLayout_21.addWidget(self.VC_pushButton_SelectTheModel)

        self.model_path_vc_edit = QLineEdit(self.verticalWidget_4)
        self.model_path_vc_edit.setObjectName(u"model_path_vc_edit")
        self.model_path_vc_edit.setMinimumSize(QSize(0, 30))
        self.model_path_vc_edit.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_21.addWidget(self.model_path_vc_edit)

        self.VC_pushButton_StartLoading = QPushButton(self.verticalWidget_4)
        self.VC_pushButton_StartLoading.setObjectName(u"VC_pushButton_StartLoading")
        self.VC_pushButton_StartLoading.setMinimumSize(QSize(0, 28))
        self.VC_pushButton_StartLoading.setFont(font)
        self.VC_pushButton_StartLoading.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid #eacd13;\n"
"	border-radius: 5px;	\n"
"	color:#04130a;\n"
"	background-color: #eacd13;\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid #fbd411;\n"
"	background-color: #fbd411;\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid #f6e56a;\n"
"	background-color: #f6e56a;\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")

        self.verticalLayout_21.addWidget(self.VC_pushButton_StartLoading)

        self.VC_label_SelectRole = QLabel(self.verticalWidget_4)
        self.VC_label_SelectRole.setObjectName(u"VC_label_SelectRole")
        self.VC_label_SelectRole.setMaximumSize(QSize(16777215, 30))
        self.VC_label_SelectRole.setFont(font4)
        self.VC_label_SelectRole.setStyleSheet(u"")
        self.VC_label_SelectRole.setMargin(5)

        self.verticalLayout_21.addWidget(self.VC_label_SelectRole)

        self.VC_comboBox_SelectRole = QComboBox(self.verticalWidget_4)
        self.VC_comboBox_SelectRole.setObjectName(u"VC_comboBox_SelectRole")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(3)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.VC_comboBox_SelectRole.sizePolicy().hasHeightForWidth())
        self.VC_comboBox_SelectRole.setSizePolicy(sizePolicy2)
        self.VC_comboBox_SelectRole.setMinimumSize(QSize(0, 29))
        self.VC_comboBox_SelectRole.setFont(font7)
        self.VC_comboBox_SelectRole.setStyleSheet(u"QComboBox {\n"
"	border: 2px solid #eacd13;\n"
"	border-radius: 5px;	\n"
"	color:#04130a;\n"
"	background-color: #eacd13;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"	border: 2px solid #f6e56a;\n"
"	border-radius: 5px;	\n"
"	color:#04130a;\n"
"	background-color: #f6e56a;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"	background: #eacd13;\n"
"}\n"
"\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background:#eacd13;\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 5px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 5px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url"
                        "(icons/1x/arrow.png);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    background:#eacd13;\n"
"}\n"
"\n"
"\n"
"")
        self.VC_comboBox_SelectRole.setIconSize(QSize(5, 5))

        self.verticalLayout_21.addWidget(self.VC_comboBox_SelectRole)


        self.verticalLayout_10.addWidget(self.verticalWidget_4)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_5)


        self.horizontalLayout_22.addWidget(self.frame_10)


        self.verticalLayout_9.addWidget(self.horizontalFrame_3)

        self.stackedWidget.addWidget(self.page_VoiceConversion)

        self.horizontalLayout_14.addWidget(self.stackedWidget)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_low = QFrame(self.frame_bottom_east)
        self.frame_low.setObjectName(u"frame_low")
        self.frame_low.setMinimumSize(QSize(0, 20))
        self.frame_low.setMaximumSize(QSize(16777215, 20))
        self.frame_low.setFont(font)
        self.frame_low.setStyleSheet(u"")
        self.frame_low.setFrameShape(QFrame.NoFrame)
        self.frame_low.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_low)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_tab = QFrame(self.frame_low)
        self.frame_tab.setObjectName(u"frame_tab")
        self.frame_tab.setFont(font)
        self.frame_tab.setStyleSheet(u"background:#f6e56a;")
        self.frame_tab.setFrameShape(QFrame.NoFrame)
        self.frame_tab.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_tab)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.lab_tab = QLabel(self.frame_tab)
        self.lab_tab.setObjectName(u"lab_tab")
        self.lab_tab.setFont(font2)
        self.lab_tab.setStyleSheet(u"background:#eacd13;")

        self.horizontalLayout_12.addWidget(self.lab_tab)


        self.horizontalLayout_11.addWidget(self.frame_tab)

        self.frame_drag = QFrame(self.frame_low)
        self.frame_drag.setObjectName(u"frame_drag")
        self.frame_drag.setMinimumSize(QSize(20, 20))
        self.frame_drag.setMaximumSize(QSize(20, 20))
        self.frame_drag.setFont(font)
        self.frame_drag.setStyleSheet(u"background:#eacd13;")
        self.frame_drag.setFrameShape(QFrame.NoFrame)
        self.frame_drag.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_drag)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_11.addWidget(self.frame_drag)


        self.verticalLayout_2.addWidget(self.frame_low)


        self.horizontalLayout_2.addWidget(self.frame_bottom_east)


        self.verticalLayout.addWidget(self.frame_bottom)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(6)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.toodle.setText("")
        self.lab_appname.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Lemon4</p></body></html>", None))
        self.lab_user.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">User8455</span></p></body></html>", None))
        self.lab_person.setText("")
#if QT_CONFIG(tooltip)
        self.bn_min.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.bn_min.setText("")
#if QT_CONFIG(tooltip)
        self.bn_max.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.bn_max.setText("")
#if QT_CONFIG(tooltip)
        self.bn_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.bn_close.setText("")
#if QT_CONFIG(tooltip)
        self.bn_text.setToolTip(QCoreApplication.translate("MainWindow", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.bn_text.setText("")
#if QT_CONFIG(tooltip)
        self.bn_voice.setToolTip(QCoreApplication.translate("MainWindow", u"Bug", None))
#endif // QT_CONFIG(tooltip)
        self.bn_voice.setText("")
#if QT_CONFIG(tooltip)
        self.bn_noise.setToolTip(QCoreApplication.translate("MainWindow", u"Cloud", None))
#endif // QT_CONFIG(tooltip)
        self.bn_noise.setText("")
#if QT_CONFIG(tooltip)
        self.bn_image.setToolTip(QCoreApplication.translate("MainWindow", u"Android", None))
#endif // QT_CONFIG(tooltip)
        self.bn_image.setText("")
        self.lab_about_home.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">\u5173\u4e8e Lemon4</span></p></body></html>", None))
        self.text_about_home.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Smiley Sans'; font-size:10pt; font-weight:400; font-style:italic;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:130%;\"><span style=\" font-size:12pt; font-style:normal; color:#121212; background-color:#e4e9cd;\">\u8f7b\u91cf\u5316\u3001\u4fbf\u643a\u5316\u3001\u6613\u7528\u6027\u5f3a\u7684\u8f7b\u91cf\u7ea7\u96c6\u6210\u591a\u5a92\u4f53\u5904\u7406\u8f6f\u4ef6Lemon4\u7684\u4e3b\u8981\u76ee\u6807\u662f\u5c06\u4ee5\u97f3\u9891\u4e3a\u4e3b\u7684\u591a\u79cd\u5a92\u4f53\u5904\u7406\u529f\u80fd\u96c6\u6210\u5230\u4e00\u4e2a\u8f6f\u4ef6\u4e2d\uff0c\u5e76\u4e14\u5c3d\u53ef\u80fd\u51cf\u5c0f\u8f6f\u4ef6\u7684\u4f53\u79ef\u548c\u5bf9\u7cfb\u7edf\u8d44\u6e90\u7684\u5360"
                        "\u7528\uff0c\u540c\u65f6\u4f7f\u8f6f\u4ef6\u6613\u4e8e\u64cd\u4f5c\u548c\u4f7f\u7528\u3002</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:130%; font-size:12pt; font-style:normal; color:#121212;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:130%;\"><span style=\" font-size:12pt; font-style:normal; color:#121212; background-color:#e4e9cd;\">Lemon4\u5177\u6709\u4ee5\u4e0b\u56db\u4e2a\u529f\u80fd\uff1a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:130%;\"><span style=\" font-size:12pt; font-style:normal; color:#121212; background-color:#e4e9cd;\">1\u3001\u8bed\u97f3\u5408\u6210\u529f\u80fd\uff1a\u7528\u6237\u8f93\u5165\u6587\u672c\uff0c\u9009\u62e9\u8bf4\u8bdd\u4eba\u5e76\u63a7\u5236\u97f3\u8c03"
                        "\u3001\u8bed\u901f\u3001\u97f3\u91cf\u7b49\u53c2\u6570\uff0cLemon4\u5408\u6210\u51fa\u5bf9\u5e94\u8bed\u97f3\u3002</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:130%;\"><span style=\" font-size:12pt; font-style:normal; color:#121212; background-color:#e4e9cd;\">2\u3001\u8bed\u97f3\u8f6c\u6362\u529f\u80fd\uff1a\u7528\u6237\u4e0a\u4f20\u6216\u5f55\u5236\u4e00\u6bb5\u8bed\u97f3\uff0c\u9009\u62e9\u76ee\u6807\u97f3\u8272\uff0cLemon4\u5408\u6210\u51fa\u5bf9\u5e94\u76ee\u6807\u8bed\u97f3\uff0c\u7528\u6237\u8fd8\u53ef\u63a7\u5236\u97f3\u8c03\u3001\u97f3\u91cf\u3001\u8bed\u901f\u7b49\u53c2\u6570\u3002</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:130%;\"><span style=\" font-size:12pt; font-style:normal; color:#121212; background-color:#e4e9cd;\">3\u3001\u8bed\u97f3\u964d\u566a\u529f\u80fd\uff1a\u7528\u6237\u8f93\u5165\u5e26"
                        "\u566a\u8bed\u97f3\uff0cLemon4\u63d0\u4f9b\u591a\u79cd\u964d\u566a\u6a21\u5f0f\uff0c\u5982\u53bb\u9664\u767d\u566a\u58f0\u3001\u80cc\u666f\u566a\u58f0\u3001\u8109\u51b2\u566a\u58f0\u7b49\uff0c\u5e76\u63d0\u4f9b\u566a\u58f0\u7b49\u7ea7\u3001\u964d\u566a\u5f3a\u5ea6\u3001\u65f6\u57df\u5e73\u6ed1\u5ea6\u7b49\u53c2\u6570\uff0c\u4ee5\u6539\u5584\u8bed\u97f3\u8bc6\u522b\u3001\u8bed\u97f3\u5408\u6210\u7b49\u5e94\u7528\u7684\u6027\u80fd\u3002</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:130%;\"><span style=\" font-size:12pt; font-style:normal; color:#121212; background-color:#e4e9cd;\">4\u3001\u56fe\u50cf\u4fee\u590d\u529f\u80fd\uff1a\u7528\u6237\u8f93\u5165\u6a21\u7cca\u7684\u56fe\u7247\uff0cLemon4\u63d0\u4f9b\u591a\u79cd\u56fe\u50cf\u4fee\u590d\u6a21\u5f0f\uff0c\u5982\u53bb\u9664\u566a\u58f0\u3001\u6a21\u7cca\u3001\u4f2a\u5f71\u7b49\uff0c\u5e76\u63d0\u4f9b\u964d\u566a\u5f3a\u5ea6\u3001\u6062\u590d\u5ea6\u3001\u7f29\u653e"
                        "\u6bd4\u4f8b\u7b49\u53c2\u6570\uff0c\u4ee5\u6539\u5584\u56fe\u50cf\u8d28\u91cf\u3001\u589e\u5f3a\u7ec6\u8282\u7b49\u5e94\u7528\u7684\u6548\u679c\u3002</span></p></body></html>", None))
        self.lab_about_home_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">\u5173\u4e8e \u6587\u672c\u8f6c\u8bed\u97f3</span></p></body></html>", None))
        self.text_about_home_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Smiley Sans'; font-size:10pt; font-weight:400; font-style:italic;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-style:normal; color:#121212; background-color:#e4e9cd;\">\u8bed\u97f3\u5408\u6210\uff08speech synthesis\uff09\u7684\u4efb\u52a1\u662f\u5c06\u6587\u672c\u8f6c\u6362\u6210\u8bed\u97f3\u3002\u5373\u8f93\u5165\u4e00\u6bb5\u6587\u672c\uff0c\u8f93\u51fa\u4e00\u6bb5\u8bed\u97f3\uff0c\u4f7f\u5f97\u542c\u8005\u80fd\u591f\u7406\u89e3\u6587\u672c\u5185\u5bb9\u5e76\u83b7\u53d6\u76f8\u5173\u4fe1\u606f\u3002</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-inden"
                        "t:0px;\"><span style=\" font-size:12pt; font-style:normal; color:#121212; background-color:#e4e9cd;\">\u7528\u6237\u53ef\u4ee5\u8f93\u5165\u5f85\u8f6c\u6362\u7684\u6587\u672c\uff0c\u70b9\u51fb\u5408\u6210\u6309\u94ae\uff0c\u5c31\u53ef\u4ee5\u5f97\u5230\u5bf9\u5e94\u7684\u8bed\u97f3\u8f93\u51fa\u3002\u540c\u65f6\uff0c\u7528\u6237\u4e5f\u53ef\u4ee5\u64ad\u653e\u548c\u4e0b\u8f7d\u5408\u6210\u540e\u7684\u8bed\u97f3\u3002</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-style:normal;\"><br /></span></p></body></html>", None))
        self.lab_about_home_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">\u5173\u4e8e \u8bed\u97f3\u8f6c\u6362</span></p></body></html>", None))
        self.text_about_home_3.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Smiley Sans'; font-size:10pt; font-weight:400; font-style:italic;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-style:normal;\">\u8bed\u97f3\u8f6c\u6362\uff08voice conversion\uff09\u7684\u4efb\u52a1\u662f\u5c06\u4e00\u6bb5</span><span style=\" font-size:12pt; font-weight:600; font-style:normal;\">\u6e90\u8bed\u97f3</span><span style=\" font-size:12pt; font-style:normal;\">\uff08source speech\uff09\u901a\u8fc7\u6a21\u578b\u8f6c\u6362\u5230</span><span style=\" font-size:12pt; font-weight:600; font-style:normal;\">\u76ee\u6807\u8bed\u97f3</span><span style=\" font-size:12pt; font-style:normal;\">\uff08target speech\uff09\uff0c\u4f7f\u5f97"
                        "\u76ee\u6807\u8bed\u97f3\u5177\u6709\u76ee\u6807\u8bed\u8005\uff08target speaker\uff09\u7684\u7279\u70b9\uff08\u97f3\u8272\u3001\u97f3\u8c03\u7b49\uff09\u7684\u540c\u65f6\uff0c\u4fdd\u7559\u6e90\u8bed\u97f3\u4e2d\u7684\u5185\u5bb9\u3002</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-style:normal;\">\u5bf9\u4e8e\u672c\u9879\u76ee\uff0c\u7528\u6237\u53ef\u4ee5\u4e0a\u4f20\u4e00\u6bb5\uff08\u6e90\uff09\u8bed\u97f3\uff0c\u9009\u62e9\u76ee\u6807\u8bed\u8005\u8eab\u4efd\uff08speaker identity\uff09\uff0c\u7136\u540e\u70b9\u51fb\u8f6c\u6362\u6309\u94ae\u5c06\u6e90\u8bed\u97f3\u8f6c\u6362\u5230\u76ee\u6807\u8bed\u97f3\u3002\u8f6f\u4ef6\u8fd8\u5e94\u5141\u8bb8\u7528\u6237\u64ad\u653e\u548c\u4e0b\u8f7d\u8f6c\u6362\u540e\u7684\u8bed\u97f3\u3002 <br /></span></p></body></html>", None))
        self.lab_about_home_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">\u5173\u4e8e \u8bed\u97f3\u964d\u566a/\u8bed\u97f3\u589e\u5f3a</span></p></body></html>", None))
        self.text_about_home_4.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Smiley Sans'; font-size:10pt; font-weight:400; font-style:italic;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-style:normal;\">\u8bed\u97f3\u589e\u5f3a\uff08speech enhancement\uff09\u7684\u4efb\u52a1\u662f\u5c06\u4e00\u6bb5\u5e26\u566a\u8bed\u97f3\u901a\u8fc7\u6a21\u578b\u8f6c\u6362\u6210\u5e72\u51c0\u8bed\u97f3\uff0c\u5373\u53bb\u9664\u80cc\u666f\u566a\u58f0\uff0c\u4fdd\u7559\u4eba\u58f0\u3002</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-style:normal;\">\u4e0e\u8bed\u97f3\u8f6c\u6362\u7c7b\u4f3c\uff0c\u7528"
                        "\u6237\u53ef\u4ee5\u4e0a\u4f20\u4e00\u6bb5\u5e26\u566a\u8bed\u97f3\uff0c\u70b9\u51fb\u964d\u566a\uff08denoise\uff09\u6309\u94ae\u5c31\u53ef\u4ee5\u5f97\u5230\u5e72\u51c0\u8bed\u97f3\u3002\u540c\u65f6\uff0c\u7528\u6237\u53ef\u4ee5\u64ad\u653e\u548c\u4e0b\u8f7d\u964d\u566a\u540e\u7684\u8bed\u97f3\u3002 </span></p></body></html>", None))
        self.lab_about_home_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">\u5173\u4e8e \u56fe\u50cf\u4fee\u590d</span></p></body></html>", None))
        self.text_about_home_5.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Smiley Sans'; font-size:10pt; font-weight:400; font-style:italic;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-style:normal;\">\u56fe\u50cf\u8d85\u5206\uff08image super resolution\uff09\u7684\u4efb\u52a1\u662f\u5c06\u4e00\u5f20\u4f4e\u5206\u8fa8\u7387\u7684\u56fe\u7247\u901a\u8fc7\u6a21\u578b\u8f6c\u6362\u6210\u4e00\u5f20\u9ad8\u5206\u8fa8\u7387\u7684\u56fe\u7247\u3002</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-style:normal;\">\u672c\u9879\u76ee\u4e2d\uff0c\u7528\u6237\u53ef\u4ee5\u4e0a\u4f20\u4e00\u5f20"
                        "\u6a21\u7cca\u7684\u56fe\u7247\uff0c\u70b9\u51fb\u8d85\u5206\u6309\u94ae\uff0c\u5f97\u5230\u4e00\u5f20\u6e05\u6670\u7684\u56fe\u7247\u3002 </span></p></body></html>", None))
        self.Denoise_label_Title.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#04130a;\">\u8bed\u97f3\u964d\u566a</span></p></body></html>\n"
"", None))
        self.groupBox_2.setTitle("")
        self.Denoise_pushButton_SelectFile.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u6587\u4ef6", None))
        self.Denoise_pushButton_PlayAudio_before.setText("")
        self.Denoise_label_AudioTime_before.setText(QCoreApplication.translate("MainWindow", u"0:00/0:00", None))
        self.Denoise_pushButton_VolumeAdjustment_before.setText("")
        self.Denoise_pushButton_StartDenoising.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u964d\u566a", None))
        self.Denoise_pushButton_PlayAudio_after.setText("")
        self.Denoise_label_AudioTime_after.setText(QCoreApplication.translate("MainWindow", u"0\uff1a00/0\uff1a00", None))
        self.Denoise_pushButton_VolumeAdjustment_after.setText("")
        self.Denoise_pushButton_more.setText("")
        self.Denoise_label_LoadtheModel.setText(QCoreApplication.translate("MainWindow", u"\u52a0\u8f7d\u6a21\u578b\u9009\u62e9", None))
        self.Denoise_pushButton_SelectTheModel.setText(QCoreApplication.translate("MainWindow", u"\u6a21\u578b\u76ee\u5f55\u9009\u62e9", None))
        self.Denoise_pushButton_StartLoading.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u52a0\u8f7d", None))
        self.TTS_label_Title.setText(QCoreApplication.translate("MainWindow", u"\u6587\u672c\u8f6c\u8bed\u97f3", None))
        self.TTS_textEdit_Text.setMarkdown("")
        self.TTS_textEdit_Text.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Smiley Sans'; font-size:10pt; font-weight:400; font-style:italic;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.TTS_textEdit_Text.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u5f85\u8f6c\u6362\u4e3a\u8bed\u97f3\u7684\u6587\u672c\u4fe1\u606f... ", None))
        self.TTS_pushButton_GenerateSpeech.setText(QCoreApplication.translate("MainWindow", u"\u751f\u6210\u8bed\u97f3", None))
        self.TTS_pushButton_FastGenerate.setText(QCoreApplication.translate("MainWindow", u"\u5feb\u901f\u751f\u6210", None))
        self.TTS_pushButton_Clear.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a\u6587\u672c", None))
        self.TTS_pushButton_PlayAudio.setText("")
        self.TTS_label_AudioTime.setText(QCoreApplication.translate("MainWindow", u"0\uff1a00/0\uff1a00", None))
        self.TTS_pushButton_more.setText("")
        self.TTS_label_SelectTheModel.setText(QCoreApplication.translate("MainWindow", u"\u52a0\u8f7d\u6a21\u578b\u9009\u62e9", None))
        self.TTS_pushButton_SelcetTheModel.setText(QCoreApplication.translate("MainWindow", u"\u6a21\u578b\u76ee\u5f55\u9009\u62e9", None))
        self.TTS_pushButton_StartLoading.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u52a0\u8f7d", None))
        self.TTS_label_SelectRole.setText(QCoreApplication.translate("MainWindow", u"\u89d2\u8272\u9009\u62e9", None))
        self.TTS_label_SpeedControl.setText(QCoreApplication.translate("MainWindow", u"\u8bed\u901f\u63a7\u5236", None))
        self.TTS_label_EmotionalControl.setText(QCoreApplication.translate("MainWindow", u"\u60c5\u611f\u53d8\u5316\u7a0b\u5ea6\u63a7\u5236", None))
        self.TTS_label_VolumeAdjustment.setText(QCoreApplication.translate("MainWindow", u"\u97f3\u91cf\u63a7\u5236", None))
        self.Image_label_Title.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u50cf\u4fee\u590d", None))
        self.Image_pushButton_StartRepairing.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u542f\u8d85\u5206", None))
        self.Image_pushButton_Download.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u8f7d\u56fe\u7247", None))
        self.Image_label_SelectTheModel.setText(QCoreApplication.translate("MainWindow", u"\u52a0\u8f7d\u6a21\u578b\u9009\u62e9", None))
        self.Image_pushButton_SelectTheModel.setText(QCoreApplication.translate("MainWindow", u"\u6a21\u578b\u76ee\u5f55\u9009\u62e9", None))
        self.Image_pushButton_StartLoading.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u52a0\u8f7d", None))
        self.groupBox_5.setTitle("")
        self.Image_pushButton_Upload.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u4e0a\u4f20\u56fe\u7247", None))
        self.VC_label_Title.setText(QCoreApplication.translate("MainWindow", u"\u8bed\u97f3\u8f6c\u6362", None))
        self.VC_pushButton_Upload.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u9009\u62e9\u672c\u5730\u6587\u4ef6\u4e0a\u4f20", None))
        self.VC_pushButton_PlayAudio_before.setText("")
        self.VC_label_AudioTime_before.setText(QCoreApplication.translate("MainWindow", u"0\uff1a00/0\uff1a00", None))
        self.VC_pushButton_VolumeAdjustment_before.setText("")
        self.VC_pushButton_StartConversion.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u8f6c\u6362", None))
        self.VC_pushButton_PlayAudio_after.setText("")
        self.VC_label_AudioTime_after.setText(QCoreApplication.translate("MainWindow", u"0\uff1a00/0\uff1a00", None))
        self.VC_pushButton_VolumeAdjustment_after.setText("")
        self.VC_pushButton_more.setText("")
        self.VC_label_SelectTheModel.setText(QCoreApplication.translate("MainWindow", u"\u52a0\u8f7d\u6a21\u578b\u9009\u62e9", None))
        self.VC_pushButton_SelectTheModel.setText(QCoreApplication.translate("MainWindow", u"\u6a21\u578b\u76ee\u5f55\u9009\u62e9", None))
        self.VC_pushButton_StartLoading.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u52a0\u8f7d", None))
        self.VC_label_SelectRole.setText(QCoreApplication.translate("MainWindow", u"\u89d2\u8272\u9009\u62e9", None))
        self.lab_tab.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.frame_drag.setToolTip(QCoreApplication.translate("MainWindow", u"Drag", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

