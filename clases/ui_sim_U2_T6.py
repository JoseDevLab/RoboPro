# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sim_U2_T6gFWuHI.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QScrollArea,
    QSizePolicy, QSpacerItem, QSpinBox, QVBoxLayout,
    QWidget)

from clases.PlotWidget import CustomPlotWidget

class Ui_sim_U2_T6(object):
    def setupUi(self, sim_U2_T6):
        if not sim_U2_T6.objectName():
            sim_U2_T6.setObjectName(u"sim_U2_T6")
        sim_U2_T6.resize(614, 475)
        sim_U2_T6.setStyleSheet(u"QWidget#sim_U2_T6{\n"
"background-color:rgba(0,0,0,0);\n"
"}")
        self.verticalLayout = QVBoxLayout(sim_U2_T6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(sim_U2_T6)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 612, 210))
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

        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font:10pt \"Britannic Bold\";\n"
"color:rgb(186, 186, 186);")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.sb_nPuntos = QSpinBox(self.scrollAreaWidgetContents)
        self.sb_nPuntos.setObjectName(u"sb_nPuntos")
        self.sb_nPuntos.setMinimum(5)
        self.sb_nPuntos.setMaximum(999)
        self.sb_nPuntos.setValue(80)

        self.horizontalLayout.addWidget(self.sb_nPuntos)

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

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(sim_U2_T6)

        QMetaObject.connectSlotsByName(sim_U2_T6)
    # setupUi

    def retranslateUi(self, sim_U2_T6):
        sim_U2_T6.setWindowTitle(QCoreApplication.translate("sim_U2_T6", u"Sim_U2_T6", None))
        self.label.setText(QCoreApplication.translate("sim_U2_T6", u"Interpolador Lineal", None))
        self.label_3.setText(QCoreApplication.translate("sim_U2_T6", u"Mueve los puntos del gr\u00e1fico haciendo clic y arrastrando.\n"
" Agrega mas puntos haciendo clic sobre las lineas.", None))
        self.label_2.setText(QCoreApplication.translate("sim_U2_T6", u"Cantidad de Puntos", None))
    # retranslateUi

