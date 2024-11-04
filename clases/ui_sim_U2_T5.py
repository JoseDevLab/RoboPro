# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sim_U2_T5YtYhlr.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

from clases.CustomTable import CustomTable
from clases.GLView import GLView
from clases.PlotWidget import CustomPlotWidget

class Ui_sim_U2_T5(object):
    def setupUi(self, sim_U2_T5):
        if not sim_U2_T5.objectName():
            sim_U2_T5.setObjectName(u"sim_U2_T5")
        sim_U2_T5.resize(547, 523)
        sim_U2_T5.setStyleSheet(u"QWidget#sim_U2_T5{\n"
"background-color:rgba(0,0,0,0);\n"
"}")
        self.verticalLayout = QVBoxLayout(sim_U2_T5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(sim_U2_T5)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 545, 460))
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
"QPushButton{\n"
"font:16pt \"Britannic Bold\";\n"
"color:white;\n"
"background-color:rgba(0,51,102,200);\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(0,51,150,200);\n"
"}\n"
"QTableWidget {\n"
"selection-background-color: black;\n"
"}\n"
"QHeaderView::section {\n"
"background-color: #CCCCCC;\n"
"padding: 4px;\n"
"border: 1px solid #000000;\n"
"font-size: 10pt;\n"
"}\n"
"QTableWidget::item {\n"
"background-color: black;\n"
"color: white;\n"
"border: 1px solid rgb(80, 80, 80); \n"
"}\n"
"QTableWidget::item:selected {\n"
"background-color: rgb(0,51,112);\n"
"}\n"
"QTableWidget QWidget{\n"
"background-color: rgb(173,51,51);\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.ct_puntos = CustomTable(self.scrollAreaWidgetContents)
        self.ct_puntos.setObjectName(u"ct_puntos")
        self.ct_puntos.setMinimumSize(QSize(50, 50))

        self.horizontalLayout_4.addWidget(self.ct_puntos)

        self.lb_flecha = QLabel(self.scrollAreaWidgetContents)
        self.lb_flecha.setObjectName(u"lb_flecha")
        self.lb_flecha.setMinimumSize(QSize(20, 0))

        self.horizontalLayout_4.addWidget(self.lb_flecha)

        self.ct_Qs = CustomTable(self.scrollAreaWidgetContents)
        self.ct_Qs.setObjectName(u"ct_Qs")
        self.ct_Qs.setMinimumSize(QSize(50, 50))

        self.horizontalLayout_4.addWidget(self.ct_Qs)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.frame = QFrame(self.scrollAreaWidgetContents)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.cb_tipoTrayec = QComboBox(self.frame)
        self.cb_tipoTrayec.addItem("")
        self.cb_tipoTrayec.addItem("")
        self.cb_tipoTrayec.setObjectName(u"cb_tipoTrayec")

        self.horizontalLayout_2.addWidget(self.cb_tipoTrayec)


        self.horizontalLayout_3.addWidget(self.frame)

        self.fr_tipoMovimiento = QFrame(self.scrollAreaWidgetContents)
        self.fr_tipoMovimiento.setObjectName(u"fr_tipoMovimiento")
        self.fr_tipoMovimiento.setFrameShape(QFrame.StyledPanel)
        self.fr_tipoMovimiento.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.fr_tipoMovimiento)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.fr_tipoMovimiento)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_3)

        self.cb_tipoMov = QComboBox(self.fr_tipoMovimiento)
        self.cb_tipoMov.addItem("")
        self.cb_tipoMov.addItem("")
        self.cb_tipoMov.addItem("")
        self.cb_tipoMov.setObjectName(u"cb_tipoMov")

        self.horizontalLayout.addWidget(self.cb_tipoMov)


        self.horizontalLayout_3.addWidget(self.fr_tipoMovimiento)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.bt_generarTrayec = QPushButton(self.scrollAreaWidgetContents)
        self.bt_generarTrayec.setObjectName(u"bt_generarTrayec")

        self.verticalLayout_2.addWidget(self.bt_generarTrayec)

        self.cp_q_1 = CustomPlotWidget(self.scrollAreaWidgetContents)
        self.cp_q_1.setObjectName(u"cp_q_1")
        self.cp_q_1.setMinimumSize(QSize(0, 50))

        self.verticalLayout_2.addWidget(self.cp_q_1)

        self.cp_q_2 = CustomPlotWidget(self.scrollAreaWidgetContents)
        self.cp_q_2.setObjectName(u"cp_q_2")
        self.cp_q_2.setMinimumSize(QSize(0, 50))

        self.verticalLayout_2.addWidget(self.cp_q_2)

        self.cp_q_3 = CustomPlotWidget(self.scrollAreaWidgetContents)
        self.cp_q_3.setObjectName(u"cp_q_3")
        self.cp_q_3.setMinimumSize(QSize(0, 50))

        self.verticalLayout_2.addWidget(self.cp_q_3)

        self.cp_q_4 = CustomPlotWidget(self.scrollAreaWidgetContents)
        self.cp_q_4.setObjectName(u"cp_q_4")
        self.cp_q_4.setMinimumSize(QSize(0, 50))

        self.verticalLayout_2.addWidget(self.cp_q_4)

        self.bt_iniciarAnimacion = QPushButton(self.scrollAreaWidgetContents)
        self.bt_iniciarAnimacion.setObjectName(u"bt_iniciarAnimacion")
        self.bt_iniciarAnimacion.setEnabled(False)

        self.verticalLayout_2.addWidget(self.bt_iniciarAnimacion)

        self.gv_1 = GLView(self.scrollAreaWidgetContents)
        self.gv_1.setObjectName(u"gv_1")
        self.gv_1.setMinimumSize(QSize(0, 50))

        self.verticalLayout_2.addWidget(self.gv_1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(sim_U2_T5)

        QMetaObject.connectSlotsByName(sim_U2_T5)
    # setupUi

    def retranslateUi(self, sim_U2_T5):
        sim_U2_T5.setWindowTitle(QCoreApplication.translate("sim_U2_T5", u"Sim_U2_T5", None))
        self.label.setText(QCoreApplication.translate("sim_U2_T5", u"Generaci\u00f3n de Trayectorias Cartesianas", None))
        self.lb_flecha.setText("")
        self.label_2.setText(QCoreApplication.translate("sim_U2_T5", u"Tipo de Trayectoria:", None))
        self.cb_tipoTrayec.setItemText(0, QCoreApplication.translate("sim_U2_T5", u"Punto a Punto", None))
        self.cb_tipoTrayec.setItemText(1, QCoreApplication.translate("sim_U2_T5", u"Continua", None))

        self.label_3.setText(QCoreApplication.translate("sim_U2_T5", u"Tipo de Movimiento:", None))
        self.cb_tipoMov.setItemText(0, QCoreApplication.translate("sim_U2_T5", u"Eje a Eje", None))
        self.cb_tipoMov.setItemText(1, QCoreApplication.translate("sim_U2_T5", u"Ejes Simultaneos", None))
        self.cb_tipoMov.setItemText(2, QCoreApplication.translate("sim_U2_T5", u"Ejes Coordinados", None))

        self.bt_generarTrayec.setText(QCoreApplication.translate("sim_U2_T5", u"Generar Trayectoria", None))
        self.bt_iniciarAnimacion.setText(QCoreApplication.translate("sim_U2_T5", u"Iniciar Animaci\u00f3n", None))
    # retranslateUi

