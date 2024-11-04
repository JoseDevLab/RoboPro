# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sim_U4_T2XTIYiS.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QScrollArea,
    QSizePolicy, QSlider, QVBoxLayout, QWidget)

from clases.PlotWidget import CustomPlotWidget

class Ui_sim_U4_T2(object):
    def setupUi(self, sim_U4_T2):
        if not sim_U4_T2.objectName():
            sim_U4_T2.setObjectName(u"sim_U4_T2")
        sim_U4_T2.resize(592, 479)
        sim_U4_T2.setStyleSheet(u"QWidget#sim_U4_T2{\n"
"background-color:rgba(0,0,0,0);\n"
"}")
        self.verticalLayout = QVBoxLayout(sim_U4_T2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(sim_U4_T2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 590, 287))
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
"QSlider::handle:horizontal {\n"
"background: qlineargradient(spread:pad, x1:0.505, y1:0, x2:0.500318, y2:1, stop:0 rgba(0, 74, 148, 255), stop:1 rgba(0, 37, 74, 255));\n"
"width: 18px;\n"
"margin: -2px 0; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"border-radius: 4px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"background: qlineargradient(spread:pad, x1:0.527773, y1:0, x2:0.517, y2:0.977409, stop:0 rgba(255, 183, 0, 255), stop:1 rgba(193, 148, 12, 255));\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.cp_1 = CustomPlotWidget(self.scrollAreaWidgetContents)
        self.cp_1.setObjectName(u"cp_1")
        self.cp_1.setMinimumSize(QSize(0, 50))

        self.verticalLayout_2.addWidget(self.cp_1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)

        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 0, 2, 1, 1)

        self.sl_r = QSlider(self.scrollAreaWidgetContents)
        self.sl_r.setObjectName(u"sl_r")
        self.sl_r.setMinimum(-255)
        self.sl_r.setMaximum(255)
        self.sl_r.setSingleStep(5)
        self.sl_r.setOrientation(Qt.Horizontal)
        self.sl_r.setInvertedAppearance(False)
        self.sl_r.setInvertedControls(False)
        self.sl_r.setTickPosition(QSlider.TicksBelow)
        self.sl_r.setTickInterval(10)

        self.gridLayout.addWidget(self.sl_r, 1, 0, 1, 1)

        self.sl_g = QSlider(self.scrollAreaWidgetContents)
        self.sl_g.setObjectName(u"sl_g")
        self.sl_g.setMinimum(-255)
        self.sl_g.setMaximum(255)
        self.sl_g.setSingleStep(5)
        self.sl_g.setOrientation(Qt.Horizontal)
        self.sl_g.setInvertedAppearance(False)
        self.sl_g.setInvertedControls(False)
        self.sl_g.setTickPosition(QSlider.TicksBelow)
        self.sl_g.setTickInterval(10)

        self.gridLayout.addWidget(self.sl_g, 1, 1, 1, 1)

        self.sl_b = QSlider(self.scrollAreaWidgetContents)
        self.sl_b.setObjectName(u"sl_b")
        self.sl_b.setMinimum(-255)
        self.sl_b.setMaximum(255)
        self.sl_b.setSingleStep(5)
        self.sl_b.setOrientation(Qt.Horizontal)
        self.sl_b.setInvertedAppearance(False)
        self.sl_b.setInvertedControls(False)
        self.sl_b.setTickPosition(QSlider.TicksBelow)
        self.sl_b.setTickInterval(10)

        self.gridLayout.addWidget(self.sl_b, 1, 2, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)

        self.label_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_6, 0, 1, 1, 1)

        self.cp_2 = CustomPlotWidget(self.scrollAreaWidgetContents)
        self.cp_2.setObjectName(u"cp_2")
        self.cp_2.setMinimumSize(QSize(0, 50))

        self.gridLayout_2.addWidget(self.cp_2, 1, 0, 1, 1)

        self.cp_3 = CustomPlotWidget(self.scrollAreaWidgetContents)
        self.cp_3.setObjectName(u"cp_3")
        self.cp_3.setMinimumSize(QSize(0, 50))

        self.gridLayout_2.addWidget(self.cp_3, 1, 1, 1, 1)

        self.label_7 = QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_7, 2, 0, 1, 1)

        self.label_8 = QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_8, 2, 1, 1, 1)

        self.cp_4 = CustomPlotWidget(self.scrollAreaWidgetContents)
        self.cp_4.setObjectName(u"cp_4")
        self.cp_4.setMinimumSize(QSize(0, 50))

        self.gridLayout_2.addWidget(self.cp_4, 3, 0, 1, 1)

        self.cp_5 = CustomPlotWidget(self.scrollAreaWidgetContents)
        self.cp_5.setObjectName(u"cp_5")
        self.cp_5.setMinimumSize(QSize(0, 50))

        self.gridLayout_2.addWidget(self.cp_5, 3, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(sim_U4_T2)

        QMetaObject.connectSlotsByName(sim_U4_T2)
    # setupUi

    def retranslateUi(self, sim_U4_T2):
        sim_U4_T2.setWindowTitle(QCoreApplication.translate("sim_U4_T2", u"Sim_U4_T2", None))
        self.label.setText(QCoreApplication.translate("sim_U4_T2", u"Espacios de Colores", None))
        self.label_2.setText(QCoreApplication.translate("sim_U4_T2", u"Componente Rojo", None))
        self.label_3.setText(QCoreApplication.translate("sim_U4_T2", u"Componente Verde", None))
        self.label_4.setText(QCoreApplication.translate("sim_U4_T2", u"Componente Azul", None))
        self.label_5.setText(QCoreApplication.translate("sim_U4_T2", u"Componente Rojo", None))
        self.label_6.setText(QCoreApplication.translate("sim_U4_T2", u"Componente Verde", None))
        self.label_7.setText(QCoreApplication.translate("sim_U4_T2", u"Componente Azul", None))
        self.label_8.setText(QCoreApplication.translate("sim_U4_T2", u"Imagen Escala de Grises", None))
    # retranslateUi

