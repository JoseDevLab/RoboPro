# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sim_U2_T7iSBAOo.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QScrollArea, QSizePolicy, QSpacerItem, QSpinBox,
    QVBoxLayout, QWidget)

from clases.PlotWidget import CustomPlotWidget

class Ui_sim_U2_T7(object):
    def setupUi(self, sim_U2_T7):
        if not sim_U2_T7.objectName():
            sim_U2_T7.setObjectName(u"sim_U2_T7")
        sim_U2_T7.resize(477, 516)
        sim_U2_T7.setStyleSheet(u"QWidget#sim_U2_T7{\n"
"background-color:rgba(0,0,0,0);\n"
"}")
        self.verticalLayout = QVBoxLayout(sim_U2_T7)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(sim_U2_T7)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 475, 306))
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
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font:10pt \"Britannic Bold\";\n"
"color:rgb(186, 186, 186);")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_2)

        self.sb_nPuntos = QSpinBox(self.scrollAreaWidgetContents)
        self.sb_nPuntos.setObjectName(u"sb_nPuntos")
        self.sb_nPuntos.setMaximum(999)
        self.sb_nPuntos.setValue(500)

        self.horizontalLayout.addWidget(self.sb_nPuntos)

        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_3)

        self.cb_velocidades = QComboBox(self.scrollAreaWidgetContents)
        self.cb_velocidades.addItem("")
        self.cb_velocidades.addItem("")
        self.cb_velocidades.addItem("")
        self.cb_velocidades.setObjectName(u"cb_velocidades")

        self.horizontalLayout.addWidget(self.cb_velocidades)

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

        self.cp_sa = CustomPlotWidget(self.scrollAreaWidgetContents)
        self.cp_sa.setObjectName(u"cp_sa")
        self.cp_sa.setMinimumSize(QSize(0, 50))

        self.verticalLayout_2.addWidget(self.cp_sa)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(sim_U2_T7)

        self.cb_velocidades.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(sim_U2_T7)
    # setupUi

    def retranslateUi(self, sim_U2_T7):
        sim_U2_T7.setWindowTitle(QCoreApplication.translate("sim_U2_T7", u"Sim_U2_T7", None))
        self.label.setText(QCoreApplication.translate("sim_U2_T7", u"Interpolador C\u00fabico", None))
        self.label_4.setText(QCoreApplication.translate("sim_U2_T7", u"Mueve los puntos del gr\u00e1fico haciendo clic y arrastrando.\n"
" Agrega mas puntos haciendo clic sobre las lineas.", None))
        self.label_2.setText(QCoreApplication.translate("sim_U2_T7", u"Cantid de Puntos:", None))
        self.label_3.setText(QCoreApplication.translate("sim_U2_T7", u"Velocidades:", None))
        self.cb_velocidades.setItemText(0, QCoreApplication.translate("sim_U2_T7", u"Dadas por Usuario", None))
        self.cb_velocidades.setItemText(1, QCoreApplication.translate("sim_U2_T7", u"Por Criterio Heur\u00edstico", None))
        self.cb_velocidades.setItemText(2, QCoreApplication.translate("sim_U2_T7", u"Por Igualaci\u00f3n de Aceleraciones", None))

    # retranslateUi

