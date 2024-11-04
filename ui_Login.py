# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LoginPlSvGg.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
    QWidget)

class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(457, 669)
        icon = QIcon()
        icon.addFile(u"resources/images/icon.jpeg", QSize(), QIcon.Normal, QIcon.Off)
        Login.setWindowIcon(icon)
        self.centralwidget = QWidget(Login)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame#frame\n"
"{\n"
"	border-radius: 10px;\n"
"	background-image: url(resources/images/resized_background.png);\n"
"}\n"
"QFrame#frame_4,\n"
"QFrame#frame_5,\n"
"QFrame#frame_6,\n"
"QFrame#frame_7\n"
"{\n"
"	border-radius: 10px;\n"
"	background-color:rgba(0,0,0,200);\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_superior = QFrame(self.frame)
        self.frame_superior.setObjectName(u"frame_superior")
        self.frame_superior.setMinimumSize(QSize(0, 40))
        self.frame_superior.setMaximumSize(QSize(16777215, 40))
        self.frame_superior.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 254);\n"
"	font: 12pt \"Arial\";\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"}\n"
"\n"
"QPushButton{\n"
"border-radius: 18px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
        self.frame_superior.setFrameShape(QFrame.StyledPanel)
        self.frame_superior.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_superior)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.frame_superior)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(40, 40))
        self.label_11.setMaximumSize(QSize(40, 40))
        self.label_11.setPixmap(QPixmap(u"resources/images/logo.png"))
        self.label_11.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_11)

        self.horizontalSpacer_2 = QSpacerItem(111, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.Titulo = QLabel(self.frame_superior)
        self.Titulo.setObjectName(u"Titulo")
        self.Titulo.setStyleSheet(u"font: 600 30pt \"Lucida Bright\";\n"
"color:white;")
        self.Titulo.setScaledContents(False)
        self.Titulo.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.Titulo)

        self.horizontalSpacer_7 = QSpacerItem(110, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_7)

        self.bt_minimize = QPushButton(self.frame_superior)
        self.bt_minimize.setObjectName(u"bt_minimize")
        self.bt_minimize.setMinimumSize(QSize(38, 38))
        self.bt_minimize.setMaximumSize(QSize(38, 38))
        icon1 = QIcon()
        icon1.addFile(u"resources/images/minimize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_minimize.setIcon(icon1)
        self.bt_minimize.setIconSize(QSize(38, 38))

        self.horizontalLayout_3.addWidget(self.bt_minimize)

        self.bt_normal = QPushButton(self.frame_superior)
        self.bt_normal.setObjectName(u"bt_normal")
        self.bt_normal.setMinimumSize(QSize(38, 38))
        self.bt_normal.setMaximumSize(QSize(38, 38))
        icon2 = QIcon()
        icon2.addFile(u"resources/images/normal.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_normal.setIcon(icon2)
        self.bt_normal.setIconSize(QSize(38, 38))

        self.horizontalLayout_3.addWidget(self.bt_normal)

        self.bt_maximize = QPushButton(self.frame_superior)
        self.bt_maximize.setObjectName(u"bt_maximize")
        self.bt_maximize.setMinimumSize(QSize(38, 38))
        self.bt_maximize.setMaximumSize(QSize(38, 38))
        icon3 = QIcon()
        icon3.addFile(u"resources/images/maximize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_maximize.setIcon(icon3)
        self.bt_maximize.setIconSize(QSize(38, 38))

        self.horizontalLayout_3.addWidget(self.bt_maximize)

        self.bt_close = QPushButton(self.frame_superior)
        self.bt_close.setObjectName(u"bt_close")
        self.bt_close.setMinimumSize(QSize(38, 38))
        self.bt_close.setMaximumSize(QSize(38, 38))
        icon4 = QIcon()
        icon4.addFile(u"resources/images/close.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_close.setIcon(icon4)
        self.bt_close.setIconSize(QSize(38, 38))

        self.horizontalLayout_3.addWidget(self.bt_close)

        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(2, 1)
        self.horizontalLayout_3.setStretch(3, 1)
        self.horizontalLayout_3.setStretch(4, 1)
        self.horizontalLayout_3.setStretch(5, 1)
        self.horizontalLayout_3.setStretch(6, 1)
        self.horizontalLayout_3.setStretch(7, 1)

        self.verticalLayout_2.addWidget(self.frame_superior)

        self.frame_inferior = QFrame(self.frame)
        self.frame_inferior.setObjectName(u"frame_inferior")
        self.frame_inferior.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 254);\n"
"	font: 12pt \"Arial\";\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"}\n"
"\n"
"QLineEdit{\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	border-radius: 10px;\n"
"	font: 12pt \"Arial\";\n"
"	color: rgb(255, 255, 254);\n"
"	border: 2px solid rgb(255, 255, 255)\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	border-radius: 10px;\n"
"	font: 12pt \"Arial\";\n"
"	border: 2px solid rgb(0,51, 102);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	background-color: rgb(0, 0, 0);\n"
"	border-radius: 10px;\n"
"	font: 12pt \"Arial\";\n"
"	border: 2px solid rgb(173, 51, 51);\n"
"}\n"
"\n"
"QCheckBox{\n"
"	font: 12pt \"Arial\";\n"
"	color: rgb(255, 255, 255)\n"
"}\n"
"\n"
"QCheckBox::indicator{\n"
"	width: 18px;\n"
"	height: 18px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked{\n"
"	background-image: url(resources/images/Login/check_box.svg);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked{\n"
"	background-image: url(resources/images/Login/check.svg);\n"
"}\n"
"\n"
"QP"
                        "ushButton{\n"
"	border-radius: 10px;\n"
"	font: 12pt \"Arial\";\n"
"	color: rgb(255, 255, 254);\n"
"	border: 2px solid #ffffff;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 10px;\n"
"	font: 12pt \"Arial\";\n"
"	color: rgb(255, 255, 254);\n"
"	border: 2px solid rgb(0,51, 102);\n"
"	background-color: rgb(0,51, 102);\n"
"}\n"
"QPushButton#bt_Registrarse,\n"
"QPushButton#bt_ResetPass,\n"
"QPushButton#bt_IniciaSesion,\n"
"QPushButton#bt_IniciaSesion_2{\n"
"	border-radius:8px;\n"
"	font: 12pt \"Arial\";\n"
"	color:rgb(255, 255, 254);\n"
"	border:None;\n"
"	background-color: None;\n"
"}\n"
"QPushButton#bt_Registrarse:hover,\n"
"QPushButton#bt_ResetPass:hover,\n"
"QPushButton#bt_IniciaSesion:hover,\n"
"QPushButton#bt_IniciaSesion_2:hover{\n"
"	border-radius:8px;\n"
"	font: 12pt \"Arial\";\n"
"	color:rgb(0,51, 102);\n"
"	background-color: white;\n"
"}")
        self.frame_inferior.setFrameShape(QFrame.StyledPanel)
        self.frame_inferior.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_inferior)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_3 = QSpacerItem(160, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer)

        self.stackedWidget = QStackedWidget(self.frame_inferior)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(290, 0))
        self.stackedWidget.setMaximumSize(QSize(300, 16777215))
        self.stackedWidget.setStyleSheet(u"")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_4 = QVBoxLayout(self.page)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.page)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(400, 600))
        self.frame_4.setStyleSheet(u"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 40))
        self.label.setMaximumSize(QSize(16777215, 50))
        self.label.setStyleSheet(u"font: 16pt \"Arial\";")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.invalidLogin = QLabel(self.frame_4)
        self.invalidLogin.setObjectName(u"invalidLogin")
        self.invalidLogin.setEnabled(True)
        self.invalidLogin.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.invalidLogin)

        self.emailEdit = QLineEdit(self.frame_4)
        self.emailEdit.setObjectName(u"emailEdit")
        self.emailEdit.setMinimumSize(QSize(0, 35))

        self.verticalLayout_3.addWidget(self.emailEdit)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)

        self.passEdit = QLineEdit(self.frame_4)
        self.passEdit.setObjectName(u"passEdit")
        self.passEdit.setMinimumSize(QSize(0, 35))
        self.passEdit.setEchoMode(QLineEdit.Password)

        self.verticalLayout_3.addWidget(self.passEdit)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_5)

        self.checkRecordarPass = QCheckBox(self.frame_4)
        self.checkRecordarPass.setObjectName(u"checkRecordarPass")
        self.checkRecordarPass.setStyleSheet(u"")
        self.checkRecordarPass.setIconSize(QSize(15, 15))

        self.verticalLayout_3.addWidget(self.checkRecordarPass)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_6)

        self.bt_IniciarSesion = QPushButton(self.frame_4)
        self.bt_IniciarSesion.setObjectName(u"bt_IniciarSesion")
        self.bt_IniciarSesion.setMinimumSize(QSize(0, 35))

        self.verticalLayout_3.addWidget(self.bt_IniciarSesion)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_7)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.bt_Registrarse = QPushButton(self.frame_4)
        self.bt_Registrarse.setObjectName(u"bt_Registrarse")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bt_Registrarse.sizePolicy().hasHeightForWidth())
        self.bt_Registrarse.setSizePolicy(sizePolicy)
        self.bt_Registrarse.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_Registrarse.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.bt_Registrarse)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.verticalSpacer_18 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_18)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_8 = QLabel(self.frame_4)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_5.addWidget(self.label_8)

        self.bt_ResetPass = QPushButton(self.frame_4)
        self.bt_ResetPass.setObjectName(u"bt_ResetPass")
        self.bt_ResetPass.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_ResetPass.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.bt_ResetPass)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_6)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_8)

        self.iniciarInvitado = QPushButton(self.frame_4)
        self.iniciarInvitado.setObjectName(u"iniciarInvitado")
        self.iniciarInvitado.setMinimumSize(QSize(0, 35))

        self.verticalLayout_3.addWidget(self.iniciarInvitado)


        self.verticalLayout_4.addWidget(self.frame_4)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_6 = QVBoxLayout(self.page_2)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.page_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(400, 600))
        self.frame_5.setStyleSheet(u"")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 40))
        self.label_3.setMaximumSize(QSize(16777215, 50))
        self.label_3.setStyleSheet(u"font: 16pt \"Arial\";")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_3)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_9)

        self.invalidSignup = QLabel(self.frame_5)
        self.invalidSignup.setObjectName(u"invalidSignup")
        self.invalidSignup.setEnabled(True)
        self.invalidSignup.setStyleSheet(u"")
        self.invalidSignup.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.invalidSignup)

        self.userEdit_2 = QLineEdit(self.frame_5)
        self.userEdit_2.setObjectName(u"userEdit_2")
        self.userEdit_2.setMinimumSize(QSize(0, 35))

        self.verticalLayout_5.addWidget(self.userEdit_2)

        self.verticalSpacer_15 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_15)

        self.emailEdit_2 = QLineEdit(self.frame_5)
        self.emailEdit_2.setObjectName(u"emailEdit_2")
        self.emailEdit_2.setMinimumSize(QSize(0, 35))

        self.verticalLayout_5.addWidget(self.emailEdit_2)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_10)

        self.passEdit_2 = QLineEdit(self.frame_5)
        self.passEdit_2.setObjectName(u"passEdit_2")
        self.passEdit_2.setMinimumSize(QSize(0, 35))
        self.passEdit_2.setEchoMode(QLineEdit.Password)

        self.verticalLayout_5.addWidget(self.passEdit_2)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_11)

        self.checkRecordarPass_2 = QCheckBox(self.frame_5)
        self.checkRecordarPass_2.setObjectName(u"checkRecordarPass_2")
        icon5 = QIcon()
        icon5.addFile(u"../resources/images/Login/circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon5.addFile(u"../resources/images/Login/check.svg", QSize(), QIcon.Normal, QIcon.On)
        self.checkRecordarPass_2.setIcon(icon5)
        self.checkRecordarPass_2.setIconSize(QSize(5, 5))

        self.verticalLayout_5.addWidget(self.checkRecordarPass_2)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_12)

        self.bt_Registrarme = QPushButton(self.frame_5)
        self.bt_Registrarme.setObjectName(u"bt_Registrarme")
        self.bt_Registrarme.setMinimumSize(QSize(0, 35))

        self.verticalLayout_5.addWidget(self.bt_Registrarme)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_13)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.bt_IniciaSesion = QPushButton(self.frame_5)
        self.bt_IniciaSesion.setObjectName(u"bt_IniciaSesion")
        self.bt_IniciaSesion.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_IniciaSesion.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.bt_IniciaSesion)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_14)

        self.iniciarInvitado_2 = QPushButton(self.frame_5)
        self.iniciarInvitado_2.setObjectName(u"iniciarInvitado_2")
        self.iniciarInvitado_2.setMinimumSize(QSize(0, 35))

        self.verticalLayout_5.addWidget(self.iniciarInvitado_2)

        self.verticalLayout_5.setStretch(0, 1)
        self.verticalLayout_5.setStretch(1, 1)
        self.verticalLayout_5.setStretch(2, 1)
        self.verticalLayout_5.setStretch(3, 1)
        self.verticalLayout_5.setStretch(4, 1)
        self.verticalLayout_5.setStretch(5, 1)
        self.verticalLayout_5.setStretch(6, 1)
        self.verticalLayout_5.setStretch(7, 1)
        self.verticalLayout_5.setStretch(8, 1)
        self.verticalLayout_5.setStretch(9, 1)
        self.verticalLayout_5.setStretch(10, 1)
        self.verticalLayout_5.setStretch(11, 1)
        self.verticalLayout_5.setStretch(12, 1)
        self.verticalLayout_5.setStretch(13, 1)
        self.verticalLayout_5.setStretch(14, 1)
        self.verticalLayout_5.setStretch(15, 1)

        self.verticalLayout_6.addWidget(self.frame_5)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_9 = QVBoxLayout(self.page_3)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.page_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(400, 600))
        self.frame_6.setStyleSheet(u"")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_6)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_17 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_17)

        self.label_5 = QLabel(self.frame_6)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 40))
        self.label_5.setMaximumSize(QSize(16777215, 50))
        self.label_5.setLayoutDirection(Qt.LeftToRight)
        self.label_5.setStyleSheet(u"font: 16pt \"Arial\";")
        self.label_5.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.verticalLayout_8.addWidget(self.label_5)

        self.label_6 = QLabel(self.frame_6)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(0, 40))
        self.label_6.setMaximumSize(QSize(16777215, 50))
        self.label_6.setStyleSheet(u"font: 16pt \"Arial\";")
        self.label_6.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_8.addWidget(self.label_6)

        self.verticalSpacer_16 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_16)

        self.label_animation = QLabel(self.frame_6)
        self.label_animation.setObjectName(u"label_animation")
        self.label_animation.setEnabled(True)
        self.label_animation.setMinimumSize(QSize(0, 300))
        self.label_animation.setMaximumSize(QSize(400, 16777215))
        self.label_animation.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_animation)

        self.label_7 = QLabel(self.frame_6)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(0, 40))
        self.label_7.setStyleSheet(u"font: 16pt \"Arial\";")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_7)

        self.verticalSpacer_21 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_21)

        self.verticalLayout_8.setStretch(0, 1)
        self.verticalLayout_8.setStretch(1, 1)
        self.verticalLayout_8.setStretch(2, 1)
        self.verticalLayout_8.setStretch(3, 1)
        self.verticalLayout_8.setStretch(4, 1)
        self.verticalLayout_8.setStretch(6, 4)

        self.verticalLayout_9.addWidget(self.frame_6)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_11 = QVBoxLayout(self.page_4)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.page_4)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(400, 600))
        self.frame_7.setStyleSheet(u"")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_7)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.frame_7)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(0, 40))
        self.label_9.setMaximumSize(QSize(16777215, 50))
        self.label_9.setStyleSheet(u"font: 16pt \"Arial\";")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_9)

        self.verticalSpacer_19 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_19)

        self.resetPassStatus = QLabel(self.frame_7)
        self.resetPassStatus.setObjectName(u"resetPassStatus")
        self.resetPassStatus.setEnabled(True)
        self.resetPassStatus.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.resetPassStatus)

        self.emailEdit_3 = QLineEdit(self.frame_7)
        self.emailEdit_3.setObjectName(u"emailEdit_3")
        self.emailEdit_3.setMinimumSize(QSize(0, 35))

        self.verticalLayout_10.addWidget(self.emailEdit_3)

        self.verticalSpacer_20 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_20)

        self.label_12 = QLabel(self.frame_7)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_12)

        self.label_13 = QLabel(self.frame_7)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_13)

        self.verticalSpacer_23 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_23)

        self.bt_ResetPass_2 = QPushButton(self.frame_7)
        self.bt_ResetPass_2.setObjectName(u"bt_ResetPass_2")
        self.bt_ResetPass_2.setMinimumSize(QSize(0, 35))

        self.verticalLayout_10.addWidget(self.bt_ResetPass_2)

        self.verticalSpacer_24 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_24)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_10 = QLabel(self.frame_7)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_6.addWidget(self.label_10)

        self.bt_IniciaSesion_2 = QPushButton(self.frame_7)
        self.bt_IniciaSesion_2.setObjectName(u"bt_IniciaSesion_2")
        self.bt_IniciaSesion_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_IniciaSesion_2.setStyleSheet(u"")

        self.horizontalLayout_6.addWidget(self.bt_IniciaSesion_2)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_8)


        self.verticalLayout_10.addLayout(self.horizontalLayout_6)

        self.verticalSpacer_26 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_26)


        self.verticalLayout_11.addWidget(self.frame_7)

        self.stackedWidget.addWidget(self.page_4)

        self.verticalLayout_7.addWidget(self.stackedWidget)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)


        self.horizontalLayout_4.addLayout(self.verticalLayout_7)

        self.horizontalSpacer_4 = QSpacerItem(160, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)


        self.verticalLayout_2.addWidget(self.frame_inferior)


        self.verticalLayout.addWidget(self.frame)

        Login.setCentralWidget(self.centralwidget)

        self.retranslateUi(Login)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"RoboPro", None))
        self.label_11.setText("")
        self.Titulo.setText(QCoreApplication.translate("Login", u"RoboPro", None))
        self.bt_minimize.setText("")
        self.bt_normal.setText("")
        self.bt_maximize.setText("")
        self.bt_close.setText("")
        self.label.setText(QCoreApplication.translate("Login", u"Iniciar Sesi\u00f3n", None))
        self.invalidLogin.setText("")
        self.emailEdit.setPlaceholderText(QCoreApplication.translate("Login", u"Ingrese el correo electr\u00f3nico", None))
        self.passEdit.setPlaceholderText(QCoreApplication.translate("Login", u"Ingrese la contrase\u00f1a", None))
        self.checkRecordarPass.setText(QCoreApplication.translate("Login", u"Permanecer conectado", None))
        self.bt_IniciarSesion.setText(QCoreApplication.translate("Login", u"Iniciar Sesi\u00f3n", None))
        self.label_2.setText(QCoreApplication.translate("Login", u"\u00bfNo tienes una cuenta?", None))
        self.bt_Registrarse.setText(QCoreApplication.translate("Login", u" Reg\u00edstrate ", None))
        self.label_8.setText(QCoreApplication.translate("Login", u"\u00bfOlvidaste tu contrase\u00f1a?", None))
        self.bt_ResetPass.setText(QCoreApplication.translate("Login", u" Restablecer ", None))
        self.iniciarInvitado.setText(QCoreApplication.translate("Login", u"Iniciar Como Invitado", None))
        self.label_3.setText(QCoreApplication.translate("Login", u"Registrarte", None))
        self.invalidSignup.setText("")
        self.userEdit_2.setPlaceholderText(QCoreApplication.translate("Login", u"Cree su nombre de usuario id", None))
        self.emailEdit_2.setPlaceholderText(QCoreApplication.translate("Login", u"Ingrese su correo electr\u00f3nico", None))
        self.passEdit_2.setPlaceholderText(QCoreApplication.translate("Login", u"Cree su contrase\u00f1a", None))
        self.checkRecordarPass_2.setText(QCoreApplication.translate("Login", u"Permanecer conectado", None))
        self.bt_Registrarme.setText(QCoreApplication.translate("Login", u"Registrarme", None))
        self.label_4.setText(QCoreApplication.translate("Login", u"\u00bfYa tienes una cuenta?", None))
        self.bt_IniciaSesion.setText(QCoreApplication.translate("Login", u" Inicia sesi\u00f3n ", None))
        self.iniciarInvitado_2.setText(QCoreApplication.translate("Login", u"Iniciar Como Invitado", None))
        self.label_5.setText(QCoreApplication.translate("Login", u"Esperando validaci\u00f3n", None))
        self.label_6.setText(QCoreApplication.translate("Login", u"de correo electr\u00f3nico", None))
        self.label_animation.setText("")
        self.label_7.setText(QCoreApplication.translate("Login", u"Revisa tu correo electr\u00f3nico", None))
        self.label_9.setText(QCoreApplication.translate("Login", u"Restablecer Contrase\u00f1a", None))
        self.resetPassStatus.setText("")
        self.emailEdit_3.setPlaceholderText(QCoreApplication.translate("Login", u"Ingrese el correo electr\u00f3nico", None))
        self.label_12.setText(QCoreApplication.translate("Login", u"Se le enviar\u00e1 un correo para", None))
        self.label_13.setText(QCoreApplication.translate("Login", u"que restablezca su contrase\u00f1a", None))
        self.bt_ResetPass_2.setText(QCoreApplication.translate("Login", u"Enviar correo", None))
        self.label_10.setText(QCoreApplication.translate("Login", u"\u00bfYa tienes tu contrase\u00f1a?", None))
        self.bt_IniciaSesion_2.setText(QCoreApplication.translate("Login", u" Inicia sesi\u00f3n ", None))
    # retranslateUi

