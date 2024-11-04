# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sim_U4_T4NACrPG.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QSpinBox, QVBoxLayout, QWidget)

from clases.PlotWidget import CustomPlotWidget

class Ui_sim_U4_T4(object):
    def setupUi(self, sim_U4_T4):
        if not sim_U4_T4.objectName():
            sim_U4_T4.setObjectName(u"sim_U4_T4")
        sim_U4_T4.resize(682, 417)
        sim_U4_T4.setStyleSheet(u"QWidget#sim_U4_T4,\n"
"QScrollArea#scrollArea{\n"
"background-color:rgba(0,0,0,0);\n"
"}")
        self.verticalLayout = QVBoxLayout(sim_U4_T4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(sim_U4_T4)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(-326, 0, 1006, 238))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setStyleSheet(u"QWidget#scrollAreaWidgetContents{\n"
"background-color:rgb(0,0,0);\n"
"}\n"
"QLabel{\n"
"color:white;\n"
"}\n"
"QTableWidget::item {\n"
"background-color: black;\n"
"color: white;\n"
"border: 1px solid rgb(80, 80, 80); \n"
"}\n"
"QTableWidget::item:selected {\n"
"background-color: rgb(0,51,112);\n"
"}\n"
"QTableWidget QWidget,\n"
"QTableWidget QFrame{\n"
"background-color: rgb(173,51,51);\n"
"}\n"
"QPushButton{\n"
"font:16pt \"Britannic Bold\";\n"
"color:white;\n"
"background-color:rgba(0,51,102,200);\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(0,51,150,200);\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.cp_1 = CustomPlotWidget(self.scrollAreaWidgetContents)
        self.cp_1.setObjectName(u"cp_1")
        self.cp_1.setMinimumSize(QSize(50, 50))

        self.horizontalLayout.addWidget(self.cp_1)

        self.cp_2 = CustomPlotWidget(self.scrollAreaWidgetContents)
        self.cp_2.setObjectName(u"cp_2")
        self.cp_2.setMinimumSize(QSize(50, 50))

        self.horizontalLayout.addWidget(self.cp_2)

        self.cp_3 = CustomPlotWidget(self.scrollAreaWidgetContents)
        self.cp_3.setObjectName(u"cp_3")
        self.cp_3.setMinimumSize(QSize(50, 50))

        self.horizontalLayout.addWidget(self.cp_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_2)

        self.cb_estruc = QComboBox(self.scrollAreaWidgetContents)
        self.cb_estruc.addItem("")
        self.cb_estruc.addItem("")
        self.cb_estruc.addItem("")
        self.cb_estruc.addItem("")
        self.cb_estruc.addItem("")
        self.cb_estruc.setObjectName(u"cb_estruc")

        self.horizontalLayout_5.addWidget(self.cb_estruc)

        self.lb_r = QLabel(self.scrollAreaWidgetContents)
        self.lb_r.setObjectName(u"lb_r")
        self.lb_r.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.lb_r)

        self.sb_r = QSpinBox(self.scrollAreaWidgetContents)
        self.sb_r.setObjectName(u"sb_r")
        self.sb_r.setMinimum(2)
        self.sb_r.setMaximum(999)
        self.sb_r.setValue(11)

        self.horizontalLayout_5.addWidget(self.sb_r)

        self.fr_grados = QFrame(self.scrollAreaWidgetContents)
        self.fr_grados.setObjectName(u"fr_grados")
        self.fr_grados.setFrameShape(QFrame.StyledPanel)
        self.fr_grados.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.fr_grados)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.fr_grados)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_4)

        self.sb_deg = QSpinBox(self.fr_grados)
        self.sb_deg.setObjectName(u"sb_deg")
        self.sb_deg.setMinimum(-360)
        self.sb_deg.setMaximum(360)
        self.sb_deg.setSingleStep(10)
        self.sb_deg.setValue(45)

        self.horizontalLayout_3.addWidget(self.sb_deg)


        self.horizontalLayout_5.addWidget(self.fr_grados)

        self.fr_ancho = QFrame(self.scrollAreaWidgetContents)
        self.fr_ancho.setObjectName(u"fr_ancho")
        self.fr_ancho.setFrameShape(QFrame.StyledPanel)
        self.fr_ancho.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.fr_ancho)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(self.fr_ancho)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_5)

        self.sb_ancho = QSpinBox(self.fr_ancho)
        self.sb_ancho.setObjectName(u"sb_ancho")
        self.sb_ancho.setMinimum(2)
        self.sb_ancho.setMaximum(999)
        self.sb_ancho.setValue(15)

        self.horizontalLayout_4.addWidget(self.sb_ancho)


        self.horizontalLayout_5.addWidget(self.fr_ancho)

        self.frame_3 = QFrame(self.scrollAreaWidgetContents)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.label_6)

        self.cb_oper = QComboBox(self.frame_3)
        self.cb_oper.addItem("")
        self.cb_oper.addItem("")
        self.cb_oper.addItem("")
        self.cb_oper.addItem("")
        self.cb_oper.setObjectName(u"cb_oper")

        self.horizontalLayout_6.addWidget(self.cb_oper)


        self.horizontalLayout_5.addWidget(self.frame_3)

        self.bt_aplicar = QPushButton(self.scrollAreaWidgetContents)
        self.bt_aplicar.setObjectName(u"bt_aplicar")

        self.horizontalLayout_5.addWidget(self.bt_aplicar)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.cp_4 = CustomPlotWidget(self.scrollAreaWidgetContents)
        self.cp_4.setObjectName(u"cp_4")
        self.cp_4.setMinimumSize(QSize(50, 50))

        self.verticalLayout_2.addWidget(self.cp_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.cp_5 = CustomPlotWidget(self.scrollAreaWidgetContents)
        self.cp_5.setObjectName(u"cp_5")
        self.cp_5.setMinimumSize(QSize(50, 50))

        self.horizontalLayout_2.addWidget(self.cp_5)

        self.cp_6 = CustomPlotWidget(self.scrollAreaWidgetContents)
        self.cp_6.setObjectName(u"cp_6")
        self.cp_6.setMinimumSize(QSize(50, 50))

        self.horizontalLayout_2.addWidget(self.cp_6)

        self.cp_7 = CustomPlotWidget(self.scrollAreaWidgetContents)
        self.cp_7.setObjectName(u"cp_7")
        self.cp_7.setMinimumSize(QSize(50, 50))

        self.horizontalLayout_2.addWidget(self.cp_7)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(sim_U4_T4)

        QMetaObject.connectSlotsByName(sim_U4_T4)
    # setupUi

    def retranslateUi(self, sim_U4_T4):
        sim_U4_T4.setWindowTitle(QCoreApplication.translate("sim_U4_T4", u"Sim_U4_T4", None))
        self.label.setText(QCoreApplication.translate("sim_U4_T4", u"Elementos Estructurantes", None))
        self.label_2.setText(QCoreApplication.translate("sim_U4_T4", u"Elemento Estructurante", None))
        self.cb_estruc.setItemText(0, QCoreApplication.translate("sim_U4_T4", u"Diamante", None))
        self.cb_estruc.setItemText(1, QCoreApplication.translate("sim_U4_T4", u"Disco", None))
        self.cb_estruc.setItemText(2, QCoreApplication.translate("sim_U4_T4", u"L\u00ednea", None))
        self.cb_estruc.setItemText(3, QCoreApplication.translate("sim_U4_T4", u"Cuadrado", None))
        self.cb_estruc.setItemText(4, QCoreApplication.translate("sim_U4_T4", u"Rectangulo", None))

        self.lb_r.setText(QCoreApplication.translate("sim_U4_T4", u"Radio", None))
        self.sb_r.setSuffix(QCoreApplication.translate("sim_U4_T4", u"px", None))
        self.label_4.setText(QCoreApplication.translate("sim_U4_T4", u"Grados", None))
        self.sb_deg.setSuffix(QCoreApplication.translate("sim_U4_T4", u"\u00b0", None))
        self.label_5.setText(QCoreApplication.translate("sim_U4_T4", u"Ancho", None))
        self.sb_ancho.setSuffix(QCoreApplication.translate("sim_U4_T4", u"px", None))
        self.label_6.setText(QCoreApplication.translate("sim_U4_T4", u"Operaci\u00f3n", None))
        self.cb_oper.setItemText(0, QCoreApplication.translate("sim_U4_T4", u"Erosionar", None))
        self.cb_oper.setItemText(1, QCoreApplication.translate("sim_U4_T4", u"Dilatar", None))
        self.cb_oper.setItemText(2, QCoreApplication.translate("sim_U4_T4", u"Dilatar + Erosionar (Closing)", None))
        self.cb_oper.setItemText(3, QCoreApplication.translate("sim_U4_T4", u"Erosionar + Dilatar (Opening)", None))

        self.bt_aplicar.setText(QCoreApplication.translate("sim_U4_T4", u"Aplicar operaci\u00f3n", None))
    # retranslateUi

