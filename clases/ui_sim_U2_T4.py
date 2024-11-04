# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sim_U2_T4QJKttb.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

from clases.CustomTable import CustomTable
from clases.GLView import GLView
from clases.PlotWidget import CustomPlotWidget

class Ui_sim_U2_T4(object):
    def setupUi(self, sim_U2_T4):
        if not sim_U2_T4.objectName():
            sim_U2_T4.setObjectName(u"sim_U2_T4")
        sim_U2_T4.resize(568, 619)
        sim_U2_T4.setStyleSheet(u"QWidget#sim_U2_T4{\n"
"background-color:rgba(0,0,0,0);\n"
"}")
        self.verticalLayout = QVBoxLayout(sim_U2_T4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(sim_U2_T4)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 566, 617))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
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
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 5)

        self.horizontalSpacer_2 = QSpacerItem(79, 238, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 0, 4, 1)

        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)

        self.label_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_6, 1, 2, 1, 1)

        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 1, 3, 1, 1)

        self.ct_orientacionIni = CustomTable(self.scrollAreaWidgetContents)
        self.ct_orientacionIni.setObjectName(u"ct_orientacionIni")
        self.ct_orientacionIni.setMinimumSize(QSize(0, 50))

        self.gridLayout.addWidget(self.ct_orientacionIni, 2, 1, 1, 1)

        self.cb_angulosEuler = QComboBox(self.scrollAreaWidgetContents)
        self.cb_angulosEuler.addItem("")
        self.cb_angulosEuler.addItem("")
        self.cb_angulosEuler.setObjectName(u"cb_angulosEuler")
        sizePolicy.setHeightForWidth(self.cb_angulosEuler.sizePolicy().hasHeightForWidth())
        self.cb_angulosEuler.setSizePolicy(sizePolicy)
        self.cb_angulosEuler.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)

        self.gridLayout.addWidget(self.cb_angulosEuler, 2, 2, 1, 1)

        self.ct_orientacionFin = CustomTable(self.scrollAreaWidgetContents)
        self.ct_orientacionFin.setObjectName(u"ct_orientacionFin")
        self.ct_orientacionFin.setMinimumSize(QSize(0, 50))

        self.gridLayout.addWidget(self.ct_orientacionFin, 2, 3, 1, 1)

        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 3, 1, 1, 1)

        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_5, 3, 3, 1, 1)

        self.ct_matrizIni = CustomTable(self.scrollAreaWidgetContents)
        self.ct_matrizIni.setObjectName(u"ct_matrizIni")
        self.ct_matrizIni.setMinimumSize(QSize(0, 50))

        self.gridLayout.addWidget(self.ct_matrizIni, 4, 1, 1, 1)

        self.bt_interpolarEuler = QPushButton(self.scrollAreaWidgetContents)
        self.bt_interpolarEuler.setObjectName(u"bt_interpolarEuler")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.bt_interpolarEuler.sizePolicy().hasHeightForWidth())
        self.bt_interpolarEuler.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.bt_interpolarEuler, 4, 2, 1, 1)

        self.cp_1 = CustomPlotWidget(self.scrollAreaWidgetContents)
        self.cp_1.setObjectName(u"cp_1")
        self.cp_1.setMinimumSize(QSize(0, 50))

        self.gridLayout.addWidget(self.cp_1, 5, 0, 1, 5)

        self.cp_2 = CustomPlotWidget(self.scrollAreaWidgetContents)
        self.cp_2.setObjectName(u"cp_2")
        self.cp_2.setMinimumSize(QSize(0, 50))

        self.gridLayout.addWidget(self.cp_2, 6, 0, 1, 5)

        self.cp_3 = CustomPlotWidget(self.scrollAreaWidgetContents)
        self.cp_3.setObjectName(u"cp_3")
        self.cp_3.setMinimumSize(QSize(0, 50))

        self.gridLayout.addWidget(self.cp_3, 7, 0, 1, 5)

        self.bt_iniciarAnimacion = QPushButton(self.scrollAreaWidgetContents)
        self.bt_iniciarAnimacion.setObjectName(u"bt_iniciarAnimacion")
        self.bt_iniciarAnimacion.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.bt_iniciarAnimacion.sizePolicy().hasHeightForWidth())
        self.bt_iniciarAnimacion.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.bt_iniciarAnimacion, 8, 0, 1, 5)

        self.gv_1 = GLView(self.scrollAreaWidgetContents)
        self.gv_1.setObjectName(u"gv_1")
        self.gv_1.setMinimumSize(QSize(0, 50))

        self.gridLayout.addWidget(self.gv_1, 9, 0, 1, 5)

        self.ct_matrizFin = CustomTable(self.scrollAreaWidgetContents)
        self.ct_matrizFin.setObjectName(u"ct_matrizFin")
        self.ct_matrizFin.setMinimumSize(QSize(0, 50))

        self.gridLayout.addWidget(self.ct_matrizFin, 4, 3, 1, 1)

        self.horizontalSpacer = QSpacerItem(79, 288, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 4, 4, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(sim_U2_T4)

        QMetaObject.connectSlotsByName(sim_U2_T4)
    # setupUi

    def retranslateUi(self, sim_U2_T4):
        sim_U2_T4.setWindowTitle(QCoreApplication.translate("sim_U2_T4", u"Sim_U2_T4", None))
        self.label.setText(QCoreApplication.translate("sim_U2_T4", u"Evoluci\u00f3n de la Orientaci\u00f3n", None))
        self.label_2.setText(QCoreApplication.translate("sim_U2_T4", u"Orientaci\u00f3n Inicial", None))
        self.label_6.setText(QCoreApplication.translate("sim_U2_T4", u"\u00c1ngulos de Euler", None))
        self.label_3.setText(QCoreApplication.translate("sim_U2_T4", u"Orientaci\u00f3n Final", None))
        self.cb_angulosEuler.setItemText(0, QCoreApplication.translate("sim_U2_T4", u"WUW", None))
        self.cb_angulosEuler.setItemText(1, QCoreApplication.translate("sim_U2_T4", u"WYW", None))

        self.label_4.setText(QCoreApplication.translate("sim_U2_T4", u"Matriz de Rotaci\u00f3n", None))
        self.label_5.setText(QCoreApplication.translate("sim_U2_T4", u"Matriz de Rotaci\u00f3n", None))
        self.bt_interpolarEuler.setText(QCoreApplication.translate("sim_U2_T4", u"Interpolar \n"
"\u00c1ngulos de Euler", None))
        self.bt_iniciarAnimacion.setText(QCoreApplication.translate("sim_U2_T4", u"Iniciar Animaci\u00f3n", None))
    # retranslateUi

