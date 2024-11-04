# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sim_U1_T5KmJWiY.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QDoubleSpinBox, QHBoxLayout,
    QLabel, QPushButton, QScrollArea, QSizePolicy,
    QSlider, QSpacerItem, QSpinBox, QVBoxLayout,
    QWidget)

from clases.GLView import GLView

class Ui_sim_U1_T5(object):
    def setupUi(self, sim_U1_T5):
        if not sim_U1_T5.objectName():
            sim_U1_T5.setObjectName(u"sim_U1_T5")
        sim_U1_T5.resize(683, 606)
        self.verticalLayout = QVBoxLayout(sim_U1_T5)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(sim_U1_T5)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 664, 1095))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setStyleSheet(u"QWidget#scrollAreaWidgetContents{\n"
"background-color:rgba(0,0,0,255);\n"
"}\n"
"QLabel{\n"
"color:white;\n"
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
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font:20pt \"Britannic Bold\";")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.sb_q1 = QSpinBox(self.scrollAreaWidgetContents)
        self.sb_q1.setObjectName(u"sb_q1")
        self.sb_q1.setMinimumSize(QSize(25, 0))
        self.sb_q1.setWrapping(False)
        self.sb_q1.setFrame(True)
        self.sb_q1.setAlignment(Qt.AlignCenter)
        self.sb_q1.setReadOnly(True)
        self.sb_q1.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sb_q1.setAccelerated(False)
        self.sb_q1.setKeyboardTracking(False)
        self.sb_q1.setProperty("showGroupSeparator", False)
        self.sb_q1.setMinimum(-999)
        self.sb_q1.setMaximum(999)

        self.horizontalLayout_2.addWidget(self.sb_q1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.sl_q1_1 = QSlider(self.scrollAreaWidgetContents)
        self.sl_q1_1.setObjectName(u"sl_q1_1")
        self.sl_q1_1.setMinimum(-360)
        self.sl_q1_1.setMaximum(360)
        self.sl_q1_1.setSingleStep(20)
        self.sl_q1_1.setPageStep(45)
        self.sl_q1_1.setOrientation(Qt.Horizontal)

        self.verticalLayout_2.addWidget(self.sl_q1_1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.sb_q2 = QSpinBox(self.scrollAreaWidgetContents)
        self.sb_q2.setObjectName(u"sb_q2")
        self.sb_q2.setMinimumSize(QSize(25, 0))
        self.sb_q2.setWrapping(False)
        self.sb_q2.setFrame(True)
        self.sb_q2.setAlignment(Qt.AlignCenter)
        self.sb_q2.setReadOnly(True)
        self.sb_q2.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sb_q2.setAccelerated(False)
        self.sb_q2.setKeyboardTracking(False)
        self.sb_q2.setProperty("showGroupSeparator", False)
        self.sb_q2.setMinimum(-999)
        self.sb_q2.setMaximum(999)

        self.horizontalLayout_4.addWidget(self.sb_q2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.sl_q2_1 = QSlider(self.scrollAreaWidgetContents)
        self.sl_q2_1.setObjectName(u"sl_q2_1")
        self.sl_q2_1.setMaximum(280)
        self.sl_q2_1.setSingleStep(40)
        self.sl_q2_1.setPageStep(40)
        self.sl_q2_1.setOrientation(Qt.Horizontal)

        self.verticalLayout_2.addWidget(self.sl_q2_1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_6.addWidget(self.label_4)

        self.sb_q3 = QSpinBox(self.scrollAreaWidgetContents)
        self.sb_q3.setObjectName(u"sb_q3")
        self.sb_q3.setMinimumSize(QSize(25, 0))
        self.sb_q3.setWrapping(False)
        self.sb_q3.setFrame(True)
        self.sb_q3.setAlignment(Qt.AlignCenter)
        self.sb_q3.setReadOnly(True)
        self.sb_q3.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sb_q3.setAccelerated(False)
        self.sb_q3.setKeyboardTracking(False)
        self.sb_q3.setProperty("showGroupSeparator", False)
        self.sb_q3.setMinimum(-999)
        self.sb_q3.setMaximum(999)

        self.horizontalLayout_6.addWidget(self.sb_q3)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.sl_q3_1 = QSlider(self.scrollAreaWidgetContents)
        self.sl_q3_1.setObjectName(u"sl_q3_1")
        self.sl_q3_1.setMaximum(420)
        self.sl_q3_1.setSingleStep(50)
        self.sl_q3_1.setPageStep(50)
        self.sl_q3_1.setOrientation(Qt.Horizontal)

        self.verticalLayout_2.addWidget(self.sl_q3_1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_7 = QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_8.addWidget(self.label_7)

        self.sb_q4 = QSpinBox(self.scrollAreaWidgetContents)
        self.sb_q4.setObjectName(u"sb_q4")
        self.sb_q4.setMinimumSize(QSize(25, 0))
        self.sb_q4.setWrapping(False)
        self.sb_q4.setFrame(True)
        self.sb_q4.setAlignment(Qt.AlignCenter)
        self.sb_q4.setReadOnly(True)
        self.sb_q4.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sb_q4.setAccelerated(False)
        self.sb_q4.setKeyboardTracking(False)
        self.sb_q4.setProperty("showGroupSeparator", False)
        self.sb_q4.setMinimum(-999)
        self.sb_q4.setMaximum(999)

        self.horizontalLayout_8.addWidget(self.sb_q4)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_7)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.sl_q4_1 = QSlider(self.scrollAreaWidgetContents)
        self.sl_q4_1.setObjectName(u"sl_q4_1")
        self.sl_q4_1.setMinimum(-360)
        self.sl_q4_1.setMaximum(360)
        self.sl_q4_1.setSingleStep(20)
        self.sl_q4_1.setPageStep(45)
        self.sl_q4_1.setOrientation(Qt.Horizontal)

        self.verticalLayout_2.addWidget(self.sl_q4_1)

        self.label_14 = QLabel(self.scrollAreaWidgetContents)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_14)

        self.glView_1 = GLView(self.scrollAreaWidgetContents)
        self.glView_1.setObjectName(u"glView_1")
        self.glView_1.setMinimumSize(QSize(0, 300))
        self.glView_1.setStyleSheet(u"background-color:black;")

        self.verticalLayout_2.addWidget(self.glView_1)

        self.label_16 = QLabel(self.scrollAreaWidgetContents)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_16)

        self.sb_nPuntos = QSpinBox(self.scrollAreaWidgetContents)
        self.sb_nPuntos.setObjectName(u"sb_nPuntos")
        self.sb_nPuntos.setStyleSheet(u"color:white;\n"
"background-color:translucid;")
        self.sb_nPuntos.setMinimum(2)
        self.sb_nPuntos.setMaximum(999)
        self.sb_nPuntos.setSingleStep(10)
        self.sb_nPuntos.setValue(60)

        self.verticalLayout_2.addWidget(self.sb_nPuntos)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_3.addWidget(self.label_5)

        self.sb_q1_2 = QSpinBox(self.scrollAreaWidgetContents)
        self.sb_q1_2.setObjectName(u"sb_q1_2")
        self.sb_q1_2.setMinimumSize(QSize(25, 0))
        self.sb_q1_2.setWrapping(False)
        self.sb_q1_2.setFrame(True)
        self.sb_q1_2.setAlignment(Qt.AlignCenter)
        self.sb_q1_2.setReadOnly(True)
        self.sb_q1_2.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sb_q1_2.setAccelerated(False)
        self.sb_q1_2.setKeyboardTracking(False)
        self.sb_q1_2.setProperty("showGroupSeparator", False)
        self.sb_q1_2.setMinimum(-999)
        self.sb_q1_2.setMaximum(999)

        self.horizontalLayout_3.addWidget(self.sb_q1_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.sl_q1_2 = QSlider(self.scrollAreaWidgetContents)
        self.sl_q1_2.setObjectName(u"sl_q1_2")
        self.sl_q1_2.setMinimum(-360)
        self.sl_q1_2.setMaximum(360)
        self.sl_q1_2.setSingleStep(20)
        self.sl_q1_2.setPageStep(45)
        self.sl_q1_2.setOrientation(Qt.Horizontal)

        self.verticalLayout_3.addWidget(self.sl_q1_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_8 = QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_5.addWidget(self.label_8)

        self.sb_q2_2 = QSpinBox(self.scrollAreaWidgetContents)
        self.sb_q2_2.setObjectName(u"sb_q2_2")
        self.sb_q2_2.setMinimumSize(QSize(25, 0))
        self.sb_q2_2.setWrapping(False)
        self.sb_q2_2.setFrame(True)
        self.sb_q2_2.setAlignment(Qt.AlignCenter)
        self.sb_q2_2.setReadOnly(True)
        self.sb_q2_2.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sb_q2_2.setAccelerated(False)
        self.sb_q2_2.setKeyboardTracking(False)
        self.sb_q2_2.setProperty("showGroupSeparator", False)
        self.sb_q2_2.setMinimum(-999)
        self.sb_q2_2.setMaximum(999)

        self.horizontalLayout_5.addWidget(self.sb_q2_2)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.sl_q2_2 = QSlider(self.scrollAreaWidgetContents)
        self.sl_q2_2.setObjectName(u"sl_q2_2")
        self.sl_q2_2.setMaximum(280)
        self.sl_q2_2.setSingleStep(40)
        self.sl_q2_2.setPageStep(40)
        self.sl_q2_2.setOrientation(Qt.Horizontal)

        self.verticalLayout_3.addWidget(self.sl_q2_2)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_7.addWidget(self.label_6)

        self.sb_q3_2 = QSpinBox(self.scrollAreaWidgetContents)
        self.sb_q3_2.setObjectName(u"sb_q3_2")
        self.sb_q3_2.setMinimumSize(QSize(25, 0))
        self.sb_q3_2.setWrapping(False)
        self.sb_q3_2.setFrame(True)
        self.sb_q3_2.setAlignment(Qt.AlignCenter)
        self.sb_q3_2.setReadOnly(True)
        self.sb_q3_2.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sb_q3_2.setAccelerated(False)
        self.sb_q3_2.setKeyboardTracking(False)
        self.sb_q3_2.setProperty("showGroupSeparator", False)
        self.sb_q3_2.setMinimum(-999)
        self.sb_q3_2.setMaximum(999)

        self.horizontalLayout_7.addWidget(self.sb_q3_2)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_6)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.sl_q3_2 = QSlider(self.scrollAreaWidgetContents)
        self.sl_q3_2.setObjectName(u"sl_q3_2")
        self.sl_q3_2.setMaximum(420)
        self.sl_q3_2.setSingleStep(50)
        self.sl_q3_2.setPageStep(50)
        self.sl_q3_2.setOrientation(Qt.Horizontal)

        self.verticalLayout_3.addWidget(self.sl_q3_2)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_9 = QLabel(self.scrollAreaWidgetContents)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_9.addWidget(self.label_9)

        self.sb_q4_2 = QSpinBox(self.scrollAreaWidgetContents)
        self.sb_q4_2.setObjectName(u"sb_q4_2")
        self.sb_q4_2.setMinimumSize(QSize(25, 0))
        self.sb_q4_2.setWrapping(False)
        self.sb_q4_2.setFrame(True)
        self.sb_q4_2.setAlignment(Qt.AlignCenter)
        self.sb_q4_2.setReadOnly(True)
        self.sb_q4_2.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sb_q4_2.setAccelerated(False)
        self.sb_q4_2.setKeyboardTracking(False)
        self.sb_q4_2.setProperty("showGroupSeparator", False)
        self.sb_q4_2.setMinimum(-999)
        self.sb_q4_2.setMaximum(999)

        self.horizontalLayout_9.addWidget(self.sb_q4_2)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_8)


        self.verticalLayout_3.addLayout(self.horizontalLayout_9)

        self.sl_q4_2 = QSlider(self.scrollAreaWidgetContents)
        self.sl_q4_2.setObjectName(u"sl_q4_2")
        self.sl_q4_2.setMinimum(-360)
        self.sl_q4_2.setMaximum(360)
        self.sl_q4_2.setSingleStep(20)
        self.sl_q4_2.setPageStep(45)
        self.sl_q4_2.setOrientation(Qt.Horizontal)

        self.verticalLayout_3.addWidget(self.sl_q4_2)

        self.label_15 = QLabel(self.scrollAreaWidgetContents)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_15)

        self.glView_2 = GLView(self.scrollAreaWidgetContents)
        self.glView_2.setObjectName(u"glView_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.glView_2.sizePolicy().hasHeightForWidth())
        self.glView_2.setSizePolicy(sizePolicy1)
        self.glView_2.setMinimumSize(QSize(0, 300))
        self.glView_2.setStyleSheet(u"background-color:black;")

        self.verticalLayout_3.addWidget(self.glView_2)

        self.label_17 = QLabel(self.scrollAreaWidgetContents)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_17)

        self.sb_tFinal = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.sb_tFinal.setObjectName(u"sb_tFinal")
        self.sb_tFinal.setStyleSheet(u"color:white;\n"
"background-color:translucid;")
        self.sb_tFinal.setDecimals(1)
        self.sb_tFinal.setMinimum(1.000000000000000)
        self.sb_tFinal.setSingleStep(0.500000000000000)
        self.sb_tFinal.setStepType(QAbstractSpinBox.DefaultStepType)

        self.verticalLayout_3.addWidget(self.sb_tFinal)


        self.horizontalLayout.addLayout(self.verticalLayout_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.bt_iniciarAnimacion = QPushButton(self.scrollAreaWidgetContents)
        self.bt_iniciarAnimacion.setObjectName(u"bt_iniciarAnimacion")
        self.bt_iniciarAnimacion.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_iniciarAnimacion.setStyleSheet(u"QPushButton{\n"
"font:16pt \"Britannic Bold\";\n"
"color:white;\n"
"background-color:rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(255,255,255,50);\n"
"}")

        self.verticalLayout_4.addWidget(self.bt_iniciarAnimacion)

        self.glView_3 = GLView(self.scrollAreaWidgetContents)
        self.glView_3.setObjectName(u"glView_3")
        self.glView_3.setMinimumSize(QSize(0, 400))
        self.glView_3.setStyleSheet(u"background-color:black;")

        self.verticalLayout_4.addWidget(self.glView_3)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(sim_U1_T5)

        QMetaObject.connectSlotsByName(sim_U1_T5)
    # setupUi

    def retranslateUi(self, sim_U1_T5):
        sim_U1_T5.setWindowTitle(QCoreApplication.translate("sim_U1_T5", u"sim_U1_T5", None))
        self.label.setText(QCoreApplication.translate("sim_U1_T5", u"Animaci\u00f3n de tobot 3D", None))
        self.label_2.setText(QCoreApplication.translate("sim_U1_T5", u"Articulaci\u00f3n 1", None))
        self.sb_q1.setSuffix(QCoreApplication.translate("sim_U1_T5", u"\u00b0", None))
        self.label_3.setText(QCoreApplication.translate("sim_U1_T5", u"Articulaci\u00f3n 2", None))
        self.sb_q2.setSuffix(QCoreApplication.translate("sim_U1_T5", u" cm", None))
        self.label_4.setText(QCoreApplication.translate("sim_U1_T5", u"Articulaci\u00f3n 3", None))
        self.sb_q3.setSuffix(QCoreApplication.translate("sim_U1_T5", u" cm", None))
        self.label_7.setText(QCoreApplication.translate("sim_U1_T5", u"Articulaci\u00f3n 4", None))
        self.sb_q4.setSuffix(QCoreApplication.translate("sim_U1_T5", u"\u00b0", None))
        self.label_14.setText(QCoreApplication.translate("sim_U1_T5", u"Localizaci\u00f3n inicial", None))
        self.label_16.setText(QCoreApplication.translate("sim_U1_T5", u"Cuadros de animaci\u00f3n", None))
        self.label_5.setText(QCoreApplication.translate("sim_U1_T5", u"Articulaci\u00f3n 1", None))
        self.sb_q1_2.setSuffix(QCoreApplication.translate("sim_U1_T5", u"\u00b0", None))
        self.label_8.setText(QCoreApplication.translate("sim_U1_T5", u"Articulaci\u00f3n 2", None))
        self.sb_q2_2.setSuffix(QCoreApplication.translate("sim_U1_T5", u" cm", None))
        self.label_6.setText(QCoreApplication.translate("sim_U1_T5", u"Articulaci\u00f3n 3", None))
        self.sb_q3_2.setSuffix(QCoreApplication.translate("sim_U1_T5", u" cm", None))
        self.label_9.setText(QCoreApplication.translate("sim_U1_T5", u"Articulaci\u00f3n 4", None))
        self.sb_q4_2.setSuffix(QCoreApplication.translate("sim_U1_T5", u"\u00b0", None))
        self.label_15.setText(QCoreApplication.translate("sim_U1_T5", u"Localizaci\u00f3n final", None))
        self.label_17.setText(QCoreApplication.translate("sim_U1_T5", u"Duraci\u00f3n de la animaci\u00f3n (s)", None))
        self.sb_tFinal.setSuffix(QCoreApplication.translate("sim_U1_T5", u" s", None))
        self.bt_iniciarAnimacion.setText(QCoreApplication.translate("sim_U1_T5", u"Iniciar animaci\u00f3n", None))
    # retranslateUi

