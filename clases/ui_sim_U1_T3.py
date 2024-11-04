# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sim_U1_T3KiSurc.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QHBoxLayout,
    QLabel, QPushButton, QScrollArea, QSizePolicy,
    QSlider, QSpacerItem, QSpinBox, QVBoxLayout,
    QWidget)

from clases.GLView import GLView

class Ui_sim_U1_T3(object):
    def setupUi(self, sim_U1_T3):
        if not sim_U1_T3.objectName():
            sim_U1_T3.setObjectName(u"sim_U1_T3")
        sim_U1_T3.resize(659, 537)
        sim_U1_T3.setMinimumSize(QSize(0, 0))
        self.verticalLayout = QVBoxLayout(sim_U1_T3)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(sim_U1_T3)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -17, 640, 584))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setStyleSheet(u"QWidget#scrollAreaWidgetContents{\n"
"background-color:rgba(0,0,0,1);\n"
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
        self.verticalLayout_7 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_7 = QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"font:20pt \"Britannic Bold\";")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_7)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")

        self.horizontalLayout_4.addWidget(self.label)

        self.sb_rX = QSpinBox(self.scrollAreaWidgetContents)
        self.sb_rX.setObjectName(u"sb_rX")
        self.sb_rX.setMinimumSize(QSize(25, 0))
        self.sb_rX.setWrapping(False)
        self.sb_rX.setFrame(True)
        self.sb_rX.setAlignment(Qt.AlignCenter)
        self.sb_rX.setReadOnly(True)
        self.sb_rX.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sb_rX.setAccelerated(False)
        self.sb_rX.setKeyboardTracking(False)
        self.sb_rX.setProperty("showGroupSeparator", False)
        self.sb_rX.setMinimum(-999)
        self.sb_rX.setMaximum(999)

        self.horizontalLayout_4.addWidget(self.sb_rX)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.sl_rotX = QSlider(self.scrollAreaWidgetContents)
        self.sl_rotX.setObjectName(u"sl_rotX")
        self.sl_rotX.setMinimum(-360)
        self.sl_rotX.setMaximum(360)
        self.sl_rotX.setSingleStep(20)
        self.sl_rotX.setPageStep(45)
        self.sl_rotX.setOrientation(Qt.Horizontal)

        self.verticalLayout_2.addWidget(self.sl_rotX)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_8.addWidget(self.label_4)

        self.sb_dX = QSpinBox(self.scrollAreaWidgetContents)
        self.sb_dX.setObjectName(u"sb_dX")
        self.sb_dX.setMinimumSize(QSize(25, 0))
        self.sb_dX.setWrapping(False)
        self.sb_dX.setFrame(True)
        self.sb_dX.setAlignment(Qt.AlignCenter)
        self.sb_dX.setReadOnly(True)
        self.sb_dX.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sb_dX.setAccelerated(False)
        self.sb_dX.setKeyboardTracking(False)
        self.sb_dX.setProperty("showGroupSeparator", False)
        self.sb_dX.setMinimum(-999)
        self.sb_dX.setMaximum(999)

        self.horizontalLayout_8.addWidget(self.sb_dX)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_8)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.sl_despX = QSlider(self.scrollAreaWidgetContents)
        self.sl_despX.setObjectName(u"sl_despX")
        self.sl_despX.setMinimum(-300)
        self.sl_despX.setMaximum(300)
        self.sl_despX.setSingleStep(40)
        self.sl_despX.setPageStep(40)
        self.sl_despX.setOrientation(Qt.Horizontal)

        self.verticalLayout_2.addWidget(self.sl_despX)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_6.addWidget(self.label_2)

        self.sb_rY = QSpinBox(self.scrollAreaWidgetContents)
        self.sb_rY.setObjectName(u"sb_rY")
        self.sb_rY.setMinimumSize(QSize(25, 0))
        self.sb_rY.setWrapping(False)
        self.sb_rY.setFrame(True)
        self.sb_rY.setAlignment(Qt.AlignCenter)
        self.sb_rY.setReadOnly(True)
        self.sb_rY.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sb_rY.setAccelerated(False)
        self.sb_rY.setKeyboardTracking(False)
        self.sb_rY.setProperty("showGroupSeparator", False)
        self.sb_rY.setMinimum(-999)
        self.sb_rY.setMaximum(999)

        self.horizontalLayout_6.addWidget(self.sb_rY)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_6)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.sl_rotY = QSlider(self.scrollAreaWidgetContents)
        self.sl_rotY.setObjectName(u"sl_rotY")
        self.sl_rotY.setMinimum(-360)
        self.sl_rotY.setMaximum(360)
        self.sl_rotY.setSingleStep(20)
        self.sl_rotY.setPageStep(45)
        self.sl_rotY.setOrientation(Qt.Horizontal)

        self.verticalLayout_3.addWidget(self.sl_rotY)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_9.addWidget(self.label_5)

        self.sb_dY = QSpinBox(self.scrollAreaWidgetContents)
        self.sb_dY.setObjectName(u"sb_dY")
        self.sb_dY.setMinimumSize(QSize(25, 0))
        self.sb_dY.setWrapping(False)
        self.sb_dY.setFrame(True)
        self.sb_dY.setAlignment(Qt.AlignCenter)
        self.sb_dY.setReadOnly(True)
        self.sb_dY.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sb_dY.setAccelerated(False)
        self.sb_dY.setKeyboardTracking(False)
        self.sb_dY.setProperty("showGroupSeparator", False)
        self.sb_dY.setMinimum(-999)
        self.sb_dY.setMaximum(999)

        self.horizontalLayout_9.addWidget(self.sb_dY)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_9)


        self.verticalLayout_3.addLayout(self.horizontalLayout_9)

        self.sl_despY = QSlider(self.scrollAreaWidgetContents)
        self.sl_despY.setObjectName(u"sl_despY")
        self.sl_despY.setMinimum(-300)
        self.sl_despY.setMaximum(300)
        self.sl_despY.setSingleStep(40)
        self.sl_despY.setPageStep(40)
        self.sl_despY.setOrientation(Qt.Horizontal)

        self.verticalLayout_3.addWidget(self.sl_despY)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_7.addWidget(self.label_3)

        self.sb_rZ = QSpinBox(self.scrollAreaWidgetContents)
        self.sb_rZ.setObjectName(u"sb_rZ")
        self.sb_rZ.setMinimumSize(QSize(25, 0))
        self.sb_rZ.setWrapping(False)
        self.sb_rZ.setFrame(True)
        self.sb_rZ.setAlignment(Qt.AlignCenter)
        self.sb_rZ.setReadOnly(True)
        self.sb_rZ.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sb_rZ.setAccelerated(False)
        self.sb_rZ.setKeyboardTracking(False)
        self.sb_rZ.setProperty("showGroupSeparator", False)
        self.sb_rZ.setMinimum(-999)
        self.sb_rZ.setMaximum(999)

        self.horizontalLayout_7.addWidget(self.sb_rZ)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_7)


        self.verticalLayout_4.addLayout(self.horizontalLayout_7)

        self.sl_rotZ = QSlider(self.scrollAreaWidgetContents)
        self.sl_rotZ.setObjectName(u"sl_rotZ")
        self.sl_rotZ.setMinimum(-360)
        self.sl_rotZ.setMaximum(360)
        self.sl_rotZ.setSingleStep(20)
        self.sl_rotZ.setPageStep(45)
        self.sl_rotZ.setOrientation(Qt.Horizontal)

        self.verticalLayout_4.addWidget(self.sl_rotZ)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_10.addWidget(self.label_6)

        self.sb_dZ = QSpinBox(self.scrollAreaWidgetContents)
        self.sb_dZ.setObjectName(u"sb_dZ")
        self.sb_dZ.setMinimumSize(QSize(25, 0))
        self.sb_dZ.setWrapping(False)
        self.sb_dZ.setFrame(True)
        self.sb_dZ.setAlignment(Qt.AlignCenter)
        self.sb_dZ.setReadOnly(True)
        self.sb_dZ.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sb_dZ.setAccelerated(False)
        self.sb_dZ.setKeyboardTracking(False)
        self.sb_dZ.setProperty("showGroupSeparator", False)
        self.sb_dZ.setMinimum(-999)
        self.sb_dZ.setMaximum(999)

        self.horizontalLayout_10.addWidget(self.sb_dZ)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_10)


        self.verticalLayout_4.addLayout(self.horizontalLayout_10)

        self.sl_despZ = QSlider(self.scrollAreaWidgetContents)
        self.sl_despZ.setObjectName(u"sl_despZ")
        self.sl_despZ.setMinimum(-300)
        self.sl_despZ.setMaximum(300)
        self.sl_despZ.setSingleStep(40)
        self.sl_despZ.setPageStep(40)
        self.sl_despZ.setOrientation(Qt.Horizontal)

        self.verticalLayout_4.addWidget(self.sl_despZ)


        self.horizontalLayout.addLayout(self.verticalLayout_4)


        self.verticalLayout_7.addLayout(self.horizontalLayout)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.label_14 = QLabel(self.scrollAreaWidgetContents)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_5.addWidget(self.label_14)

        self.cb_ecuaciones = QComboBox(self.scrollAreaWidgetContents)
        self.cb_ecuaciones.addItem("")
        self.cb_ecuaciones.addItem("")
        self.cb_ecuaciones.addItem("")
        self.cb_ecuaciones.addItem("")
        self.cb_ecuaciones.addItem("")
        self.cb_ecuaciones.addItem("")
        self.cb_ecuaciones.setObjectName(u"cb_ecuaciones")
        self.cb_ecuaciones.setMinimumSize(QSize(250, 0))

        self.horizontalLayout_5.addWidget(self.cb_ecuaciones)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)


        self.verticalLayout_7.addLayout(self.horizontalLayout_5)

        self.glView_1 = GLView(self.scrollAreaWidgetContents)
        self.glView_1.setObjectName(u"glView_1")
        self.glView_1.setMinimumSize(QSize(0, 100))
        self.glView_1.setStyleSheet(u"background-color:black;")

        self.verticalLayout_7.addWidget(self.glView_1)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer)

        self.label_8 = QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"font:20pt \"Britannic Bold\";")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_8)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_9 = QLabel(self.scrollAreaWidgetContents)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_3.addWidget(self.label_9)

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

        self.horizontalLayout_3.addWidget(self.sb_q1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.sl_q1 = QSlider(self.scrollAreaWidgetContents)
        self.sl_q1.setObjectName(u"sl_q1")
        self.sl_q1.setMinimum(-360)
        self.sl_q1.setMaximum(360)
        self.sl_q1.setSingleStep(20)
        self.sl_q1.setPageStep(45)
        self.sl_q1.setOrientation(Qt.Horizontal)

        self.verticalLayout_5.addWidget(self.sl_q1)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_11 = QLabel(self.scrollAreaWidgetContents)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_12.addWidget(self.label_11)

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

        self.horizontalLayout_12.addWidget(self.sb_q3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_2)


        self.verticalLayout_5.addLayout(self.horizontalLayout_12)

        self.sl_q3 = QSlider(self.scrollAreaWidgetContents)
        self.sl_q3.setObjectName(u"sl_q3")
        self.sl_q3.setMaximum(420)
        self.sl_q3.setSingleStep(50)
        self.sl_q3.setPageStep(50)
        self.sl_q3.setOrientation(Qt.Horizontal)

        self.verticalLayout_5.addWidget(self.sl_q3)


        self.horizontalLayout_2.addLayout(self.verticalLayout_5)

        self.bt_ver3D = QPushButton(self.scrollAreaWidgetContents)
        self.bt_ver3D.setObjectName(u"bt_ver3D")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.bt_ver3D.sizePolicy().hasHeightForWidth())
        self.bt_ver3D.setSizePolicy(sizePolicy1)
        self.bt_ver3D.setStyleSheet(u"QPushButton{\n"
"font:16pt \"Britannic Bold\";\n"
"color:white;\n"
"background-color:rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(255,255,255,50);\n"
"}")

        self.horizontalLayout_2.addWidget(self.bt_ver3D)

        self.bt_verLineas = QPushButton(self.scrollAreaWidgetContents)
        self.bt_verLineas.setObjectName(u"bt_verLineas")
        sizePolicy1.setHeightForWidth(self.bt_verLineas.sizePolicy().hasHeightForWidth())
        self.bt_verLineas.setSizePolicy(sizePolicy1)
        self.bt_verLineas.setStyleSheet(u"QPushButton{\n"
"font:16pt \"Britannic Bold\";\n"
"color:white;\n"
"background-color:rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(255,255,255,50);\n"
"}")

        self.horizontalLayout_2.addWidget(self.bt_verLineas)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_10 = QLabel(self.scrollAreaWidgetContents)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_11.addWidget(self.label_10)

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

        self.horizontalLayout_11.addWidget(self.sb_q2)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_11)


        self.verticalLayout_6.addLayout(self.horizontalLayout_11)

        self.sl_q2 = QSlider(self.scrollAreaWidgetContents)
        self.sl_q2.setObjectName(u"sl_q2")
        self.sl_q2.setMaximum(280)
        self.sl_q2.setSingleStep(40)
        self.sl_q2.setPageStep(40)
        self.sl_q2.setOrientation(Qt.Horizontal)

        self.verticalLayout_6.addWidget(self.sl_q2)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_12 = QLabel(self.scrollAreaWidgetContents)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_13.addWidget(self.label_12)

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

        self.horizontalLayout_13.addWidget(self.sb_q4)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_12)


        self.verticalLayout_6.addLayout(self.horizontalLayout_13)

        self.sl_q4 = QSlider(self.scrollAreaWidgetContents)
        self.sl_q4.setObjectName(u"sl_q4")
        self.sl_q4.setMinimum(-360)
        self.sl_q4.setMaximum(360)
        self.sl_q4.setSingleStep(20)
        self.sl_q4.setPageStep(45)
        self.sl_q4.setOrientation(Qt.Horizontal)

        self.verticalLayout_6.addWidget(self.sl_q4)


        self.horizontalLayout_2.addLayout(self.verticalLayout_6)

        self.horizontalLayout_2.setStretch(0, 3)
        self.horizontalLayout_2.setStretch(3, 3)

        self.verticalLayout_7.addLayout(self.horizontalLayout_2)

        self.glView_2 = GLView(self.scrollAreaWidgetContents)
        self.glView_2.setObjectName(u"glView_2")
        self.glView_2.setMinimumSize(QSize(0, 100))
        self.glView_2.setStyleSheet(u"background-color:black;")

        self.verticalLayout_7.addWidget(self.glView_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(sim_U1_T3)

        QMetaObject.connectSlotsByName(sim_U1_T3)
    # setupUi

    def retranslateUi(self, sim_U1_T3):
        sim_U1_T3.setWindowTitle(QCoreApplication.translate("sim_U1_T3", u"sim_U1_T3", None))
        self.label_7.setText(QCoreApplication.translate("sim_U1_T3", u"Localizaci\u00f3n de un s\u00f3lido", None))
        self.label.setText(QCoreApplication.translate("sim_U1_T3", u"Rotaci\u00f3n X", None))
        self.sb_rX.setSuffix(QCoreApplication.translate("sim_U1_T3", u"\u00b0", None))
        self.label_4.setText(QCoreApplication.translate("sim_U1_T3", u"Desplazamiento X", None))
        self.sb_dX.setSuffix(QCoreApplication.translate("sim_U1_T3", u" cm", None))
        self.label_2.setText(QCoreApplication.translate("sim_U1_T3", u"Rotaci\u00f3n Y", None))
        self.sb_rY.setSuffix(QCoreApplication.translate("sim_U1_T3", u"\u00b0", None))
        self.label_5.setText(QCoreApplication.translate("sim_U1_T3", u"Desplazamiento Y", None))
        self.sb_dY.setSuffix(QCoreApplication.translate("sim_U1_T3", u" cm", None))
        self.label_3.setText(QCoreApplication.translate("sim_U1_T3", u"Rotaci\u00f3n Z", None))
        self.sb_rZ.setSuffix(QCoreApplication.translate("sim_U1_T3", u"\u00b0", None))
        self.label_6.setText(QCoreApplication.translate("sim_U1_T3", u"Desplazamiento Z", None))
        self.sb_dZ.setSuffix(QCoreApplication.translate("sim_U1_T3", u" cm", None))
        self.label_14.setText(QCoreApplication.translate("sim_U1_T3", u"Ecuaci\u00f3n de localizaci\u00f3n: ", None))
        self.cb_ecuaciones.setItemText(0, QCoreApplication.translate("sim_U1_T3", u"A = rotX * rotY * rotZ * desplazamientoXYZ", None))
        self.cb_ecuaciones.setItemText(1, QCoreApplication.translate("sim_U1_T3", u"A = rotX * rotZ * rotY * desplazamientoXYZ", None))
        self.cb_ecuaciones.setItemText(2, QCoreApplication.translate("sim_U1_T3", u"A = rotY * rotZ * rotX * desplazamientoXYZ", None))
        self.cb_ecuaciones.setItemText(3, QCoreApplication.translate("sim_U1_T3", u"A = rotY * rotX * rotZ * desplazamientoXYZ", None))
        self.cb_ecuaciones.setItemText(4, QCoreApplication.translate("sim_U1_T3", u"A = rotZ * rotX * rotY * desplazamientoXYZ", None))
        self.cb_ecuaciones.setItemText(5, QCoreApplication.translate("sim_U1_T3", u"A = rotZ * rotY * rotX * desplazamientoXYZ", None))

        self.label_8.setText(QCoreApplication.translate("sim_U1_T3", u"Dibujo de robot 3D", None))
        self.label_9.setText(QCoreApplication.translate("sim_U1_T3", u"Articulaci\u00f3n 1", None))
        self.sb_q1.setSuffix(QCoreApplication.translate("sim_U1_T3", u"\u00b0", None))
        self.label_11.setText(QCoreApplication.translate("sim_U1_T3", u"Articulaci\u00f3n 3", None))
        self.sb_q3.setSuffix(QCoreApplication.translate("sim_U1_T3", u" cm", None))
        self.bt_ver3D.setText(QCoreApplication.translate("sim_U1_T3", u"Ver en \n"
"3D", None))
        self.bt_verLineas.setText(QCoreApplication.translate("sim_U1_T3", u"Ver en \n"
"Lineas", None))
        self.label_10.setText(QCoreApplication.translate("sim_U1_T3", u"Articulaci\u00f3n 2", None))
        self.sb_q2.setSuffix(QCoreApplication.translate("sim_U1_T3", u" cm", None))
        self.label_12.setText(QCoreApplication.translate("sim_U1_T3", u"Articulaci\u00f3n 4", None))
        self.sb_q4.setSuffix(QCoreApplication.translate("sim_U1_T3", u"\u00b0", None))
    # retranslateUi

