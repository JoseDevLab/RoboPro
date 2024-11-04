# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PdfViewqkSJrs.ui'
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
from PySide6.QtPdfWidgets import QPdfView
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QFrame, QHBoxLayout,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QVBoxLayout, QWidget)

from clases.zoomselector import ZoomSelector

class Ui_PdfView(object):
    def setupUi(self, PdfView):
        if not PdfView.objectName():
            PdfView.setObjectName(u"PdfView")
        PdfView.resize(616, 527)
        PdfView.setStyleSheet(u"QFrame{\n"
"background-color:rgb(160, 160, 160);\n"
"}\n"
"\n"
"QPdfView{\n"
"background-color:rgba(0,0,0,0);\n"
"}\n"
"\n"
"QMessageBox QFrame{\n"
"background-color:rgba(255,255,255,255);\n"
"color:black;\n"
"}\n"
"QMessageBox QPushButton{\n"
"color:black;\n"
"}")
        self.verticalLayout = QVBoxLayout(PdfView)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(PdfView)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QSize(0, 0))
        self.frame_2.setStyleSheet(u"QFrame#frame_2{\n"
"background-color:rgba(0,0,0,0);\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(146, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame#frame{\n"
"background-color:rgba(0,0,0,0);\n"
"border-radius:10px\n"
"}\n"
"QFrame#controlPdf, \n"
"QFrame#controlPdf QFrame{\n"
"background-color:rgba(173, 51, 51,255);\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.controlPdf = QFrame(self.frame)
        self.controlPdf.setObjectName(u"controlPdf")
        sizePolicy.setHeightForWidth(self.controlPdf.sizePolicy().hasHeightForWidth())
        self.controlPdf.setSizePolicy(sizePolicy)
        self.controlPdf.setMinimumSize(QSize(0, 20))
        self.controlPdf.setMaximumSize(QSize(16777215, 20))
        self.controlPdf.setStyleSheet(u"QFrame#controlPdf{\n"
"border-radius:10px\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color:rgba(0,0,0,0);\n"
"color:black;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgba(255,255,255,25);\n"
"}\n"
"\n"
"QMessageBox QFrame{\n"
"background-color:rgba(255,255,255,255);\n"
"color:black;\n"
"}\n"
"QMessageBox QPushButton,\n"
"QMessageBox QPushButton:hover{\n"
"background-color:None;\n"
"color:black;\n"
"}")
        self.controlPdf.setFrameShape(QFrame.StyledPanel)
        self.controlPdf.setFrameShadow(QFrame.Raised)
        self.controlesLayout = QHBoxLayout(self.controlPdf)
        self.controlesLayout.setSpacing(0)
        self.controlesLayout.setObjectName(u"controlesLayout")
        self.controlesLayout.setContentsMargins(0, 0, 0, 0)
        self.actionZoom_Out = QPushButton(self.controlPdf)
        self.actionZoom_Out.setObjectName(u"actionZoom_Out")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.actionZoom_Out.sizePolicy().hasHeightForWidth())
        self.actionZoom_Out.setSizePolicy(sizePolicy1)
        self.actionZoom_Out.setMinimumSize(QSize(35, 0))
        icon = QIcon()
        icon.addFile(u"resources/images/MainWindow/zoom-out.svgz", QSize(), QIcon.Normal, QIcon.Off)
        self.actionZoom_Out.setIcon(icon)
        self.actionZoom_Out.setIconSize(QSize(20, 20))

        self.controlesLayout.addWidget(self.actionZoom_Out)

        self.m_zoomSelector = ZoomSelector(self.controlPdf)
        self.m_zoomSelector.setObjectName(u"m_zoomSelector")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.m_zoomSelector.sizePolicy().hasHeightForWidth())
        self.m_zoomSelector.setSizePolicy(sizePolicy2)
        self.m_zoomSelector.setStyleSheet(u"")

        self.controlesLayout.addWidget(self.m_zoomSelector)

        self.actionZoom_In = QPushButton(self.controlPdf)
        self.actionZoom_In.setObjectName(u"actionZoom_In")
        sizePolicy1.setHeightForWidth(self.actionZoom_In.sizePolicy().hasHeightForWidth())
        self.actionZoom_In.setSizePolicy(sizePolicy1)
        self.actionZoom_In.setMinimumSize(QSize(35, 0))
        icon1 = QIcon()
        icon1.addFile(u"resources/images/MainWindow/zoom-in.svgz", QSize(), QIcon.Normal, QIcon.Off)
        self.actionZoom_In.setIcon(icon1)
        self.actionZoom_In.setIconSize(QSize(20, 20))

        self.controlesLayout.addWidget(self.actionZoom_In)

        self.line_2 = QFrame(self.controlPdf)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.controlesLayout.addWidget(self.line_2)

        self.bt_descargar = QPushButton(self.controlPdf)
        self.bt_descargar.setObjectName(u"bt_descargar")
        self.bt_descargar.setCursor(QCursor(Qt.PointingHandCursor))

        self.controlesLayout.addWidget(self.bt_descargar)

        self.line = QFrame(self.controlPdf)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.controlesLayout.addWidget(self.line)

        self.actionBack = QPushButton(self.controlPdf)
        self.actionBack.setObjectName(u"actionBack")
        self.actionBack.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.actionBack.sizePolicy().hasHeightForWidth())
        self.actionBack.setSizePolicy(sizePolicy1)
        self.actionBack.setMinimumSize(QSize(35, 0))
        icon2 = QIcon()
        icon2.addFile(u"resources/images/MainWindow/go-previous-view-page.svgz", QSize(), QIcon.Normal, QIcon.Off)
        self.actionBack.setIcon(icon2)
        self.actionBack.setIconSize(QSize(20, 20))

        self.controlesLayout.addWidget(self.actionBack)

        self.m_pageSelector = QSpinBox(self.controlPdf)
        self.m_pageSelector.setObjectName(u"m_pageSelector")
        self.m_pageSelector.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.m_pageSelector.sizePolicy().hasHeightForWidth())
        self.m_pageSelector.setSizePolicy(sizePolicy1)
        self.m_pageSelector.setMinimumSize(QSize(70, 0))
        self.m_pageSelector.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.m_pageSelector.setAccelerated(False)
        self.m_pageSelector.setMinimum(1)
        self.m_pageSelector.setMaximum(99)
        self.m_pageSelector.setSingleStep(1)
        self.m_pageSelector.setDisplayIntegerBase(10)

        self.controlesLayout.addWidget(self.m_pageSelector)

        self.actionForward = QPushButton(self.controlPdf)
        self.actionForward.setObjectName(u"actionForward")
        self.actionForward.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.actionForward.sizePolicy().hasHeightForWidth())
        self.actionForward.setSizePolicy(sizePolicy1)
        self.actionForward.setMinimumSize(QSize(35, 0))
        icon3 = QIcon()
        icon3.addFile(u"resources/images/MainWindow/go-next-view-page.svgz", QSize(), QIcon.Normal, QIcon.Off)
        self.actionForward.setIcon(icon3)
        self.actionForward.setIconSize(QSize(20, 20))

        self.controlesLayout.addWidget(self.actionForward)


        self.verticalLayout_2.addWidget(self.controlPdf)


        self.horizontalLayout_2.addWidget(self.frame)

        self.horizontalSpacer_2 = QSpacerItem(146, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.frame_2)

        self.pdfView = QPdfView(PdfView)
        self.pdfView.setObjectName(u"pdfView")
        self.pdfView.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.pdfView)


        self.retranslateUi(PdfView)

        QMetaObject.connectSlotsByName(PdfView)
    # setupUi

    def retranslateUi(self, PdfView):
        PdfView.setWindowTitle(QCoreApplication.translate("PdfView", u"PDF Viewer", None))
        self.actionZoom_Out.setText("")
        self.actionZoom_In.setText("")
        self.bt_descargar.setText(QCoreApplication.translate("PdfView", u"Descargar PDF", None))
        self.actionBack.setText("")
        self.m_pageSelector.setSuffix("")
        self.m_pageSelector.setPrefix(QCoreApplication.translate("PdfView", u"P\u00e1gina ", None))
        self.actionForward.setText("")
    # retranslateUi

