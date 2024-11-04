# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'v_U1_T1ImKYIc.ui'
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QScrollArea, QSizePolicy,
    QVBoxLayout, QWidget)

from clases.WebView import WebView

class Ui_v_U1_T1(object):
    def setupUi(self, v_U1_T1):
        if not v_U1_T1.objectName():
            v_U1_T1.setObjectName(u"v_U1_T1")
        v_U1_T1.resize(733, 474)
        v_U1_T1.setStyleSheet(u"background-color:rgba(0,0,0,0);")
        self.centralwidget = QWidget(v_U1_T1)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"/****QScrollBar Vertical****/\n"
"QScrollBar:vertical {\n"
"    border: 2px solid rgb(218, 218, 218);\n"
"    background: rgb(239, 184, 16);\n"
"    width: 17px;\n"
"    margin: 22px 0 22px 0;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background: rgb(0, 51, 102);\n"
"    min-height: 20px;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"    border: 2px solid rgba(173, 51, 51,255);\n"
"    background: rgb(0, 51, 102);\n"
"    height: 20px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    border: 2px solid rgba(173, 51, 51,255);\n"
"    background: rgb(0, 51, 102);\n"
"    height: 20px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    border: 2px solid rgb(239, 184, 16);\n"
"    width: 3px;\n"
"    height: 3px;\n"
"    background: rgb(218, 218, 218);\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
""
                        "    background: rgb(218, 218, 218);\n"
"}\n"
"\n"
"\n"
"/****QScrillBar horizontal****/\n"
"QScrollBar:horizontal {\n"
"    border: 2px solid rgb(218, 218, 218);\n"
"    background: rgb(218, 218, 218);\n"
"    height: 17px;\n"
"    margin: 0px 22px 0 22px;\n"
"}        \n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(0, 51, 102);\n"
"    min-width: 20px;\n"
"}        \n"
"QScrollBar::add-line:horizontal {\n"
"    border: 2px solid rgba(173, 51, 51,255);\n"
"    background: rgb(0, 51, 102);\n"
"    width: 20px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: 2px solid rgba(173, 51, 51,255);\n"
"    background: rgb(0, 51, 102);\n"
"    width: 20px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar:left-arrow:horizontal, QScrollBar::right-arrow:horizontal {\n"
"    border: 2px solid rgb(239, 184, 16);\n"
"    width: 3px;\n"
"    height: 3px;\n"
"    background: rgb(218, 218,"
                        " 218);\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"    background: rgb(218, 218, 218);\n"
"}")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 731, 100))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setStyleSheet(u"")
        self.layoutContents = QVBoxLayout(self.scrollAreaWidgetContents)
        self.layoutContents.setSpacing(0)
        self.layoutContents.setObjectName(u"layoutContents")
        self.layoutContents.setContentsMargins(0, 0, 0, 0)
        self.video_1 = WebView(self.scrollAreaWidgetContents)
        self.video_1.setObjectName(u"video_1")
        self.video_1.setMinimumSize(QSize(0, 100))

        self.layoutContents.addWidget(self.video_1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        v_U1_T1.setCentralWidget(self.centralwidget)

        self.retranslateUi(v_U1_T1)

        QMetaObject.connectSlotsByName(v_U1_T1)
    # setupUi

    def retranslateUi(self, v_U1_T1):
        v_U1_T1.setWindowTitle(QCoreApplication.translate("v_U1_T1", u"v_U1_T1", None))
    # retranslateUi

