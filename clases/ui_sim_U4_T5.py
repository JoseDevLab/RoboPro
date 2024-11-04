# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sim_U4_T5zFSRiv.ui'
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
    QFrame, QHBoxLayout, QLabel, QScrollArea,
    QSizePolicy, QSlider, QSpacerItem, QVBoxLayout,
    QWidget)

from clases.PlotWidget import CustomPlotWidget

class Ui_sim_U4_T5(object):
    def setupUi(self, sim_U4_T5):
        if not sim_U4_T5.objectName():
            sim_U4_T5.setObjectName(u"sim_U4_T5")
        sim_U4_T5.resize(538, 430)
        sim_U4_T5.setStyleSheet(u"QWidget#sim_U4_T5,\n"
"QScrollArea#scrollArea{\n"
"background-color:rgba(0,0,0,0);\n"
"}")
        self.verticalLayout = QVBoxLayout(sim_U4_T5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(sim_U4_T5)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 536, 160))
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

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.cb_filtros = QComboBox(self.scrollAreaWidgetContents)
        self.cb_filtros.addItem("")
        self.cb_filtros.addItem("")
        self.cb_filtros.addItem("")
        self.cb_filtros.addItem("")
        self.cb_filtros.addItem("")
        self.cb_filtros.setObjectName(u"cb_filtros")

        self.horizontalLayout.addWidget(self.cb_filtros)

        self.fr_realce = QFrame(self.scrollAreaWidgetContents)
        self.fr_realce.setObjectName(u"fr_realce")
        self.fr_realce.setFrameShape(QFrame.StyledPanel)
        self.fr_realce.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.fr_realce)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.sb_realce = QDoubleSpinBox(self.fr_realce)
        self.sb_realce.setObjectName(u"sb_realce")
        self.sb_realce.setReadOnly(True)
        self.sb_realce.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.horizontalLayout_2.addWidget(self.sb_realce)

        self.sl_realce = QSlider(self.fr_realce)
        self.sl_realce.setObjectName(u"sl_realce")
        self.sl_realce.setMaximum(100)
        self.sl_realce.setSingleStep(5)
        self.sl_realce.setPageStep(10)
        self.sl_realce.setValue(50)
        self.sl_realce.setOrientation(Qt.Horizontal)

        self.horizontalLayout_2.addWidget(self.sl_realce)


        self.horizontalLayout.addWidget(self.fr_realce)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.cp_2 = CustomPlotWidget(self.scrollAreaWidgetContents)
        self.cp_2.setObjectName(u"cp_2")
        self.cp_2.setMinimumSize(QSize(0, 50))

        self.verticalLayout_2.addWidget(self.cp_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(sim_U4_T5)

        QMetaObject.connectSlotsByName(sim_U4_T5)
    # setupUi

    def retranslateUi(self, sim_U4_T5):
        sim_U4_T5.setWindowTitle(QCoreApplication.translate("sim_U4_T5", u"Sim_U4_T5", None))
        self.label.setText(QCoreApplication.translate("sim_U4_T5", u"Filtros", None))
        self.label_2.setText(QCoreApplication.translate("sim_U4_T5", u"Tipo de Filtro:", None))
        self.cb_filtros.setItemText(0, QCoreApplication.translate("sim_U4_T5", u"Media", None))
        self.cb_filtros.setItemText(1, QCoreApplication.translate("sim_U4_T5", u"Distribuci\u00f3n Gaussiana (3x3)", None))
        self.cb_filtros.setItemText(2, QCoreApplication.translate("sim_U4_T5", u"Distribuci\u00f3n Gaussiana (5x5)", None))
        self.cb_filtros.setItemText(3, QCoreApplication.translate("sim_U4_T5", u"Mediana", None))
        self.cb_filtros.setItemText(4, QCoreApplication.translate("sim_U4_T5", u"Realce (Sharpening)", None))

    # retranslateUi

