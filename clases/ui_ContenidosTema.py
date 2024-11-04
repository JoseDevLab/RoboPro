# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ContenidosTemaJDxGuS.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QSizePolicy, QTabWidget,
    QVBoxLayout, QWidget)

from clases.PdfView import PdfView

class Ui_contenidosTema(object):
    def setupUi(self, contenidosTema):
        if not contenidosTema.objectName():
            contenidosTema.setObjectName(u"contenidosTema")
        contenidosTema.resize(715, 485)
        self.verticalLayout = QVBoxLayout(contenidosTema)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(contenidosTema)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"QTabBar::tab {\n"
"width: 150px; /* Ajusta el ancho de las pesta\u00f1as seg\u00fan sea necesario */\n"
"}\n"
"\n"
"QTabWidget::pane { /* The tab widget frame */\n"
"    border-top: 0px solid #C2C7CB;  /*Lo hace invisible*/\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"	alignment: center;\n"
"}\n"
"\n"
"/* Style the tab using the tab sub-control. Note that\n"
"    it reads QTabBar _not_ QTabWidget */\n"
"QTabBar::tab {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"    border: 2px solid #C4C4C3;\n"
"    border-bottom-color: #C2C7CB; /* same as the pane color */\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"    min-width: 8ex;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #fafaf"
                        "a, stop: 0.4 #f4f4f4,\n"
"                                stop: 0.5 #e7e7e7, stop: 1.0 #fafafa);\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    border-color: #9B9B9B;\n"
"    border-bottom-color: #C2C7CB; /* same as pane color */\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    margin-top: 2px; /* make non-selected tabs look smaller */\n"
"}\n"
"\n"
"/* make use of negative margins for overlapping tabs */\n"
"QTabBar::tab:selected {\n"
"    /* expand/overlap to the left and right by 4px */\n"
"    margin-left: -4px;\n"
"    margin-right: -4px;\n"
"}\n"
"\n"
"QTabBar::tab:first:selected {\n"
"    margin-left: 0; /* the first selected tab has nothing to overlap with on the left */\n"
"}\n"
"\n"
"QTabBar::tab:last:selected {\n"
"    margin-right: 0; /* the last selected tab has nothing to overlap with on the right */\n"
"}\n"
"\n"
"QTabBar::tab:only-one {\n"
"    margin: 0; /* if there is only one tab, we don't want overlapping margins */\n"
"}\n"
"\n"
"/****QScrollBar Vertical****/\n"
"QScrollBar:vertical {\n"
" "
                        "   border: 2px solid rgb(218, 218, 218);\n"
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
"    background: rgb(218, 218, 218);\n"
"}\n"
"\n"
"\n"
"/****"
                        "QScrillBar horizontal****/\n"
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
"    background: rgb(218, 218, 218);\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrol"
                        "lBar::sub-page:horizontal {\n"
"    background: rgb(218, 218, 218);\n"
"}")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tab.setStyleSheet(u"background-color:None;")
        self.verticalLayout_2 = QVBoxLayout(self.tab)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pdfView = PdfView(self.tab)
        self.pdfView.setObjectName(u"pdfView")

        self.verticalLayout_2.addWidget(self.pdfView)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_3 = QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, -1, -1)
        self.frameVideo = QFrame(self.tab_2)
        self.frameVideo.setObjectName(u"frameVideo")
        self.frameVideo.setFrameShape(QFrame.StyledPanel)
        self.frameVideo.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.frameVideo)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.simLayout = QVBoxLayout(self.tab_3)
        self.simLayout.setSpacing(0)
        self.simLayout.setObjectName(u"simLayout")
        self.simLayout.setContentsMargins(0, 0, 0, 0)
        self.tabWidget.addTab(self.tab_3, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.retranslateUi(contenidosTema)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(contenidosTema)
    # setupUi

    def retranslateUi(self, contenidosTema):
        contenidosTema.setWindowTitle(QCoreApplication.translate("contenidosTema", u"contenidosTema", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("contenidosTema", u"Explicaci\u00f3n", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("contenidosTema", u"Videos", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("contenidosTema", u"Simulaci\u00f3n", None))
    # retranslateUi

