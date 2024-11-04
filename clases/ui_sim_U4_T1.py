# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sim_U4_T1frYDDy.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QScrollArea, QSizePolicy, QVBoxLayout, QWidget)

from clases.PlotWidget import CustomPlotWidget
from pyqtgraph import ImageView

class Ui_sim_U4_T1(object):
    def setupUi(self, sim_U4_T1):
        if not sim_U4_T1.objectName():
            sim_U4_T1.setObjectName(u"sim_U4_T1")
        sim_U4_T1.resize(548, 469)
        sim_U4_T1.setStyleSheet(u"QWidget#sim_U4_T1{\n"
"background-color:rgba(0,0,0,0);\n"
"}")
        self.verticalLayout = QVBoxLayout(sim_U4_T1)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(sim_U4_T1)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 529, 780))
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
"}\n"
"QPushButton{\n"
"font:16pt \"Britannic Bold\";\n"
"color:white;\n"
"background-color:rgba(0,51,102,200);\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(0,51,150,200);\n"
"}\n"
"QRadioButton,\n"
"QCheckBox{\n"
"color:white;\n"
"background-color:translucid;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)

        self.fr_imv = QFrame(self.scrollAreaWidgetContents)
        self.fr_imv.setObjectName(u"fr_imv")
        self.fr_imv.setMinimumSize(QSize(0, 600))
        self.fr_imv.setFrameShape(QFrame.StyledPanel)
        self.fr_imv.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.fr_imv)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.imv = ImageView(self.fr_imv)
        self.imv.setObjectName(u"imv")
        self.imv.setMinimumSize(QSize(0, 50))

        self.verticalLayout_2.addWidget(self.imv)


        self.verticalLayout_3.addWidget(self.fr_imv)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)

        self.cp_3 = CustomPlotWidget(self.scrollAreaWidgetContents)
        self.cp_3.setObjectName(u"cp_3")
        self.cp_3.setMinimumSize(QSize(0, 50))

        self.gridLayout.addWidget(self.cp_3, 3, 0, 1, 1)

        self.cp_1 = CustomPlotWidget(self.scrollAreaWidgetContents)
        self.cp_1.setObjectName(u"cp_1")
        self.cp_1.setMinimumSize(QSize(0, 50))

        self.gridLayout.addWidget(self.cp_1, 1, 0, 1, 1)

        self.cp_4 = CustomPlotWidget(self.scrollAreaWidgetContents)
        self.cp_4.setObjectName(u"cp_4")
        self.cp_4.setMinimumSize(QSize(0, 50))

        self.gridLayout.addWidget(self.cp_4, 3, 1, 1, 1)

        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.cp_2 = CustomPlotWidget(self.scrollAreaWidgetContents)
        self.cp_2.setObjectName(u"cp_2")
        self.cp_2.setMinimumSize(QSize(0, 50))

        self.gridLayout.addWidget(self.cp_2, 1, 1, 1, 1)

        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_5, 2, 1, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(sim_U4_T1)

        QMetaObject.connectSlotsByName(sim_U4_T1)
    # setupUi

    def retranslateUi(self, sim_U4_T1):
        sim_U4_T1.setWindowTitle(QCoreApplication.translate("sim_U4_T1", u"Sim_U4_T1", None))
        self.label.setText(QCoreApplication.translate("sim_U4_T1", u"Fundamentos de Visi\u00f3n Artificial", None))
        self.label_3.setText(QCoreApplication.translate("sim_U4_T1", u"Zoom Replicado", None))
        self.label_2.setText(QCoreApplication.translate("sim_U4_T1", u"Imagen Original", None))
        self.label_4.setText(QCoreApplication.translate("sim_U4_T1", u"Imagen Expandida", None))
        self.label_5.setText(QCoreApplication.translate("sim_U4_T1", u"Zoom Interpolado", None))
    # retranslateUi

