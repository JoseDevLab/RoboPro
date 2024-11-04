# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sim_U3_T3nnGIPM.ui'
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

class Ui_sim_U3_T3(object):
    def setupUi(self, sim_U3_T3):
        if not sim_U3_T3.objectName():
            sim_U3_T3.setObjectName(u"sim_U3_T3")
        sim_U3_T3.resize(560, 412)
        sim_U3_T3.setStyleSheet(u"QWidget#sim_U3_T3{\n"
"background-color:rgba(0,0,0,0);\n"
"}")
        self.verticalLayout = QVBoxLayout(sim_U3_T3)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(sim_U3_T3)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 569, 169))
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

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.sb_Je = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.sb_Je.setObjectName(u"sb_Je")
        self.sb_Je.setSingleStep(0.100000000000000)
        self.sb_Je.setValue(1.000000000000000)

        self.horizontalLayout_3.addWidget(self.sb_Je)

        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_4)

        self.sb_Be = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.sb_Be.setObjectName(u"sb_Be")
        self.sb_Be.setSingleStep(0.100000000000000)
        self.sb_Be.setValue(10.000000000000000)

        self.horizontalLayout_3.addWidget(self.sb_Be)

        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_5)

        self.sb_Ke = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.sb_Ke.setObjectName(u"sb_Ke")
        self.sb_Ke.setSingleStep(0.100000000000000)
        self.sb_Ke.setValue(1.000000000000000)

        self.horizontalLayout_3.addWidget(self.sb_Ke)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.bt_pertOn = QPushButton(self.scrollAreaWidgetContents)
        self.bt_pertOn.setObjectName(u"bt_pertOn")

        self.horizontalLayout_2.addWidget(self.bt_pertOn)

        self.bt_pertOff = QPushButton(self.scrollAreaWidgetContents)
        self.bt_pertOff.setObjectName(u"bt_pertOff")

        self.horizontalLayout_2.addWidget(self.bt_pertOff)

        self.widget = QWidget(self.scrollAreaWidgetContents)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_2)

        self.sb_amplitud = QDoubleSpinBox(self.widget)
        self.sb_amplitud.setObjectName(u"sb_amplitud")
        self.sb_amplitud.setSingleStep(0.100000000000000)
        self.sb_amplitud.setValue(1.000000000000000)

        self.horizontalLayout.addWidget(self.sb_amplitud)


        self.horizontalLayout_2.addWidget(self.widget)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.cp = CustomPlotWidget(self.scrollAreaWidgetContents)
        self.cp.setObjectName(u"cp")
        self.cp.setMinimumSize(QSize(0, 50))

        self.verticalLayout_2.addWidget(self.cp)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(sim_U3_T3)

        QMetaObject.connectSlotsByName(sim_U3_T3)
    # setupUi

    def retranslateUi(self, sim_U3_T3):
        sim_U3_T3.setWindowTitle(QCoreApplication.translate("sim_U3_T3", u"Sim_U3_T3", None))
        self.label.setText(QCoreApplication.translate("sim_U3_T3", u"Control Prealimentado", None))
        self.label_3.setText(QCoreApplication.translate("sim_U3_T3", u"Inercia estimada (Je)", None))
        self.label_4.setText(QCoreApplication.translate("sim_U3_T3", u"Coeficiente de fricci\u00f3n\n"
"estimado (Be)", None))
        self.label_5.setText(QCoreApplication.translate("sim_U3_T3", u"Constante del motor\n"
"estimada (Ke)", None))
        self.bt_pertOn.setText(QCoreApplication.translate("sim_U3_T3", u"Con perturbaci\u00f3n", None))
        self.bt_pertOff.setText(QCoreApplication.translate("sim_U3_T3", u"Sin perturbaci\u00f3n", None))
        self.label_2.setText(QCoreApplication.translate("sim_U3_T3", u"Amplitud de perturbaci\u00f3n", None))
    # retranslateUi

