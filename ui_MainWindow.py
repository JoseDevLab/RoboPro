# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowrYQTPX.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
    QWidget)

from clases.BotonesPersonalizados import AnimatedButton
from clases.ContenidosTemas import ContenidosTemas

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1350, 710)
        icon = QIcon()
        icon.addFile(u"resources/images/icon.jpeg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frameBackground = QFrame(self.centralwidget)
        self.frameBackground.setObjectName(u"frameBackground")
        self.frameBackground.setStyleSheet(u"QFrame#frameBackground{\n"
"background-color:qlineargradient(spread:reflect, x1:0.494, y1:0.108409, x2:0.5, y2:0.495, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(38, 38, 38, 255));\n"
"background-image: url(resources/images/resized_background.png);\n"
"border-radius:12px\n"
"}")
        self.frameBackground.setFrameShape(QFrame.StyledPanel)
        self.frameBackground.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frameBackground)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_superior = QFrame(self.frameBackground)
        self.frame_superior.setObjectName(u"frame_superior")
        self.frame_superior.setMinimumSize(QSize(0, 40))
        self.frame_superior.setMaximumSize(QSize(16777215, 40))
        self.frame_superior.setStyleSheet(u"QFrame{\n"
"background-color: rgba(0,0,0,0);\n"
"}\n"
"\n"
"QLabel{\n"
"background-color: None;\n"
"color: white;\n"
"font: 600 30pt \"Lucida Bright\";\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgba(0,0,0,0);\n"
"border-radius: 17px\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255,255,255,50);\n"
"}")
        self.frame_superior.setFrameShape(QFrame.StyledPanel)
        self.frame_superior.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_superior)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_38 = QLabel(self.frame_superior)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setMinimumSize(QSize(40, 0))
        self.label_38.setMaximumSize(QSize(40, 16777215))
        self.label_38.setPixmap(QPixmap(u"resources/images/logo.png"))
        self.label_38.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_38)

        self.bt_contraer = QPushButton(self.frame_superior)
        self.bt_contraer.setObjectName(u"bt_contraer")
        self.bt_contraer.setMinimumSize(QSize(35, 35))
        self.bt_contraer.setMaximumSize(QSize(35, 35))
        icon1 = QIcon()
        icon1.addFile(u"resources/images/MainWindow/Flecha_Izquierda.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_contraer.setIcon(icon1)
        self.bt_contraer.setIconSize(QSize(35, 35))

        self.horizontalLayout.addWidget(self.bt_contraer)

        self.bt_expandir = QPushButton(self.frame_superior)
        self.bt_expandir.setObjectName(u"bt_expandir")
        self.bt_expandir.setMinimumSize(QSize(35, 35))
        self.bt_expandir.setMaximumSize(QSize(35, 35))
        icon2 = QIcon()
        icon2.addFile(u"resources/images/MainWindow/Flecha_Derecha.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_expandir.setIcon(icon2)
        self.bt_expandir.setIconSize(QSize(35, 35))

        self.horizontalLayout.addWidget(self.bt_expandir)

        self.horizontalSpacer = QSpacerItem(279, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label = QLabel(self.frame_superior)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(279, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.bt_minimize = QPushButton(self.frame_superior)
        self.bt_minimize.setObjectName(u"bt_minimize")
        self.bt_minimize.setMinimumSize(QSize(35, 35))
        self.bt_minimize.setMaximumSize(QSize(35, 35))
        icon3 = QIcon()
        icon3.addFile(u"resources/images/minimize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_minimize.setIcon(icon3)
        self.bt_minimize.setIconSize(QSize(35, 35))

        self.horizontalLayout.addWidget(self.bt_minimize)

        self.bt_normal = QPushButton(self.frame_superior)
        self.bt_normal.setObjectName(u"bt_normal")
        self.bt_normal.setMinimumSize(QSize(35, 35))
        self.bt_normal.setMaximumSize(QSize(35, 35))
        icon4 = QIcon()
        icon4.addFile(u"resources/images/normal.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_normal.setIcon(icon4)
        self.bt_normal.setIconSize(QSize(35, 35))

        self.horizontalLayout.addWidget(self.bt_normal)

        self.bt_maximize = QPushButton(self.frame_superior)
        self.bt_maximize.setObjectName(u"bt_maximize")
        self.bt_maximize.setMinimumSize(QSize(35, 35))
        self.bt_maximize.setMaximumSize(QSize(35, 35))
        icon5 = QIcon()
        icon5.addFile(u"resources/images/maximize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_maximize.setIcon(icon5)
        self.bt_maximize.setIconSize(QSize(35, 35))

        self.horizontalLayout.addWidget(self.bt_maximize)

        self.bt_close = QPushButton(self.frame_superior)
        self.bt_close.setObjectName(u"bt_close")
        self.bt_close.setMinimumSize(QSize(35, 35))
        self.bt_close.setMaximumSize(QSize(35, 35))
        icon6 = QIcon()
        icon6.addFile(u"resources/images/close.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_close.setIcon(icon6)
        self.bt_close.setIconSize(QSize(35, 35))

        self.horizontalLayout.addWidget(self.bt_close)


        self.verticalLayout_2.addWidget(self.frame_superior)

        self.frame_inferior = QFrame(self.frameBackground)
        self.frame_inferior.setObjectName(u"frame_inferior")
        self.frame_inferior.setStyleSheet(u"QFrame{\n"
"background-color: None;\n"
"}\n"
"QTabBar::tab {\n"
"width: 150px; /* Ajusta el ancho de las pesta\u00f1as seg\u00fan sea necesario */\n"
"}\n"
"\n"
"QTabWidget::pane { /* The tab widget frame */\n"
"    border-top: 0px solid #C2C7CB;  /*Lo hace invisible*/\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"	alignment: center;\n"
"}\n"
"\n"
"/* Style the tab using the tab sub-control. Note that\n"
"    it reads QTabBar _not_ QTabWidget */\n"
"QTabBar::tab {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"    border: 2px solid #C4C4C3;\n"
"    border-bottom-color: #C2C7CB; /* same as the pane color */\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"    min-width: 8ex;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
""
                        "                                stop: 0 #fafafa, stop: 0.4 #f4f4f4,\n"
"                                stop: 0.5 #e7e7e7, stop: 1.0 #fafafa);\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    border-color: #9B9B9B;\n"
"    border-bottom-color: #C2C7CB; /* same as pane color */\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    margin-top: 2px; /* make non-selected tabs look smaller */\n"
"}\n"
"\n"
"/* make use of negative margins for overlapping tabs */\n"
"QTabBar::tab:selected {\n"
"    /* expand/overlap to the left and right by 4px */\n"
"    margin-left: -4px;\n"
"    margin-right: -4px;\n"
"}\n"
"\n"
"QTabBar::tab:first:selected {\n"
"    margin-left: 0; /* the first selected tab has nothing to overlap with on the left */\n"
"}\n"
"\n"
"QTabBar::tab:last:selected {\n"
"    margin-right: 0; /* the last selected tab has nothing to overlap with on the right */\n"
"}\n"
"\n"
"QTabBar::tab:only-one {\n"
"    margin: 0; /* if there is only one tab, we don't want overlapping margins */\n"
"}\n"
"\n"
"/****QScrollBar"
                        " Vertical****/\n"
"QScrollBar:vertical {\n"
"    border: 2px solid rgb(218, 218, 218);\n"
"    background: rgb(239, 184, 16);\n"
"    width: 17px;\n"
"    margin: 22px 0 22px 0;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background: rgb(0, 51, 102);\n"
"    min-height: 20px;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"    border: 2px solid rgba(173, 51, 51,255);\n"
"    background: rgb(0, 51, 102);\n"
"    height: 20px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    border: 2px solid rgba(173, 51, 51,255);\n"
"    background: rgb(0, 51, 102);\n"
"    height: 20px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    border: 2px solid rgb(239, 184, 16);\n"
"    width: 3px;\n"
"    height: 3px;\n"
"    background: rgb(218, 218, 218);\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background:"
                        " rgb(218, 218, 218);\n"
"}\n"
"\n"
"\n"
"/****QScrillBar horizontal****/\n"
"QScrollBar:horizontal {\n"
"    border: 2px solid rgb(218, 218, 218);\n"
"    background: rgb(218, 218, 218);\n"
"    height: 17px;\n"
"    margin: 0px 22px 0 22px;\n"
"}        \n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(0, 51, 102);\n"
"    min-width: 20px;\n"
"}        \n"
"QScrollBar::add-line:horizontal {\n"
"    border: 2px solid rgba(173, 51, 51,255);\n"
"    background: rgb(0, 51, 102);\n"
"    width: 20px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: 2px solid rgba(173, 51, 51,255);\n"
"    background: rgb(0, 51, 102);\n"
"    width: 20px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar:left-arrow:horizontal, QScrollBar::right-arrow:horizontal {\n"
"    border: 2px solid rgb(239, 184, 16);\n"
"    width: 3px;\n"
"    height: 3px;\n"
"    background: rgb(218, 218, 218);\n"
"}\n"
""
                        "\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"    background: rgb(218, 218, 218);\n"
"}")
        self.frame_inferior.setFrameShape(QFrame.StyledPanel)
        self.frame_inferior.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_inferior)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.menu_lateral = QFrame(self.frame_inferior)
        self.menu_lateral.setObjectName(u"menu_lateral")
        self.menu_lateral.setMinimumSize(QSize(0, 0))
        self.menu_lateral.setMaximumSize(QSize(300, 16777215))
        self.menu_lateral.setStyleSheet(u"QFrame#menu_lateral{\n"
"background-color:rgba(0, 0, 0,0)\n"
"}\n"
"QLabel{\n"
"color:white;\n"
"font: 700 14pt \"Segoe UI\";\n"
"}\n"
"QLabel#lb_userID,\n"
"QLabel#lb_bienvenido,\n"
"QLabel#lb_userName{\n"
"background-color:rgba(0,0,0,100);\n"
"}\n"
"QPushButton{\n"
"color:white;\n"
"border-radius:10px;\n"
"	font: 14pt \"Segoe UI\";\n"
"}\n"
"QPushButton#bt_cerrarSesion:hover{\n"
"color:rgba(173, 51, 51,255);\n"
"background-color: rgba(0, 51, 102,100);\n"
"}\n"
"QPushButton#bt_acercaDe:hover,\n"
"QPushButton#bt_perfil:hover{\n"
"/*color:rgb(0, 51, 102);*/\n"
"background-color: rgba(0, 51, 102,100);\n"
"}")
        self.menu_lateral.setFrameShape(QFrame.StyledPanel)
        self.menu_lateral.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.menu_lateral)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.bt_perfil = QPushButton(self.menu_lateral)
        self.bt_perfil.setObjectName(u"bt_perfil")
        self.bt_perfil.setMinimumSize(QSize(200, 200))
        self.bt_perfil.setCursor(QCursor(Qt.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(u"resources/images/MainWindow/perfiles/avatar_0.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_perfil.setIcon(icon7)
        self.bt_perfil.setIconSize(QSize(200, 200))

        self.verticalLayout_15.addWidget(self.bt_perfil)

        self.lb_userID = QLabel(self.menu_lateral)
        self.lb_userID.setObjectName(u"lb_userID")
        self.lb_userID.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.lb_userID)

        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_15.addItem(self.verticalSpacer_4)

        self.lb_bienvenido = QLabel(self.menu_lateral)
        self.lb_bienvenido.setObjectName(u"lb_bienvenido")
        self.lb_bienvenido.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.lb_bienvenido)

        self.lb_userName = QLabel(self.menu_lateral)
        self.lb_userName.setObjectName(u"lb_userName")
        self.lb_userName.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.lb_userName)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer)

        self.horizontalLayout_39 = QHBoxLayout()
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalSpacer_74 = QSpacerItem(0, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_39.addItem(self.horizontalSpacer_74)

        self.bt_cerrarSesion = QPushButton(self.menu_lateral)
        self.bt_cerrarSesion.setObjectName(u"bt_cerrarSesion")
        self.bt_cerrarSesion.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_39.addWidget(self.bt_cerrarSesion)

        self.horizontalSpacer_73 = QSpacerItem(0, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_39.addItem(self.horizontalSpacer_73)


        self.verticalLayout_15.addLayout(self.horizontalLayout_39)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_15.addItem(self.verticalSpacer_3)

        self.horizontalLayout_40 = QHBoxLayout()
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalSpacer_75 = QSpacerItem(0, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_40.addItem(self.horizontalSpacer_75)

        self.bt_acercaDe = QPushButton(self.menu_lateral)
        self.bt_acercaDe.setObjectName(u"bt_acercaDe")
        self.bt_acercaDe.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_40.addWidget(self.bt_acercaDe)

        self.horizontalSpacer_76 = QSpacerItem(0, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_40.addItem(self.horizontalSpacer_76)


        self.verticalLayout_15.addLayout(self.horizontalLayout_40)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_15.addItem(self.verticalSpacer_2)


        self.horizontalLayout_2.addWidget(self.menu_lateral)

        self.stackedWidget = QStackedWidget(self.frame_inferior)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"QPushButton#bt_U1_T1,\n"
"QPushButton#bt_U1_T2,\n"
"QPushButton#bt_U1_T3,\n"
"QPushButton#bt_U1_T4,\n"
"QPushButton#bt_U1_T5,\n"
"QPushButton#bt_U2_T1,\n"
"QPushButton#bt_U2_T2,\n"
"QPushButton#bt_U2_T3,\n"
"QPushButton#bt_U2_T4,\n"
"QPushButton#bt_U2_T5,\n"
"QPushButton#bt_U2_T6,\n"
"QPushButton#bt_U2_T7,\n"
"QPushButton#bt_U2_T8,\n"
"QPushButton#bt_U2_T9,\n"
"QPushButton#bt_U3_T1,\n"
"QPushButton#bt_U3_T2,\n"
"QPushButton#bt_U3_T3,\n"
"QPushButton#bt_U3_T4,\n"
"QPushButton#bt_U3_T5,\n"
"QPushButton#bt_U3_T6,\n"
"QPushButton#bt_U3_T7,\n"
"QPushButton#bt_U3_T8,\n"
"QPushButton#bt_U3_T9,\n"
"QPushButton#bt_U4_T1,\n"
"QPushButton#bt_U4_T2,\n"
"QPushButton#bt_U4_T3,\n"
"QPushButton#bt_U4_T4,\n"
"QPushButton#bt_U4_T5,\n"
"QPushButton#bt_U4_T6,\n"
"QPushButton#bt_U4_T7,\n"
"QPushButton#bt_U4_T8{\n"
"border:1px solid black;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.unidades = QWidget()
        self.unidades.setObjectName(u"unidades")
        self.unidades.setStyleSheet(u"QLabel{\n"
"background-color: None;\n"
"color: white;\n"
"font: 10pt \"Snap ITC\";\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgba(0,0,0,0);\n"
"color: white;\n"
"}")
        self.horizontalLayout_3 = QHBoxLayout(self.unidades)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_U1 = QFrame(self.unidades)
        self.frame_U1.setObjectName(u"frame_U1")
        self.frame_U1.setStyleSheet(u"QFrame{\n"
"background-color: rgba(173, 51, 51,255);\n"
"}\n"
"")
        self.frame_U1.setFrameShape(QFrame.StyledPanel)
        self.frame_U1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_U1)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.bt_unidad_1 = AnimatedButton(self.frame_U1)
        self.bt_unidad_1.setObjectName(u"bt_unidad_1")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bt_unidad_1.sizePolicy().hasHeightForWidth())
        self.bt_unidad_1.setSizePolicy(sizePolicy)
        self.bt_unidad_1.setMinimumSize(QSize(0, 0))
        self.bt_unidad_1.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.bt_unidad_1)


        self.horizontalLayout_3.addWidget(self.frame_U1)

        self.frame_U2 = QFrame(self.unidades)
        self.frame_U2.setObjectName(u"frame_U2")
        self.frame_U2.setStyleSheet(u"QFrame{\n"
"background-color: rgb(0, 51, 102);\n"
"}")
        self.frame_U2.setFrameShape(QFrame.StyledPanel)
        self.frame_U2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_U2)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.bt_unidad_2 = AnimatedButton(self.frame_U2)
        self.bt_unidad_2.setObjectName(u"bt_unidad_2")
        sizePolicy.setHeightForWidth(self.bt_unidad_2.sizePolicy().hasHeightForWidth())
        self.bt_unidad_2.setSizePolicy(sizePolicy)
        self.bt_unidad_2.setStyleSheet(u"")

        self.verticalLayout_4.addWidget(self.bt_unidad_2)


        self.horizontalLayout_3.addWidget(self.frame_U2)

        self.frame_U3 = QFrame(self.unidades)
        self.frame_U3.setObjectName(u"frame_U3")
        self.frame_U3.setStyleSheet(u"QFrame{\n"
"background-color: rgb(218, 218, 218);\n"
"}")
        self.frame_U3.setFrameShape(QFrame.StyledPanel)
        self.frame_U3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_U3)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.bt_unidad_3 = AnimatedButton(self.frame_U3)
        self.bt_unidad_3.setObjectName(u"bt_unidad_3")
        sizePolicy.setHeightForWidth(self.bt_unidad_3.sizePolicy().hasHeightForWidth())
        self.bt_unidad_3.setSizePolicy(sizePolicy)

        self.verticalLayout_5.addWidget(self.bt_unidad_3)


        self.horizontalLayout_3.addWidget(self.frame_U3)

        self.frame_U4 = QFrame(self.unidades)
        self.frame_U4.setObjectName(u"frame_U4")
        self.frame_U4.setStyleSheet(u"QFrame{\n"
"background-color:rgb(239, 184, 16);\n"
"}")
        self.frame_U4.setFrameShape(QFrame.StyledPanel)
        self.frame_U4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_U4)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.bt_unidad_4 = AnimatedButton(self.frame_U4)
        self.bt_unidad_4.setObjectName(u"bt_unidad_4")
        sizePolicy.setHeightForWidth(self.bt_unidad_4.sizePolicy().hasHeightForWidth())
        self.bt_unidad_4.setSizePolicy(sizePolicy)

        self.verticalLayout_6.addWidget(self.bt_unidad_4)


        self.horizontalLayout_3.addWidget(self.frame_U4)

        self.stackedWidget.addWidget(self.unidades)
        self.unidad_1 = QWidget()
        self.unidad_1.setObjectName(u"unidad_1")
        self.unidad_1.setStyleSheet(u"QLabel{\n"
"background-color: None;\n"
"color: white;\n"
"font: 16pt \"Britannic Bold\";\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgba(173, 51, 51,0);\n"
"color: white;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255,255,255,50);\n"
"}\n"
"")
        self.verticalLayout_7 = QVBoxLayout(self.unidad_1)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.stackedUnidad_1 = QStackedWidget(self.unidad_1)
        self.stackedUnidad_1.setObjectName(u"stackedUnidad_1")
        self.stackedUnidad_1.setStyleSheet(u"")
        self.temas = QWidget()
        self.temas.setObjectName(u"temas")
        self.temas.setStyleSheet(u"QFrame#frame_8,\n"
"QFrame#frame_7{\n"
"background-color:rgba(173, 51, 51,255);\n"
"}")
        self.verticalLayout_8 = QVBoxLayout(self.temas)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.temas)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 35))
        self.frame_7.setMaximumSize(QSize(16777215, 40))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.bt_return = QPushButton(self.frame_7)
        self.bt_return.setObjectName(u"bt_return")
        self.bt_return.setMinimumSize(QSize(35, 35))
        self.bt_return.setMaximumSize(QSize(35, 35))
        icon8 = QIcon()
        icon8.addFile(u"resources/images/MainWindow/return.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_return.setIcon(icon8)
        self.bt_return.setIconSize(QSize(35, 35))

        self.horizontalLayout_4.addWidget(self.bt_return)

        self.horizontalSpacer_3 = QSpacerItem(0, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.label_2 = QLabel(self.frame_7)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_2)

        self.horizontalSpacer_4 = QSpacerItem(0, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)


        self.verticalLayout_8.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.temas)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_8)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.frame_8)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_9)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.bt_U1_T1 = AnimatedButton(self.frame_9)
        self.bt_U1_T1.setObjectName(u"bt_U1_T1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.bt_U1_T1.sizePolicy().hasHeightForWidth())
        self.bt_U1_T1.setSizePolicy(sizePolicy1)

        self.verticalLayout_9.addWidget(self.bt_U1_T1)


        self.gridLayout.addWidget(self.frame_9, 0, 0, 1, 1)

        self.frame_10 = QFrame(self.frame_8)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_10)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.bt_U1_T2 = AnimatedButton(self.frame_10)
        self.bt_U1_T2.setObjectName(u"bt_U1_T2")
        sizePolicy1.setHeightForWidth(self.bt_U1_T2.sizePolicy().hasHeightForWidth())
        self.bt_U1_T2.setSizePolicy(sizePolicy1)

        self.verticalLayout_10.addWidget(self.bt_U1_T2)


        self.gridLayout.addWidget(self.frame_10, 0, 1, 1, 1)

        self.frame_11 = QFrame(self.frame_8)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_11)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.bt_U1_T3 = AnimatedButton(self.frame_11)
        self.bt_U1_T3.setObjectName(u"bt_U1_T3")
        sizePolicy1.setHeightForWidth(self.bt_U1_T3.sizePolicy().hasHeightForWidth())
        self.bt_U1_T3.setSizePolicy(sizePolicy1)

        self.verticalLayout_11.addWidget(self.bt_U1_T3)


        self.gridLayout.addWidget(self.frame_11, 0, 2, 1, 1)

        self.frame_12 = QFrame(self.frame_8)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_12)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.bt_U1_T4 = AnimatedButton(self.frame_12)
        self.bt_U1_T4.setObjectName(u"bt_U1_T4")
        sizePolicy1.setHeightForWidth(self.bt_U1_T4.sizePolicy().hasHeightForWidth())
        self.bt_U1_T4.setSizePolicy(sizePolicy1)

        self.verticalLayout_12.addWidget(self.bt_U1_T4)


        self.gridLayout.addWidget(self.frame_12, 1, 0, 1, 1)

        self.frame_13 = QFrame(self.frame_8)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_13)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.bt_U1_T5 = AnimatedButton(self.frame_13)
        self.bt_U1_T5.setObjectName(u"bt_U1_T5")
        sizePolicy1.setHeightForWidth(self.bt_U1_T5.sizePolicy().hasHeightForWidth())
        self.bt_U1_T5.setSizePolicy(sizePolicy1)

        self.verticalLayout_13.addWidget(self.bt_U1_T5)


        self.gridLayout.addWidget(self.frame_13, 1, 1, 1, 1)


        self.verticalLayout_8.addWidget(self.frame_8)

        self.stackedUnidad_1.addWidget(self.temas)
        self.sk_U1_T1 = QWidget()
        self.sk_U1_T1.setObjectName(u"sk_U1_T1")
        self.sk_U1_T1.setStyleSheet(u"")
        self.verticalLayout_14 = QVBoxLayout(self.sk_U1_T1)
        self.verticalLayout_14.setSpacing(5)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frame_14 = QFrame(self.sk_U1_T1)
        self.frame_14.setObjectName(u"frame_14")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy2)
        self.frame_14.setMinimumSize(QSize(0, 35))
        self.frame_14.setMaximumSize(QSize(16777215, 70))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.bt_return_1 = QPushButton(self.frame_14)
        self.bt_return_1.setObjectName(u"bt_return_1")
        self.bt_return_1.setMinimumSize(QSize(35, 35))
        self.bt_return_1.setMaximumSize(QSize(35, 35))
        self.bt_return_1.setIcon(icon8)
        self.bt_return_1.setIconSize(QSize(35, 35))

        self.horizontalLayout_5.addWidget(self.bt_return_1)

        self.horizontalSpacer_5 = QSpacerItem(131, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)

        self.label_3 = QLabel(self.frame_14)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_3)

        self.horizontalSpacer_6 = QSpacerItem(131, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_6)


        self.verticalLayout_14.addWidget(self.frame_14)

        self.U1_T1 = ContenidosTemas(self.sk_U1_T1)
        self.U1_T1.setObjectName(u"U1_T1")

        self.verticalLayout_14.addWidget(self.U1_T1)

        self.stackedUnidad_1.addWidget(self.sk_U1_T1)
        self.sk_U1_T2 = QWidget()
        self.sk_U1_T2.setObjectName(u"sk_U1_T2")
        self.verticalLayout_16 = QVBoxLayout(self.sk_U1_T2)
        self.verticalLayout_16.setSpacing(5)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_15 = QFrame(self.sk_U1_T2)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(0, 35))
        self.frame_15.setMaximumSize(QSize(16777215, 40))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.bt_return_2 = QPushButton(self.frame_15)
        self.bt_return_2.setObjectName(u"bt_return_2")
        self.bt_return_2.setMinimumSize(QSize(35, 35))
        self.bt_return_2.setMaximumSize(QSize(35, 35))
        self.bt_return_2.setIcon(icon8)
        self.bt_return_2.setIconSize(QSize(35, 35))

        self.horizontalLayout_6.addWidget(self.bt_return_2)

        self.horizontalSpacer_7 = QSpacerItem(131, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_7)

        self.label_5 = QLabel(self.frame_15)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_5)

        self.horizontalSpacer_8 = QSpacerItem(131, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_8)


        self.verticalLayout_16.addWidget(self.frame_15)

        self.U1_T2 = ContenidosTemas(self.sk_U1_T2)
        self.U1_T2.setObjectName(u"U1_T2")
        self.U1_T2.setMinimumSize(QSize(0, 300))

        self.verticalLayout_16.addWidget(self.U1_T2)

        self.stackedUnidad_1.addWidget(self.sk_U1_T2)
        self.sk_U1_T3 = QWidget()
        self.sk_U1_T3.setObjectName(u"sk_U1_T3")
        self.verticalLayout_17 = QVBoxLayout(self.sk_U1_T3)
        self.verticalLayout_17.setSpacing(5)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_16 = QFrame(self.sk_U1_T3)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(0, 35))
        self.frame_16.setMaximumSize(QSize(16777215, 40))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.bt_return_3 = QPushButton(self.frame_16)
        self.bt_return_3.setObjectName(u"bt_return_3")
        self.bt_return_3.setMinimumSize(QSize(35, 35))
        self.bt_return_3.setMaximumSize(QSize(35, 35))
        self.bt_return_3.setIcon(icon8)
        self.bt_return_3.setIconSize(QSize(35, 35))

        self.horizontalLayout_7.addWidget(self.bt_return_3)

        self.horizontalSpacer_9 = QSpacerItem(131, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_9)

        self.label_6 = QLabel(self.frame_16)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_6)

        self.horizontalSpacer_10 = QSpacerItem(131, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_10)


        self.verticalLayout_17.addWidget(self.frame_16)

        self.U1_T3 = ContenidosTemas(self.sk_U1_T3)
        self.U1_T3.setObjectName(u"U1_T3")

        self.verticalLayout_17.addWidget(self.U1_T3)

        self.stackedUnidad_1.addWidget(self.sk_U1_T3)
        self.sk_U1_T4 = QWidget()
        self.sk_U1_T4.setObjectName(u"sk_U1_T4")
        self.verticalLayout_18 = QVBoxLayout(self.sk_U1_T4)
        self.verticalLayout_18.setSpacing(5)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.frame_17 = QFrame(self.sk_U1_T4)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMinimumSize(QSize(0, 35))
        self.frame_17.setMaximumSize(QSize(16777215, 40))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.bt_return_4 = QPushButton(self.frame_17)
        self.bt_return_4.setObjectName(u"bt_return_4")
        self.bt_return_4.setMinimumSize(QSize(35, 35))
        self.bt_return_4.setMaximumSize(QSize(35, 35))
        self.bt_return_4.setIcon(icon8)
        self.bt_return_4.setIconSize(QSize(35, 35))

        self.horizontalLayout_8.addWidget(self.bt_return_4)

        self.horizontalSpacer_11 = QSpacerItem(131, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_11)

        self.label_7 = QLabel(self.frame_17)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_7)

        self.horizontalSpacer_12 = QSpacerItem(131, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_12)


        self.verticalLayout_18.addWidget(self.frame_17)

        self.U1_T4 = ContenidosTemas(self.sk_U1_T4)
        self.U1_T4.setObjectName(u"U1_T4")

        self.verticalLayout_18.addWidget(self.U1_T4)

        self.stackedUnidad_1.addWidget(self.sk_U1_T4)
        self.sk_U1_T5 = QWidget()
        self.sk_U1_T5.setObjectName(u"sk_U1_T5")
        self.verticalLayout_19 = QVBoxLayout(self.sk_U1_T5)
        self.verticalLayout_19.setSpacing(5)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.frame_18 = QFrame(self.sk_U1_T5)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMinimumSize(QSize(0, 35))
        self.frame_18.setMaximumSize(QSize(16777215, 40))
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.bt_return_5 = QPushButton(self.frame_18)
        self.bt_return_5.setObjectName(u"bt_return_5")
        self.bt_return_5.setMinimumSize(QSize(35, 35))
        self.bt_return_5.setMaximumSize(QSize(35, 35))
        self.bt_return_5.setIcon(icon8)
        self.bt_return_5.setIconSize(QSize(35, 35))

        self.horizontalLayout_9.addWidget(self.bt_return_5)

        self.horizontalSpacer_13 = QSpacerItem(131, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_13)

        self.label_8 = QLabel(self.frame_18)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_8)

        self.horizontalSpacer_14 = QSpacerItem(131, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_14)


        self.verticalLayout_19.addWidget(self.frame_18)

        self.U1_T5 = ContenidosTemas(self.sk_U1_T5)
        self.U1_T5.setObjectName(u"U1_T5")

        self.verticalLayout_19.addWidget(self.U1_T5)

        self.stackedUnidad_1.addWidget(self.sk_U1_T5)

        self.verticalLayout_7.addWidget(self.stackedUnidad_1)

        self.stackedWidget.addWidget(self.unidad_1)
        self.unidad_2 = QWidget()
        self.unidad_2.setObjectName(u"unidad_2")
        self.unidad_2.setStyleSheet(u"QLabel{\n"
"background-color: None;\n"
"color: white;\n"
"font: 16pt \"Britannic Bold\";\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgba(0,0,0,0);\n"
"color: white;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255,255,255,50);\n"
"}\n"
"")
        self.verticalLayout_31 = QVBoxLayout(self.unidad_2)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.stackedUnidad_2 = QStackedWidget(self.unidad_2)
        self.stackedUnidad_2.setObjectName(u"stackedUnidad_2")
        self.temas_2 = QWidget()
        self.temas_2.setObjectName(u"temas_2")
        self.temas_2.setStyleSheet(u"QFrame#frame_19,\n"
"QFrame#frame_20{\n"
"background-color:rgb(0, 51, 102);\n"
"}")
        self.verticalLayout_20 = QVBoxLayout(self.temas_2)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.frame_19 = QFrame(self.temas_2)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMinimumSize(QSize(0, 35))
        self.frame_19.setMaximumSize(QSize(16777215, 40))
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.bt_return_6 = QPushButton(self.frame_19)
        self.bt_return_6.setObjectName(u"bt_return_6")
        self.bt_return_6.setMinimumSize(QSize(35, 35))
        self.bt_return_6.setMaximumSize(QSize(35, 35))
        self.bt_return_6.setStyleSheet(u"QPushButton{\n"
"background-color:rgba(0,0,0,200);\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(255,255,255,50);\n"
"}")
        self.bt_return_6.setIcon(icon8)
        self.bt_return_6.setIconSize(QSize(35, 35))

        self.horizontalLayout_10.addWidget(self.bt_return_6)

        self.horizontalSpacer_15 = QSpacerItem(0, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_15)

        self.label_9 = QLabel(self.frame_19)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_9)

        self.horizontalSpacer_16 = QSpacerItem(0, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_16)


        self.verticalLayout_20.addWidget(self.frame_19)

        self.frame_20 = QFrame(self.temas_2)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setStyleSheet(u"")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_20)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_21 = QFrame(self.frame_20)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_21)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.bt_U2_T1 = AnimatedButton(self.frame_21)
        self.bt_U2_T1.setObjectName(u"bt_U2_T1")
        sizePolicy1.setHeightForWidth(self.bt_U2_T1.sizePolicy().hasHeightForWidth())
        self.bt_U2_T1.setSizePolicy(sizePolicy1)

        self.verticalLayout_21.addWidget(self.bt_U2_T1)


        self.gridLayout_2.addWidget(self.frame_21, 0, 0, 1, 1)

        self.frame_22 = QFrame(self.frame_20)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_22)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.bt_U2_T2 = AnimatedButton(self.frame_22)
        self.bt_U2_T2.setObjectName(u"bt_U2_T2")
        sizePolicy1.setHeightForWidth(self.bt_U2_T2.sizePolicy().hasHeightForWidth())
        self.bt_U2_T2.setSizePolicy(sizePolicy1)

        self.verticalLayout_22.addWidget(self.bt_U2_T2)


        self.gridLayout_2.addWidget(self.frame_22, 0, 1, 1, 1)

        self.frame_23 = QFrame(self.frame_20)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_23)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.bt_U2_T3 = AnimatedButton(self.frame_23)
        self.bt_U2_T3.setObjectName(u"bt_U2_T3")
        sizePolicy1.setHeightForWidth(self.bt_U2_T3.sizePolicy().hasHeightForWidth())
        self.bt_U2_T3.setSizePolicy(sizePolicy1)

        self.verticalLayout_23.addWidget(self.bt_U2_T3)


        self.gridLayout_2.addWidget(self.frame_23, 0, 2, 1, 1)

        self.frame_24 = QFrame(self.frame_20)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_24)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.bt_U2_T4 = AnimatedButton(self.frame_24)
        self.bt_U2_T4.setObjectName(u"bt_U2_T4")
        sizePolicy1.setHeightForWidth(self.bt_U2_T4.sizePolicy().hasHeightForWidth())
        self.bt_U2_T4.setSizePolicy(sizePolicy1)

        self.verticalLayout_24.addWidget(self.bt_U2_T4)


        self.gridLayout_2.addWidget(self.frame_24, 1, 0, 1, 1)

        self.frame_25 = QFrame(self.frame_20)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_25)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.bt_U2_T5 = AnimatedButton(self.frame_25)
        self.bt_U2_T5.setObjectName(u"bt_U2_T5")
        sizePolicy1.setHeightForWidth(self.bt_U2_T5.sizePolicy().hasHeightForWidth())
        self.bt_U2_T5.setSizePolicy(sizePolicy1)

        self.verticalLayout_25.addWidget(self.bt_U2_T5)


        self.gridLayout_2.addWidget(self.frame_25, 1, 1, 1, 1)

        self.frame_59 = QFrame(self.frame_20)
        self.frame_59.setObjectName(u"frame_59")
        self.frame_59.setFrameShape(QFrame.StyledPanel)
        self.frame_59.setFrameShadow(QFrame.Raised)
        self.verticalLayout_60 = QVBoxLayout(self.frame_59)
        self.verticalLayout_60.setSpacing(0)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.verticalLayout_60.setContentsMargins(0, 0, 0, 0)
        self.bt_U2_T6 = AnimatedButton(self.frame_59)
        self.bt_U2_T6.setObjectName(u"bt_U2_T6")
        sizePolicy1.setHeightForWidth(self.bt_U2_T6.sizePolicy().hasHeightForWidth())
        self.bt_U2_T6.setSizePolicy(sizePolicy1)

        self.verticalLayout_60.addWidget(self.bt_U2_T6)


        self.gridLayout_2.addWidget(self.frame_59, 1, 2, 1, 1)

        self.frame_60 = QFrame(self.frame_20)
        self.frame_60.setObjectName(u"frame_60")
        self.frame_60.setFrameShape(QFrame.StyledPanel)
        self.frame_60.setFrameShadow(QFrame.Raised)
        self.verticalLayout_62 = QVBoxLayout(self.frame_60)
        self.verticalLayout_62.setSpacing(0)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.verticalLayout_62.setContentsMargins(0, 0, 0, 0)
        self.bt_U2_T7 = AnimatedButton(self.frame_60)
        self.bt_U2_T7.setObjectName(u"bt_U2_T7")
        sizePolicy1.setHeightForWidth(self.bt_U2_T7.sizePolicy().hasHeightForWidth())
        self.bt_U2_T7.setSizePolicy(sizePolicy1)

        self.verticalLayout_62.addWidget(self.bt_U2_T7)


        self.gridLayout_2.addWidget(self.frame_60, 2, 0, 1, 1)

        self.frame_61 = QFrame(self.frame_20)
        self.frame_61.setObjectName(u"frame_61")
        self.frame_61.setFrameShape(QFrame.StyledPanel)
        self.frame_61.setFrameShadow(QFrame.Raised)
        self.verticalLayout_63 = QVBoxLayout(self.frame_61)
        self.verticalLayout_63.setSpacing(0)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.verticalLayout_63.setContentsMargins(0, 0, 0, 0)
        self.bt_U2_T8 = AnimatedButton(self.frame_61)
        self.bt_U2_T8.setObjectName(u"bt_U2_T8")
        sizePolicy1.setHeightForWidth(self.bt_U2_T8.sizePolicy().hasHeightForWidth())
        self.bt_U2_T8.setSizePolicy(sizePolicy1)

        self.verticalLayout_63.addWidget(self.bt_U2_T8)


        self.gridLayout_2.addWidget(self.frame_61, 2, 1, 1, 1)

        self.frame_62 = QFrame(self.frame_20)
        self.frame_62.setObjectName(u"frame_62")
        self.frame_62.setFrameShape(QFrame.StyledPanel)
        self.frame_62.setFrameShadow(QFrame.Raised)
        self.verticalLayout_64 = QVBoxLayout(self.frame_62)
        self.verticalLayout_64.setSpacing(0)
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.verticalLayout_64.setContentsMargins(0, 0, 0, 0)
        self.bt_U2_T9 = AnimatedButton(self.frame_62)
        self.bt_U2_T9.setObjectName(u"bt_U2_T9")
        sizePolicy1.setHeightForWidth(self.bt_U2_T9.sizePolicy().hasHeightForWidth())
        self.bt_U2_T9.setSizePolicy(sizePolicy1)

        self.verticalLayout_64.addWidget(self.bt_U2_T9)


        self.gridLayout_2.addWidget(self.frame_62, 2, 2, 1, 1)


        self.verticalLayout_20.addWidget(self.frame_20)

        self.stackedUnidad_2.addWidget(self.temas_2)
        self.sk_U2_T1 = QWidget()
        self.sk_U2_T1.setObjectName(u"sk_U2_T1")
        self.verticalLayout_26 = QVBoxLayout(self.sk_U2_T1)
        self.verticalLayout_26.setSpacing(5)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.frame_26 = QFrame(self.sk_U2_T1)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setMinimumSize(QSize(0, 35))
        self.frame_26.setMaximumSize(QSize(16777215, 40))
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.bt_return_7 = QPushButton(self.frame_26)
        self.bt_return_7.setObjectName(u"bt_return_7")
        self.bt_return_7.setMinimumSize(QSize(35, 35))
        self.bt_return_7.setMaximumSize(QSize(35, 35))
        self.bt_return_7.setIcon(icon8)
        self.bt_return_7.setIconSize(QSize(35, 35))

        self.horizontalLayout_11.addWidget(self.bt_return_7)

        self.horizontalSpacer_17 = QSpacerItem(131, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_17)

        self.label_10 = QLabel(self.frame_26)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label_10)

        self.horizontalSpacer_18 = QSpacerItem(131, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_18)


        self.verticalLayout_26.addWidget(self.frame_26)

        self.U2_T1 = ContenidosTemas(self.sk_U2_T1)
        self.U2_T1.setObjectName(u"U2_T1")

        self.verticalLayout_26.addWidget(self.U2_T1)

        self.stackedUnidad_2.addWidget(self.sk_U2_T1)
        self.sk_U2_T2 = QWidget()
        self.sk_U2_T2.setObjectName(u"sk_U2_T2")
        self.verticalLayout_27 = QVBoxLayout(self.sk_U2_T2)
        self.verticalLayout_27.setSpacing(5)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.frame_27 = QFrame(self.sk_U2_T2)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setMinimumSize(QSize(0, 35))
        self.frame_27.setMaximumSize(QSize(16777215, 40))
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.bt_return_8 = QPushButton(self.frame_27)
        self.bt_return_8.setObjectName(u"bt_return_8")
        self.bt_return_8.setMinimumSize(QSize(35, 35))
        self.bt_return_8.setMaximumSize(QSize(35, 35))
        self.bt_return_8.setIcon(icon8)
        self.bt_return_8.setIconSize(QSize(35, 35))

        self.horizontalLayout_12.addWidget(self.bt_return_8)

        self.horizontalSpacer_19 = QSpacerItem(131, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_19)

        self.label_11 = QLabel(self.frame_27)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.label_11)

        self.horizontalSpacer_20 = QSpacerItem(131, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_20)


        self.verticalLayout_27.addWidget(self.frame_27)

        self.U2_T2 = ContenidosTemas(self.sk_U2_T2)
        self.U2_T2.setObjectName(u"U2_T2")

        self.verticalLayout_27.addWidget(self.U2_T2)

        self.stackedUnidad_2.addWidget(self.sk_U2_T2)
        self.sk_U2_T3 = QWidget()
        self.sk_U2_T3.setObjectName(u"sk_U2_T3")
        self.verticalLayout_28 = QVBoxLayout(self.sk_U2_T3)
        self.verticalLayout_28.setSpacing(5)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.frame_28 = QFrame(self.sk_U2_T3)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setMinimumSize(QSize(0, 35))
        self.frame_28.setMaximumSize(QSize(16777215, 40))
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.bt_return_9 = QPushButton(self.frame_28)
        self.bt_return_9.setObjectName(u"bt_return_9")
        self.bt_return_9.setMinimumSize(QSize(35, 35))
        self.bt_return_9.setMaximumSize(QSize(35, 35))
        self.bt_return_9.setIcon(icon8)
        self.bt_return_9.setIconSize(QSize(35, 35))

        self.horizontalLayout_13.addWidget(self.bt_return_9)

        self.horizontalSpacer_21 = QSpacerItem(131, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_21)

        self.label_12 = QLabel(self.frame_28)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_12)

        self.horizontalSpacer_22 = QSpacerItem(131, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_22)


        self.verticalLayout_28.addWidget(self.frame_28)

        self.U2_T3 = ContenidosTemas(self.sk_U2_T3)
        self.U2_T3.setObjectName(u"U2_T3")

        self.verticalLayout_28.addWidget(self.U2_T3)

        self.stackedUnidad_2.addWidget(self.sk_U2_T3)
        self.sk_U2_T4 = QWidget()
        self.sk_U2_T4.setObjectName(u"sk_U2_T4")
        self.verticalLayout_29 = QVBoxLayout(self.sk_U2_T4)
        self.verticalLayout_29.setSpacing(5)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.frame_29 = QFrame(self.sk_U2_T4)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setMinimumSize(QSize(0, 35))
        self.frame_29.setMaximumSize(QSize(16777215, 40))
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.bt_return_10 = QPushButton(self.frame_29)
        self.bt_return_10.setObjectName(u"bt_return_10")
        self.bt_return_10.setMinimumSize(QSize(35, 35))
        self.bt_return_10.setMaximumSize(QSize(35, 35))
        self.bt_return_10.setIcon(icon8)
        self.bt_return_10.setIconSize(QSize(35, 35))

        self.horizontalLayout_14.addWidget(self.bt_return_10)

        self.horizontalSpacer_23 = QSpacerItem(131, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_23)

        self.label_13 = QLabel(self.frame_29)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.label_13)

        self.horizontalSpacer_24 = QSpacerItem(131, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_24)


        self.verticalLayout_29.addWidget(self.frame_29)

        self.U2_T4 = ContenidosTemas(self.sk_U2_T4)
        self.U2_T4.setObjectName(u"U2_T4")

        self.verticalLayout_29.addWidget(self.U2_T4)

        self.stackedUnidad_2.addWidget(self.sk_U2_T4)
        self.sk_U2_T5 = QWidget()
        self.sk_U2_T5.setObjectName(u"sk_U2_T5")
        self.verticalLayout_30 = QVBoxLayout(self.sk_U2_T5)
        self.verticalLayout_30.setSpacing(5)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.frame_30 = QFrame(self.sk_U2_T5)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setMinimumSize(QSize(0, 35))
        self.frame_30.setMaximumSize(QSize(16777215, 40))
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.bt_return_11 = QPushButton(self.frame_30)
        self.bt_return_11.setObjectName(u"bt_return_11")
        self.bt_return_11.setMinimumSize(QSize(35, 35))
        self.bt_return_11.setMaximumSize(QSize(35, 35))
        self.bt_return_11.setIcon(icon8)
        self.bt_return_11.setIconSize(QSize(35, 35))

        self.horizontalLayout_15.addWidget(self.bt_return_11)

        self.horizontalSpacer_25 = QSpacerItem(131, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_25)

        self.label_14 = QLabel(self.frame_30)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.label_14)

        self.horizontalSpacer_26 = QSpacerItem(131, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_26)


        self.verticalLayout_30.addWidget(self.frame_30)

        self.U2_T5 = ContenidosTemas(self.sk_U2_T5)
        self.U2_T5.setObjectName(u"U2_T5")

        self.verticalLayout_30.addWidget(self.U2_T5)

        self.stackedUnidad_2.addWidget(self.sk_U2_T5)
        self.sk_U2_T6 = QWidget()
        self.sk_U2_T6.setObjectName(u"sk_U2_T6")
        self.verticalLayout_56 = QVBoxLayout(self.sk_U2_T6)
        self.verticalLayout_56.setSpacing(5)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.verticalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.frame_55 = QFrame(self.sk_U2_T6)
        self.frame_55.setObjectName(u"frame_55")
        self.frame_55.setMinimumSize(QSize(0, 35))
        self.frame_55.setMaximumSize(QSize(16777215, 40))
        self.frame_55.setFrameShape(QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_55)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.bt_return_24 = QPushButton(self.frame_55)
        self.bt_return_24.setObjectName(u"bt_return_24")
        self.bt_return_24.setMinimumSize(QSize(35, 35))
        self.bt_return_24.setMaximumSize(QSize(35, 35))
        self.bt_return_24.setIcon(icon8)
        self.bt_return_24.setIconSize(QSize(35, 35))

        self.horizontalLayout_28.addWidget(self.bt_return_24)

        self.horizontalSpacer_51 = QSpacerItem(131, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_51)

        self.label_27 = QLabel(self.frame_55)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_28.addWidget(self.label_27)

        self.horizontalSpacer_52 = QSpacerItem(131, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_52)


        self.verticalLayout_56.addWidget(self.frame_55)

        self.U2_T6 = ContenidosTemas(self.sk_U2_T6)
        self.U2_T6.setObjectName(u"U2_T6")

        self.verticalLayout_56.addWidget(self.U2_T6)

        self.stackedUnidad_2.addWidget(self.sk_U2_T6)
        self.sk_U2_T7 = QWidget()
        self.sk_U2_T7.setObjectName(u"sk_U2_T7")
        self.verticalLayout_57 = QVBoxLayout(self.sk_U2_T7)
        self.verticalLayout_57.setSpacing(5)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.verticalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.frame_56 = QFrame(self.sk_U2_T7)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setMinimumSize(QSize(0, 35))
        self.frame_56.setMaximumSize(QSize(16777215, 40))
        self.frame_56.setFrameShape(QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_56)
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.bt_return_25 = QPushButton(self.frame_56)
        self.bt_return_25.setObjectName(u"bt_return_25")
        self.bt_return_25.setMinimumSize(QSize(35, 35))
        self.bt_return_25.setMaximumSize(QSize(35, 35))
        self.bt_return_25.setIcon(icon8)
        self.bt_return_25.setIconSize(QSize(35, 35))

        self.horizontalLayout_29.addWidget(self.bt_return_25)

        self.horizontalSpacer_53 = QSpacerItem(131, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer_53)

        self.label_28 = QLabel(self.frame_56)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_29.addWidget(self.label_28)

        self.horizontalSpacer_54 = QSpacerItem(131, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer_54)


        self.verticalLayout_57.addWidget(self.frame_56)

        self.U2_T7 = ContenidosTemas(self.sk_U2_T7)
        self.U2_T7.setObjectName(u"U2_T7")

        self.verticalLayout_57.addWidget(self.U2_T7)

        self.stackedUnidad_2.addWidget(self.sk_U2_T7)
        self.sk_U2_T8 = QWidget()
        self.sk_U2_T8.setObjectName(u"sk_U2_T8")
        self.verticalLayout_58 = QVBoxLayout(self.sk_U2_T8)
        self.verticalLayout_58.setSpacing(5)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.verticalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.frame_57 = QFrame(self.sk_U2_T8)
        self.frame_57.setObjectName(u"frame_57")
        self.frame_57.setMinimumSize(QSize(0, 35))
        self.frame_57.setMaximumSize(QSize(16777215, 40))
        self.frame_57.setFrameShape(QFrame.StyledPanel)
        self.frame_57.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_57)
        self.horizontalLayout_30.setSpacing(0)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.bt_return_26 = QPushButton(self.frame_57)
        self.bt_return_26.setObjectName(u"bt_return_26")
        self.bt_return_26.setMinimumSize(QSize(35, 35))
        self.bt_return_26.setMaximumSize(QSize(35, 35))
        self.bt_return_26.setIcon(icon8)
        self.bt_return_26.setIconSize(QSize(35, 35))

        self.horizontalLayout_30.addWidget(self.bt_return_26)

        self.horizontalSpacer_55 = QSpacerItem(131, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_55)

        self.label_29 = QLabel(self.frame_57)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_30.addWidget(self.label_29)

        self.horizontalSpacer_56 = QSpacerItem(131, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_56)


        self.verticalLayout_58.addWidget(self.frame_57)

        self.U2_T8 = ContenidosTemas(self.sk_U2_T8)
        self.U2_T8.setObjectName(u"U2_T8")

        self.verticalLayout_58.addWidget(self.U2_T8)

        self.stackedUnidad_2.addWidget(self.sk_U2_T8)
        self.sk_U2_T9 = QWidget()
        self.sk_U2_T9.setObjectName(u"sk_U2_T9")
        self.verticalLayout_59 = QVBoxLayout(self.sk_U2_T9)
        self.verticalLayout_59.setSpacing(5)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.verticalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.frame_58 = QFrame(self.sk_U2_T9)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setMinimumSize(QSize(0, 35))
        self.frame_58.setMaximumSize(QSize(16777215, 40))
        self.frame_58.setFrameShape(QFrame.StyledPanel)
        self.frame_58.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_58)
        self.horizontalLayout_31.setSpacing(0)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.bt_return_27 = QPushButton(self.frame_58)
        self.bt_return_27.setObjectName(u"bt_return_27")
        self.bt_return_27.setMinimumSize(QSize(35, 35))
        self.bt_return_27.setMaximumSize(QSize(35, 35))
        self.bt_return_27.setIcon(icon8)
        self.bt_return_27.setIconSize(QSize(35, 35))

        self.horizontalLayout_31.addWidget(self.bt_return_27)

        self.horizontalSpacer_57 = QSpacerItem(131, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_57)

        self.label_30 = QLabel(self.frame_58)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_31.addWidget(self.label_30)

        self.horizontalSpacer_58 = QSpacerItem(131, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_58)


        self.verticalLayout_59.addWidget(self.frame_58)

        self.U2_T9 = ContenidosTemas(self.sk_U2_T9)
        self.U2_T9.setObjectName(u"U2_T9")

        self.verticalLayout_59.addWidget(self.U2_T9)

        self.stackedUnidad_2.addWidget(self.sk_U2_T9)

        self.verticalLayout_31.addWidget(self.stackedUnidad_2)

        self.stackedWidget.addWidget(self.unidad_2)
        self.unidad_3 = QWidget()
        self.unidad_3.setObjectName(u"unidad_3")
        self.unidad_3.setStyleSheet(u"QLabel{\n"
"background-color: None;\n"
"color: white;\n"
"font: 16pt \"Britannic Bold\";\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgba(0,0,0,0);\n"
"color: white;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255,255,255,50);\n"
"}\n"
"\n"
"")
        self.verticalLayout_43 = QVBoxLayout(self.unidad_3)
        self.verticalLayout_43.setSpacing(0)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.stackedUnidad_3 = QStackedWidget(self.unidad_3)
        self.stackedUnidad_3.setObjectName(u"stackedUnidad_3")
        self.stackedUnidad_3.setStyleSheet(u"")
        self.temas_3 = QWidget()
        self.temas_3.setObjectName(u"temas_3")
        self.temas_3.setStyleSheet(u"QFrame#frame_32,\n"
"QFrame#frame_31{\n"
"background-color: rgb(218, 218, 218)\n"
"}")
        self.verticalLayout_32 = QVBoxLayout(self.temas_3)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.frame_31 = QFrame(self.temas_3)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setMinimumSize(QSize(0, 35))
        self.frame_31.setMaximumSize(QSize(16777215, 40))
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.bt_return_12 = QPushButton(self.frame_31)
        self.bt_return_12.setObjectName(u"bt_return_12")
        self.bt_return_12.setMinimumSize(QSize(35, 35))
        self.bt_return_12.setMaximumSize(QSize(35, 35))
        self.bt_return_12.setIcon(icon8)
        self.bt_return_12.setIconSize(QSize(35, 35))

        self.horizontalLayout_16.addWidget(self.bt_return_12)

        self.horizontalSpacer_27 = QSpacerItem(0, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_27)

        self.label_15 = QLabel(self.frame_31)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.label_15)

        self.horizontalSpacer_28 = QSpacerItem(0, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_28)


        self.verticalLayout_32.addWidget(self.frame_31)

        self.frame_32 = QFrame(self.temas_3)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setStyleSheet(u"")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_32)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_33 = QFrame(self.frame_32)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_33)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.bt_U3_T1 = AnimatedButton(self.frame_33)
        self.bt_U3_T1.setObjectName(u"bt_U3_T1")
        sizePolicy1.setHeightForWidth(self.bt_U3_T1.sizePolicy().hasHeightForWidth())
        self.bt_U3_T1.setSizePolicy(sizePolicy1)

        self.verticalLayout_33.addWidget(self.bt_U3_T1)


        self.gridLayout_3.addWidget(self.frame_33, 0, 0, 1, 1)

        self.frame_34 = QFrame(self.frame_32)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_34)
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.bt_U3_T2 = AnimatedButton(self.frame_34)
        self.bt_U3_T2.setObjectName(u"bt_U3_T2")
        sizePolicy1.setHeightForWidth(self.bt_U3_T2.sizePolicy().hasHeightForWidth())
        self.bt_U3_T2.setSizePolicy(sizePolicy1)

        self.verticalLayout_34.addWidget(self.bt_U3_T2)


        self.gridLayout_3.addWidget(self.frame_34, 0, 1, 1, 1)

        self.frame_35 = QFrame(self.frame_32)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame_35)
        self.verticalLayout_35.setSpacing(0)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.bt_U3_T3 = AnimatedButton(self.frame_35)
        self.bt_U3_T3.setObjectName(u"bt_U3_T3")
        sizePolicy1.setHeightForWidth(self.bt_U3_T3.sizePolicy().hasHeightForWidth())
        self.bt_U3_T3.setSizePolicy(sizePolicy1)

        self.verticalLayout_35.addWidget(self.bt_U3_T3)


        self.gridLayout_3.addWidget(self.frame_35, 0, 2, 1, 1)

        self.frame_36 = QFrame(self.frame_32)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.frame_36)
        self.verticalLayout_36.setSpacing(0)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.bt_U3_T4 = AnimatedButton(self.frame_36)
        self.bt_U3_T4.setObjectName(u"bt_U3_T4")
        sizePolicy1.setHeightForWidth(self.bt_U3_T4.sizePolicy().hasHeightForWidth())
        self.bt_U3_T4.setSizePolicy(sizePolicy1)

        self.verticalLayout_36.addWidget(self.bt_U3_T4)


        self.gridLayout_3.addWidget(self.frame_36, 1, 0, 1, 1)

        self.frame_37 = QFrame(self.frame_32)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.frame_37)
        self.verticalLayout_37.setSpacing(0)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.bt_U3_T5 = AnimatedButton(self.frame_37)
        self.bt_U3_T5.setObjectName(u"bt_U3_T5")
        sizePolicy1.setHeightForWidth(self.bt_U3_T5.sizePolicy().hasHeightForWidth())
        self.bt_U3_T5.setSizePolicy(sizePolicy1)

        self.verticalLayout_37.addWidget(self.bt_U3_T5)


        self.gridLayout_3.addWidget(self.frame_37, 1, 1, 1, 1)

        self.frame_63 = QFrame(self.frame_32)
        self.frame_63.setObjectName(u"frame_63")
        self.frame_63.setFrameShape(QFrame.StyledPanel)
        self.frame_63.setFrameShadow(QFrame.Raised)
        self.verticalLayout_65 = QVBoxLayout(self.frame_63)
        self.verticalLayout_65.setSpacing(0)
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.verticalLayout_65.setContentsMargins(0, 0, 0, 0)
        self.bt_U3_T6 = AnimatedButton(self.frame_63)
        self.bt_U3_T6.setObjectName(u"bt_U3_T6")
        sizePolicy1.setHeightForWidth(self.bt_U3_T6.sizePolicy().hasHeightForWidth())
        self.bt_U3_T6.setSizePolicy(sizePolicy1)

        self.verticalLayout_65.addWidget(self.bt_U3_T6)


        self.gridLayout_3.addWidget(self.frame_63, 1, 2, 1, 1)

        self.frame_64 = QFrame(self.frame_32)
        self.frame_64.setObjectName(u"frame_64")
        self.frame_64.setFrameShape(QFrame.StyledPanel)
        self.frame_64.setFrameShadow(QFrame.Raised)
        self.verticalLayout_66 = QVBoxLayout(self.frame_64)
        self.verticalLayout_66.setSpacing(0)
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.verticalLayout_66.setContentsMargins(0, 0, 0, 0)
        self.bt_U3_T7 = AnimatedButton(self.frame_64)
        self.bt_U3_T7.setObjectName(u"bt_U3_T7")
        sizePolicy1.setHeightForWidth(self.bt_U3_T7.sizePolicy().hasHeightForWidth())
        self.bt_U3_T7.setSizePolicy(sizePolicy1)

        self.verticalLayout_66.addWidget(self.bt_U3_T7)


        self.gridLayout_3.addWidget(self.frame_64, 2, 0, 1, 1)

        self.frame_65 = QFrame(self.frame_32)
        self.frame_65.setObjectName(u"frame_65")
        self.frame_65.setFrameShape(QFrame.StyledPanel)
        self.frame_65.setFrameShadow(QFrame.Raised)
        self.verticalLayout_67 = QVBoxLayout(self.frame_65)
        self.verticalLayout_67.setSpacing(0)
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.verticalLayout_67.setContentsMargins(0, 0, 0, 0)
        self.bt_U3_T8 = AnimatedButton(self.frame_65)
        self.bt_U3_T8.setObjectName(u"bt_U3_T8")
        sizePolicy1.setHeightForWidth(self.bt_U3_T8.sizePolicy().hasHeightForWidth())
        self.bt_U3_T8.setSizePolicy(sizePolicy1)

        self.verticalLayout_67.addWidget(self.bt_U3_T8)


        self.gridLayout_3.addWidget(self.frame_65, 2, 1, 1, 1)

        self.frame_66 = QFrame(self.frame_32)
        self.frame_66.setObjectName(u"frame_66")
        self.frame_66.setFrameShape(QFrame.StyledPanel)
        self.frame_66.setFrameShadow(QFrame.Raised)
        self.verticalLayout_68 = QVBoxLayout(self.frame_66)
        self.verticalLayout_68.setSpacing(0)
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.verticalLayout_68.setContentsMargins(0, 0, 0, 0)
        self.bt_U3_T9 = AnimatedButton(self.frame_66)
        self.bt_U3_T9.setObjectName(u"bt_U3_T9")
        sizePolicy1.setHeightForWidth(self.bt_U3_T9.sizePolicy().hasHeightForWidth())
        self.bt_U3_T9.setSizePolicy(sizePolicy1)

        self.verticalLayout_68.addWidget(self.bt_U3_T9)


        self.gridLayout_3.addWidget(self.frame_66, 2, 2, 1, 1)


        self.verticalLayout_32.addWidget(self.frame_32)

        self.stackedUnidad_3.addWidget(self.temas_3)
        self.sk_U3_T1 = QWidget()
        self.sk_U3_T1.setObjectName(u"sk_U3_T1")
        self.verticalLayout_38 = QVBoxLayout(self.sk_U3_T1)
        self.verticalLayout_38.setSpacing(5)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.frame_38 = QFrame(self.sk_U3_T1)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setMinimumSize(QSize(0, 35))
        self.frame_38.setMaximumSize(QSize(16777215, 40))
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_38)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.bt_return_13 = QPushButton(self.frame_38)
        self.bt_return_13.setObjectName(u"bt_return_13")
        self.bt_return_13.setMinimumSize(QSize(35, 35))
        self.bt_return_13.setMaximumSize(QSize(35, 35))
        self.bt_return_13.setIcon(icon8)
        self.bt_return_13.setIconSize(QSize(35, 35))

        self.horizontalLayout_17.addWidget(self.bt_return_13)

        self.horizontalSpacer_29 = QSpacerItem(131, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_29)

        self.label_16 = QLabel(self.frame_38)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.label_16)

        self.horizontalSpacer_30 = QSpacerItem(131, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_30)


        self.verticalLayout_38.addWidget(self.frame_38)

        self.U3_T1 = ContenidosTemas(self.sk_U3_T1)
        self.U3_T1.setObjectName(u"U3_T1")

        self.verticalLayout_38.addWidget(self.U3_T1)

        self.stackedUnidad_3.addWidget(self.sk_U3_T1)
        self.sk_U3_T2 = QWidget()
        self.sk_U3_T2.setObjectName(u"sk_U3_T2")
        self.verticalLayout_39 = QVBoxLayout(self.sk_U3_T2)
        self.verticalLayout_39.setSpacing(5)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.frame_39 = QFrame(self.sk_U3_T2)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setMinimumSize(QSize(0, 35))
        self.frame_39.setMaximumSize(QSize(16777215, 40))
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_39)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.bt_return_14 = QPushButton(self.frame_39)
        self.bt_return_14.setObjectName(u"bt_return_14")
        self.bt_return_14.setMinimumSize(QSize(35, 35))
        self.bt_return_14.setMaximumSize(QSize(35, 35))
        self.bt_return_14.setIcon(icon8)
        self.bt_return_14.setIconSize(QSize(35, 35))

        self.horizontalLayout_18.addWidget(self.bt_return_14)

        self.horizontalSpacer_31 = QSpacerItem(131, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_31)

        self.label_17 = QLabel(self.frame_39)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.label_17)

        self.horizontalSpacer_32 = QSpacerItem(131, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_32)


        self.verticalLayout_39.addWidget(self.frame_39)

        self.U3_T2 = ContenidosTemas(self.sk_U3_T2)
        self.U3_T2.setObjectName(u"U3_T2")

        self.verticalLayout_39.addWidget(self.U3_T2)

        self.stackedUnidad_3.addWidget(self.sk_U3_T2)
        self.sk_U3_T3 = QWidget()
        self.sk_U3_T3.setObjectName(u"sk_U3_T3")
        self.sk_U3_T3.setStyleSheet(u"")
        self.verticalLayout_40 = QVBoxLayout(self.sk_U3_T3)
        self.verticalLayout_40.setSpacing(5)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.frame_40 = QFrame(self.sk_U3_T3)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setMinimumSize(QSize(0, 35))
        self.frame_40.setMaximumSize(QSize(16777215, 40))
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_40)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.bt_return_15 = QPushButton(self.frame_40)
        self.bt_return_15.setObjectName(u"bt_return_15")
        self.bt_return_15.setMinimumSize(QSize(35, 35))
        self.bt_return_15.setMaximumSize(QSize(35, 35))
        self.bt_return_15.setIcon(icon8)
        self.bt_return_15.setIconSize(QSize(35, 35))

        self.horizontalLayout_19.addWidget(self.bt_return_15)

        self.horizontalSpacer_33 = QSpacerItem(131, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_33)

        self.label_18 = QLabel(self.frame_40)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_19.addWidget(self.label_18)

        self.horizontalSpacer_34 = QSpacerItem(131, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_34)


        self.verticalLayout_40.addWidget(self.frame_40)

        self.U3_T3 = ContenidosTemas(self.sk_U3_T3)
        self.U3_T3.setObjectName(u"U3_T3")

        self.verticalLayout_40.addWidget(self.U3_T3)

        self.stackedUnidad_3.addWidget(self.sk_U3_T3)
        self.sk_U3_T4 = QWidget()
        self.sk_U3_T4.setObjectName(u"sk_U3_T4")
        self.verticalLayout_41 = QVBoxLayout(self.sk_U3_T4)
        self.verticalLayout_41.setSpacing(5)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.frame_41 = QFrame(self.sk_U3_T4)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setMinimumSize(QSize(0, 35))
        self.frame_41.setMaximumSize(QSize(16777215, 40))
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_41)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.bt_return_16 = QPushButton(self.frame_41)
        self.bt_return_16.setObjectName(u"bt_return_16")
        self.bt_return_16.setMinimumSize(QSize(35, 35))
        self.bt_return_16.setMaximumSize(QSize(35, 35))
        self.bt_return_16.setIcon(icon8)
        self.bt_return_16.setIconSize(QSize(35, 35))

        self.horizontalLayout_20.addWidget(self.bt_return_16)

        self.horizontalSpacer_35 = QSpacerItem(131, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_35)

        self.label_19 = QLabel(self.frame_41)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_20.addWidget(self.label_19)

        self.horizontalSpacer_36 = QSpacerItem(131, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_36)


        self.verticalLayout_41.addWidget(self.frame_41)

        self.U3_T4 = ContenidosTemas(self.sk_U3_T4)
        self.U3_T4.setObjectName(u"U3_T4")

        self.verticalLayout_41.addWidget(self.U3_T4)

        self.stackedUnidad_3.addWidget(self.sk_U3_T4)
        self.sk_U3_T5 = QWidget()
        self.sk_U3_T5.setObjectName(u"sk_U3_T5")
        self.verticalLayout_42 = QVBoxLayout(self.sk_U3_T5)
        self.verticalLayout_42.setSpacing(5)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.frame_42 = QFrame(self.sk_U3_T5)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setMinimumSize(QSize(0, 35))
        self.frame_42.setMaximumSize(QSize(16777215, 40))
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_42)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.bt_return_17 = QPushButton(self.frame_42)
        self.bt_return_17.setObjectName(u"bt_return_17")
        self.bt_return_17.setMinimumSize(QSize(35, 35))
        self.bt_return_17.setMaximumSize(QSize(35, 35))
        self.bt_return_17.setIcon(icon8)
        self.bt_return_17.setIconSize(QSize(35, 35))

        self.horizontalLayout_21.addWidget(self.bt_return_17)

        self.horizontalSpacer_37 = QSpacerItem(131, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_37)

        self.label_20 = QLabel(self.frame_42)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_21.addWidget(self.label_20)

        self.horizontalSpacer_38 = QSpacerItem(131, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_38)


        self.verticalLayout_42.addWidget(self.frame_42)

        self.U3_T5 = ContenidosTemas(self.sk_U3_T5)
        self.U3_T5.setObjectName(u"U3_T5")

        self.verticalLayout_42.addWidget(self.U3_T5)

        self.stackedUnidad_3.addWidget(self.sk_U3_T5)
        self.sk_U3_T6 = QWidget()
        self.sk_U3_T6.setObjectName(u"sk_U3_T6")
        self.verticalLayout_69 = QVBoxLayout(self.sk_U3_T6)
        self.verticalLayout_69.setSpacing(5)
        self.verticalLayout_69.setObjectName(u"verticalLayout_69")
        self.verticalLayout_69.setContentsMargins(0, 0, 0, 0)
        self.frame_67 = QFrame(self.sk_U3_T6)
        self.frame_67.setObjectName(u"frame_67")
        self.frame_67.setMinimumSize(QSize(0, 35))
        self.frame_67.setMaximumSize(QSize(16777215, 40))
        self.frame_67.setFrameShape(QFrame.StyledPanel)
        self.frame_67.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_67)
        self.horizontalLayout_32.setSpacing(0)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.bt_return_28 = QPushButton(self.frame_67)
        self.bt_return_28.setObjectName(u"bt_return_28")
        self.bt_return_28.setMinimumSize(QSize(35, 35))
        self.bt_return_28.setMaximumSize(QSize(35, 35))
        self.bt_return_28.setIcon(icon8)
        self.bt_return_28.setIconSize(QSize(35, 35))

        self.horizontalLayout_32.addWidget(self.bt_return_28)

        self.horizontalSpacer_59 = QSpacerItem(131, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_32.addItem(self.horizontalSpacer_59)

        self.label_31 = QLabel(self.frame_67)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_32.addWidget(self.label_31)

        self.horizontalSpacer_60 = QSpacerItem(131, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_32.addItem(self.horizontalSpacer_60)


        self.verticalLayout_69.addWidget(self.frame_67)

        self.U3_T6 = ContenidosTemas(self.sk_U3_T6)
        self.U3_T6.setObjectName(u"U3_T6")

        self.verticalLayout_69.addWidget(self.U3_T6)

        self.stackedUnidad_3.addWidget(self.sk_U3_T6)
        self.sk_U3_T7 = QWidget()
        self.sk_U3_T7.setObjectName(u"sk_U3_T7")
        self.verticalLayout_70 = QVBoxLayout(self.sk_U3_T7)
        self.verticalLayout_70.setSpacing(5)
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.verticalLayout_70.setContentsMargins(0, 0, 0, 0)
        self.frame_68 = QFrame(self.sk_U3_T7)
        self.frame_68.setObjectName(u"frame_68")
        self.frame_68.setMinimumSize(QSize(0, 35))
        self.frame_68.setMaximumSize(QSize(16777215, 40))
        self.frame_68.setFrameShape(QFrame.StyledPanel)
        self.frame_68.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.frame_68)
        self.horizontalLayout_33.setSpacing(0)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.bt_return_29 = QPushButton(self.frame_68)
        self.bt_return_29.setObjectName(u"bt_return_29")
        self.bt_return_29.setMinimumSize(QSize(35, 35))
        self.bt_return_29.setMaximumSize(QSize(35, 35))
        self.bt_return_29.setIcon(icon8)
        self.bt_return_29.setIconSize(QSize(35, 35))

        self.horizontalLayout_33.addWidget(self.bt_return_29)

        self.horizontalSpacer_61 = QSpacerItem(131, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_33.addItem(self.horizontalSpacer_61)

        self.label_32 = QLabel(self.frame_68)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_33.addWidget(self.label_32)

        self.horizontalSpacer_62 = QSpacerItem(131, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_33.addItem(self.horizontalSpacer_62)


        self.verticalLayout_70.addWidget(self.frame_68)

        self.U3_T7 = ContenidosTemas(self.sk_U3_T7)
        self.U3_T7.setObjectName(u"U3_T7")

        self.verticalLayout_70.addWidget(self.U3_T7)

        self.stackedUnidad_3.addWidget(self.sk_U3_T7)
        self.sk_U3_T8 = QWidget()
        self.sk_U3_T8.setObjectName(u"sk_U3_T8")
        self.verticalLayout_71 = QVBoxLayout(self.sk_U3_T8)
        self.verticalLayout_71.setSpacing(5)
        self.verticalLayout_71.setObjectName(u"verticalLayout_71")
        self.verticalLayout_71.setContentsMargins(0, 0, 0, 0)
        self.frame_69 = QFrame(self.sk_U3_T8)
        self.frame_69.setObjectName(u"frame_69")
        self.frame_69.setMinimumSize(QSize(0, 35))
        self.frame_69.setMaximumSize(QSize(16777215, 40))
        self.frame_69.setFrameShape(QFrame.StyledPanel)
        self.frame_69.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.frame_69)
        self.horizontalLayout_34.setSpacing(0)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.bt_return_30 = QPushButton(self.frame_69)
        self.bt_return_30.setObjectName(u"bt_return_30")
        self.bt_return_30.setMinimumSize(QSize(35, 35))
        self.bt_return_30.setMaximumSize(QSize(35, 35))
        self.bt_return_30.setIcon(icon8)
        self.bt_return_30.setIconSize(QSize(35, 35))

        self.horizontalLayout_34.addWidget(self.bt_return_30)

        self.horizontalSpacer_63 = QSpacerItem(131, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_34.addItem(self.horizontalSpacer_63)

        self.label_33 = QLabel(self.frame_69)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_34.addWidget(self.label_33)

        self.horizontalSpacer_64 = QSpacerItem(131, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_34.addItem(self.horizontalSpacer_64)


        self.verticalLayout_71.addWidget(self.frame_69)

        self.U3_T8 = ContenidosTemas(self.sk_U3_T8)
        self.U3_T8.setObjectName(u"U3_T8")

        self.verticalLayout_71.addWidget(self.U3_T8)

        self.stackedUnidad_3.addWidget(self.sk_U3_T8)
        self.sk_U3_T9 = QWidget()
        self.sk_U3_T9.setObjectName(u"sk_U3_T9")
        self.verticalLayout_72 = QVBoxLayout(self.sk_U3_T9)
        self.verticalLayout_72.setSpacing(5)
        self.verticalLayout_72.setObjectName(u"verticalLayout_72")
        self.verticalLayout_72.setContentsMargins(0, 0, 0, 0)
        self.frame_70 = QFrame(self.sk_U3_T9)
        self.frame_70.setObjectName(u"frame_70")
        self.frame_70.setMinimumSize(QSize(0, 35))
        self.frame_70.setMaximumSize(QSize(16777215, 40))
        self.frame_70.setFrameShape(QFrame.StyledPanel)
        self.frame_70.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.frame_70)
        self.horizontalLayout_35.setSpacing(0)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.bt_return_31 = QPushButton(self.frame_70)
        self.bt_return_31.setObjectName(u"bt_return_31")
        self.bt_return_31.setMinimumSize(QSize(35, 35))
        self.bt_return_31.setMaximumSize(QSize(35, 35))
        self.bt_return_31.setIcon(icon8)
        self.bt_return_31.setIconSize(QSize(35, 35))

        self.horizontalLayout_35.addWidget(self.bt_return_31)

        self.horizontalSpacer_65 = QSpacerItem(131, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_35.addItem(self.horizontalSpacer_65)

        self.label_34 = QLabel(self.frame_70)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_35.addWidget(self.label_34)

        self.horizontalSpacer_66 = QSpacerItem(131, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_35.addItem(self.horizontalSpacer_66)


        self.verticalLayout_72.addWidget(self.frame_70)

        self.U3_T9 = ContenidosTemas(self.sk_U3_T9)
        self.U3_T9.setObjectName(u"U3_T9")

        self.verticalLayout_72.addWidget(self.U3_T9)

        self.stackedUnidad_3.addWidget(self.sk_U3_T9)

        self.verticalLayout_43.addWidget(self.stackedUnidad_3)

        self.stackedWidget.addWidget(self.unidad_3)
        self.unidad_4 = QWidget()
        self.unidad_4.setObjectName(u"unidad_4")
        self.unidad_4.setStyleSheet(u"QLabel{\n"
"background-color: None;\n"
"color: white;\n"
"font: 16pt \"Britannic Bold\";\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgba(0,0,0,0);\n"
"color: white;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255,255,255,50);\n"
"}\n"
"")
        self.verticalLayout_55 = QVBoxLayout(self.unidad_4)
        self.verticalLayout_55.setSpacing(0)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.verticalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.stackedUnidad_4 = QStackedWidget(self.unidad_4)
        self.stackedUnidad_4.setObjectName(u"stackedUnidad_4")
        self.stackedUnidad_4.setStyleSheet(u"")
        self.temas_4 = QWidget()
        self.temas_4.setObjectName(u"temas_4")
        self.temas_4.setStyleSheet(u"QFrame#frame_44,\n"
"QFrame#frame_43{\n"
"background-color:rgb(239, 184, 16);\n"
"}")
        self.verticalLayout_44 = QVBoxLayout(self.temas_4)
        self.verticalLayout_44.setSpacing(0)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.frame_43 = QFrame(self.temas_4)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setMinimumSize(QSize(0, 35))
        self.frame_43.setMaximumSize(QSize(16777215, 40))
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_43)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.bt_return_18 = QPushButton(self.frame_43)
        self.bt_return_18.setObjectName(u"bt_return_18")
        self.bt_return_18.setMinimumSize(QSize(35, 35))
        self.bt_return_18.setMaximumSize(QSize(35, 35))
        self.bt_return_18.setIcon(icon8)
        self.bt_return_18.setIconSize(QSize(35, 35))

        self.horizontalLayout_22.addWidget(self.bt_return_18)

        self.horizontalSpacer_39 = QSpacerItem(0, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_39)

        self.label_21 = QLabel(self.frame_43)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_22.addWidget(self.label_21)

        self.horizontalSpacer_40 = QSpacerItem(0, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_40)


        self.verticalLayout_44.addWidget(self.frame_43)

        self.frame_44 = QFrame(self.temas_4)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setStyleSheet(u"")
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_44)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_45 = QFrame(self.frame_44)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.verticalLayout_45 = QVBoxLayout(self.frame_45)
        self.verticalLayout_45.setSpacing(0)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.bt_U4_T1 = AnimatedButton(self.frame_45)
        self.bt_U4_T1.setObjectName(u"bt_U4_T1")
        sizePolicy1.setHeightForWidth(self.bt_U4_T1.sizePolicy().hasHeightForWidth())
        self.bt_U4_T1.setSizePolicy(sizePolicy1)

        self.verticalLayout_45.addWidget(self.bt_U4_T1)


        self.gridLayout_4.addWidget(self.frame_45, 0, 0, 1, 1)

        self.frame_46 = QFrame(self.frame_44)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.verticalLayout_46 = QVBoxLayout(self.frame_46)
        self.verticalLayout_46.setSpacing(0)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.bt_U4_T2 = AnimatedButton(self.frame_46)
        self.bt_U4_T2.setObjectName(u"bt_U4_T2")
        sizePolicy1.setHeightForWidth(self.bt_U4_T2.sizePolicy().hasHeightForWidth())
        self.bt_U4_T2.setSizePolicy(sizePolicy1)

        self.verticalLayout_46.addWidget(self.bt_U4_T2)


        self.gridLayout_4.addWidget(self.frame_46, 0, 1, 1, 1)

        self.frame_47 = QFrame(self.frame_44)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.verticalLayout_47 = QVBoxLayout(self.frame_47)
        self.verticalLayout_47.setSpacing(0)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.bt_U4_T3 = AnimatedButton(self.frame_47)
        self.bt_U4_T3.setObjectName(u"bt_U4_T3")
        sizePolicy1.setHeightForWidth(self.bt_U4_T3.sizePolicy().hasHeightForWidth())
        self.bt_U4_T3.setSizePolicy(sizePolicy1)

        self.verticalLayout_47.addWidget(self.bt_U4_T3)


        self.gridLayout_4.addWidget(self.frame_47, 0, 2, 1, 1)

        self.frame_48 = QFrame(self.frame_44)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.verticalLayout_48 = QVBoxLayout(self.frame_48)
        self.verticalLayout_48.setSpacing(0)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.verticalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.bt_U4_T4 = AnimatedButton(self.frame_48)
        self.bt_U4_T4.setObjectName(u"bt_U4_T4")
        sizePolicy1.setHeightForWidth(self.bt_U4_T4.sizePolicy().hasHeightForWidth())
        self.bt_U4_T4.setSizePolicy(sizePolicy1)

        self.verticalLayout_48.addWidget(self.bt_U4_T4)


        self.gridLayout_4.addWidget(self.frame_48, 1, 0, 1, 1)

        self.frame_49 = QFrame(self.frame_44)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setFrameShape(QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.verticalLayout_49 = QVBoxLayout(self.frame_49)
        self.verticalLayout_49.setSpacing(0)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.verticalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.bt_U4_T5 = AnimatedButton(self.frame_49)
        self.bt_U4_T5.setObjectName(u"bt_U4_T5")
        sizePolicy1.setHeightForWidth(self.bt_U4_T5.sizePolicy().hasHeightForWidth())
        self.bt_U4_T5.setSizePolicy(sizePolicy1)

        self.verticalLayout_49.addWidget(self.bt_U4_T5)


        self.gridLayout_4.addWidget(self.frame_49, 1, 1, 1, 1)

        self.frame_71 = QFrame(self.frame_44)
        self.frame_71.setObjectName(u"frame_71")
        self.frame_71.setFrameShape(QFrame.StyledPanel)
        self.frame_71.setFrameShadow(QFrame.Raised)
        self.verticalLayout_73 = QVBoxLayout(self.frame_71)
        self.verticalLayout_73.setSpacing(0)
        self.verticalLayout_73.setObjectName(u"verticalLayout_73")
        self.verticalLayout_73.setContentsMargins(0, 0, 0, 0)
        self.bt_U4_T6 = AnimatedButton(self.frame_71)
        self.bt_U4_T6.setObjectName(u"bt_U4_T6")
        sizePolicy1.setHeightForWidth(self.bt_U4_T6.sizePolicy().hasHeightForWidth())
        self.bt_U4_T6.setSizePolicy(sizePolicy1)

        self.verticalLayout_73.addWidget(self.bt_U4_T6)


        self.gridLayout_4.addWidget(self.frame_71, 1, 2, 1, 1)

        self.frame_72 = QFrame(self.frame_44)
        self.frame_72.setObjectName(u"frame_72")
        self.frame_72.setFrameShape(QFrame.StyledPanel)
        self.frame_72.setFrameShadow(QFrame.Raised)
        self.verticalLayout_74 = QVBoxLayout(self.frame_72)
        self.verticalLayout_74.setSpacing(0)
        self.verticalLayout_74.setObjectName(u"verticalLayout_74")
        self.verticalLayout_74.setContentsMargins(0, 0, 0, 0)
        self.bt_U4_T7 = AnimatedButton(self.frame_72)
        self.bt_U4_T7.setObjectName(u"bt_U4_T7")
        sizePolicy1.setHeightForWidth(self.bt_U4_T7.sizePolicy().hasHeightForWidth())
        self.bt_U4_T7.setSizePolicy(sizePolicy1)

        self.verticalLayout_74.addWidget(self.bt_U4_T7)


        self.gridLayout_4.addWidget(self.frame_72, 2, 0, 1, 1)

        self.frame_73 = QFrame(self.frame_44)
        self.frame_73.setObjectName(u"frame_73")
        self.frame_73.setFrameShape(QFrame.StyledPanel)
        self.frame_73.setFrameShadow(QFrame.Raised)
        self.verticalLayout_75 = QVBoxLayout(self.frame_73)
        self.verticalLayout_75.setSpacing(0)
        self.verticalLayout_75.setObjectName(u"verticalLayout_75")
        self.verticalLayout_75.setContentsMargins(0, 0, 0, 0)
        self.bt_U4_T8 = AnimatedButton(self.frame_73)
        self.bt_U4_T8.setObjectName(u"bt_U4_T8")
        sizePolicy1.setHeightForWidth(self.bt_U4_T8.sizePolicy().hasHeightForWidth())
        self.bt_U4_T8.setSizePolicy(sizePolicy1)

        self.verticalLayout_75.addWidget(self.bt_U4_T8)


        self.gridLayout_4.addWidget(self.frame_73, 2, 1, 1, 1)


        self.verticalLayout_44.addWidget(self.frame_44)

        self.stackedUnidad_4.addWidget(self.temas_4)
        self.sk_U4_T1 = QWidget()
        self.sk_U4_T1.setObjectName(u"sk_U4_T1")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.sk_U4_T1.sizePolicy().hasHeightForWidth())
        self.sk_U4_T1.setSizePolicy(sizePolicy3)
        self.sk_U4_T1.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_50 = QVBoxLayout(self.sk_U4_T1)
        self.verticalLayout_50.setSpacing(5)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.verticalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.frame_50 = QFrame(self.sk_U4_T1)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setMinimumSize(QSize(0, 35))
        self.frame_50.setMaximumSize(QSize(16777215, 40))
        self.frame_50.setFrameShape(QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_50)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.bt_return_19 = QPushButton(self.frame_50)
        self.bt_return_19.setObjectName(u"bt_return_19")
        self.bt_return_19.setMinimumSize(QSize(35, 35))
        self.bt_return_19.setMaximumSize(QSize(35, 35))
        self.bt_return_19.setIcon(icon8)
        self.bt_return_19.setIconSize(QSize(35, 35))

        self.horizontalLayout_23.addWidget(self.bt_return_19)

        self.horizontalSpacer_41 = QSpacerItem(131, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_41)

        self.label_22 = QLabel(self.frame_50)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_23.addWidget(self.label_22)

        self.horizontalSpacer_42 = QSpacerItem(131, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_42)


        self.verticalLayout_50.addWidget(self.frame_50)

        self.U4_T1 = ContenidosTemas(self.sk_U4_T1)
        self.U4_T1.setObjectName(u"U4_T1")

        self.verticalLayout_50.addWidget(self.U4_T1)

        self.stackedUnidad_4.addWidget(self.sk_U4_T1)
        self.sk_U4_T2 = QWidget()
        self.sk_U4_T2.setObjectName(u"sk_U4_T2")
        self.verticalLayout_51 = QVBoxLayout(self.sk_U4_T2)
        self.verticalLayout_51.setSpacing(5)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.verticalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.frame_51 = QFrame(self.sk_U4_T2)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setMinimumSize(QSize(0, 35))
        self.frame_51.setMaximumSize(QSize(16777215, 40))
        self.frame_51.setFrameShape(QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_51)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.bt_return_20 = QPushButton(self.frame_51)
        self.bt_return_20.setObjectName(u"bt_return_20")
        self.bt_return_20.setMinimumSize(QSize(35, 35))
        self.bt_return_20.setMaximumSize(QSize(35, 35))
        self.bt_return_20.setIcon(icon8)
        self.bt_return_20.setIconSize(QSize(35, 35))

        self.horizontalLayout_24.addWidget(self.bt_return_20)

        self.horizontalSpacer_43 = QSpacerItem(131, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_43)

        self.label_23 = QLabel(self.frame_51)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_24.addWidget(self.label_23)

        self.horizontalSpacer_44 = QSpacerItem(131, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_44)


        self.verticalLayout_51.addWidget(self.frame_51)

        self.U4_T2 = ContenidosTemas(self.sk_U4_T2)
        self.U4_T2.setObjectName(u"U4_T2")

        self.verticalLayout_51.addWidget(self.U4_T2)

        self.stackedUnidad_4.addWidget(self.sk_U4_T2)
        self.sk_U4_T3 = QWidget()
        self.sk_U4_T3.setObjectName(u"sk_U4_T3")
        self.verticalLayout_52 = QVBoxLayout(self.sk_U4_T3)
        self.verticalLayout_52.setSpacing(5)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.verticalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.frame_52 = QFrame(self.sk_U4_T3)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setMinimumSize(QSize(0, 35))
        self.frame_52.setMaximumSize(QSize(16777215, 40))
        self.frame_52.setFrameShape(QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_52)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.bt_return_21 = QPushButton(self.frame_52)
        self.bt_return_21.setObjectName(u"bt_return_21")
        self.bt_return_21.setMinimumSize(QSize(35, 35))
        self.bt_return_21.setMaximumSize(QSize(35, 35))
        self.bt_return_21.setIcon(icon8)
        self.bt_return_21.setIconSize(QSize(35, 35))

        self.horizontalLayout_25.addWidget(self.bt_return_21)

        self.horizontalSpacer_45 = QSpacerItem(131, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_45)

        self.label_24 = QLabel(self.frame_52)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_25.addWidget(self.label_24)

        self.horizontalSpacer_46 = QSpacerItem(131, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_46)


        self.verticalLayout_52.addWidget(self.frame_52)

        self.U4_T3 = ContenidosTemas(self.sk_U4_T3)
        self.U4_T3.setObjectName(u"U4_T3")

        self.verticalLayout_52.addWidget(self.U4_T3)

        self.stackedUnidad_4.addWidget(self.sk_U4_T3)
        self.sk_U4_T4 = QWidget()
        self.sk_U4_T4.setObjectName(u"sk_U4_T4")
        self.sk_U4_T4.setStyleSheet(u"")
        self.verticalLayout_53 = QVBoxLayout(self.sk_U4_T4)
        self.verticalLayout_53.setSpacing(5)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.verticalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.frame_53 = QFrame(self.sk_U4_T4)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setMinimumSize(QSize(0, 35))
        self.frame_53.setMaximumSize(QSize(16777215, 40))
        self.frame_53.setFrameShape(QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_53)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.bt_return_22 = QPushButton(self.frame_53)
        self.bt_return_22.setObjectName(u"bt_return_22")
        self.bt_return_22.setMinimumSize(QSize(35, 35))
        self.bt_return_22.setMaximumSize(QSize(35, 35))
        self.bt_return_22.setIcon(icon8)
        self.bt_return_22.setIconSize(QSize(35, 35))

        self.horizontalLayout_26.addWidget(self.bt_return_22)

        self.horizontalSpacer_47 = QSpacerItem(131, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_47)

        self.label_25 = QLabel(self.frame_53)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_26.addWidget(self.label_25)

        self.horizontalSpacer_48 = QSpacerItem(131, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_48)


        self.verticalLayout_53.addWidget(self.frame_53)

        self.U4_T4 = ContenidosTemas(self.sk_U4_T4)
        self.U4_T4.setObjectName(u"U4_T4")

        self.verticalLayout_53.addWidget(self.U4_T4)

        self.stackedUnidad_4.addWidget(self.sk_U4_T4)
        self.sk_U4_T5 = QWidget()
        self.sk_U4_T5.setObjectName(u"sk_U4_T5")
        self.verticalLayout_54 = QVBoxLayout(self.sk_U4_T5)
        self.verticalLayout_54.setSpacing(5)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.verticalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.frame_54 = QFrame(self.sk_U4_T5)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setMinimumSize(QSize(0, 35))
        self.frame_54.setMaximumSize(QSize(16777215, 40))
        self.frame_54.setFrameShape(QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_54)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.bt_return_23 = QPushButton(self.frame_54)
        self.bt_return_23.setObjectName(u"bt_return_23")
        self.bt_return_23.setMinimumSize(QSize(35, 35))
        self.bt_return_23.setMaximumSize(QSize(35, 35))
        self.bt_return_23.setIcon(icon8)
        self.bt_return_23.setIconSize(QSize(35, 35))

        self.horizontalLayout_27.addWidget(self.bt_return_23)

        self.horizontalSpacer_49 = QSpacerItem(131, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_49)

        self.label_26 = QLabel(self.frame_54)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_27.addWidget(self.label_26)

        self.horizontalSpacer_50 = QSpacerItem(131, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_50)


        self.verticalLayout_54.addWidget(self.frame_54)

        self.U4_T5 = ContenidosTemas(self.sk_U4_T5)
        self.U4_T5.setObjectName(u"U4_T5")

        self.verticalLayout_54.addWidget(self.U4_T5)

        self.stackedUnidad_4.addWidget(self.sk_U4_T5)
        self.sk_U4_T6 = QWidget()
        self.sk_U4_T6.setObjectName(u"sk_U4_T6")
        self.verticalLayout_77 = QVBoxLayout(self.sk_U4_T6)
        self.verticalLayout_77.setSpacing(5)
        self.verticalLayout_77.setObjectName(u"verticalLayout_77")
        self.verticalLayout_77.setContentsMargins(0, 0, 0, 0)
        self.frame_75 = QFrame(self.sk_U4_T6)
        self.frame_75.setObjectName(u"frame_75")
        self.frame_75.setMinimumSize(QSize(0, 35))
        self.frame_75.setMaximumSize(QSize(16777215, 40))
        self.frame_75.setFrameShape(QFrame.StyledPanel)
        self.frame_75.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.frame_75)
        self.horizontalLayout_36.setSpacing(0)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.bt_return_32 = QPushButton(self.frame_75)
        self.bt_return_32.setObjectName(u"bt_return_32")
        self.bt_return_32.setMinimumSize(QSize(35, 35))
        self.bt_return_32.setMaximumSize(QSize(35, 35))
        self.bt_return_32.setIcon(icon8)
        self.bt_return_32.setIconSize(QSize(35, 35))

        self.horizontalLayout_36.addWidget(self.bt_return_32)

        self.horizontalSpacer_67 = QSpacerItem(131, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_36.addItem(self.horizontalSpacer_67)

        self.label_35 = QLabel(self.frame_75)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_36.addWidget(self.label_35)

        self.horizontalSpacer_68 = QSpacerItem(131, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_36.addItem(self.horizontalSpacer_68)


        self.verticalLayout_77.addWidget(self.frame_75)

        self.U4_T6 = ContenidosTemas(self.sk_U4_T6)
        self.U4_T6.setObjectName(u"U4_T6")

        self.verticalLayout_77.addWidget(self.U4_T6)

        self.stackedUnidad_4.addWidget(self.sk_U4_T6)
        self.sk_U4_T7 = QWidget()
        self.sk_U4_T7.setObjectName(u"sk_U4_T7")
        self.verticalLayout_78 = QVBoxLayout(self.sk_U4_T7)
        self.verticalLayout_78.setSpacing(5)
        self.verticalLayout_78.setObjectName(u"verticalLayout_78")
        self.verticalLayout_78.setContentsMargins(0, 0, 0, 0)
        self.frame_76 = QFrame(self.sk_U4_T7)
        self.frame_76.setObjectName(u"frame_76")
        self.frame_76.setMinimumSize(QSize(0, 35))
        self.frame_76.setMaximumSize(QSize(16777215, 40))
        self.frame_76.setFrameShape(QFrame.StyledPanel)
        self.frame_76.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.frame_76)
        self.horizontalLayout_37.setSpacing(0)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.bt_return_33 = QPushButton(self.frame_76)
        self.bt_return_33.setObjectName(u"bt_return_33")
        self.bt_return_33.setMinimumSize(QSize(35, 35))
        self.bt_return_33.setMaximumSize(QSize(35, 35))
        self.bt_return_33.setIcon(icon8)
        self.bt_return_33.setIconSize(QSize(35, 35))

        self.horizontalLayout_37.addWidget(self.bt_return_33)

        self.horizontalSpacer_69 = QSpacerItem(131, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_37.addItem(self.horizontalSpacer_69)

        self.label_36 = QLabel(self.frame_76)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_37.addWidget(self.label_36)

        self.horizontalSpacer_70 = QSpacerItem(131, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_37.addItem(self.horizontalSpacer_70)


        self.verticalLayout_78.addWidget(self.frame_76)

        self.U4_T7 = ContenidosTemas(self.sk_U4_T7)
        self.U4_T7.setObjectName(u"U4_T7")

        self.verticalLayout_78.addWidget(self.U4_T7)

        self.stackedUnidad_4.addWidget(self.sk_U4_T7)
        self.sk_U4_T8 = QWidget()
        self.sk_U4_T8.setObjectName(u"sk_U4_T8")
        self.verticalLayout_79 = QVBoxLayout(self.sk_U4_T8)
        self.verticalLayout_79.setSpacing(5)
        self.verticalLayout_79.setObjectName(u"verticalLayout_79")
        self.verticalLayout_79.setContentsMargins(0, 0, 0, 0)
        self.frame_77 = QFrame(self.sk_U4_T8)
        self.frame_77.setObjectName(u"frame_77")
        self.frame_77.setMinimumSize(QSize(0, 35))
        self.frame_77.setMaximumSize(QSize(16777215, 40))
        self.frame_77.setFrameShape(QFrame.StyledPanel)
        self.frame_77.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.frame_77)
        self.horizontalLayout_38.setSpacing(0)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.bt_return_34 = QPushButton(self.frame_77)
        self.bt_return_34.setObjectName(u"bt_return_34")
        self.bt_return_34.setMinimumSize(QSize(35, 35))
        self.bt_return_34.setMaximumSize(QSize(35, 35))
        self.bt_return_34.setIcon(icon8)
        self.bt_return_34.setIconSize(QSize(35, 35))

        self.horizontalLayout_38.addWidget(self.bt_return_34)

        self.horizontalSpacer_71 = QSpacerItem(131, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_38.addItem(self.horizontalSpacer_71)

        self.label_37 = QLabel(self.frame_77)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_38.addWidget(self.label_37)

        self.horizontalSpacer_72 = QSpacerItem(131, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_38.addItem(self.horizontalSpacer_72)


        self.verticalLayout_79.addWidget(self.frame_77)

        self.U4_T8 = ContenidosTemas(self.sk_U4_T8)
        self.U4_T8.setObjectName(u"U4_T8")

        self.verticalLayout_79.addWidget(self.U4_T8)

        self.stackedUnidad_4.addWidget(self.sk_U4_T8)

        self.verticalLayout_55.addWidget(self.stackedUnidad_4)

        self.stackedWidget.addWidget(self.unidad_4)

        self.horizontalLayout_2.addWidget(self.stackedWidget)


        self.verticalLayout_2.addWidget(self.frame_inferior)


        self.verticalLayout.addWidget(self.frameBackground)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"RoboPro", None))
        self.label_38.setText("")
#if QT_CONFIG(tooltip)
        self.bt_contraer.setToolTip(QCoreApplication.translate("MainWindow", u"Ocultar panel de usuario", None))
#endif // QT_CONFIG(tooltip)
        self.bt_contraer.setText("")
#if QT_CONFIG(tooltip)
        self.bt_expandir.setToolTip(QCoreApplication.translate("MainWindow", u"Mostrar panel de usuario", None))
#endif // QT_CONFIG(tooltip)
        self.bt_expandir.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"RoboPro", None))
        self.bt_minimize.setText("")
        self.bt_normal.setText("")
        self.bt_maximize.setText("")
        self.bt_close.setText("")
#if QT_CONFIG(tooltip)
        self.bt_perfil.setToolTip(QCoreApplication.translate("MainWindow", u"Editar perfil", None))
#endif // QT_CONFIG(tooltip)
        self.bt_perfil.setText("")
        self.lb_userID.setText(QCoreApplication.translate("MainWindow", u"UID: ", None))
        self.lb_bienvenido.setText(QCoreApplication.translate("MainWindow", u"Bienvenid@", None))
        self.lb_userName.setText("")
        self.bt_cerrarSesion.setText(QCoreApplication.translate("MainWindow", u" Cerrar Sesi\u00f3n ", None))
        self.bt_acercaDe.setText(QCoreApplication.translate("MainWindow", u" Acerca de RoboPro ", None))
        self.bt_unidad_1.setText("")
        self.bt_unidad_2.setText("")
        self.bt_unidad_3.setText("")
        self.bt_unidad_4.setText("")
        self.bt_return.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"HERRAMIENTAS COMPUTACIONALES PARA LA SIMULACI\u00d3N DE ROBOTS", None))
        self.bt_U1_T1.setText("")
        self.bt_U1_T2.setText("")
        self.bt_U1_T3.setText("")
        self.bt_U1_T4.setText("")
        self.bt_U1_T5.setText("")
        self.bt_return_1.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Implementaci\u00f3n computacional del m\u00e9todo recursivo de Lagrange- Euler", None))
        self.bt_return_2.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Representaci\u00f3n tridimensional de objetos", None))
        self.bt_return_3.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Representaci\u00f3n tridimensional de robots", None))
        self.bt_return_4.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Animaci\u00f3n de objetos en movimiento", None))
        self.bt_return_5.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Animaci\u00f3n de robots de acuerdo a los modelos cinem\u00e1ticos y din\u00e1micos", None))
        self.bt_return_6.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"CONTROL CINEM\u00c1TICO DE ROBOTS", None))
        self.bt_U2_T1.setText("")
        self.bt_U2_T2.setText("")
        self.bt_U2_T3.setText("")
        self.bt_U2_T4.setText("")
        self.bt_U2_T5.setText("")
        self.bt_U2_T6.setText("")
        self.bt_U2_T7.setText("")
        self.bt_U2_T8.setText("")
        self.bt_U2_T9.setText("")
        self.bt_return_7.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Generalidades del control cinem\u00e1tico", None))
        self.bt_return_8.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Trayectorias punto a punto", None))
        self.bt_return_9.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Trayectorias continuas", None))
        self.bt_return_10.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Evoluci\u00f3n de la orientaci\u00f3n", None))
        self.bt_return_11.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Generaci\u00f3n de trayectorias cartesianas", None))
        self.bt_return_24.setText("")
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Interpolador lineal", None))
        self.bt_return_25.setText("")
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Interpolador cubico", None))
        self.bt_return_26.setText("")
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Interpolador trapezoidal", None))
        self.bt_return_27.setText("")
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Implementaci\u00f3n de interpoladores", None))
        self.bt_return_12.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"CONTROL DIN\u00c1MICO", None))
        self.bt_U3_T1.setText("")
        self.bt_U3_T2.setText("")
        self.bt_U3_T3.setText("")
        self.bt_U3_T4.setText("")
        self.bt_U3_T5.setText("")
        self.bt_U3_T6.setText("")
        self.bt_U3_T7.setText("")
        self.bt_U3_T8.setText("")
        self.bt_U3_T9.setText("")
        self.bt_return_13.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Influencia del factor de reducci\u00f3n en el control monoarticular", None))
        self.bt_return_14.setText("")
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Esquema general de control monoarticular", None))
        self.bt_return_15.setText("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Control prealimentado por inversi\u00f3n de modelo", None))
        self.bt_return_16.setText("")
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Control realimentado", None))
        self.bt_return_17.setText("")
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Control prealimentado y realimentado", None))
        self.bt_return_28.setText("")
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Control con compensaci\u00f3n de gravedad", None))
        self.bt_return_29.setText("")
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Control multiarticular por desacoplamiento por inversi\u00f3n de modelo", None))
        self.bt_return_30.setText("")
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Control multiarticular PID con prealimentaci\u00f3n", None))
        self.bt_return_31.setText("")
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Esquemas avanzados de control de robots", None))
        self.bt_return_18.setText("")
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"VISI\u00d3N ARTIFICIAL APLICADA A ROB\u00d3TICA", None))
        self.bt_U4_T1.setText("")
        self.bt_U4_T2.setText("")
        self.bt_U4_T3.setText("")
        self.bt_U4_T4.setText("")
        self.bt_U4_T5.setText("")
        self.bt_U4_T6.setText("")
        self.bt_U4_T7.setText("")
        self.bt_U4_T8.setText("")
        self.bt_return_19.setText("")
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Fundamentos de visi\u00f3n artificial", None))
        self.bt_return_20.setText("")
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Espacios de colores", None))
        self.bt_return_21.setText("")
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Operadores l\u00f3gicos", None))
        self.bt_return_22.setText("")
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Elementos estructurantes", None))
        self.bt_return_23.setText("")
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Filtros", None))
        self.bt_return_32.setText("")
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Operaciones morfol\u00f3gicas", None))
        self.bt_return_33.setText("")
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Extracci\u00f3n de caracter\u00edsticas de una imagen", None))
        self.bt_return_34.setText("")
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Aplicaciones en rob\u00f3tica", None))
    # retranslateUi

