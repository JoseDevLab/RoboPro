# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sim_U2_T9GcwIzk.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QSpinBox, QTabWidget,
    QVBoxLayout, QWidget)

from clases.CustomTable import CustomTable
from clases.GLView import GLView
from clases.PlotWidget import CustomPlotWidget

class Ui_sim_U2_T9(object):
    def setupUi(self, sim_U2_T9):
        if not sim_U2_T9.objectName():
            sim_U2_T9.setObjectName(u"sim_U2_T9")
        sim_U2_T9.resize(651, 611)
        sim_U2_T9.setStyleSheet(u"QWidget#sim_U2_T9{\n"
"background-color:rgba(0,0,0,0);\n"
"}")
        self.verticalLayout = QVBoxLayout(sim_U2_T9)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(sim_U2_T9)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 854, 592))
        self.scrollAreaWidgetContents.setStyleSheet(u"QWidget#scrollAreaWidgetContents{\n"
"background-color:rgb(0,0,0);\n"
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
"QPushButton:hover{\n"
"background-color:rgba(0,51,150,200);\n"
"}\n"
"QTabWidget#tabWidget QWidget#tab,\n"
"QTabWidget#tabWidget QWidget#tab_2,\n"
"QTabWidget#tabWidget QWidget#tab QWidget#scrollAreaWidgetContents_2{\n"
"background-color:translucid;\n"
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
"QTableWidget::item:selected {\n"
"background-color: rgb(0,51,112);\n"
"}\n"
"QTableWidget QWidget{\n"
"background-color: rgb(173,51,51);\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.tabWidget = QTabWidget(self.scrollAreaWidgetContents)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_5 = QVBoxLayout(self.tab)
        self.verticalLayout_5.setSpacing(2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(5)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.scrollArea_2 = QScrollArea(self.tab)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setMinimumSize(QSize(200, 232))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 198, 230))
        self.horizontalLayout = QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(56, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.ct_puntos = CustomTable(self.scrollAreaWidgetContents_2)
        self.ct_puntos.setObjectName(u"ct_puntos")
        self.ct_puntos.setMinimumSize(QSize(50, 50))

        self.horizontalLayout.addWidget(self.ct_puntos)

        self.horizontalSpacer_2 = QSpacerItem(56, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.horizontalLayout_11.addWidget(self.scrollArea_2)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalSpacer_4 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_4)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.frame_6 = QFrame(self.tab)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_6)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_2)

        self.sb_nPuntosEnt = QSpinBox(self.frame_6)
        self.sb_nPuntosEnt.setObjectName(u"sb_nPuntosEnt")
        self.sb_nPuntosEnt.setEnabled(False)
        self.sb_nPuntosEnt.setMinimum(2)

        self.horizontalLayout_7.addWidget(self.sb_nPuntosEnt)


        self.horizontalLayout_8.addWidget(self.frame_6)

        self.bt_ValidarPuntos = QPushButton(self.tab)
        self.bt_ValidarPuntos.setObjectName(u"bt_ValidarPuntos")

        self.horizontalLayout_8.addWidget(self.bt_ValidarPuntos)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_3)


        self.verticalLayout_8.addLayout(self.horizontalLayout_8)

        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_3)


        self.verticalLayout_4.addLayout(self.verticalLayout_8)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalSpacer_6 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_6)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.frame = QFrame(self.tab)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.cb_tipoTrayec = QComboBox(self.frame)
        self.cb_tipoTrayec.addItem("")
        self.cb_tipoTrayec.addItem("")
        self.cb_tipoTrayec.setObjectName(u"cb_tipoTrayec")

        self.horizontalLayout_2.addWidget(self.cb_tipoTrayec)


        self.horizontalLayout_9.addWidget(self.frame)

        self.fr_tipoMov = QFrame(self.tab)
        self.fr_tipoMov.setObjectName(u"fr_tipoMov")
        self.fr_tipoMov.setFrameShape(QFrame.StyledPanel)
        self.fr_tipoMov.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.fr_tipoMov)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.fr_tipoMov)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_4)

        self.cb_tipoMov = QComboBox(self.fr_tipoMov)
        self.cb_tipoMov.addItem("")
        self.cb_tipoMov.addItem("")
        self.cb_tipoMov.addItem("")
        self.cb_tipoMov.setObjectName(u"cb_tipoMov")

        self.horizontalLayout_3.addWidget(self.cb_tipoMov)


        self.horizontalLayout_9.addWidget(self.fr_tipoMov)

        self.fr_nPuntosR3 = QFrame(self.tab)
        self.fr_nPuntosR3.setObjectName(u"fr_nPuntosR3")
        self.fr_nPuntosR3.setFrameShape(QFrame.StyledPanel)
        self.fr_nPuntosR3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.fr_nPuntosR3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.fr_nPuntosR3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_5)

        self.sb_nPuntosR3 = QSpinBox(self.fr_nPuntosR3)
        self.sb_nPuntosR3.setObjectName(u"sb_nPuntosR3")
        self.sb_nPuntosR3.setMinimum(2)
        self.sb_nPuntosR3.setMaximum(999)
        self.sb_nPuntosR3.setValue(10)

        self.horizontalLayout_4.addWidget(self.sb_nPuntosR3)


        self.horizontalLayout_9.addWidget(self.fr_nPuntosR3)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_4)


        self.verticalLayout_9.addLayout(self.horizontalLayout_9)

        self.verticalSpacer_5 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_5)


        self.verticalLayout_4.addLayout(self.verticalLayout_9)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalSpacer_8 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_8)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.frame_4 = QFrame(self.tab)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.frame_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_6)

        self.cb_tipoInt = QComboBox(self.frame_4)
        self.cb_tipoInt.addItem("")
        self.cb_tipoInt.addItem("")
        self.cb_tipoInt.setObjectName(u"cb_tipoInt")

        self.horizontalLayout_5.addWidget(self.cb_tipoInt)


        self.horizontalLayout_10.addWidget(self.frame_4)

        self.fr_Tm = QFrame(self.tab)
        self.fr_Tm.setObjectName(u"fr_Tm")
        self.fr_Tm.setFrameShape(QFrame.StyledPanel)
        self.fr_Tm.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.fr_Tm)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.fr_Tm)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.label_7)

        self.sb_Tm = QSpinBox(self.fr_Tm)
        self.sb_Tm.setObjectName(u"sb_Tm")
        self.sb_Tm.setMinimum(10)
        self.sb_Tm.setMaximum(9999)
        self.sb_Tm.setValue(40)

        self.horizontalLayout_6.addWidget(self.sb_Tm)


        self.horizontalLayout_10.addWidget(self.fr_Tm)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_5)


        self.verticalLayout_10.addLayout(self.horizontalLayout_10)

        self.verticalSpacer_7 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_7)


        self.verticalLayout_4.addLayout(self.verticalLayout_10)


        self.horizontalLayout_11.addLayout(self.verticalLayout_4)


        self.verticalLayout_5.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.bt_genTrayec = QPushButton(self.tab)
        self.bt_genTrayec.setObjectName(u"bt_genTrayec")
        self.bt_genTrayec.setEnabled(False)
        self.bt_genTrayec.setMinimumSize(QSize(0, 50))

        self.horizontalLayout_12.addWidget(self.bt_genTrayec)

        self.bt_movRob = QPushButton(self.tab)
        self.bt_movRob.setObjectName(u"bt_movRob")
        self.bt_movRob.setEnabled(False)
        self.bt_movRob.setMinimumSize(QSize(0, 50))

        self.horizontalLayout_12.addWidget(self.bt_movRob)

        self.bt_detRob = QPushButton(self.tab)
        self.bt_detRob.setObjectName(u"bt_detRob")
        self.bt_detRob.setMinimumSize(QSize(0, 50))

        self.horizontalLayout_12.addWidget(self.bt_detRob)


        self.verticalLayout_5.addLayout(self.horizontalLayout_12)

        self.gv_1 = GLView(self.tab)
        self.gv_1.setObjectName(u"gv_1")
        self.gv_1.setMinimumSize(QSize(0, 50))

        self.verticalLayout_5.addWidget(self.gv_1)

        self.verticalSpacer = QSpacerItem(20, 178, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.verticalLayout_5.setStretch(3, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_3 = QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_8 = QLabel(self.tab_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_8, 0, 0, 1, 1)

        self.label_9 = QLabel(self.tab_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_9, 0, 1, 1, 1)

        self.label_10 = QLabel(self.tab_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_10, 0, 2, 1, 1)

        self.label_11 = QLabel(self.tab_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_11, 0, 3, 1, 1)

        self.cp_q_1 = CustomPlotWidget(self.tab_2)
        self.cp_q_1.setObjectName(u"cp_q_1")
        self.cp_q_1.setMinimumSize(QSize(50, 50))
        self.cp_q_1.setStyleSheet(u"background-color:gray;")

        self.gridLayout.addWidget(self.cp_q_1, 1, 0, 1, 1)

        self.cp_q_2 = CustomPlotWidget(self.tab_2)
        self.cp_q_2.setObjectName(u"cp_q_2")
        self.cp_q_2.setMinimumSize(QSize(50, 50))
        self.cp_q_2.setStyleSheet(u"background-color:gray;")

        self.gridLayout.addWidget(self.cp_q_2, 1, 1, 1, 1)

        self.cp_q_3 = CustomPlotWidget(self.tab_2)
        self.cp_q_3.setObjectName(u"cp_q_3")
        self.cp_q_3.setMinimumSize(QSize(50, 50))
        self.cp_q_3.setStyleSheet(u"background-color:gray;")

        self.gridLayout.addWidget(self.cp_q_3, 1, 2, 1, 1)

        self.cp_q_4 = CustomPlotWidget(self.tab_2)
        self.cp_q_4.setObjectName(u"cp_q_4")
        self.cp_q_4.setMinimumSize(QSize(50, 50))
        self.cp_q_4.setStyleSheet(u"background-color:gray;")

        self.gridLayout.addWidget(self.cp_q_4, 1, 3, 1, 1)

        self.cp_qp_1 = CustomPlotWidget(self.tab_2)
        self.cp_qp_1.setObjectName(u"cp_qp_1")
        self.cp_qp_1.setMinimumSize(QSize(50, 50))
        self.cp_qp_1.setStyleSheet(u"background-color:gray;")

        self.gridLayout.addWidget(self.cp_qp_1, 2, 0, 1, 1)

        self.cp_qp_2 = CustomPlotWidget(self.tab_2)
        self.cp_qp_2.setObjectName(u"cp_qp_2")
        self.cp_qp_2.setMinimumSize(QSize(50, 50))
        self.cp_qp_2.setStyleSheet(u"background-color:gray;")

        self.gridLayout.addWidget(self.cp_qp_2, 2, 1, 1, 1)

        self.cp_qp_3 = CustomPlotWidget(self.tab_2)
        self.cp_qp_3.setObjectName(u"cp_qp_3")
        self.cp_qp_3.setMinimumSize(QSize(50, 50))
        self.cp_qp_3.setStyleSheet(u"background-color:gray;")

        self.gridLayout.addWidget(self.cp_qp_3, 2, 2, 1, 1)

        self.cp_qp_4 = CustomPlotWidget(self.tab_2)
        self.cp_qp_4.setObjectName(u"cp_qp_4")
        self.cp_qp_4.setMinimumSize(QSize(50, 50))
        self.cp_qp_4.setStyleSheet(u"background-color:gray;")

        self.gridLayout.addWidget(self.cp_qp_4, 2, 3, 1, 1)

        self.cp_qpp_1 = CustomPlotWidget(self.tab_2)
        self.cp_qpp_1.setObjectName(u"cp_qpp_1")
        self.cp_qpp_1.setMinimumSize(QSize(50, 50))
        self.cp_qpp_1.setStyleSheet(u"background-color:gray;")

        self.gridLayout.addWidget(self.cp_qpp_1, 3, 0, 1, 1)

        self.cp_qpp_2 = CustomPlotWidget(self.tab_2)
        self.cp_qpp_2.setObjectName(u"cp_qpp_2")
        self.cp_qpp_2.setMinimumSize(QSize(50, 50))
        self.cp_qpp_2.setStyleSheet(u"background-color:gray;")

        self.gridLayout.addWidget(self.cp_qpp_2, 3, 1, 1, 1)

        self.cp_qpp_3 = CustomPlotWidget(self.tab_2)
        self.cp_qpp_3.setObjectName(u"cp_qpp_3")
        self.cp_qpp_3.setMinimumSize(QSize(50, 50))
        self.cp_qpp_3.setStyleSheet(u"background-color:gray;")

        self.gridLayout.addWidget(self.cp_qpp_3, 3, 2, 1, 1)

        self.cp_qpp_4 = CustomPlotWidget(self.tab_2)
        self.cp_qpp_4.setObjectName(u"cp_qpp_4")
        self.cp_qpp_4.setMinimumSize(QSize(50, 50))
        self.cp_qpp_4.setStyleSheet(u"background-color:gray;")

        self.gridLayout.addWidget(self.cp_qpp_4, 3, 3, 1, 1)

        self.cp_qppp_1 = CustomPlotWidget(self.tab_2)
        self.cp_qppp_1.setObjectName(u"cp_qppp_1")
        self.cp_qppp_1.setMinimumSize(QSize(50, 50))
        self.cp_qppp_1.setStyleSheet(u"background-color:gray;")

        self.gridLayout.addWidget(self.cp_qppp_1, 4, 0, 1, 1)

        self.cp_qppp_2 = CustomPlotWidget(self.tab_2)
        self.cp_qppp_2.setObjectName(u"cp_qppp_2")
        self.cp_qppp_2.setMinimumSize(QSize(50, 50))
        self.cp_qppp_2.setStyleSheet(u"background-color:gray;")

        self.gridLayout.addWidget(self.cp_qppp_2, 4, 1, 1, 1)

        self.cp_qppp_3 = CustomPlotWidget(self.tab_2)
        self.cp_qppp_3.setObjectName(u"cp_qppp_3")
        self.cp_qppp_3.setMinimumSize(QSize(50, 50))
        self.cp_qppp_3.setStyleSheet(u"background-color:gray;")

        self.gridLayout.addWidget(self.cp_qppp_3, 4, 2, 1, 1)

        self.cp_qppp_4 = CustomPlotWidget(self.tab_2)
        self.cp_qppp_4.setObjectName(u"cp_qppp_4")
        self.cp_qppp_4.setMinimumSize(QSize(50, 50))
        self.cp_qppp_4.setStyleSheet(u"background-color:gray;")

        self.gridLayout.addWidget(self.cp_qppp_4, 4, 3, 1, 1)

        self.gridLayout.setColumnStretch(0, 20)
        self.gridLayout.setColumnStretch(1, 19)
        self.gridLayout.setColumnStretch(2, 19)
        self.gridLayout.setColumnStretch(3, 19)

        self.verticalLayout_3.addLayout(self.gridLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 306, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.verticalLayout_3.setStretch(1, 1)
        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(sim_U2_T9)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(sim_U2_T9)
    # setupUi

    def retranslateUi(self, sim_U2_T9):
        sim_U2_T9.setWindowTitle(QCoreApplication.translate("sim_U2_T9", u"Sim_U2_T9", None))
        self.label.setText(QCoreApplication.translate("sim_U2_T9", u"Implementaci\u00f3n de Interpoladores", None))
        self.label_2.setText(QCoreApplication.translate("sim_U2_T9", u"Puntos de Entrada:", None))
        self.bt_ValidarPuntos.setText(QCoreApplication.translate("sim_U2_T9", u"Validar Puntos", None))
        self.label_3.setText(QCoreApplication.translate("sim_U2_T9", u"Tipo de Trayectoria:", None))
        self.cb_tipoTrayec.setItemText(0, QCoreApplication.translate("sim_U2_T9", u"Punto a Punto", None))
        self.cb_tipoTrayec.setItemText(1, QCoreApplication.translate("sim_U2_T9", u"Continua", None))

        self.label_4.setText(QCoreApplication.translate("sim_U2_T9", u"Tipo de Movimiento:", None))
        self.cb_tipoMov.setItemText(0, QCoreApplication.translate("sim_U2_T9", u"Eje a Eje", None))
        self.cb_tipoMov.setItemText(1, QCoreApplication.translate("sim_U2_T9", u"Ejes Simultaneos", None))
        self.cb_tipoMov.setItemText(2, QCoreApplication.translate("sim_U2_T9", u"Ejes Coordinados", None))

        self.label_5.setText(QCoreApplication.translate("sim_U2_T9", u"Cantidad de Puntos R3:", None))
        self.label_6.setText(QCoreApplication.translate("sim_U2_T9", u"Interpolador:", None))
        self.cb_tipoInt.setItemText(0, QCoreApplication.translate("sim_U2_T9", u"Lineal", None))
        self.cb_tipoInt.setItemText(1, QCoreApplication.translate("sim_U2_T9", u"Trapezoidal", None))

        self.label_7.setText(QCoreApplication.translate("sim_U2_T9", u"Periodo de Muestreo:", None))
        self.sb_Tm.setSuffix(QCoreApplication.translate("sim_U2_T9", u" ms", None))
#if QT_CONFIG(tooltip)
        self.bt_genTrayec.setToolTip(QCoreApplication.translate("sim_U2_T9", u"Valida los puntos primero", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.bt_genTrayec.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.bt_genTrayec.setText(QCoreApplication.translate("sim_U2_T9", u"Generar Trayectoria", None))
        self.bt_movRob.setText(QCoreApplication.translate("sim_U2_T9", u"Mover Robot", None))
        self.bt_detRob.setText(QCoreApplication.translate("sim_U2_T9", u"Detener Robot", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("sim_U2_T9", u"Espacio Cartesiano", None))
        self.label_8.setText(QCoreApplication.translate("sim_U2_T9", u"Articulaci\u00f3n 1", None))
        self.label_9.setText(QCoreApplication.translate("sim_U2_T9", u"Articulaci\u00f3n 2", None))
        self.label_10.setText(QCoreApplication.translate("sim_U2_T9", u"Articulaci\u00f3n 3", None))
        self.label_11.setText(QCoreApplication.translate("sim_U2_T9", u"Articulaci\u00f3n 4", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("sim_U2_T9", u"Espacio Articular", None))
    # retranslateUi

