# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ejemplo_pdfViewWFsJMW.ui'
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenuBar, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

from clases.PdfView import PdfView

class Ui_Ejemplo_pdfView(object):
    def setupUi(self, Ejemplo_pdfView):
        if not Ejemplo_pdfView.objectName():
            Ejemplo_pdfView.setObjectName(u"Ejemplo_pdfView")
        Ejemplo_pdfView.resize(692, 468)
        self.centralwidget = QWidget(Ejemplo_pdfView)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pdfView_1 = PdfView(self.centralwidget)
        self.pdfView_1.setObjectName(u"pdfView_1")

        self.verticalLayout.addWidget(self.pdfView_1)

        Ejemplo_pdfView.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Ejemplo_pdfView)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 692, 22))
        Ejemplo_pdfView.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Ejemplo_pdfView)
        self.statusbar.setObjectName(u"statusbar")
        Ejemplo_pdfView.setStatusBar(self.statusbar)

        self.retranslateUi(Ejemplo_pdfView)

        QMetaObject.connectSlotsByName(Ejemplo_pdfView)
    # setupUi

    def retranslateUi(self, Ejemplo_pdfView):
        Ejemplo_pdfView.setWindowTitle(QCoreApplication.translate("Ejemplo_pdfView", u"Ejemplo PDF View", None))
    # retranslateUi

