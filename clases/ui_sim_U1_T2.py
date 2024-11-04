# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sim_U1_T2YmoqAS.ui'
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
    QLabel, QScrollArea, QSizePolicy, QSlider,
    QSpacerItem, QSpinBox, QVBoxLayout, QWidget)

from clases.GLView import GLView

class Ui_sim_U1_T2(object):
    def setupUi(self, sim_U1_T2):
        if not sim_U1_T2.objectName():
            sim_U1_T2.setObjectName(u"sim_U1_T2")
        sim_U1_T2.resize(629, 472)
        sim_U1_T2.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(sim_U1_T2)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(sim_U1_T2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 610, 842))
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
        self.verticalLayout_11 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"font:20pt \"Britannic Bold\";")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_5)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.sl_n = QSlider(self.scrollAreaWidgetContents)
        self.sl_n.setObjectName(u"sl_n")
        self.sl_n.setCursor(QCursor(Qt.ArrowCursor))
        self.sl_n.setMinimum(3)
        self.sl_n.setMaximum(100)
        self.sl_n.setValue(10)
        self.sl_n.setOrientation(Qt.Horizontal)

        self.verticalLayout_2.addWidget(self.sl_n)

        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.sl_nCaras = QSlider(self.scrollAreaWidgetContents)
        self.sl_nCaras.setObjectName(u"sl_nCaras")
        self.sl_nCaras.setMinimum(0)
        self.sl_nCaras.setPageStep(1)
        self.sl_nCaras.setOrientation(Qt.Horizontal)

        self.verticalLayout_2.addWidget(self.sl_nCaras)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)

        self.sl_lCono_1 = QSlider(self.scrollAreaWidgetContents)
        self.sl_lCono_1.setObjectName(u"sl_lCono_1")
        self.sl_lCono_1.setMinimum(1)
        self.sl_lCono_1.setMaximum(20)
        self.sl_lCono_1.setPageStep(1)
        self.sl_lCono_1.setValue(5)
        self.sl_lCono_1.setOrientation(Qt.Horizontal)

        self.verticalLayout_3.addWidget(self.sl_lCono_1)

        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_3.addWidget(self.label_4)

        self.sl_dCono_1 = QSlider(self.scrollAreaWidgetContents)
        self.sl_dCono_1.setObjectName(u"sl_dCono_1")
        self.sl_dCono_1.setMinimum(1)
        self.sl_dCono_1.setMaximum(20)
        self.sl_dCono_1.setPageStep(1)
        self.sl_dCono_1.setValue(4)
        self.sl_dCono_1.setOrientation(Qt.Horizontal)

        self.verticalLayout_3.addWidget(self.sl_dCono_1)


        self.horizontalLayout.addLayout(self.verticalLayout_3)


        self.verticalLayout_11.addLayout(self.horizontalLayout)

        self.glView_1 = GLView(self.scrollAreaWidgetContents)
        self.glView_1.setObjectName(u"glView_1")
        self.glView_1.setMinimumSize(QSize(0, 100))
        self.glView_1.setStyleSheet(u"background-color:black;")

        self.verticalLayout_11.addWidget(self.glView_1)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer)

        self.label_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"font:20pt \"Britannic Bold\";")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_6)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_7 = QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_4.addWidget(self.label_7)

        self.sl_lFlecha_1 = QSlider(self.scrollAreaWidgetContents)
        self.sl_lFlecha_1.setObjectName(u"sl_lFlecha_1")
        self.sl_lFlecha_1.setCursor(QCursor(Qt.ArrowCursor))
        self.sl_lFlecha_1.setMinimum(2)
        self.sl_lFlecha_1.setMaximum(12)
        self.sl_lFlecha_1.setPageStep(1)
        self.sl_lFlecha_1.setValue(2)
        self.sl_lFlecha_1.setOrientation(Qt.Horizontal)

        self.verticalLayout_4.addWidget(self.sl_lFlecha_1)

        self.label_8 = QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_4.addWidget(self.label_8)

        self.sl_dCilindro = QSlider(self.scrollAreaWidgetContents)
        self.sl_dCilindro.setObjectName(u"sl_dCilindro")
        self.sl_dCilindro.setMinimum(1)
        self.sl_dCilindro.setMaximum(10)
        self.sl_dCilindro.setPageStep(1)
        self.sl_dCilindro.setValue(1)
        self.sl_dCilindro.setOrientation(Qt.Horizontal)

        self.verticalLayout_4.addWidget(self.sl_dCilindro)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_9 = QLabel(self.scrollAreaWidgetContents)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_5.addWidget(self.label_9)

        self.sl_lCono_2 = QSlider(self.scrollAreaWidgetContents)
        self.sl_lCono_2.setObjectName(u"sl_lCono_2")
        self.sl_lCono_2.setMinimum(1)
        self.sl_lCono_2.setMaximum(1)
        self.sl_lCono_2.setPageStep(1)
        self.sl_lCono_2.setValue(1)
        self.sl_lCono_2.setOrientation(Qt.Horizontal)

        self.verticalLayout_5.addWidget(self.sl_lCono_2)

        self.label_10 = QLabel(self.scrollAreaWidgetContents)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_5.addWidget(self.label_10)

        self.sl_dCono_2 = QSlider(self.scrollAreaWidgetContents)
        self.sl_dCono_2.setObjectName(u"sl_dCono_2")
        self.sl_dCono_2.setMinimum(1)
        self.sl_dCono_2.setMaximum(10)
        self.sl_dCono_2.setPageStep(1)
        self.sl_dCono_2.setValue(2)
        self.sl_dCono_2.setOrientation(Qt.Horizontal)

        self.verticalLayout_5.addWidget(self.sl_dCono_2)


        self.horizontalLayout_2.addLayout(self.verticalLayout_5)


        self.verticalLayout_11.addLayout(self.horizontalLayout_2)

        self.glView_2 = GLView(self.scrollAreaWidgetContents)
        self.glView_2.setObjectName(u"glView_2")
        self.glView_2.setMinimumSize(QSize(0, 100))
        self.glView_2.setStyleSheet(u"background-color:black;")

        self.verticalLayout_11.addWidget(self.glView_2)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_2)

        self.label_11 = QLabel(self.scrollAreaWidgetContents)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"font:20pt \"Britannic Bold\";")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_11)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_19 = QLabel(self.scrollAreaWidgetContents)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_6.addWidget(self.label_19)

        self.sb_X = QSpinBox(self.scrollAreaWidgetContents)
        self.sb_X.setObjectName(u"sb_X")
        self.sb_X.setMinimumSize(QSize(25, 0))
        self.sb_X.setWrapping(False)
        self.sb_X.setFrame(True)
        self.sb_X.setAlignment(Qt.AlignCenter)
        self.sb_X.setReadOnly(True)
        self.sb_X.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sb_X.setAccelerated(False)
        self.sb_X.setKeyboardTracking(False)
        self.sb_X.setProperty("showGroupSeparator", False)
        self.sb_X.setMinimum(-999)
        self.sb_X.setMaximum(999)

        self.horizontalLayout_6.addWidget(self.sb_X)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)


        self.verticalLayout_12.addLayout(self.horizontalLayout_6)

        self.sl_rotX = QSlider(self.scrollAreaWidgetContents)
        self.sl_rotX.setObjectName(u"sl_rotX")
        self.sl_rotX.setMinimum(-360)
        self.sl_rotX.setMaximum(360)
        self.sl_rotX.setSingleStep(10)
        self.sl_rotX.setPageStep(40)
        self.sl_rotX.setValue(0)
        self.sl_rotX.setTracking(True)
        self.sl_rotX.setOrientation(Qt.Horizontal)
        self.sl_rotX.setInvertedAppearance(False)
        self.sl_rotX.setInvertedControls(False)
        self.sl_rotX.setTickPosition(QSlider.NoTicks)
        self.sl_rotX.setTickInterval(40)

        self.verticalLayout_12.addWidget(self.sl_rotX)


        self.horizontalLayout_3.addLayout(self.verticalLayout_12)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_21 = QLabel(self.scrollAreaWidgetContents)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_7.addWidget(self.label_21)

        self.sb_Y = QSpinBox(self.scrollAreaWidgetContents)
        self.sb_Y.setObjectName(u"sb_Y")
        self.sb_Y.setMinimumSize(QSize(25, 0))
        self.sb_Y.setWrapping(False)
        self.sb_Y.setFrame(True)
        self.sb_Y.setAlignment(Qt.AlignCenter)
        self.sb_Y.setReadOnly(True)
        self.sb_Y.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sb_Y.setAccelerated(False)
        self.sb_Y.setKeyboardTracking(False)
        self.sb_Y.setProperty("showGroupSeparator", False)
        self.sb_Y.setMinimum(-999)
        self.sb_Y.setMaximum(999)

        self.horizontalLayout_7.addWidget(self.sb_Y)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_4)


        self.verticalLayout_14.addLayout(self.horizontalLayout_7)

        self.sl_rotY = QSlider(self.scrollAreaWidgetContents)
        self.sl_rotY.setObjectName(u"sl_rotY")
        self.sl_rotY.setMinimum(-360)
        self.sl_rotY.setMaximum(360)
        self.sl_rotY.setSingleStep(10)
        self.sl_rotY.setPageStep(40)
        self.sl_rotY.setValue(0)
        self.sl_rotY.setOrientation(Qt.Horizontal)

        self.verticalLayout_14.addWidget(self.sl_rotY)


        self.horizontalLayout_3.addLayout(self.verticalLayout_14)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_20 = QLabel(self.scrollAreaWidgetContents)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_8.addWidget(self.label_20)

        self.sb_Z = QSpinBox(self.scrollAreaWidgetContents)
        self.sb_Z.setObjectName(u"sb_Z")
        self.sb_Z.setMinimumSize(QSize(25, 0))
        self.sb_Z.setWrapping(False)
        self.sb_Z.setFrame(True)
        self.sb_Z.setAlignment(Qt.AlignCenter)
        self.sb_Z.setReadOnly(True)
        self.sb_Z.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sb_Z.setAccelerated(False)
        self.sb_Z.setKeyboardTracking(False)
        self.sb_Z.setProperty("showGroupSeparator", False)
        self.sb_Z.setMinimum(-999)
        self.sb_Z.setMaximum(999)

        self.horizontalLayout_8.addWidget(self.sb_Z)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_5)


        self.verticalLayout_13.addLayout(self.horizontalLayout_8)

        self.sl_rotZ = QSlider(self.scrollAreaWidgetContents)
        self.sl_rotZ.setObjectName(u"sl_rotZ")
        self.sl_rotZ.setMinimum(-360)
        self.sl_rotZ.setMaximum(360)
        self.sl_rotZ.setSingleStep(10)
        self.sl_rotZ.setPageStep(40)
        self.sl_rotZ.setValue(0)
        self.sl_rotZ.setOrientation(Qt.Horizontal)

        self.verticalLayout_13.addWidget(self.sl_rotZ)


        self.horizontalLayout_3.addLayout(self.verticalLayout_13)


        self.verticalLayout_11.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.label_12 = QLabel(self.scrollAreaWidgetContents)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_5.addWidget(self.label_12)

        self.cb_ecuaciones = QComboBox(self.scrollAreaWidgetContents)
        self.cb_ecuaciones.addItem("")
        self.cb_ecuaciones.addItem("")
        self.cb_ecuaciones.addItem("")
        self.cb_ecuaciones.addItem("")
        self.cb_ecuaciones.addItem("")
        self.cb_ecuaciones.addItem("")
        self.cb_ecuaciones.setObjectName(u"cb_ecuaciones")
        self.cb_ecuaciones.setMinimumSize(QSize(135, 0))

        self.horizontalLayout_5.addWidget(self.cb_ecuaciones)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)


        self.verticalLayout_11.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_16 = QLabel(self.scrollAreaWidgetContents)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_16)

        self.sl_lFlecha_2 = QSlider(self.scrollAreaWidgetContents)
        self.sl_lFlecha_2.setObjectName(u"sl_lFlecha_2")
        self.sl_lFlecha_2.setMinimum(2)
        self.sl_lFlecha_2.setMaximum(30)
        self.sl_lFlecha_2.setPageStep(1)
        self.sl_lFlecha_2.setValue(10)
        self.sl_lFlecha_2.setOrientation(Qt.Horizontal)

        self.verticalLayout_8.addWidget(self.sl_lFlecha_2)


        self.horizontalLayout_4.addLayout(self.verticalLayout_8)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_17 = QLabel(self.scrollAreaWidgetContents)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout_9.addWidget(self.label_17)

        self.sb_subindice = QSpinBox(self.scrollAreaWidgetContents)
        self.sb_subindice.setObjectName(u"sb_subindice")
        self.sb_subindice.setStyleSheet(u"")
        self.sb_subindice.setMaximum(9999)

        self.verticalLayout_9.addWidget(self.sb_subindice)


        self.horizontalLayout_4.addLayout(self.verticalLayout_9)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_18 = QLabel(self.scrollAreaWidgetContents)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_18)

        self.sl_dFlecha = QSlider(self.scrollAreaWidgetContents)
        self.sl_dFlecha.setObjectName(u"sl_dFlecha")
        self.sl_dFlecha.setMinimum(1)
        self.sl_dFlecha.setMaximum(10)
        self.sl_dFlecha.setPageStep(1)
        self.sl_dFlecha.setValue(2)
        self.sl_dFlecha.setOrientation(Qt.Horizontal)

        self.verticalLayout_10.addWidget(self.sl_dFlecha)


        self.horizontalLayout_4.addLayout(self.verticalLayout_10)


        self.verticalLayout_11.addLayout(self.horizontalLayout_4)

        self.glView_3 = GLView(self.scrollAreaWidgetContents)
        self.glView_3.setObjectName(u"glView_3")
        self.glView_3.setMinimumSize(QSize(0, 100))
        self.glView_3.setStyleSheet(u"background-color:black;")

        self.verticalLayout_11.addWidget(self.glView_3)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(sim_U1_T2)

        QMetaObject.connectSlotsByName(sim_U1_T2)
    # setupUi

    def retranslateUi(self, sim_U1_T2):
        sim_U1_T2.setWindowTitle(QCoreApplication.translate("sim_U1_T2", u"sim_U1_T2", None))
        self.label_5.setText(QCoreApplication.translate("sim_U1_T2", u"Dibujo de cono 3D", None))
        self.label.setText(QCoreApplication.translate("sim_U1_T2", u"N\u00famero de puntos en la base", None))
#if QT_CONFIG(tooltip)
        self.sl_n.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.sl_n.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.sl_n.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.label_2.setText(QCoreApplication.translate("sim_U1_T2", u"N\u00famero de caras visibles", None))
        self.label_3.setText(QCoreApplication.translate("sim_U1_T2", u"Largo del cono", None))
        self.label_4.setText(QCoreApplication.translate("sim_U1_T2", u"Diametro del cono", None))
        self.label_6.setText(QCoreApplication.translate("sim_U1_T2", u"Dibujo de flecha 3D", None))
        self.label_7.setText(QCoreApplication.translate("sim_U1_T2", u"Largo de la flecha", None))
#if QT_CONFIG(tooltip)
        self.sl_lFlecha_1.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.sl_lFlecha_1.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.sl_lFlecha_1.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.label_8.setText(QCoreApplication.translate("sim_U1_T2", u"Diametro del cilindro", None))
        self.label_9.setText(QCoreApplication.translate("sim_U1_T2", u"Largo del cono", None))
        self.label_10.setText(QCoreApplication.translate("sim_U1_T2", u"Diametro del cono", None))
        self.label_11.setText(QCoreApplication.translate("sim_U1_T2", u"Dibujo de sistema de coordenadas 3D", None))
        self.label_19.setText(QCoreApplication.translate("sim_U1_T2", u"Rotaci\u00f3n X", None))
        self.label_21.setText(QCoreApplication.translate("sim_U1_T2", u"Rotaci\u00f3n Y", None))
        self.label_20.setText(QCoreApplication.translate("sim_U1_T2", u"Rotaci\u00f3n Z", None))
        self.label_12.setText(QCoreApplication.translate("sim_U1_T2", u"Ecuaci\u00f3n de localizaci\u00f3n: ", None))
        self.cb_ecuaciones.setItemText(0, QCoreApplication.translate("sim_U1_T2", u"A = rotX * rotY * rotZ", None))
        self.cb_ecuaciones.setItemText(1, QCoreApplication.translate("sim_U1_T2", u"A = rotX * rotZ * rotY", None))
        self.cb_ecuaciones.setItemText(2, QCoreApplication.translate("sim_U1_T2", u"A = rotY * rotZ * rotX", None))
        self.cb_ecuaciones.setItemText(3, QCoreApplication.translate("sim_U1_T2", u"A = rotY * rotX * rotZ", None))
        self.cb_ecuaciones.setItemText(4, QCoreApplication.translate("sim_U1_T2", u"A = rotZ * rotX * rotY", None))
        self.cb_ecuaciones.setItemText(5, QCoreApplication.translate("sim_U1_T2", u"A = rotZ * rotY * rotX", None))

        self.label_16.setText(QCoreApplication.translate("sim_U1_T2", u"Largo de las flechas", None))
        self.label_17.setText(QCoreApplication.translate("sim_U1_T2", u"Subindice del sistema", None))
        self.label_18.setText(QCoreApplication.translate("sim_U1_T2", u"Diametros de las flechas", None))
    # retranslateUi

