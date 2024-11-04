# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sim_U3_T5jJRguW.ui'
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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QHBoxLayout, QLabel,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

from clases.PlotWidget import CustomPlotWidget

class Ui_sim_U3_T5(object):
    def setupUi(self, sim_U3_T5):
        if not sim_U3_T5.objectName():
            sim_U3_T5.setObjectName(u"sim_U3_T5")
        sim_U3_T5.resize(695, 549)
        sim_U3_T5.setStyleSheet(u"QWidget#sim_U3_T5{\n"
"background-color:rgba(0,0,0,0);\n"
"}")
        self.verticalLayout = QVBoxLayout(sim_U3_T5)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(sim_U3_T5)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 693, 241))
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

        self.sb_Je = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.sb_Je.setObjectName(u"sb_Je")
        self.sb_Je.setMaximum(999.990000000000009)
        self.sb_Je.setSingleStep(0.100000000000000)
        self.sb_Je.setValue(1.100000000000000)

        self.horizontalLayout.addWidget(self.sb_Je)

        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_3)

        self.sb_Be = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.sb_Be.setObjectName(u"sb_Be")
        self.sb_Be.setMaximum(999.990000000000009)
        self.sb_Be.setSingleStep(0.100000000000000)
        self.sb_Be.setValue(9.000000000000000)

        self.horizontalLayout.addWidget(self.sb_Be)

        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_4)

        self.sb_Ke = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.sb_Ke.setObjectName(u"sb_Ke")
        self.sb_Ke.setMaximum(999.990000000000009)
        self.sb_Ke.setSingleStep(0.100000000000000)
        self.sb_Ke.setValue(1.050000000000000)

        self.horizontalLayout.addWidget(self.sb_Ke)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_5)

        self.sb_Kp = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.sb_Kp.setObjectName(u"sb_Kp")
        self.sb_Kp.setDecimals(3)
        self.sb_Kp.setMaximum(999.990000000000009)
        self.sb_Kp.setValue(10.000000000000000)

        self.horizontalLayout_2.addWidget(self.sb_Kp)

        self.label_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_6)

        self.sb_Ki = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.sb_Ki.setObjectName(u"sb_Ki")
        self.sb_Ki.setDecimals(3)
        self.sb_Ki.setMaximum(999.990000000000009)
        self.sb_Ki.setSingleStep(0.100000000000000)
        self.sb_Ki.setValue(0.300000000000000)

        self.horizontalLayout_2.addWidget(self.sb_Ki)

        self.label_7 = QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_7)

        self.sb_Kd = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.sb_Kd.setObjectName(u"sb_Kd")
        self.sb_Kd.setDecimals(3)
        self.sb_Kd.setMaximum(999.990000000000009)
        self.sb_Kd.setSingleStep(0.100000000000000)
        self.sb_Kd.setValue(0.500000000000000)

        self.horizontalLayout_2.addWidget(self.sb_Kd)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.bt_pertOn = QPushButton(self.scrollAreaWidgetContents)
        self.bt_pertOn.setObjectName(u"bt_pertOn")

        self.horizontalLayout_3.addWidget(self.bt_pertOn)

        self.bt_pertOff = QPushButton(self.scrollAreaWidgetContents)
        self.bt_pertOff.setObjectName(u"bt_pertOff")

        self.horizontalLayout_3.addWidget(self.bt_pertOff)

        self.label_8 = QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_8)

        self.sb_aPert = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.sb_aPert.setObjectName(u"sb_aPert")
        self.sb_aPert.setValue(5.000000000000000)

        self.horizontalLayout_3.addWidget(self.sb_aPert)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.cp_1 = CustomPlotWidget(self.scrollAreaWidgetContents)
        self.cp_1.setObjectName(u"cp_1")
        self.cp_1.setMinimumSize(QSize(0, 50))

        self.verticalLayout_2.addWidget(self.cp_1)

        self.cp_2 = CustomPlotWidget(self.scrollAreaWidgetContents)
        self.cp_2.setObjectName(u"cp_2")
        self.cp_2.setMinimumSize(QSize(0, 50))

        self.verticalLayout_2.addWidget(self.cp_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(sim_U3_T5)

        QMetaObject.connectSlotsByName(sim_U3_T5)
    # setupUi

    def retranslateUi(self, sim_U3_T5):
        sim_U3_T5.setWindowTitle(QCoreApplication.translate("sim_U3_T5", u"Sim_U3_T5", None))
        self.label.setText(QCoreApplication.translate("sim_U3_T5", u"Control Prealimentado y Realimentado", None))
        self.label_2.setText(QCoreApplication.translate("sim_U3_T5", u"Inercia estimada (Je)", None))
        self.label_3.setText(QCoreApplication.translate("sim_U3_T5", u"Amortiguamiento estimado (Be)", None))
        self.label_4.setText(QCoreApplication.translate("sim_U3_T5", u"Constante del motor estimada (Ke)", None))
        self.label_5.setText(QCoreApplication.translate("sim_U3_T5", u"Constante proporcional (Kp)", None))
        self.label_6.setText(QCoreApplication.translate("sim_U3_T5", u"Constante integral (Ki)", None))
        self.label_7.setText(QCoreApplication.translate("sim_U3_T5", u"Constante derivativa (Kd)", None))
        self.bt_pertOn.setText(QCoreApplication.translate("sim_U3_T5", u"Con perturbaci\u00f3n", None))
        self.bt_pertOff.setText(QCoreApplication.translate("sim_U3_T5", u"Sin perturbaci\u00f3n", None))
        self.label_8.setText(QCoreApplication.translate("sim_U3_T5", u"Amplitud de perturbaci\u00f3n", None))
    # retranslateUi

