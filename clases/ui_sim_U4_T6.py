# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sim_U4_T6JVCpou.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QScrollArea, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

from clases.CustomTable import CustomTable
from clases.PlotWidget import CustomPlotWidget

class Ui_sim_U4_T6(object):
    def setupUi(self, sim_U4_T6):
        if not sim_U4_T6.objectName():
            sim_U4_T6.setObjectName(u"sim_U4_T6")
        sim_U4_T6.resize(550, 386)
        sim_U4_T6.setStyleSheet(u"QWidget#sim_U4_T6,\n"
"QScrollArea#scrollArea{\n"
"background-color:rgba(0,0,0,0);\n"
"}")
        self.verticalLayout = QVBoxLayout(sim_U4_T6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(sim_U4_T6)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 548, 246))
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
"}")
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)

        self.cp_1 = CustomPlotWidget(self.scrollAreaWidgetContents)
        self.cp_1.setObjectName(u"cp_1")
        self.cp_1.setMinimumSize(QSize(0, 50))

        self.verticalLayout_3.addWidget(self.cp_1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.cp_2 = CustomPlotWidget(self.scrollAreaWidgetContents)
        self.cp_2.setObjectName(u"cp_2")
        self.cp_2.setMinimumSize(QSize(0, 50))

        self.horizontalLayout.addWidget(self.cp_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.cb_oper = QComboBox(self.scrollAreaWidgetContents)
        self.cb_oper.addItem("")
        self.cb_oper.addItem("")
        self.cb_oper.addItem("")
        self.cb_oper.addItem("")
        self.cb_oper.addItem("")
        self.cb_oper.addItem("")
        self.cb_oper.addItem("")
        self.cb_oper.addItem("")
        self.cb_oper.addItem("")
        self.cb_oper.addItem("")
        self.cb_oper.addItem("")
        self.cb_oper.addItem("")
        self.cb_oper.setObjectName(u"cb_oper")

        self.verticalLayout_2.addWidget(self.cb_oper)

        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(2, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.ct_oper = CustomTable(self.scrollAreaWidgetContents)
        self.ct_oper.setObjectName(u"ct_oper")
        self.ct_oper.setMinimumSize(QSize(20, 10))

        self.horizontalLayout_2.addWidget(self.ct_oper)

        self.horizontalSpacer_2 = QSpacerItem(2, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(2, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(4, 1)

        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.horizontalLayout.setStretch(0, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(sim_U4_T6)

        QMetaObject.connectSlotsByName(sim_U4_T6)
    # setupUi

    def retranslateUi(self, sim_U4_T6):
        sim_U4_T6.setWindowTitle(QCoreApplication.translate("sim_U4_T6", u"Sim_U4_T6", None))
        self.label.setText(QCoreApplication.translate("sim_U4_T6", u"Operaciones Morfol\u00f3gicas", None))
        self.cb_oper.setItemText(0, QCoreApplication.translate("sim_U4_T6", u"Gradiente dy", None))
        self.cb_oper.setItemText(1, QCoreApplication.translate("sim_U4_T6", u"Gradiente dx", None))
        self.cb_oper.setItemText(2, QCoreApplication.translate("sim_U4_T6", u"Roberts 1", None))
        self.cb_oper.setItemText(3, QCoreApplication.translate("sim_U4_T6", u"Roberts 2", None))
        self.cb_oper.setItemText(4, QCoreApplication.translate("sim_U4_T6", u"Segunda Derivada", None))
        self.cb_oper.setItemText(5, QCoreApplication.translate("sim_U4_T6", u"Laplaciana", None))
        self.cb_oper.setItemText(6, QCoreApplication.translate("sim_U4_T6", u"Prewitt Horizontal", None))
        self.cb_oper.setItemText(7, QCoreApplication.translate("sim_U4_T6", u"Prewitt Vertical", None))
        self.cb_oper.setItemText(8, QCoreApplication.translate("sim_U4_T6", u"Diagonal 1", None))
        self.cb_oper.setItemText(9, QCoreApplication.translate("sim_U4_T6", u"Diagonal 2", None))
        self.cb_oper.setItemText(10, QCoreApplication.translate("sim_U4_T6", u"Sobel 1", None))
        self.cb_oper.setItemText(11, QCoreApplication.translate("sim_U4_T6", u"Sobel 2", None))

        self.label_2.setText(QCoreApplication.translate("sim_U4_T6", u"Matriz de Operador", None))
    # retranslateUi

