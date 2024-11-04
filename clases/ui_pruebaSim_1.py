# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pruebaSim_1qdgUbO.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_pruebaSim_1(object):
    def setupUi(self, pruebaSim_1):
        if not pruebaSim_1.objectName():
            pruebaSim_1.setObjectName(u"pruebaSim_1")
        pruebaSim_1.resize(1300, 700)
        self.centralwidget = QWidget(pruebaSim_1)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_2.addWidget(self.pushButton)

        self.tabWidget = QTabWidget(self.frame)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"\n"
"background-color:bkack;\n"
"")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.verticalLayout_3 = QVBoxLayout(self.tab_1)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_video = QFrame(self.tab_1)
        self.frame_video.setObjectName(u"frame_video")
        self.frame_video.setFrameShape(QFrame.StyledPanel)
        self.frame_video.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.frame_video)

        self.tabWidget.addTab(self.tab_1, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout_4 = QVBoxLayout(self.tab_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.tabWidget.addTab(self.tab_4, "")

        self.verticalLayout_2.addWidget(self.tabWidget)


        self.verticalLayout.addWidget(self.frame)

        pruebaSim_1.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(pruebaSim_1)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1300, 22))
        pruebaSim_1.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(pruebaSim_1)
        self.statusbar.setObjectName(u"statusbar")
        pruebaSim_1.setStatusBar(self.statusbar)

        self.retranslateUi(pruebaSim_1)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(pruebaSim_1)
    # setupUi

    def retranslateUi(self, pruebaSim_1):
        pruebaSim_1.setWindowTitle(QCoreApplication.translate("pruebaSim_1", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("pruebaSim_1", u"Retorno", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("pruebaSim_1", u"Teor\u00eda", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QCoreApplication.translate("pruebaSim_1", u"Videos", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("pruebaSim_1", u"Simulaci\u00f3n", None))
    # retranslateUi

