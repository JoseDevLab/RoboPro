# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'abstractVideosNybOmx.ui'
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

class Ui_abstractVideos(object):
    def setupUi(self, abstractVideos):
        if not abstractVideos.objectName():
            abstractVideos.setObjectName(u"abstractVideos")
        abstractVideos.resize(733, 474)
        icon = QIcon()
        icon.addFile(u"resources/images/icon.jpeg", QSize(), QIcon.Normal, QIcon.Off)
        abstractVideos.setWindowIcon(icon)
        abstractVideos.setStyleSheet(u"background-color:rgba(0,0,0,0);")
        self.centralwidget = QWidget(abstractVideos)
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
        self.layoutVideos = QVBoxLayout(self.scrollAreaWidgetContents)
        self.layoutVideos.setSpacing(0)
        self.layoutVideos.setObjectName(u"layoutVideos")
        self.layoutVideos.setContentsMargins(0, 0, 0, 0)
        self.video_1 = WebView(self.scrollAreaWidgetContents)
        self.video_1.setObjectName(u"video_1")
        self.video_1.setMinimumSize(QSize(0, 100))

        self.layoutVideos.addWidget(self.video_1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        abstractVideos.setCentralWidget(self.centralwidget)

        self.retranslateUi(abstractVideos)

        QMetaObject.connectSlotsByName(abstractVideos)
    # setupUi

    def retranslateUi(self, abstractVideos):
        abstractVideos.setWindowTitle(QCoreApplication.translate("abstractVideos", u"Videos", None))
    # retranslateUi
