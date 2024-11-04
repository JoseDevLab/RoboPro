# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sim_U2_T3AEDhrG.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QSpinBox,
    QVBoxLayout, QWidget)

from clases.CustomTable import CustomTable
from clases.PlotWidget import CustomPlotWidget

class Ui_sim_U2_T3(object):
    def setupUi(self, sim_U2_T3):
        if not sim_U2_T3.objectName():
            sim_U2_T3.setObjectName(u"sim_U2_T3")
        sim_U2_T3.resize(585, 492)
        sim_U2_T3.setStyleSheet(u"QWidget#sim_U2_T3{\n"
"background-color:rgba(0,0,0,0);\n"
"}")
        self.verticalLayout = QVBoxLayout(sim_U2_T3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(sim_U2_T3)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 566, 563))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setStyleSheet(u"QWidget#scrollAreaWidgetContents{\n"
"background-color:rgb(0,0,0);\n"
"}\n"
"QScrollArea#scrollArea_2 QWidget#scrollAreaWidgetContents_2{\n"
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
"QTableWidget::item:selected {\n"
"background-color: rgb(0,51,112);\n"
"}\n"
"QTableWidget QWidget{\n"
"background-color: rgb(173,51,51);\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_2)

        self.sb_nPuntos = QSpinBox(self.scrollAreaWidgetContents)
        self.sb_nPuntos.setObjectName(u"sb_nPuntos")
        self.sb_nPuntos.setMinimum(2)
        self.sb_nPuntos.setValue(7)

        self.horizontalLayout.addWidget(self.sb_nPuntos)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.scrollArea_2 = QScrollArea(self.scrollAreaWidgetContents)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setMinimumSize(QSize(0, 234))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 546, 232))
        self.horizontalLayout_2 = QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(239, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.ct_puntos = CustomTable(self.scrollAreaWidgetContents_2)
        self.ct_puntos.setObjectName(u"ct_puntos")
        self.ct_puntos.setMinimumSize(QSize(50, 50))

        self.horizontalLayout_2.addWidget(self.ct_puntos)

        self.horizontalSpacer_4 = QSpacerItem(239, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_2.addWidget(self.scrollArea_2)

        self.bt_calcularTrayectoria = QPushButton(self.scrollAreaWidgetContents)
        self.bt_calcularTrayectoria.setObjectName(u"bt_calcularTrayectoria")

        self.verticalLayout_2.addWidget(self.bt_calcularTrayectoria)

        self.cp_q_1 = CustomPlotWidget(self.scrollAreaWidgetContents)
        self.cp_q_1.setObjectName(u"cp_q_1")
        self.cp_q_1.setMinimumSize(QSize(0, 50))

        self.verticalLayout_2.addWidget(self.cp_q_1)

        self.cp_q_2 = CustomPlotWidget(self.scrollAreaWidgetContents)
        self.cp_q_2.setObjectName(u"cp_q_2")
        self.cp_q_2.setMinimumSize(QSize(0, 50))

        self.verticalLayout_2.addWidget(self.cp_q_2)

        self.cp_q_3 = CustomPlotWidget(self.scrollAreaWidgetContents)
        self.cp_q_3.setObjectName(u"cp_q_3")
        self.cp_q_3.setMinimumSize(QSize(0, 50))

        self.verticalLayout_2.addWidget(self.cp_q_3)

        self.cp_q_4 = CustomPlotWidget(self.scrollAreaWidgetContents)
        self.cp_q_4.setObjectName(u"cp_q_4")
        self.cp_q_4.setMinimumSize(QSize(0, 50))

        self.verticalLayout_2.addWidget(self.cp_q_4)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(sim_U2_T3)

        QMetaObject.connectSlotsByName(sim_U2_T3)
    # setupUi

    def retranslateUi(self, sim_U2_T3):
        sim_U2_T3.setWindowTitle(QCoreApplication.translate("sim_U2_T3", u"Sim_U2_T3", None))
        self.label.setText(QCoreApplication.translate("sim_U2_T3", u"Trayectorias Continuas", None))
        self.label_2.setText(QCoreApplication.translate("sim_U2_T3", u"Cantidad de Puntos", None))
        self.bt_calcularTrayectoria.setText(QCoreApplication.translate("sim_U2_T3", u"Calcular Trayectoria", None))
    # retranslateUi

