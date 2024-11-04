# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sim_U2_T2unLaHN.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QGridLayout,
    QHBoxLayout, QLabel, QLayout, QPushButton,
    QScrollArea, QSizePolicy, QSlider, QSpinBox,
    QVBoxLayout, QWidget)

from clases.PlotWidget import CustomPlotWidget

class Ui_sim_U2_T2(object):
    def setupUi(self, sim_U2_T2):
        if not sim_U2_T2.objectName():
            sim_U2_T2.setObjectName(u"sim_U2_T2")
        sim_U2_T2.resize(660, 581)
        sim_U2_T2.setStyleSheet(u"QWidget#sim_U2_T2{\n"
"background-color:rgba(0,0,0,0);\n"
"}")
        self.verticalLayout = QVBoxLayout(sim_U2_T2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(sim_U2_T2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 658, 451))
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
"QSlider::handle:horizontal {\n"
"background: qlineargradient(spread:pad, x1:0.505, y1:0, x2:0.500318, y2:1, stop:0 rgba(0, 74, 148, 255), stop:1 rgba(0, 37, 74, 255))\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    /*background: rgba(173, 51, 51,255);*/\n"
"background: qlineargradient(spread:pad, x1:0.506, y1:0, x2:0.506, y2:1, stop:0 rgba(203, 60, 60, 255), stop:1 rgba(150, 44, 44, 255))\n"
"}\n"
"QSpinBox{\n"
"color:white;\n"
"background-color:black;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_7)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)

        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)

        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.sb_q1Min = QSpinBox(self.scrollAreaWidgetContents)
        self.sb_q1Min.setObjectName(u"sb_q1Min")
        self.sb_q1Min.setAlignment(Qt.AlignCenter)
        self.sb_q1Min.setReadOnly(True)
        self.sb_q1Min.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sb_q1Min.setKeyboardTracking(True)
        self.sb_q1Min.setMinimum(-180)
        self.sb_q1Min.setMaximum(180)

        self.horizontalLayout_2.addWidget(self.sb_q1Min)

        self.sl_q1Min = QSlider(self.scrollAreaWidgetContents)
        self.sl_q1Min.setObjectName(u"sl_q1Min")
        self.sl_q1Min.setMinimum(-180)
        self.sl_q1Min.setMaximum(180)
        self.sl_q1Min.setOrientation(Qt.Horizontal)

        self.horizontalLayout_2.addWidget(self.sl_q1Min)


        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 1, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.sb_q1Max = QSpinBox(self.scrollAreaWidgetContents)
        self.sb_q1Max.setObjectName(u"sb_q1Max")
        self.sb_q1Max.setAlignment(Qt.AlignCenter)
        self.sb_q1Max.setReadOnly(True)
        self.sb_q1Max.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sb_q1Max.setKeyboardTracking(True)
        self.sb_q1Max.setMinimum(-180)
        self.sb_q1Max.setMaximum(180)

        self.horizontalLayout_3.addWidget(self.sb_q1Max)

        self.sl_q1Max = QSlider(self.scrollAreaWidgetContents)
        self.sl_q1Max.setObjectName(u"sl_q1Max")
        self.sl_q1Max.setMinimum(-180)
        self.sl_q1Max.setMaximum(180)
        self.sl_q1Max.setOrientation(Qt.Horizontal)

        self.horizontalLayout_3.addWidget(self.sl_q1Max)


        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 2, 1, 1)

        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.sb_q2Min = QSpinBox(self.scrollAreaWidgetContents)
        self.sb_q2Min.setObjectName(u"sb_q2Min")
        self.sb_q2Min.setAlignment(Qt.AlignCenter)
        self.sb_q2Min.setReadOnly(True)
        self.sb_q2Min.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sb_q2Min.setKeyboardTracking(True)
        self.sb_q2Min.setMaximum(280)

        self.horizontalLayout_4.addWidget(self.sb_q2Min)

        self.sl_q2Min = QSlider(self.scrollAreaWidgetContents)
        self.sl_q2Min.setObjectName(u"sl_q2Min")
        self.sl_q2Min.setMaximum(280)
        self.sl_q2Min.setOrientation(Qt.Horizontal)

        self.horizontalLayout_4.addWidget(self.sl_q2Min)


        self.gridLayout.addLayout(self.horizontalLayout_4, 2, 1, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.sb_q2Max = QSpinBox(self.scrollAreaWidgetContents)
        self.sb_q2Max.setObjectName(u"sb_q2Max")
        self.sb_q2Max.setAlignment(Qt.AlignCenter)
        self.sb_q2Max.setReadOnly(True)
        self.sb_q2Max.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sb_q2Max.setKeyboardTracking(True)
        self.sb_q2Max.setMaximum(280)

        self.horizontalLayout_5.addWidget(self.sb_q2Max)

        self.sl_q2Max = QSlider(self.scrollAreaWidgetContents)
        self.sl_q2Max.setObjectName(u"sl_q2Max")
        self.sl_q2Max.setMaximum(280)
        self.sl_q2Max.setOrientation(Qt.Horizontal)

        self.horizontalLayout_5.addWidget(self.sl_q2Max)


        self.gridLayout.addLayout(self.horizontalLayout_5, 2, 2, 1, 1)

        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.sb_q3Min = QSpinBox(self.scrollAreaWidgetContents)
        self.sb_q3Min.setObjectName(u"sb_q3Min")
        self.sb_q3Min.setAlignment(Qt.AlignCenter)
        self.sb_q3Min.setReadOnly(True)
        self.sb_q3Min.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sb_q3Min.setKeyboardTracking(True)
        self.sb_q3Min.setMaximum(420)

        self.horizontalLayout_6.addWidget(self.sb_q3Min)

        self.sl_q3Min = QSlider(self.scrollAreaWidgetContents)
        self.sl_q3Min.setObjectName(u"sl_q3Min")
        self.sl_q3Min.setMaximum(420)
        self.sl_q3Min.setOrientation(Qt.Horizontal)

        self.horizontalLayout_6.addWidget(self.sl_q3Min)


        self.gridLayout.addLayout(self.horizontalLayout_6, 3, 1, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.sb_q3Max = QSpinBox(self.scrollAreaWidgetContents)
        self.sb_q3Max.setObjectName(u"sb_q3Max")
        self.sb_q3Max.setAlignment(Qt.AlignCenter)
        self.sb_q3Max.setReadOnly(True)
        self.sb_q3Max.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sb_q3Max.setKeyboardTracking(True)
        self.sb_q3Max.setMaximum(420)

        self.horizontalLayout_7.addWidget(self.sb_q3Max)

        self.sl_q3Max = QSlider(self.scrollAreaWidgetContents)
        self.sl_q3Max.setObjectName(u"sl_q3Max")
        self.sl_q3Max.setMaximum(420)
        self.sl_q3Max.setOrientation(Qt.Horizontal)

        self.horizontalLayout_7.addWidget(self.sl_q3Max)


        self.gridLayout.addLayout(self.horizontalLayout_7, 3, 2, 1, 1)

        self.label_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.sb_q4Min = QSpinBox(self.scrollAreaWidgetContents)
        self.sb_q4Min.setObjectName(u"sb_q4Min")
        self.sb_q4Min.setAlignment(Qt.AlignCenter)
        self.sb_q4Min.setReadOnly(True)
        self.sb_q4Min.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sb_q4Min.setKeyboardTracking(True)
        self.sb_q4Min.setMinimum(-180)
        self.sb_q4Min.setMaximum(180)

        self.horizontalLayout_8.addWidget(self.sb_q4Min)

        self.sl_q4Min = QSlider(self.scrollAreaWidgetContents)
        self.sl_q4Min.setObjectName(u"sl_q4Min")
        self.sl_q4Min.setMinimum(-180)
        self.sl_q4Min.setMaximum(180)
        self.sl_q4Min.setOrientation(Qt.Horizontal)

        self.horizontalLayout_8.addWidget(self.sl_q4Min)


        self.gridLayout.addLayout(self.horizontalLayout_8, 4, 1, 1, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.sb_q4Max = QSpinBox(self.scrollAreaWidgetContents)
        self.sb_q4Max.setObjectName(u"sb_q4Max")
        self.sb_q4Max.setAlignment(Qt.AlignCenter)
        self.sb_q4Max.setReadOnly(True)
        self.sb_q4Max.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sb_q4Max.setKeyboardTracking(True)
        self.sb_q4Max.setMinimum(-180)
        self.sb_q4Max.setMaximum(180)

        self.horizontalLayout_9.addWidget(self.sb_q4Max)

        self.sl_q4Max = QSlider(self.scrollAreaWidgetContents)
        self.sl_q4Max.setObjectName(u"sl_q4Max")
        self.sl_q4Max.setMinimum(-180)
        self.sl_q4Max.setMaximum(180)
        self.sl_q4Max.setOrientation(Qt.Horizontal)

        self.horizontalLayout_9.addWidget(self.sl_q4Max)


        self.gridLayout.addLayout(self.horizontalLayout_9, 4, 2, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_8 = QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_8)

        self.cb_tiposMovimiento = QComboBox(self.scrollAreaWidgetContents)
        self.cb_tiposMovimiento.addItem("")
        self.cb_tiposMovimiento.addItem("")
        self.cb_tiposMovimiento.addItem("")
        self.cb_tiposMovimiento.setObjectName(u"cb_tiposMovimiento")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.cb_tiposMovimiento.sizePolicy().hasHeightForWidth())
        self.cb_tiposMovimiento.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.cb_tiposMovimiento)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.bt_CalcularTrayectoria = QPushButton(self.scrollAreaWidgetContents)
        self.bt_CalcularTrayectoria.setObjectName(u"bt_CalcularTrayectoria")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.bt_CalcularTrayectoria.sizePolicy().hasHeightForWidth())
        self.bt_CalcularTrayectoria.setSizePolicy(sizePolicy2)

        self.verticalLayout_2.addWidget(self.bt_CalcularTrayectoria)

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


        self.retranslateUi(sim_U2_T2)

        QMetaObject.connectSlotsByName(sim_U2_T2)
    # setupUi

    def retranslateUi(self, sim_U2_T2):
        sim_U2_T2.setWindowTitle(QCoreApplication.translate("sim_U2_T2", u"Sim_U2_T2", None))
        self.label_7.setText(QCoreApplication.translate("sim_U2_T2", u"Trayectorias Punto a Punto", None))
        self.label_2.setText(QCoreApplication.translate("sim_U2_T2", u"Posici\u00f3n Inicial", None))
        self.label_3.setText(QCoreApplication.translate("sim_U2_T2", u"Posici\u00f3n Final", None))
        self.label.setText(QCoreApplication.translate("sim_U2_T2", u"q1", None))
        self.sb_q1Min.setSpecialValueText("")
        self.sb_q1Min.setSuffix(QCoreApplication.translate("sim_U2_T2", u"\u00b0", None))
        self.sb_q1Max.setSpecialValueText("")
        self.sb_q1Max.setSuffix(QCoreApplication.translate("sim_U2_T2", u"\u00b0", None))
        self.label_4.setText(QCoreApplication.translate("sim_U2_T2", u"q2", None))
        self.sb_q2Min.setSpecialValueText("")
        self.sb_q2Min.setSuffix(QCoreApplication.translate("sim_U2_T2", u" cm", None))
        self.sb_q2Max.setSpecialValueText("")
        self.sb_q2Max.setSuffix(QCoreApplication.translate("sim_U2_T2", u" cm", None))
        self.label_5.setText(QCoreApplication.translate("sim_U2_T2", u"q3", None))
        self.sb_q3Min.setSpecialValueText("")
        self.sb_q3Min.setSuffix(QCoreApplication.translate("sim_U2_T2", u" cm", None))
        self.sb_q3Max.setSpecialValueText("")
        self.sb_q3Max.setSuffix(QCoreApplication.translate("sim_U2_T2", u" cm", None))
        self.label_6.setText(QCoreApplication.translate("sim_U2_T2", u"q4", None))
        self.sb_q4Min.setSpecialValueText("")
        self.sb_q4Min.setSuffix(QCoreApplication.translate("sim_U2_T2", u"\u00b0", None))
        self.sb_q4Max.setSpecialValueText("")
        self.sb_q4Max.setSuffix(QCoreApplication.translate("sim_U2_T2", u"\u00b0", None))
        self.label_8.setText(QCoreApplication.translate("sim_U2_T2", u"Tipo de Movimiento", None))
        self.cb_tiposMovimiento.setItemText(0, QCoreApplication.translate("sim_U2_T2", u"Movimiento Eje a Eje", None))
        self.cb_tiposMovimiento.setItemText(1, QCoreApplication.translate("sim_U2_T2", u"Movimiento Simultaneo", None))
        self.cb_tiposMovimiento.setItemText(2, QCoreApplication.translate("sim_U2_T2", u"Movimiento Coordinado o Isocrono", None))

        self.bt_CalcularTrayectoria.setText(QCoreApplication.translate("sim_U2_T2", u"Calcular Trayectoria", None))
    # retranslateUi

