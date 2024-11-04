# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sim_U2_T8Jewkmz.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QScrollArea, QSizePolicy, QSpacerItem,
    QSpinBox, QVBoxLayout, QWidget)

from clases.PlotWidget import CustomPlotWidget

class Ui_sim_U2_T8(object):
    def setupUi(self, sim_U2_T8):
        if not sim_U2_T8.objectName():
            sim_U2_T8.setObjectName(u"sim_U2_T8")
        sim_U2_T8.resize(484, 434)
        sim_U2_T8.setStyleSheet(u"QWidget#sim_U2_T8{\n"
"background-color:rgba(0,0,0,0);\n"
"}")
        self.verticalLayout = QVBoxLayout(sim_U2_T8)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(sim_U2_T8)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 482, 281))
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
"}")
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.label_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"font:10pt \"Britannic Bold\";\n"
"color:rgb(186, 186, 186);")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_6)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.sb_nPuntos = QSpinBox(self.scrollAreaWidgetContents)
        self.sb_nPuntos.setObjectName(u"sb_nPuntos")
        self.sb_nPuntos.setMinimum(5)
        self.sb_nPuntos.setMaximum(999)
        self.sb_nPuntos.setSingleStep(10)
        self.sb_nPuntos.setValue(200)

        self.gridLayout.addWidget(self.sb_nPuntos, 0, 1, 1, 1)

        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)

        self.sb_vMax = QSpinBox(self.scrollAreaWidgetContents)
        self.sb_vMax.setObjectName(u"sb_vMax")
        self.sb_vMax.setMinimum(5)
        self.sb_vMax.setMaximum(999)
        self.sb_vMax.setSingleStep(10)
        self.sb_vMax.setValue(180)

        self.gridLayout.addWidget(self.sb_vMax, 0, 3, 1, 1)

        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.sb_a = QSpinBox(self.scrollAreaWidgetContents)
        self.sb_a.setObjectName(u"sb_a")
        self.sb_a.setMinimum(5)
        self.sb_a.setMaximum(999)
        self.sb_a.setSingleStep(10)
        self.sb_a.setValue(180)

        self.gridLayout.addWidget(self.sb_a, 1, 1, 1, 1)

        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_5, 1, 2, 1, 1)

        self.cb_tipoT = QComboBox(self.scrollAreaWidgetContents)
        self.cb_tipoT.addItem("")
        self.cb_tipoT.addItem("")
        self.cb_tipoT.setObjectName(u"cb_tipoT")

        self.gridLayout.addWidget(self.cb_tipoT, 1, 3, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.cp_p = CustomPlotWidget(self.scrollAreaWidgetContents)
        self.cp_p.setObjectName(u"cp_p")
        self.cp_p.setMinimumSize(QSize(0, 50))

        self.verticalLayout_2.addWidget(self.cp_p)

        self.cp_v = CustomPlotWidget(self.scrollAreaWidgetContents)
        self.cp_v.setObjectName(u"cp_v")
        self.cp_v.setMinimumSize(QSize(0, 50))

        self.verticalLayout_2.addWidget(self.cp_v)

        self.cp_a = CustomPlotWidget(self.scrollAreaWidgetContents)
        self.cp_a.setObjectName(u"cp_a")
        self.cp_a.setMinimumSize(QSize(0, 50))

        self.verticalLayout_2.addWidget(self.cp_a)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(sim_U2_T8)

        QMetaObject.connectSlotsByName(sim_U2_T8)
    # setupUi

    def retranslateUi(self, sim_U2_T8):
        sim_U2_T8.setWindowTitle(QCoreApplication.translate("sim_U2_T8", u"Sim_U2_T8", None))
        self.label.setText(QCoreApplication.translate("sim_U2_T8", u"Interpolador Trapezoidal", None))
        self.label_6.setText(QCoreApplication.translate("sim_U2_T8", u"Mueva los puntos del gr\u00e1fico haciendo clic y arrastrando.", None))
        self.label_2.setText(QCoreApplication.translate("sim_U2_T8", u"Cantidad de Puntos", None))
        self.label_3.setText(QCoreApplication.translate("sim_U2_T8", u"Velocidad M\u00e1xima", None))
        self.sb_vMax.setSuffix(QCoreApplication.translate("sim_U2_T8", u"\u00b0/s", None))
        self.label_4.setText(QCoreApplication.translate("sim_U2_T8", u"Aceleraci\u00f3n", None))
        self.sb_a.setSuffix(QCoreApplication.translate("sim_U2_T8", u"\u00b0/s^2", None))
        self.label_5.setText(QCoreApplication.translate("sim_U2_T8", u"Tiempo de Recorrido", None))
        self.cb_tipoT.setItemText(0, QCoreApplication.translate("sim_U2_T8", u"M\u00ednimo Posible", None))
        self.cb_tipoT.setItemText(1, QCoreApplication.translate("sim_U2_T8", u"Definido por Usuario", None))

    # retranslateUi

