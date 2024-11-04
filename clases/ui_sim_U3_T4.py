# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sim_U3_T4OgtwaN.ui'
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

class Ui_sim_U3_T4(object):
    def setupUi(self, sim_U3_T4):
        if not sim_U3_T4.objectName():
            sim_U3_T4.setObjectName(u"sim_U3_T4")
        sim_U3_T4.resize(624, 493)
        sim_U3_T4.setStyleSheet(u"QWidget#sim_U3_T4{\n"
"background-color:rgba(0,0,0,0);\n"
"}")
        self.verticalLayout = QVBoxLayout(sim_U3_T4)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(sim_U3_T4)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(-144, 0, 772, 157))
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

        self.horizontalLayout.addWidget(self.label_2)

        self.sb_ref = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.sb_ref.setObjectName(u"sb_ref")
        self.sb_ref.setDecimals(3)
        self.sb_ref.setMinimum(-99.989999999999995)
        self.sb_ref.setSingleStep(0.100000000000000)
        self.sb_ref.setValue(1.000000000000000)

        self.horizontalLayout.addWidget(self.sb_ref)

        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.sb_Kp = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.sb_Kp.setObjectName(u"sb_Kp")
        self.sb_Kp.setDecimals(3)
        self.sb_Kp.setSingleStep(0.100000000000000)
        self.sb_Kp.setValue(1.000000000000000)

        self.horizontalLayout.addWidget(self.sb_Kp)

        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4)

        self.sb_Ki = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.sb_Ki.setObjectName(u"sb_Ki")
        self.sb_Ki.setDecimals(3)
        self.sb_Ki.setSingleStep(0.010000000000000)
        self.sb_Ki.setValue(0.030000000000000)

        self.horizontalLayout.addWidget(self.sb_Ki)

        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout.addWidget(self.label_5)

        self.sb_Kd = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.sb_Kd.setObjectName(u"sb_Kd")
        self.sb_Kd.setDecimals(3)
        self.sb_Kd.setSingleStep(0.010000000000000)
        self.sb_Kd.setValue(0.200000000000000)

        self.horizontalLayout.addWidget(self.sb_Kd)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.bt_perturbOn = QPushButton(self.scrollAreaWidgetContents)
        self.bt_perturbOn.setObjectName(u"bt_perturbOn")

        self.horizontalLayout_2.addWidget(self.bt_perturbOn)

        self.bt_perturbOff = QPushButton(self.scrollAreaWidgetContents)
        self.bt_perturbOff.setObjectName(u"bt_perturbOff")

        self.horizontalLayout_2.addWidget(self.bt_perturbOff)

        self.label_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_2.addWidget(self.label_6)

        self.sb_tPerturb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.sb_tPerturb.setObjectName(u"sb_tPerturb")
        self.sb_tPerturb.setMinimum(1.000000000000000)
        self.sb_tPerturb.setMaximum(250.000000000000000)
        self.sb_tPerturb.setSingleStep(5.000000000000000)
        self.sb_tPerturb.setValue(100.000000000000000)

        self.horizontalLayout_2.addWidget(self.sb_tPerturb)

        self.label_7 = QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_2.addWidget(self.label_7)

        self.sb_aPerturb = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.sb_aPerturb.setObjectName(u"sb_aPerturb")
        self.sb_aPerturb.setDecimals(3)
        self.sb_aPerturb.setSingleStep(0.100000000000000)
        self.sb_aPerturb.setValue(1.000000000000000)

        self.horizontalLayout_2.addWidget(self.sb_aPerturb)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.cp = CustomPlotWidget(self.scrollAreaWidgetContents)
        self.cp.setObjectName(u"cp")
        self.cp.setMinimumSize(QSize(0, 50))

        self.verticalLayout_2.addWidget(self.cp)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(sim_U3_T4)

        QMetaObject.connectSlotsByName(sim_U3_T4)
    # setupUi

    def retranslateUi(self, sim_U3_T4):
        sim_U3_T4.setWindowTitle(QCoreApplication.translate("sim_U3_T4", u"Sim_U3_T4", None))
        self.label.setText(QCoreApplication.translate("sim_U3_T4", u"Control Realimentado", None))
        self.label_2.setText(QCoreApplication.translate("sim_U3_T4", u"Referencia", None))
        self.label_3.setText(QCoreApplication.translate("sim_U3_T4", u"Kp", None))
        self.label_4.setText(QCoreApplication.translate("sim_U3_T4", u"Ki", None))
        self.label_5.setText(QCoreApplication.translate("sim_U3_T4", u"Kd", None))
        self.bt_perturbOn.setText(QCoreApplication.translate("sim_U3_T4", u"Con perturbaci\u00f3n", None))
        self.bt_perturbOff.setText(QCoreApplication.translate("sim_U3_T4", u"Sin perturbaci\u00f3n", None))
        self.label_6.setText(QCoreApplication.translate("sim_U3_T4", u"Tiempo de perturbaci\u00f3n", None))
        self.label_7.setText(QCoreApplication.translate("sim_U3_T4", u"Magnitud de perturbaci\u00f3n", None))
    # retranslateUi

