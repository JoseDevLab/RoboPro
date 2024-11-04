# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sim_U1_T1JfIIdT.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QSpinBox,
    QVBoxLayout, QWidget)

from clases.CustomTable import CustomTable

class Ui_sim_U1_T1(object):
    def setupUi(self, sim_U1_T1):
        if not sim_U1_T1.objectName():
            sim_U1_T1.setObjectName(u"sim_U1_T1")
        sim_U1_T1.resize(653, 575)
        sim_U1_T1.setStyleSheet(u"QWidget{\n"
"background-color:rgba(0,0,0,0);\n"
"}")
        self.verticalLayout = QVBoxLayout(sim_U1_T1)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(sim_U1_T1)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 651, 505))
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
        self.verticalLayout_13 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font:20pt \"Britannic Bold\";")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label)

        self.label_15 = QLabel(self.scrollAreaWidgetContents)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"font:10pt \"Britannic Bold\";\n"
"color:rgb(186, 186, 186);")
        self.label_15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_15)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_5)

        self.sb_n = QSpinBox(self.scrollAreaWidgetContents)
        self.sb_n.setObjectName(u"sb_n")
        self.sb_n.setStyleSheet(u"color:white;\n"
"background-color:translucid;")
        self.sb_n.setMinimum(1)
        self.sb_n.setValue(2)

        self.horizontalLayout.addWidget(self.sb_n)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_13.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_4 = QSpacerItem(5000, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_10 = QSpacerItem(1000, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_10)

        self.tb_par = CustomTable(self.scrollAreaWidgetContents)
        self.tb_par.setObjectName(u"tb_par")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tb_par.sizePolicy().hasHeightForWidth())
        self.tb_par.setSizePolicy(sizePolicy1)
        self.tb_par.setMinimumSize(QSize(50, 50))
        self.tb_par.setStyleSheet(u"QFrame{\n"
"background-color:translucid;\n"
"color:white;\n"
"}\n"
"QTableWidget::item { \n"
"border: 1px solid rgb(80, 80, 80); \n"
"}")

        self.horizontalLayout_5.addWidget(self.tb_par)

        self.horizontalSpacer_9 = QSpacerItem(1000, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_9)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.verticalSpacer_8 = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_8)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_7 = QSpacerItem(1000, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_7)

        self.tb_jrj = CustomTable(self.scrollAreaWidgetContents)
        self.tb_jrj.setObjectName(u"tb_jrj")
        sizePolicy1.setHeightForWidth(self.tb_jrj.sizePolicy().hasHeightForWidth())
        self.tb_jrj.setSizePolicy(sizePolicy1)
        self.tb_jrj.setMinimumSize(QSize(50, 50))
        self.tb_jrj.setStyleSheet(u"QFrame{\n"
"background-color:translucid;\n"
"color:white;\n"
"}\n"
"QTableWidget::item { \n"
"border: 1px solid rgb(80, 80, 80); \n"
"}")

        self.horizontalLayout_4.addWidget(self.tb_jrj)

        self.horizontalSpacer_8 = QSpacerItem(1000, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_8)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_5 = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_5)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_4)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_12 = QSpacerItem(1000, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_12)

        self.tb_g = CustomTable(self.scrollAreaWidgetContents)
        self.tb_g.setObjectName(u"tb_g")
        sizePolicy1.setHeightForWidth(self.tb_g.sizePolicy().hasHeightForWidth())
        self.tb_g.setSizePolicy(sizePolicy1)
        self.tb_g.setMinimumSize(QSize(50, 50))
        self.tb_g.setStyleSheet(u"QFrame{\n"
"background-color:translucid;\n"
"color:white;\n"
"}\n"
"QTableWidget::item { \n"
"border: 1px solid rgb(80, 80, 80); \n"
"}")

        self.horizontalLayout_6.addWidget(self.tb_g)

        self.horizontalSpacer_11 = QSpacerItem(1000, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_11)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.verticalSpacer_6 = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_6)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.horizontalSpacer_3 = QSpacerItem(5000, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.verticalLayout_13.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(38, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_13.addItem(self.verticalSpacer)

        self.bt_ejecutar = QPushButton(self.scrollAreaWidgetContents)
        self.bt_ejecutar.setObjectName(u"bt_ejecutar")
        self.bt_ejecutar.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_ejecutar.setStyleSheet(u"QPushButton{\n"
"font:16pt \"Britannic Bold\";\n"
"color:white;\n"
"background-color:rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(255,255,255,50);\n"
"}")

        self.verticalLayout_13.addWidget(self.bt_ejecutar)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_6 = QSpacerItem(5000, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_13 = QSpacerItem(200, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_13)

        self.tb_fuerzas = CustomTable(self.scrollAreaWidgetContents)
        self.tb_fuerzas.setObjectName(u"tb_fuerzas")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tb_fuerzas.sizePolicy().hasHeightForWidth())
        self.tb_fuerzas.setSizePolicy(sizePolicy2)
        self.tb_fuerzas.setMinimumSize(QSize(50, 50))
        self.tb_fuerzas.setStyleSheet(u"QFrame{\n"
"background-color:translucid;\n"
"color:white;\n"
"}\n"
"QTableWidget::item { \n"
"border: 1px solid rgb(80, 80, 80); \n"
"}")

        self.horizontalLayout_7.addWidget(self.tb_fuerzas)

        self.horizontalSpacer_14 = QSpacerItem(200, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_14)


        self.verticalLayout_5.addLayout(self.horizontalLayout_7)


        self.horizontalLayout_3.addLayout(self.verticalLayout_5)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalSpacer_2 = QSpacerItem(20, 25, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_10.addItem(self.verticalSpacer_2)

        self.label_7 = QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName(u"label_7")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy3)
        self.label_7.setStyleSheet(u"font: 16pt \"Adobe Devanagari\";")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_7)


        self.horizontalLayout_3.addLayout(self.verticalLayout_10)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_8 = QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_8)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_16 = QSpacerItem(200, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_16)

        self.tb_D = CustomTable(self.scrollAreaWidgetContents)
        self.tb_D.setObjectName(u"tb_D")
        sizePolicy2.setHeightForWidth(self.tb_D.sizePolicy().hasHeightForWidth())
        self.tb_D.setSizePolicy(sizePolicy2)
        self.tb_D.setMinimumSize(QSize(50, 50))
        self.tb_D.setStyleSheet(u"QFrame{\n"
"background-color:translucid;\n"
"color:white;\n"
"}\n"
"QTableWidget::item { \n"
"border: 1px solid rgb(80, 80, 80); \n"
"}")

        self.horizontalLayout_8.addWidget(self.tb_D)

        self.horizontalSpacer_15 = QSpacerItem(200, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_15)


        self.verticalLayout_6.addLayout(self.horizontalLayout_8)


        self.horizontalLayout_3.addLayout(self.verticalLayout_6)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalSpacer_7 = QSpacerItem(20, 25, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_14.addItem(self.verticalSpacer_7)

        self.label_14 = QLabel(self.scrollAreaWidgetContents)
        self.label_14.setObjectName(u"label_14")
        sizePolicy3.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy3)
        self.label_14.setStyleSheet(u"font: 16pt \"Adobe Devanagari\";")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_14)


        self.horizontalLayout_3.addLayout(self.verticalLayout_14)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_9 = QLabel(self.scrollAreaWidgetContents)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_9)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_17 = QSpacerItem(200, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_17)

        self.tb_ddq = CustomTable(self.scrollAreaWidgetContents)
        self.tb_ddq.setObjectName(u"tb_ddq")
        sizePolicy2.setHeightForWidth(self.tb_ddq.sizePolicy().hasHeightForWidth())
        self.tb_ddq.setSizePolicy(sizePolicy2)
        self.tb_ddq.setMinimumSize(QSize(50, 50))
        self.tb_ddq.setStyleSheet(u"QFrame{\n"
"background-color:translucid;\n"
"color:white;\n"
"}\n"
"QTableWidget::item { \n"
"border: 1px solid rgb(80, 80, 80); \n"
"}")

        self.horizontalLayout_9.addWidget(self.tb_ddq)

        self.horizontalSpacer_18 = QSpacerItem(200, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_18)


        self.verticalLayout_7.addLayout(self.horizontalLayout_9)


        self.horizontalLayout_3.addLayout(self.verticalLayout_7)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalSpacer_3 = QSpacerItem(20, 25, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_11.addItem(self.verticalSpacer_3)

        self.label_12 = QLabel(self.scrollAreaWidgetContents)
        self.label_12.setObjectName(u"label_12")
        sizePolicy3.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy3)
        self.label_12.setStyleSheet(u"font: 16pt \"Adobe Devanagari\";")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_12)


        self.horizontalLayout_3.addLayout(self.verticalLayout_11)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_10 = QLabel(self.scrollAreaWidgetContents)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer_20 = QSpacerItem(200, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_20)

        self.tb_H = CustomTable(self.scrollAreaWidgetContents)
        self.tb_H.setObjectName(u"tb_H")
        sizePolicy2.setHeightForWidth(self.tb_H.sizePolicy().hasHeightForWidth())
        self.tb_H.setSizePolicy(sizePolicy2)
        self.tb_H.setMinimumSize(QSize(50, 50))
        self.tb_H.setStyleSheet(u"QFrame{\n"
"background-color:translucid;\n"
"color:white;\n"
"}\n"
"QTableWidget::item { \n"
"border: 1px solid rgb(80, 80, 80); \n"
"}")

        self.horizontalLayout_11.addWidget(self.tb_H)

        self.horizontalSpacer_19 = QSpacerItem(200, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_19)


        self.verticalLayout_8.addLayout(self.horizontalLayout_11)


        self.horizontalLayout_3.addLayout(self.verticalLayout_8)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalSpacer_4 = QSpacerItem(20, 25, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_12.addItem(self.verticalSpacer_4)

        self.label_13 = QLabel(self.scrollAreaWidgetContents)
        self.label_13.setObjectName(u"label_13")
        sizePolicy3.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy3)
        self.label_13.setStyleSheet(u"font: 16pt \"Adobe Devanagari\";")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_13)


        self.horizontalLayout_3.addLayout(self.verticalLayout_12)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_11 = QLabel(self.scrollAreaWidgetContents)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalSpacer_22 = QSpacerItem(200, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_22)

        self.tb_C = CustomTable(self.scrollAreaWidgetContents)
        self.tb_C.setObjectName(u"tb_C")
        sizePolicy2.setHeightForWidth(self.tb_C.sizePolicy().hasHeightForWidth())
        self.tb_C.setSizePolicy(sizePolicy2)
        self.tb_C.setMinimumSize(QSize(50, 50))
        self.tb_C.setStyleSheet(u"QFrame{\n"
"background-color:translucid;\n"
"color:white;\n"
"}\n"
"QTableWidget::item { \n"
"border: 1px solid rgb(80, 80, 80); \n"
"}")

        self.horizontalLayout_12.addWidget(self.tb_C)

        self.horizontalSpacer_21 = QSpacerItem(200, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_21)


        self.verticalLayout_9.addLayout(self.horizontalLayout_12)


        self.horizontalLayout_3.addLayout(self.verticalLayout_9)

        self.horizontalSpacer_5 = QSpacerItem(5000, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)


        self.verticalLayout_13.addLayout(self.horizontalLayout_3)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(sim_U1_T1)

        QMetaObject.connectSlotsByName(sim_U1_T1)
    # setupUi

    def retranslateUi(self, sim_U1_T1):
        sim_U1_T1.setWindowTitle(QCoreApplication.translate("sim_U1_T1", u"sim_U1_T1", None))
        self.label.setText(QCoreApplication.translate("sim_U1_T1", u"Algoritmo computacional \n"
"de Lagrange-Euler", None))
        self.label_15.setText(QCoreApplication.translate("sim_U1_T1", u"En los par\u00e1metros de D_H los \u00e1ngulos deben estar expresados en \n"
"radianes y las variables articulares de la forma q1, q2, q3, ...etc. \n"
"Ademas verifique que la celda (n,4) sea igal a 0\n"
"\n"
"En la matriz de centros de masas, cada columna debe contener \n"
"las coordenadas X, Y y Z de los centros de masas de cada eslab\u00f3n, \n"
"con respecto a su sistema de referencia solidario.\n"
"\n"
"En el vector de gravedad, deben digitarse las componentes X, Y y Z \n"
"de la gravedad con respecto al sistema 0 del robot.", None))
        self.label_5.setText(QCoreApplication.translate("sim_U1_T1", u"N\u00famero de grados de libertad", None))
        self.label_2.setText(QCoreApplication.translate("sim_U1_T1", u"Par\u00e1metros \n"
"D-H del robot", None))
        self.label_3.setText(QCoreApplication.translate("sim_U1_T1", u"Centros de masa \n"
"de eslab\u00f3nes", None))
        self.label_4.setText(QCoreApplication.translate("sim_U1_T1", u"Vector \n"
"gravedad", None))
        self.bt_ejecutar.setText(QCoreApplication.translate("sim_U1_T1", u"Ejecutar algoritmo", None))
        self.label_6.setText(QCoreApplication.translate("sim_U1_T1", u"F/T", None))
        self.label_7.setText(QCoreApplication.translate("sim_U1_T1", u"=", None))
        self.label_8.setText(QCoreApplication.translate("sim_U1_T1", u"Matriz D", None))
        self.label_14.setText(QCoreApplication.translate("sim_U1_T1", u"x", None))
        self.label_9.setText(QCoreApplication.translate("sim_U1_T1", u"ddq", None))
        self.label_12.setText(QCoreApplication.translate("sim_U1_T1", u"+", None))
        self.label_10.setText(QCoreApplication.translate("sim_U1_T1", u"Matriz H", None))
        self.label_13.setText(QCoreApplication.translate("sim_U1_T1", u"+", None))
        self.label_11.setText(QCoreApplication.translate("sim_U1_T1", u"Matriz C", None))
    # retranslateUi

