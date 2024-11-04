# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sim_U1_T4eozykr.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QDoubleSpinBox,
    QHBoxLayout, QLabel, QPushButton, QScrollArea,
    QSizePolicy, QSlider, QSpacerItem, QSpinBox,
    QVBoxLayout, QWidget)

from clases.GLView import GLView

class Ui_Sim_U1_T4(object):
    def setupUi(self, Sim_U1_T4):
        if not Sim_U1_T4.objectName():
            Sim_U1_T4.setObjectName(u"Sim_U1_T4")
        Sim_U1_T4.resize(644, 603)
        self.verticalLayout = QVBoxLayout(Sim_U1_T4)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(Sim_U1_T4)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -88, 625, 1243))
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
        self.verticalLayout_6 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font:20pt \"Britannic Bold\";")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_4.addWidget(self.label_2)

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

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.sl_rotX_1 = QSlider(self.scrollAreaWidgetContents)
        self.sl_rotX_1.setObjectName(u"sl_rotX_1")
        self.sl_rotX_1.setMinimum(-360)
        self.sl_rotX_1.setMaximum(360)
        self.sl_rotX_1.setSingleStep(20)
        self.sl_rotX_1.setPageStep(45)
        self.sl_rotX_1.setOrientation(Qt.Horizontal)

        self.verticalLayout_2.addWidget(self.sl_rotX_1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_6.addWidget(self.label_3)

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

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.sl_rotY_1 = QSlider(self.scrollAreaWidgetContents)
        self.sl_rotY_1.setObjectName(u"sl_rotY_1")
        self.sl_rotY_1.setMinimum(-360)
        self.sl_rotY_1.setMaximum(360)
        self.sl_rotY_1.setSingleStep(20)
        self.sl_rotY_1.setPageStep(45)
        self.sl_rotY_1.setOrientation(Qt.Horizontal)

        self.verticalLayout_2.addWidget(self.sl_rotY_1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_8.addWidget(self.label_4)

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

        self.horizontalLayout_8.addWidget(self.sb_rZ)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_5)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.sl_rotZ_1 = QSlider(self.scrollAreaWidgetContents)
        self.sl_rotZ_1.setObjectName(u"sl_rotZ_1")
        self.sl_rotZ_1.setMinimum(-360)
        self.sl_rotZ_1.setMaximum(360)
        self.sl_rotZ_1.setSingleStep(20)
        self.sl_rotZ_1.setPageStep(45)
        self.sl_rotZ_1.setOrientation(Qt.Horizontal)

        self.verticalLayout_2.addWidget(self.sl_rotZ_1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_7 = QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_10.addWidget(self.label_7)

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

        self.horizontalLayout_10.addWidget(self.sb_dX)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_7)


        self.verticalLayout_2.addLayout(self.horizontalLayout_10)

        self.sl_despX_1 = QSlider(self.scrollAreaWidgetContents)
        self.sl_despX_1.setObjectName(u"sl_despX_1")
        self.sl_despX_1.setMinimum(-300)
        self.sl_despX_1.setMaximum(300)
        self.sl_despX_1.setSingleStep(40)
        self.sl_despX_1.setPageStep(40)
        self.sl_despX_1.setOrientation(Qt.Horizontal)

        self.verticalLayout_2.addWidget(self.sl_despX_1)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_12.addWidget(self.label_5)

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

        self.horizontalLayout_12.addWidget(self.sb_dY)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_9)


        self.verticalLayout_2.addLayout(self.horizontalLayout_12)

        self.sl_despY_1 = QSlider(self.scrollAreaWidgetContents)
        self.sl_despY_1.setObjectName(u"sl_despY_1")
        self.sl_despY_1.setMinimum(-300)
        self.sl_despY_1.setMaximum(300)
        self.sl_despY_1.setSingleStep(40)
        self.sl_despY_1.setPageStep(40)
        self.sl_despY_1.setOrientation(Qt.Horizontal)

        self.verticalLayout_2.addWidget(self.sl_despY_1)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_14.addWidget(self.label_6)

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

        self.horizontalLayout_14.addWidget(self.sb_dZ)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_11)


        self.verticalLayout_2.addLayout(self.horizontalLayout_14)

        self.sl_despZ_1 = QSlider(self.scrollAreaWidgetContents)
        self.sl_despZ_1.setObjectName(u"sl_despZ_1")
        self.sl_despZ_1.setMinimum(-300)
        self.sl_despZ_1.setMaximum(300)
        self.sl_despZ_1.setSingleStep(40)
        self.sl_despZ_1.setPageStep(40)
        self.sl_despZ_1.setOrientation(Qt.Horizontal)

        self.verticalLayout_2.addWidget(self.sl_despZ_1)

        self.label_14 = QLabel(self.scrollAreaWidgetContents)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_14)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_8 = QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_5.addWidget(self.label_8)

        self.sb_rX_2 = QSpinBox(self.scrollAreaWidgetContents)
        self.sb_rX_2.setObjectName(u"sb_rX_2")
        self.sb_rX_2.setMinimumSize(QSize(25, 0))
        self.sb_rX_2.setWrapping(False)
        self.sb_rX_2.setFrame(True)
        self.sb_rX_2.setAlignment(Qt.AlignCenter)
        self.sb_rX_2.setReadOnly(True)
        self.sb_rX_2.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sb_rX_2.setAccelerated(False)
        self.sb_rX_2.setKeyboardTracking(False)
        self.sb_rX_2.setProperty("showGroupSeparator", False)
        self.sb_rX_2.setMinimum(-999)
        self.sb_rX_2.setMaximum(999)

        self.horizontalLayout_5.addWidget(self.sb_rX_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.sl_rotX_2 = QSlider(self.scrollAreaWidgetContents)
        self.sl_rotX_2.setObjectName(u"sl_rotX_2")
        self.sl_rotX_2.setMinimum(-360)
        self.sl_rotX_2.setMaximum(360)
        self.sl_rotX_2.setSingleStep(20)
        self.sl_rotX_2.setPageStep(45)
        self.sl_rotX_2.setOrientation(Qt.Horizontal)

        self.verticalLayout_3.addWidget(self.sl_rotX_2)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_9 = QLabel(self.scrollAreaWidgetContents)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_7.addWidget(self.label_9)

        self.sb_rY_2 = QSpinBox(self.scrollAreaWidgetContents)
        self.sb_rY_2.setObjectName(u"sb_rY_2")
        self.sb_rY_2.setMinimumSize(QSize(25, 0))
        self.sb_rY_2.setWrapping(False)
        self.sb_rY_2.setFrame(True)
        self.sb_rY_2.setAlignment(Qt.AlignCenter)
        self.sb_rY_2.setReadOnly(True)
        self.sb_rY_2.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sb_rY_2.setAccelerated(False)
        self.sb_rY_2.setKeyboardTracking(False)
        self.sb_rY_2.setProperty("showGroupSeparator", False)
        self.sb_rY_2.setMinimum(-999)
        self.sb_rY_2.setMaximum(999)

        self.horizontalLayout_7.addWidget(self.sb_rY_2)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_4)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.sl_rotY_2 = QSlider(self.scrollAreaWidgetContents)
        self.sl_rotY_2.setObjectName(u"sl_rotY_2")
        self.sl_rotY_2.setMinimum(-360)
        self.sl_rotY_2.setMaximum(360)
        self.sl_rotY_2.setSingleStep(20)
        self.sl_rotY_2.setPageStep(45)
        self.sl_rotY_2.setOrientation(Qt.Horizontal)

        self.verticalLayout_3.addWidget(self.sl_rotY_2)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_10 = QLabel(self.scrollAreaWidgetContents)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_9.addWidget(self.label_10)

        self.sb_rZ_2 = QSpinBox(self.scrollAreaWidgetContents)
        self.sb_rZ_2.setObjectName(u"sb_rZ_2")
        self.sb_rZ_2.setMinimumSize(QSize(25, 0))
        self.sb_rZ_2.setWrapping(False)
        self.sb_rZ_2.setFrame(True)
        self.sb_rZ_2.setAlignment(Qt.AlignCenter)
        self.sb_rZ_2.setReadOnly(True)
        self.sb_rZ_2.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sb_rZ_2.setAccelerated(False)
        self.sb_rZ_2.setKeyboardTracking(False)
        self.sb_rZ_2.setProperty("showGroupSeparator", False)
        self.sb_rZ_2.setMinimum(-999)
        self.sb_rZ_2.setMaximum(999)

        self.horizontalLayout_9.addWidget(self.sb_rZ_2)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_6)


        self.verticalLayout_3.addLayout(self.horizontalLayout_9)

        self.sl_rotZ_2 = QSlider(self.scrollAreaWidgetContents)
        self.sl_rotZ_2.setObjectName(u"sl_rotZ_2")
        self.sl_rotZ_2.setMinimum(-360)
        self.sl_rotZ_2.setMaximum(360)
        self.sl_rotZ_2.setSingleStep(20)
        self.sl_rotZ_2.setPageStep(45)
        self.sl_rotZ_2.setOrientation(Qt.Horizontal)

        self.verticalLayout_3.addWidget(self.sl_rotZ_2)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_11 = QLabel(self.scrollAreaWidgetContents)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_11.addWidget(self.label_11)

        self.sb_dX_2 = QSpinBox(self.scrollAreaWidgetContents)
        self.sb_dX_2.setObjectName(u"sb_dX_2")
        self.sb_dX_2.setMinimumSize(QSize(25, 0))
        self.sb_dX_2.setWrapping(False)
        self.sb_dX_2.setFrame(True)
        self.sb_dX_2.setAlignment(Qt.AlignCenter)
        self.sb_dX_2.setReadOnly(True)
        self.sb_dX_2.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sb_dX_2.setAccelerated(False)
        self.sb_dX_2.setKeyboardTracking(False)
        self.sb_dX_2.setProperty("showGroupSeparator", False)
        self.sb_dX_2.setMinimum(-999)
        self.sb_dX_2.setMaximum(999)

        self.horizontalLayout_11.addWidget(self.sb_dX_2)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_8)


        self.verticalLayout_3.addLayout(self.horizontalLayout_11)

        self.sl_despX_2 = QSlider(self.scrollAreaWidgetContents)
        self.sl_despX_2.setObjectName(u"sl_despX_2")
        self.sl_despX_2.setMinimum(-300)
        self.sl_despX_2.setMaximum(300)
        self.sl_despX_2.setSingleStep(40)
        self.sl_despX_2.setPageStep(40)
        self.sl_despX_2.setOrientation(Qt.Horizontal)

        self.verticalLayout_3.addWidget(self.sl_despX_2)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_12 = QLabel(self.scrollAreaWidgetContents)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_13.addWidget(self.label_12)

        self.sb_dY_2 = QSpinBox(self.scrollAreaWidgetContents)
        self.sb_dY_2.setObjectName(u"sb_dY_2")
        self.sb_dY_2.setMinimumSize(QSize(25, 0))
        self.sb_dY_2.setWrapping(False)
        self.sb_dY_2.setFrame(True)
        self.sb_dY_2.setAlignment(Qt.AlignCenter)
        self.sb_dY_2.setReadOnly(True)
        self.sb_dY_2.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sb_dY_2.setAccelerated(False)
        self.sb_dY_2.setKeyboardTracking(False)
        self.sb_dY_2.setProperty("showGroupSeparator", False)
        self.sb_dY_2.setMinimum(-999)
        self.sb_dY_2.setMaximum(999)

        self.horizontalLayout_13.addWidget(self.sb_dY_2)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_10)


        self.verticalLayout_3.addLayout(self.horizontalLayout_13)

        self.sl_despY_2 = QSlider(self.scrollAreaWidgetContents)
        self.sl_despY_2.setObjectName(u"sl_despY_2")
        self.sl_despY_2.setMinimum(-300)
        self.sl_despY_2.setMaximum(300)
        self.sl_despY_2.setSingleStep(40)
        self.sl_despY_2.setPageStep(40)
        self.sl_despY_2.setOrientation(Qt.Horizontal)

        self.verticalLayout_3.addWidget(self.sl_despY_2)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_13 = QLabel(self.scrollAreaWidgetContents)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_15.addWidget(self.label_13)

        self.sb_dZ_2 = QSpinBox(self.scrollAreaWidgetContents)
        self.sb_dZ_2.setObjectName(u"sb_dZ_2")
        self.sb_dZ_2.setMinimumSize(QSize(25, 0))
        self.sb_dZ_2.setWrapping(False)
        self.sb_dZ_2.setFrame(True)
        self.sb_dZ_2.setAlignment(Qt.AlignCenter)
        self.sb_dZ_2.setReadOnly(True)
        self.sb_dZ_2.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sb_dZ_2.setAccelerated(False)
        self.sb_dZ_2.setKeyboardTracking(False)
        self.sb_dZ_2.setProperty("showGroupSeparator", False)
        self.sb_dZ_2.setMinimum(-999)
        self.sb_dZ_2.setMaximum(999)

        self.horizontalLayout_15.addWidget(self.sb_dZ_2)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_12)


        self.verticalLayout_3.addLayout(self.horizontalLayout_15)

        self.sl_despZ_2 = QSlider(self.scrollAreaWidgetContents)
        self.sl_despZ_2.setObjectName(u"sl_despZ_2")
        self.sl_despZ_2.setMinimum(-300)
        self.sl_despZ_2.setMaximum(300)
        self.sl_despZ_2.setSingleStep(40)
        self.sl_despZ_2.setPageStep(40)
        self.sl_despZ_2.setOrientation(Qt.Horizontal)

        self.verticalLayout_3.addWidget(self.sl_despZ_2)

        self.label_15 = QLabel(self.scrollAreaWidgetContents)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_15)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)


        self.verticalLayout_6.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_13)

        self.label_18 = QLabel(self.scrollAreaWidgetContents)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_16.addWidget(self.label_18)

        self.cb_ecuaciones = QComboBox(self.scrollAreaWidgetContents)
        self.cb_ecuaciones.addItem("")
        self.cb_ecuaciones.addItem("")
        self.cb_ecuaciones.addItem("")
        self.cb_ecuaciones.addItem("")
        self.cb_ecuaciones.addItem("")
        self.cb_ecuaciones.addItem("")
        self.cb_ecuaciones.setObjectName(u"cb_ecuaciones")
        self.cb_ecuaciones.setMinimumSize(QSize(250, 0))

        self.horizontalLayout_16.addWidget(self.cb_ecuaciones)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_14)


        self.verticalLayout_6.addLayout(self.horizontalLayout_16)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.glView_2 = GLView(self.scrollAreaWidgetContents)
        self.glView_2.setObjectName(u"glView_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.glView_2.sizePolicy().hasHeightForWidth())
        self.glView_2.setSizePolicy(sizePolicy1)
        self.glView_2.setMinimumSize(QSize(0, 300))

        self.horizontalLayout.addWidget(self.glView_2)

        self.glView_3 = GLView(self.scrollAreaWidgetContents)
        self.glView_3.setObjectName(u"glView_3")
        sizePolicy1.setHeightForWidth(self.glView_3.sizePolicy().hasHeightForWidth())
        self.glView_3.setSizePolicy(sizePolicy1)
        self.glView_3.setMinimumSize(QSize(0, 300))

        self.horizontalLayout.addWidget(self.glView_3)


        self.verticalLayout_6.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_16 = QLabel(self.scrollAreaWidgetContents)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_16)

        self.sb_nPuntos = QSpinBox(self.scrollAreaWidgetContents)
        self.sb_nPuntos.setObjectName(u"sb_nPuntos")
        self.sb_nPuntos.setStyleSheet(u"color:white;\n"
"background-color:translucid;")
        self.sb_nPuntos.setMinimum(2)
        self.sb_nPuntos.setMaximum(999)
        self.sb_nPuntos.setSingleStep(10)
        self.sb_nPuntos.setValue(60)

        self.verticalLayout_4.addWidget(self.sb_nPuntos)


        self.horizontalLayout_3.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_17 = QLabel(self.scrollAreaWidgetContents)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_17)

        self.sb_tFinal = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.sb_tFinal.setObjectName(u"sb_tFinal")
        self.sb_tFinal.setStyleSheet(u"color:white;\n"
"background-color:translucid;")
        self.sb_tFinal.setDecimals(1)
        self.sb_tFinal.setMinimum(1.000000000000000)
        self.sb_tFinal.setSingleStep(0.500000000000000)
        self.sb_tFinal.setStepType(QAbstractSpinBox.DefaultStepType)

        self.verticalLayout_5.addWidget(self.sb_tFinal)


        self.horizontalLayout_3.addLayout(self.verticalLayout_5)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)

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

        self.verticalLayout_6.addWidget(self.bt_iniciarAnimacion)

        self.glView_1 = GLView(self.scrollAreaWidgetContents)
        self.glView_1.setObjectName(u"glView_1")
        sizePolicy1.setHeightForWidth(self.glView_1.sizePolicy().hasHeightForWidth())
        self.glView_1.setSizePolicy(sizePolicy1)
        self.glView_1.setMinimumSize(QSize(0, 400))
        self.glView_1.setStyleSheet(u"background-color:black;")

        self.verticalLayout_6.addWidget(self.glView_1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(Sim_U1_T4)

        QMetaObject.connectSlotsByName(Sim_U1_T4)
    # setupUi

    def retranslateUi(self, Sim_U1_T4):
        Sim_U1_T4.setWindowTitle(QCoreApplication.translate("Sim_U1_T4", u"sim_U1_T4", None))
        self.label.setText(QCoreApplication.translate("Sim_U1_T4", u"Animaci\u00f3n de objeto 3D", None))
        self.label_2.setText(QCoreApplication.translate("Sim_U1_T4", u"Rotaci\u00f3n X", None))
        self.sb_rX.setSuffix(QCoreApplication.translate("Sim_U1_T4", u"\u00b0", None))
        self.label_3.setText(QCoreApplication.translate("Sim_U1_T4", u"Rotaci\u00f3n Y", None))
        self.sb_rY.setSuffix(QCoreApplication.translate("Sim_U1_T4", u"\u00b0", None))
        self.label_4.setText(QCoreApplication.translate("Sim_U1_T4", u"Rotaci\u00f3n Z", None))
        self.sb_rZ.setSuffix(QCoreApplication.translate("Sim_U1_T4", u"\u00b0", None))
        self.label_7.setText(QCoreApplication.translate("Sim_U1_T4", u"Desplazamiento X", None))
        self.sb_dX.setSuffix(QCoreApplication.translate("Sim_U1_T4", u" cm", None))
        self.label_5.setText(QCoreApplication.translate("Sim_U1_T4", u"Desplazamiento Y", None))
        self.sb_dY.setSuffix(QCoreApplication.translate("Sim_U1_T4", u" cm", None))
        self.label_6.setText(QCoreApplication.translate("Sim_U1_T4", u"Desplazamiento Z", None))
        self.sb_dZ.setSuffix(QCoreApplication.translate("Sim_U1_T4", u" cm", None))
        self.label_14.setText(QCoreApplication.translate("Sim_U1_T4", u"Localizaci\u00f3n inicial", None))
        self.label_8.setText(QCoreApplication.translate("Sim_U1_T4", u"Rotaci\u00f3n X", None))
        self.sb_rX_2.setSuffix(QCoreApplication.translate("Sim_U1_T4", u"\u00b0", None))
        self.label_9.setText(QCoreApplication.translate("Sim_U1_T4", u"Rotaci\u00f3n Y", None))
        self.sb_rY_2.setSuffix(QCoreApplication.translate("Sim_U1_T4", u"\u00b0", None))
        self.label_10.setText(QCoreApplication.translate("Sim_U1_T4", u"Rotaci\u00f3n Z", None))
        self.sb_rZ_2.setSuffix(QCoreApplication.translate("Sim_U1_T4", u"\u00b0", None))
        self.label_11.setText(QCoreApplication.translate("Sim_U1_T4", u"Desplazamiento X", None))
        self.sb_dX_2.setSuffix(QCoreApplication.translate("Sim_U1_T4", u" cm", None))
        self.label_12.setText(QCoreApplication.translate("Sim_U1_T4", u"Desplazamiento Y", None))
        self.sb_dY_2.setSuffix(QCoreApplication.translate("Sim_U1_T4", u" cm", None))
        self.label_13.setText(QCoreApplication.translate("Sim_U1_T4", u"Desplazamiento Z", None))
        self.sb_dZ_2.setSuffix(QCoreApplication.translate("Sim_U1_T4", u" cm", None))
        self.label_15.setText(QCoreApplication.translate("Sim_U1_T4", u"Localizaci\u00f3n final", None))
        self.label_18.setText(QCoreApplication.translate("Sim_U1_T4", u"Ecuaci\u00f3n de localizaci\u00f3n:", None))
        self.cb_ecuaciones.setItemText(0, QCoreApplication.translate("Sim_U1_T4", u"A = rotX * rotY * rotZ * desplazamientoXYZ", None))
        self.cb_ecuaciones.setItemText(1, QCoreApplication.translate("Sim_U1_T4", u"A = rotX * rotZ * rotY * desplazamientoXYZ", None))
        self.cb_ecuaciones.setItemText(2, QCoreApplication.translate("Sim_U1_T4", u"A = rotY * rotZ * rotX * desplazamientoXYZ", None))
        self.cb_ecuaciones.setItemText(3, QCoreApplication.translate("Sim_U1_T4", u"A = rotY * rotX * rotZ * desplazamientoXYZ", None))
        self.cb_ecuaciones.setItemText(4, QCoreApplication.translate("Sim_U1_T4", u"A = rotZ * rotX * rotY * desplazamientoXYZ", None))
        self.cb_ecuaciones.setItemText(5, QCoreApplication.translate("Sim_U1_T4", u"A = rotZ * rotY * rotX * desplazamientoXYZ", None))

        self.label_16.setText(QCoreApplication.translate("Sim_U1_T4", u"Cuadros de animaci\u00f3n", None))
        self.label_17.setText(QCoreApplication.translate("Sim_U1_T4", u"Duraci\u00f3n de la animaci\u00f3n (s)", None))
        self.sb_tFinal.setSuffix(QCoreApplication.translate("Sim_U1_T4", u" s", None))
        self.bt_iniciarAnimacion.setText(QCoreApplication.translate("Sim_U1_T4", u"Iniciar animaci\u00f3n", None))
    # retranslateUi

