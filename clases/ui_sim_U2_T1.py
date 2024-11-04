# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sim_U2_T1AAVrau.ui'
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
    QLabel, QLayout, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QSpinBox, QVBoxLayout,
    QWidget)

from clases.CustomTable import CustomTable
from clases.GLView import GLView
from clases.MTHList import MTHList
from clases.PlotWidget import CustomPlotWidget

class Ui_sim_U2_T1(object):
    def setupUi(self, sim_U2_T1):
        if not sim_U2_T1.objectName():
            sim_U2_T1.setObjectName(u"sim_U2_T1")
        sim_U2_T1.resize(725, 653)
        sim_U2_T1.setStyleSheet(u"QWidget#sim_U2_T1{\n"
"background-color:rgba(0,0,0,0);\n"
"}")
        self.verticalLayout = QVBoxLayout(sim_U2_T1)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(sim_U2_T1)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 793, 1586))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setStyleSheet(u"QWidget#scrollAreaWidgetContents{\n"
"background-color:rgb(0,0,0);\n"
"}\n"
"QScrollArea#scrollArea_5 QWidget#scrollAreaWidgetContents_5,\n"
"QScrollArea#scrollArea_6 QWidget#scrollAreaWidgetContents_6{\n"
"background-color:translucid;\n"
"}\n"
"QLabel{\n"
"color:white;\n"
"}\n"
"QSpinBox{\n"
"color:white;\n"
"background-color:translucid;\n"
"}\n"
"QPushButton{\n"
"font:16pt \"Britannic Bold\";\n"
"color:white;\n"
"background-color:rgba(0,51,102,200);\n"
"}\n"
"QPushButton#bt_transformarInversa{\n"
"font:24pt \"Britannic Bold\";\n"
"}\n"
"QPushButton#bt_transformarDirecta{\n"
"font:24pt \"Britannic Bold\";\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(0,51,150,200);\n"
"}\n"
"QTableWidget {\n"
"selection-background-color: black;\n"
"}\n"
"QHeaderView::section {\n"
"background-color: #CCCCCC;\n"
"padding: 4px;\n"
"border: 1px solid #000000;\n"
"font-size: 10pt;\n"
"}\n"
"QTableWidget::item {\n"
"background-color: black;\n"
"color: white;\n"
"border: 1px solid rgb(80, 80, 80); \n"
"}\n"
"QTableWidget::i"
                        "tem:selected {\n"
"background-color: rgb(0,51,112);\n"
"}\n"
"QTableWidget QWidget{\n"
"background-color: rgb(173,51,51);\n"
"}\n"
"QFrame#frame{\n"
"background-color:rgba(173,51,51,100);\n"
"}\n"
"QFrame#frame_2{\n"
"background-color:rgba(239, 184, 16,100);\n"
"}\n"
"QFrame#frame_3{\n"
"background-color:rgba(218,218,218,100)\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"QLabel{\n"
"font:24pt \"Britannic Bold\";\n"
"}")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)

        self.frame = QFrame(self.scrollAreaWidgetContents)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.sb_nPuntosR3_1 = QSpinBox(self.frame)
        self.sb_nPuntosR3_1.setObjectName(u"sb_nPuntosR3_1")
        self.sb_nPuntosR3_1.setMinimum(2)
        self.sb_nPuntosR3_1.setValue(4)

        self.horizontalLayout.addWidget(self.sb_nPuntosR3_1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.scrollArea_5 = QScrollArea(self.frame)
        self.scrollArea_5.setObjectName(u"scrollArea_5")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scrollArea_5.sizePolicy().hasHeightForWidth())
        self.scrollArea_5.setSizePolicy(sizePolicy1)
        self.scrollArea_5.setMinimumSize(QSize(0, 232))
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 789, 230))
        self.horizontalLayout_2 = QHBoxLayout(self.scrollAreaWidgetContents_5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(361, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.ct_puntosR3 = CustomTable(self.scrollAreaWidgetContents_5)
        self.ct_puntosR3.setObjectName(u"ct_puntosR3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.ct_puntosR3.sizePolicy().hasHeightForWidth())
        self.ct_puntosR3.setSizePolicy(sizePolicy2)
        self.ct_puntosR3.setMinimumSize(QSize(50, 50))
        self.ct_puntosR3.setStyleSheet(u"")

        self.verticalLayout_9.addWidget(self.ct_puntosR3)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_2)


        self.horizontalLayout_2.addLayout(self.verticalLayout_9)

        self.horizontalSpacer_4 = QSpacerItem(360, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_5)

        self.verticalLayout_2.addWidget(self.scrollArea_5)

        self.bt_generarMTHs = QPushButton(self.frame)
        self.bt_generarMTHs.setObjectName(u"bt_generarMTHs")

        self.verticalLayout_2.addWidget(self.bt_generarMTHs)

        self.mthList_1 = MTHList(self.frame)
        self.mthList_1.setObjectName(u"mthList_1")
        self.mthList_1.setMinimumSize(QSize(0, 50))

        self.verticalLayout_2.addWidget(self.mthList_1)

        self.glView_1 = GLView(self.frame)
        self.glView_1.setObjectName(u"glView_1")
        self.glView_1.setMinimumSize(QSize(0, 50))

        self.verticalLayout_2.addWidget(self.glView_1)

        self.bt_interpolarR3 = QPushButton(self.frame)
        self.bt_interpolarR3.setObjectName(u"bt_interpolarR3")
        self.bt_interpolarR3.setEnabled(False)

        self.verticalLayout_2.addWidget(self.bt_interpolarR3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)

        self.bt_basadoTiempo = QPushButton(self.frame)
        self.bt_basadoTiempo.setObjectName(u"bt_basadoTiempo")

        self.horizontalLayout_5.addWidget(self.bt_basadoTiempo)

        self.bt_basadoPuntos = QPushButton(self.frame)
        self.bt_basadoPuntos.setObjectName(u"bt_basadoPuntos")
        self.bt_basadoPuntos.setEnabled(False)

        self.horizontalLayout_5.addWidget(self.bt_basadoPuntos)

        self.fr_nPuntos = QFrame(self.frame)
        self.fr_nPuntos.setObjectName(u"fr_nPuntos")
        self.fr_nPuntos.setFrameShape(QFrame.StyledPanel)
        self.fr_nPuntos.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.fr_nPuntos)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.fr_nPuntos)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.sb_nPuntosR3_2 = QSpinBox(self.fr_nPuntos)
        self.sb_nPuntosR3_2.setObjectName(u"sb_nPuntosR3_2")
        self.sb_nPuntosR3_2.setEnabled(False)
        self.sb_nPuntosR3_2.setMinimum(4)
        self.sb_nPuntosR3_2.setMaximum(999)
        self.sb_nPuntosR3_2.setValue(19)

        self.horizontalLayout_3.addWidget(self.sb_nPuntosR3_2)


        self.horizontalLayout_5.addWidget(self.fr_nPuntos)

        self.fr_deltaT = QFrame(self.frame)
        self.fr_deltaT.setObjectName(u"fr_deltaT")
        self.fr_deltaT.setFrameShape(QFrame.StyledPanel)
        self.fr_deltaT.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.fr_deltaT)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.fr_deltaT)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.sb_dT_1 = QSpinBox(self.fr_deltaT)
        self.sb_dT_1.setObjectName(u"sb_dT_1")
        self.sb_dT_1.setMinimum(10)
        self.sb_dT_1.setMaximum(9999)
        self.sb_dT_1.setValue(400)

        self.horizontalLayout_4.addWidget(self.sb_dT_1)


        self.horizontalLayout_5.addWidget(self.fr_deltaT)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_6)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.scrollArea_6 = QScrollArea(self.frame)
        self.scrollArea_6.setObjectName(u"scrollArea_6")
        self.scrollArea_6.setMinimumSize(QSize(0, 232))
        self.scrollArea_6.setWidgetResizable(True)
        self.scrollAreaWidgetContents_6 = QWidget()
        self.scrollAreaWidgetContents_6.setObjectName(u"scrollAreaWidgetContents_6")
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, 0, 789, 230))
        self.horizontalLayout_6 = QHBoxLayout(self.scrollAreaWidgetContents_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_7 = QSpacerItem(361, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_7)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.ct_puntosR3_2 = CustomTable(self.scrollAreaWidgetContents_6)
        self.ct_puntosR3_2.setObjectName(u"ct_puntosR3_2")
        sizePolicy2.setHeightForWidth(self.ct_puntosR3_2.sizePolicy().hasHeightForWidth())
        self.ct_puntosR3_2.setSizePolicy(sizePolicy2)
        self.ct_puntosR3_2.setMinimumSize(QSize(50, 50))

        self.verticalLayout_8.addWidget(self.ct_puntosR3_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer)


        self.horizontalLayout_6.addLayout(self.verticalLayout_8)

        self.horizontalSpacer_8 = QSpacerItem(360, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_8)

        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_6)

        self.verticalLayout_2.addWidget(self.scrollArea_6)

        self.mthList_2 = MTHList(self.frame)
        self.mthList_2.setObjectName(u"mthList_2")
        self.mthList_2.setMinimumSize(QSize(0, 50))

        self.verticalLayout_2.addWidget(self.mthList_2)

        self.glView_2 = GLView(self.frame)
        self.glView_2.setObjectName(u"glView_2")
        self.glView_2.setMinimumSize(QSize(0, 50))

        self.verticalLayout_2.addWidget(self.glView_2)


        self.verticalLayout_3.addWidget(self.frame)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_9)

        self.bt_transformarInversa = QPushButton(self.scrollAreaWidgetContents)
        self.bt_transformarInversa.setObjectName(u"bt_transformarInversa")
        self.bt_transformarInversa.setEnabled(False)
        self.bt_transformarInversa.setMinimumSize(QSize(0, 50))
        font = QFont()
        font.setFamilies([u"Britannic Bold"])
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        self.bt_transformarInversa.setFont(font)
        icon = QIcon()
        icon.addFile(u"resources/images/down_arrow_icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_transformarInversa.setIcon(icon)
        self.bt_transformarInversa.setIconSize(QSize(100, 100))

        self.horizontalLayout_8.addWidget(self.bt_transformarInversa)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_10)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.frame_2 = QFrame(self.scrollAreaWidgetContents)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QSize(0, 0))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_2)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName(u"label_8")
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_8)

        self.plot_pos_q3 = CustomPlotWidget(self.frame_2)
        self.plot_pos_q3.setObjectName(u"plot_pos_q3")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.plot_pos_q3.sizePolicy().hasHeightForWidth())
        self.plot_pos_q3.setSizePolicy(sizePolicy3)
        self.plot_pos_q3.setMinimumSize(QSize(50, 50))

        self.verticalLayout_6.addWidget(self.plot_pos_q3)


        self.gridLayout.addLayout(self.verticalLayout_6, 0, 2, 1, 1)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_9 = QLabel(self.frame_2)
        self.label_9.setObjectName(u"label_9")
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_9)

        self.plot_pos_q4 = CustomPlotWidget(self.frame_2)
        self.plot_pos_q4.setObjectName(u"plot_pos_q4")
        sizePolicy3.setHeightForWidth(self.plot_pos_q4.sizePolicy().hasHeightForWidth())
        self.plot_pos_q4.setSizePolicy(sizePolicy3)
        self.plot_pos_q4.setMinimumSize(QSize(50, 50))

        self.verticalLayout_7.addWidget(self.plot_pos_q4)


        self.gridLayout.addLayout(self.verticalLayout_7, 0, 3, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_5)

        self.plot_pos_q1 = CustomPlotWidget(self.frame_2)
        self.plot_pos_q1.setObjectName(u"plot_pos_q1")
        sizePolicy3.setHeightForWidth(self.plot_pos_q1.sizePolicy().hasHeightForWidth())
        self.plot_pos_q1.setSizePolicy(sizePolicy3)
        self.plot_pos_q1.setMinimumSize(QSize(50, 50))

        self.verticalLayout_4.addWidget(self.plot_pos_q1)


        self.gridLayout.addLayout(self.verticalLayout_4, 0, 0, 1, 1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_7)

        self.plot_pos_q2 = CustomPlotWidget(self.frame_2)
        self.plot_pos_q2.setObjectName(u"plot_pos_q2")
        sizePolicy3.setHeightForWidth(self.plot_pos_q2.sizePolicy().hasHeightForWidth())
        self.plot_pos_q2.setSizePolicy(sizePolicy3)
        self.plot_pos_q2.setMinimumSize(QSize(50, 50))

        self.verticalLayout_5.addWidget(self.plot_pos_q2)


        self.gridLayout.addLayout(self.verticalLayout_5, 0, 1, 1, 1)

        self.gridLayout.setColumnStretch(0, 20)
        self.gridLayout.setColumnStretch(1, 19)
        self.gridLayout.setColumnStretch(2, 19)
        self.gridLayout.setColumnStretch(3, 19)

        self.verticalLayout_33.addLayout(self.gridLayout)

        self.bt_interpolarArt = QPushButton(self.frame_2)
        self.bt_interpolarArt.setObjectName(u"bt_interpolarArt")
        self.bt_interpolarArt.setEnabled(False)

        self.verticalLayout_33.addWidget(self.bt_interpolarArt)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_13)

        self.bt_basadoTiempo_2 = QPushButton(self.frame_2)
        self.bt_basadoTiempo_2.setObjectName(u"bt_basadoTiempo_2")

        self.horizontalLayout_10.addWidget(self.bt_basadoTiempo_2)

        self.bt_basadoPuntos_2 = QPushButton(self.frame_2)
        self.bt_basadoPuntos_2.setObjectName(u"bt_basadoPuntos_2")
        self.bt_basadoPuntos_2.setEnabled(False)

        self.horizontalLayout_10.addWidget(self.bt_basadoPuntos_2)

        self.fr_nPuntos_2 = QFrame(self.frame_2)
        self.fr_nPuntos_2.setObjectName(u"fr_nPuntos_2")
        self.fr_nPuntos_2.setFrameShape(QFrame.StyledPanel)
        self.fr_nPuntos_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.fr_nPuntos_2)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_28 = QLabel(self.fr_nPuntos_2)
        self.label_28.setObjectName(u"label_28")

        self.horizontalLayout_13.addWidget(self.label_28)

        self.sb_nPuntosArt = QSpinBox(self.fr_nPuntos_2)
        self.sb_nPuntosArt.setObjectName(u"sb_nPuntosArt")
        self.sb_nPuntosArt.setEnabled(False)
        self.sb_nPuntosArt.setMinimum(20)
        self.sb_nPuntosArt.setMaximum(999)
        self.sb_nPuntosArt.setValue(100)

        self.horizontalLayout_13.addWidget(self.sb_nPuntosArt)


        self.horizontalLayout_10.addWidget(self.fr_nPuntos_2)

        self.fr_deltaT_2 = QFrame(self.frame_2)
        self.fr_deltaT_2.setObjectName(u"fr_deltaT_2")
        self.fr_deltaT_2.setFrameShape(QFrame.StyledPanel)
        self.fr_deltaT_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.fr_deltaT_2)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_29 = QLabel(self.fr_deltaT_2)
        self.label_29.setObjectName(u"label_29")

        self.horizontalLayout_14.addWidget(self.label_29)

        self.sb_dT_2 = QSpinBox(self.fr_deltaT_2)
        self.sb_dT_2.setObjectName(u"sb_dT_2")
        self.sb_dT_2.setMinimum(10)
        self.sb_dT_2.setMaximum(9999)
        self.sb_dT_2.setValue(50)

        self.horizontalLayout_14.addWidget(self.sb_dT_2)


        self.horizontalLayout_10.addWidget(self.fr_deltaT_2)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_14)


        self.verticalLayout_33.addLayout(self.horizontalLayout_10)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.label_34 = QLabel(self.frame_2)
        self.label_34.setObjectName(u"label_34")
        sizePolicy.setHeightForWidth(self.label_34.sizePolicy().hasHeightForWidth())
        self.label_34.setSizePolicy(sizePolicy)
        self.label_34.setAlignment(Qt.AlignCenter)

        self.verticalLayout_26.addWidget(self.label_34)

        self.plot_pos_q3_2 = CustomPlotWidget(self.frame_2)
        self.plot_pos_q3_2.setObjectName(u"plot_pos_q3_2")
        self.plot_pos_q3_2.setMinimumSize(QSize(50, 50))

        self.verticalLayout_26.addWidget(self.plot_pos_q3_2)


        self.gridLayout_2.addLayout(self.verticalLayout_26, 0, 2, 1, 1)

        self.verticalLayout_31 = QVBoxLayout()
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.label_40 = QLabel(self.frame_2)
        self.label_40.setObjectName(u"label_40")
        sizePolicy.setHeightForWidth(self.label_40.sizePolicy().hasHeightForWidth())
        self.label_40.setSizePolicy(sizePolicy)
        self.label_40.setAlignment(Qt.AlignCenter)

        self.verticalLayout_31.addWidget(self.label_40)

        self.plot_vel_q3_2 = CustomPlotWidget(self.frame_2)
        self.plot_vel_q3_2.setObjectName(u"plot_vel_q3_2")
        self.plot_vel_q3_2.setMinimumSize(QSize(50, 50))

        self.verticalLayout_31.addWidget(self.plot_vel_q3_2)


        self.gridLayout_2.addLayout(self.verticalLayout_31, 1, 2, 1, 1)

        self.verticalLayout_32 = QVBoxLayout()
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.label_41 = QLabel(self.frame_2)
        self.label_41.setObjectName(u"label_41")
        sizePolicy.setHeightForWidth(self.label_41.sizePolicy().hasHeightForWidth())
        self.label_41.setSizePolicy(sizePolicy)
        self.label_41.setAlignment(Qt.AlignCenter)

        self.verticalLayout_32.addWidget(self.label_41)

        self.plot_vel_q4_2 = CustomPlotWidget(self.frame_2)
        self.plot_vel_q4_2.setObjectName(u"plot_vel_q4_2")
        self.plot_vel_q4_2.setMinimumSize(QSize(50, 50))

        self.verticalLayout_32.addWidget(self.plot_vel_q4_2)


        self.gridLayout_2.addLayout(self.verticalLayout_32, 1, 3, 1, 1)

        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_32 = QLabel(self.frame_2)
        self.label_32.setObjectName(u"label_32")
        sizePolicy.setHeightForWidth(self.label_32.sizePolicy().hasHeightForWidth())
        self.label_32.setSizePolicy(sizePolicy)
        self.label_32.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.label_32)

        self.plot_pos_q1_2 = CustomPlotWidget(self.frame_2)
        self.plot_pos_q1_2.setObjectName(u"plot_pos_q1_2")
        self.plot_pos_q1_2.setMinimumSize(QSize(50, 50))

        self.verticalLayout_24.addWidget(self.plot_pos_q1_2)


        self.gridLayout_2.addLayout(self.verticalLayout_24, 0, 0, 1, 1)

        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.label_35 = QLabel(self.frame_2)
        self.label_35.setObjectName(u"label_35")
        sizePolicy.setHeightForWidth(self.label_35.sizePolicy().hasHeightForWidth())
        self.label_35.setSizePolicy(sizePolicy)
        self.label_35.setAlignment(Qt.AlignCenter)

        self.verticalLayout_27.addWidget(self.label_35)

        self.plot_pos_q4_2 = CustomPlotWidget(self.frame_2)
        self.plot_pos_q4_2.setObjectName(u"plot_pos_q4_2")
        self.plot_pos_q4_2.setMinimumSize(QSize(50, 50))

        self.verticalLayout_27.addWidget(self.plot_pos_q4_2)


        self.gridLayout_2.addLayout(self.verticalLayout_27, 0, 3, 1, 1)

        self.verticalLayout_29 = QVBoxLayout()
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.label_38 = QLabel(self.frame_2)
        self.label_38.setObjectName(u"label_38")
        sizePolicy.setHeightForWidth(self.label_38.sizePolicy().hasHeightForWidth())
        self.label_38.setSizePolicy(sizePolicy)
        self.label_38.setAlignment(Qt.AlignCenter)

        self.verticalLayout_29.addWidget(self.label_38)

        self.plot_vel_q1_2 = CustomPlotWidget(self.frame_2)
        self.plot_vel_q1_2.setObjectName(u"plot_vel_q1_2")
        self.plot_vel_q1_2.setMinimumSize(QSize(50, 50))

        self.verticalLayout_29.addWidget(self.plot_vel_q1_2)


        self.gridLayout_2.addLayout(self.verticalLayout_29, 1, 0, 1, 1)

        self.verticalLayout_30 = QVBoxLayout()
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.label_39 = QLabel(self.frame_2)
        self.label_39.setObjectName(u"label_39")
        sizePolicy.setHeightForWidth(self.label_39.sizePolicy().hasHeightForWidth())
        self.label_39.setSizePolicy(sizePolicy)
        self.label_39.setAlignment(Qt.AlignCenter)

        self.verticalLayout_30.addWidget(self.label_39)

        self.plot_vel_q2_2 = CustomPlotWidget(self.frame_2)
        self.plot_vel_q2_2.setObjectName(u"plot_vel_q2_2")
        self.plot_vel_q2_2.setMinimumSize(QSize(50, 50))

        self.verticalLayout_30.addWidget(self.plot_vel_q2_2)


        self.gridLayout_2.addLayout(self.verticalLayout_30, 1, 1, 1, 1)

        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_33 = QLabel(self.frame_2)
        self.label_33.setObjectName(u"label_33")
        sizePolicy.setHeightForWidth(self.label_33.sizePolicy().hasHeightForWidth())
        self.label_33.setSizePolicy(sizePolicy)
        self.label_33.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.label_33)

        self.plot_pos_q2_2 = CustomPlotWidget(self.frame_2)
        self.plot_pos_q2_2.setObjectName(u"plot_pos_q2_2")
        self.plot_pos_q2_2.setMinimumSize(QSize(50, 50))

        self.verticalLayout_25.addWidget(self.plot_pos_q2_2)


        self.gridLayout_2.addLayout(self.verticalLayout_25, 0, 1, 1, 1)

        self.gridLayout_2.setColumnStretch(0, 20)
        self.gridLayout_2.setColumnStretch(1, 19)
        self.gridLayout_2.setColumnStretch(2, 19)
        self.gridLayout_2.setColumnStretch(3, 19)

        self.verticalLayout_33.addLayout(self.gridLayout_2)


        self.verticalLayout_3.addWidget(self.frame_2)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_11)

        self.bt_transformarDirecta = QPushButton(self.scrollAreaWidgetContents)
        self.bt_transformarDirecta.setObjectName(u"bt_transformarDirecta")
        self.bt_transformarDirecta.setEnabled(False)
        self.bt_transformarDirecta.setMinimumSize(QSize(0, 50))
        self.bt_transformarDirecta.setFont(font)
        self.bt_transformarDirecta.setIcon(icon)
        self.bt_transformarDirecta.setIconSize(QSize(100, 100))

        self.horizontalLayout_9.addWidget(self.bt_transformarDirecta)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_12)


        self.verticalLayout_3.addLayout(self.horizontalLayout_9)

        self.frame_3 = QFrame(self.scrollAreaWidgetContents)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 0))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_3)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.mthList_3 = MTHList(self.frame_3)
        self.mthList_3.setObjectName(u"mthList_3")
        self.mthList_3.setMinimumSize(QSize(0, 50))

        self.verticalLayout_34.addWidget(self.mthList_3)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.bt_iniciarAnimacion = QPushButton(self.frame_3)
        self.bt_iniciarAnimacion.setObjectName(u"bt_iniciarAnimacion")
        self.bt_iniciarAnimacion.setEnabled(False)

        self.horizontalLayout_15.addWidget(self.bt_iniciarAnimacion)

        self.bt_verEn3D = QPushButton(self.frame_3)
        self.bt_verEn3D.setObjectName(u"bt_verEn3D")

        self.horizontalLayout_15.addWidget(self.bt_verEn3D)

        self.bt_verEnLineas = QPushButton(self.frame_3)
        self.bt_verEnLineas.setObjectName(u"bt_verEnLineas")
        self.bt_verEnLineas.setEnabled(False)

        self.horizontalLayout_15.addWidget(self.bt_verEnLineas)

        self.bt_ocultar = QPushButton(self.frame_3)
        self.bt_ocultar.setObjectName(u"bt_ocultar")

        self.horizontalLayout_15.addWidget(self.bt_ocultar)


        self.verticalLayout_34.addLayout(self.horizontalLayout_15)

        self.glView_3 = GLView(self.frame_3)
        self.glView_3.setObjectName(u"glView_3")
        self.glView_3.setMinimumSize(QSize(0, 50))

        self.verticalLayout_34.addWidget(self.glView_3)


        self.verticalLayout_3.addWidget(self.frame_3)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(sim_U2_T1)

        QMetaObject.connectSlotsByName(sim_U2_T1)
    # setupUi

    def retranslateUi(self, sim_U2_T1):
        sim_U2_T1.setWindowTitle(QCoreApplication.translate("sim_U2_T1", u"sim_U2_T1", None))
        self.label.setText(QCoreApplication.translate("sim_U2_T1", u"Espacio Cartesiano", None))
        self.label_2.setText(QCoreApplication.translate("sim_U2_T1", u"N\u00famero de puntos en R3", None))
        self.bt_generarMTHs.setText(QCoreApplication.translate("sim_U2_T1", u"Generar Localizaciones MTH", None))
        self.bt_interpolarR3.setText(QCoreApplication.translate("sim_U2_T1", u"Interpolar en R3", None))
        self.bt_basadoTiempo.setText(QCoreApplication.translate("sim_U2_T1", u"Basado en tiempo: ", None))
        self.bt_basadoPuntos.setText(QCoreApplication.translate("sim_U2_T1", u"Basado en puntos: ", None))
        self.label_3.setText(QCoreApplication.translate("sim_U2_T1", u"N\u00famero de puntos a mustrear", None))
        self.label_4.setText(QCoreApplication.translate("sim_U2_T1", u"Tiempo entre puntos", None))
        self.sb_dT_1.setSuffix(QCoreApplication.translate("sim_U2_T1", u" ms", None))
        self.bt_transformarInversa.setText(QCoreApplication.translate("sim_U2_T1", u"Transformar con Inversa\n"
"Espacio Articular", None))
        self.label_8.setText(QCoreApplication.translate("sim_U2_T1", u"q3", None))
        self.label_9.setText(QCoreApplication.translate("sim_U2_T1", u"q4", None))
        self.label_5.setText(QCoreApplication.translate("sim_U2_T1", u"q1", None))
        self.label_7.setText(QCoreApplication.translate("sim_U2_T1", u"q2", None))
        self.bt_interpolarArt.setText(QCoreApplication.translate("sim_U2_T1", u"Interpolar en espacio articular", None))
        self.bt_basadoTiempo_2.setText(QCoreApplication.translate("sim_U2_T1", u"Basado en tiempo: ", None))
        self.bt_basadoPuntos_2.setText(QCoreApplication.translate("sim_U2_T1", u"Basado en puntos: ", None))
        self.label_28.setText(QCoreApplication.translate("sim_U2_T1", u"N\u00famero de puntos a mustrear", None))
        self.label_29.setText(QCoreApplication.translate("sim_U2_T1", u"Tiempo entre puntos", None))
        self.sb_dT_2.setSuffix(QCoreApplication.translate("sim_U2_T1", u" ms", None))
        self.label_34.setText(QCoreApplication.translate("sim_U2_T1", u"q3", None))
        self.label_40.setText(QCoreApplication.translate("sim_U2_T1", u"q3", None))
        self.label_41.setText(QCoreApplication.translate("sim_U2_T1", u"q4", None))
        self.label_32.setText(QCoreApplication.translate("sim_U2_T1", u"q1", None))
        self.label_35.setText(QCoreApplication.translate("sim_U2_T1", u"q4", None))
        self.label_38.setText(QCoreApplication.translate("sim_U2_T1", u"q1", None))
        self.label_39.setText(QCoreApplication.translate("sim_U2_T1", u"q2", None))
        self.label_33.setText(QCoreApplication.translate("sim_U2_T1", u"q2", None))
        self.bt_transformarDirecta.setText(QCoreApplication.translate("sim_U2_T1", u"Transformar con Directa\n"
"Espacio Cartesiano", None))
        self.bt_iniciarAnimacion.setText(QCoreApplication.translate("sim_U2_T1", u"Iniciar animaci\u00f3n de trayectoria", None))
        self.bt_verEn3D.setText(QCoreApplication.translate("sim_U2_T1", u"Ver en 3D", None))
        self.bt_verEnLineas.setText(QCoreApplication.translate("sim_U2_T1", u"Ver en Lineas", None))
        self.bt_ocultar.setText(QCoreApplication.translate("sim_U2_T1", u"Ocultar", None))
    # retranslateUi

