# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sim_U4_T3EGQlnl.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QScrollArea, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

from clases.PlotWidget import CustomPlotWidget

class Ui_sim_U4_T3(object):
    def setupUi(self, sim_U4_T3):
        if not sim_U4_T3.objectName():
            sim_U4_T3.setObjectName(u"sim_U4_T3")
        sim_U4_T3.resize(603, 452)
        sim_U4_T3.setStyleSheet(u"QWidget#sim_U4_T3,\n"
"QScrollArea#scrollArea{\n"
"background-color:rgba(0,0,0,0);\n"
"}")
        self.verticalLayout = QVBoxLayout(sim_U4_T3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(sim_U4_T3)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 601, 284))
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
"}")
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)

        self.cp_1 = CustomPlotWidget(self.scrollAreaWidgetContents)
        self.cp_1.setObjectName(u"cp_1")
        self.cp_1.setMinimumSize(QSize(0, 50))

        self.gridLayout.addWidget(self.cp_1, 1, 0, 1, 1)

        self.cp_2 = CustomPlotWidget(self.scrollAreaWidgetContents)
        self.cp_2.setObjectName(u"cp_2")
        self.cp_2.setMinimumSize(QSize(0, 50))

        self.gridLayout.addWidget(self.cp_2, 1, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_7 = QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_7)

        self.cb_imgBin_1 = QComboBox(self.scrollAreaWidgetContents)
        self.cb_imgBin_1.addItem("")
        self.cb_imgBin_1.addItem("")
        self.cb_imgBin_1.addItem("")
        self.cb_imgBin_1.addItem("")
        self.cb_imgBin_1.addItem("")
        self.cb_imgBin_1.addItem("")
        self.cb_imgBin_1.setObjectName(u"cb_imgBin_1")

        self.horizontalLayout.addWidget(self.cb_imgBin_1)

        self.cb_opLog_1 = QComboBox(self.scrollAreaWidgetContents)
        self.cb_opLog_1.addItem("")
        self.cb_opLog_1.addItem("")
        self.cb_opLog_1.addItem("")
        self.cb_opLog_1.setObjectName(u"cb_opLog_1")

        self.horizontalLayout.addWidget(self.cb_opLog_1)

        self.cb_imgBin_2 = QComboBox(self.scrollAreaWidgetContents)
        self.cb_imgBin_2.addItem("")
        self.cb_imgBin_2.addItem("")
        self.cb_imgBin_2.addItem("")
        self.cb_imgBin_2.addItem("")
        self.cb_imgBin_2.addItem("")
        self.cb_imgBin_2.addItem("")
        self.cb_imgBin_2.setObjectName(u"cb_imgBin_2")

        self.horizontalLayout.addWidget(self.cb_imgBin_2)

        self.label_9 = QLabel(self.scrollAreaWidgetContents)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_9)

        self.cb_opLog_2 = QComboBox(self.scrollAreaWidgetContents)
        self.cb_opLog_2.addItem("")
        self.cb_opLog_2.addItem("")
        self.cb_opLog_2.addItem("")
        self.cb_opLog_2.setObjectName(u"cb_opLog_2")

        self.horizontalLayout.addWidget(self.cb_opLog_2)

        self.cb_imgBin_3 = QComboBox(self.scrollAreaWidgetContents)
        self.cb_imgBin_3.addItem("")
        self.cb_imgBin_3.addItem("")
        self.cb_imgBin_3.addItem("")
        self.cb_imgBin_3.addItem("")
        self.cb_imgBin_3.addItem("")
        self.cb_imgBin_3.addItem("")
        self.cb_imgBin_3.addItem("")
        self.cb_imgBin_3.setObjectName(u"cb_imgBin_3")

        self.horizontalLayout.addWidget(self.cb_imgBin_3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.cp_5 = CustomPlotWidget(self.scrollAreaWidgetContents)
        self.cp_5.setObjectName(u"cp_5")
        self.cp_5.setMinimumSize(QSize(0, 50))

        self.gridLayout_2.addWidget(self.cp_5, 1, 2, 1, 1)

        self.label_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_6, 0, 2, 1, 1)

        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)

        self.cp_4 = CustomPlotWidget(self.scrollAreaWidgetContents)
        self.cp_4.setObjectName(u"cp_4")
        self.cp_4.setMinimumSize(QSize(0, 50))

        self.gridLayout_2.addWidget(self.cp_4, 1, 1, 1, 1)

        self.cp_3 = CustomPlotWidget(self.scrollAreaWidgetContents)
        self.cp_3.setObjectName(u"cp_3")
        self.cp_3.setMinimumSize(QSize(0, 50))

        self.gridLayout_2.addWidget(self.cp_3, 1, 0, 1, 1)

        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_5, 0, 1, 1, 1)

        self.label_8 = QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_8, 2, 0, 1, 1)

        self.cp_6 = CustomPlotWidget(self.scrollAreaWidgetContents)
        self.cp_6.setObjectName(u"cp_6")
        self.cp_6.setMinimumSize(QSize(0, 50))

        self.gridLayout_2.addWidget(self.cp_6, 3, 0, 1, 1)

        self.label_10 = QLabel(self.scrollAreaWidgetContents)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_10, 2, 1, 1, 1)

        self.label_11 = QLabel(self.scrollAreaWidgetContents)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_11, 2, 2, 1, 1)

        self.cp_7 = CustomPlotWidget(self.scrollAreaWidgetContents)
        self.cp_7.setObjectName(u"cp_7")
        self.cp_7.setMinimumSize(QSize(0, 50))

        self.gridLayout_2.addWidget(self.cp_7, 3, 1, 1, 1)

        self.cp_8 = CustomPlotWidget(self.scrollAreaWidgetContents)
        self.cp_8.setObjectName(u"cp_8")
        self.cp_8.setMinimumSize(QSize(0, 50))

        self.gridLayout_2.addWidget(self.cp_8, 3, 2, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(sim_U4_T3)

        QMetaObject.connectSlotsByName(sim_U4_T3)
    # setupUi

    def retranslateUi(self, sim_U4_T3):
        sim_U4_T3.setWindowTitle(QCoreApplication.translate("sim_U4_T3", u"Sim_U4_T3", None))
        self.label.setText(QCoreApplication.translate("sim_U4_T3", u"Operadores L\u00f3gicos", None))
        self.label_2.setText(QCoreApplication.translate("sim_U4_T3", u"Imagen Original", None))
        self.label_3.setText(QCoreApplication.translate("sim_U4_T3", u"Imagen Resultante", None))
        self.label_7.setText(QCoreApplication.translate("sim_U4_T3", u"(", None))
        self.cb_imgBin_1.setItemText(0, QCoreApplication.translate("sim_U4_T3", u"Rojo Binaria", None))
        self.cb_imgBin_1.setItemText(1, QCoreApplication.translate("sim_U4_T3", u"Verde Binaria", None))
        self.cb_imgBin_1.setItemText(2, QCoreApplication.translate("sim_U4_T3", u"Azul Binaria", None))
        self.cb_imgBin_1.setItemText(3, QCoreApplication.translate("sim_U4_T3", u"NOT Rojo Binaria", None))
        self.cb_imgBin_1.setItemText(4, QCoreApplication.translate("sim_U4_T3", u"NOT Verde Binaria", None))
        self.cb_imgBin_1.setItemText(5, QCoreApplication.translate("sim_U4_T3", u"NOT Azul Binaria", None))

        self.cb_opLog_1.setItemText(0, QCoreApplication.translate("sim_U4_T3", u"AND", None))
        self.cb_opLog_1.setItemText(1, QCoreApplication.translate("sim_U4_T3", u"OR", None))
        self.cb_opLog_1.setItemText(2, QCoreApplication.translate("sim_U4_T3", u"XOR", None))

        self.cb_imgBin_2.setItemText(0, QCoreApplication.translate("sim_U4_T3", u"Rojo Binaria", None))
        self.cb_imgBin_2.setItemText(1, QCoreApplication.translate("sim_U4_T3", u"Verde Binaria", None))
        self.cb_imgBin_2.setItemText(2, QCoreApplication.translate("sim_U4_T3", u"Azul Binaria", None))
        self.cb_imgBin_2.setItemText(3, QCoreApplication.translate("sim_U4_T3", u"NOT Rojo Binaria", None))
        self.cb_imgBin_2.setItemText(4, QCoreApplication.translate("sim_U4_T3", u"NOT Verde Binaria", None))
        self.cb_imgBin_2.setItemText(5, QCoreApplication.translate("sim_U4_T3", u"NOT Azul Binaria", None))

        self.label_9.setText(QCoreApplication.translate("sim_U4_T3", u")", None))
        self.cb_opLog_2.setItemText(0, QCoreApplication.translate("sim_U4_T3", u"AND", None))
        self.cb_opLog_2.setItemText(1, QCoreApplication.translate("sim_U4_T3", u"OR", None))
        self.cb_opLog_2.setItemText(2, QCoreApplication.translate("sim_U4_T3", u"XOR", None))

        self.cb_imgBin_3.setItemText(0, QCoreApplication.translate("sim_U4_T3", u"Ignorar", None))
        self.cb_imgBin_3.setItemText(1, QCoreApplication.translate("sim_U4_T3", u"Rojo Binaria", None))
        self.cb_imgBin_3.setItemText(2, QCoreApplication.translate("sim_U4_T3", u"Verde Binaria", None))
        self.cb_imgBin_3.setItemText(3, QCoreApplication.translate("sim_U4_T3", u"Azul Binaria", None))
        self.cb_imgBin_3.setItemText(4, QCoreApplication.translate("sim_U4_T3", u"NOT Rojo Binaria", None))
        self.cb_imgBin_3.setItemText(5, QCoreApplication.translate("sim_U4_T3", u"NOT Verde Binaria", None))
        self.cb_imgBin_3.setItemText(6, QCoreApplication.translate("sim_U4_T3", u"NOT Azul Binaria", None))

        self.label_6.setText(QCoreApplication.translate("sim_U4_T3", u"Azul >10% Binaria", None))
        self.label_4.setText(QCoreApplication.translate("sim_U4_T3", u"Rojo >50% Binaria", None))
        self.label_5.setText(QCoreApplication.translate("sim_U4_T3", u"Verde >50% Binaria", None))
        self.label_8.setText(QCoreApplication.translate("sim_U4_T3", u"NOT Rojo >50% Binaria", None))
        self.label_10.setText(QCoreApplication.translate("sim_U4_T3", u"NOT Verde >50% Binaria", None))
        self.label_11.setText(QCoreApplication.translate("sim_U4_T3", u"NOT Azul >10% Binaria", None))
    # retranslateUi

