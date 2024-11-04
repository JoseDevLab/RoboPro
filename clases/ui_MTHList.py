# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MTHListjrLpIn.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QScrollArea, QSizePolicy,
    QSpacerItem, QWidget)

class Ui_MTHList(object):
    def setupUi(self, MTHList):
        if not MTHList.objectName():
            MTHList.setObjectName(u"MTHList")
        MTHList.resize(662, 224)
        self.horizontalLayout = QHBoxLayout(MTHList)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(MTHList)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 660, 222))
        self.layout = QHBoxLayout(self.scrollAreaWidgetContents)
        self.layout.setObjectName(u"layout")
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layout.addItem(self.horizontalSpacer_2)

        self.layoutMTH = QHBoxLayout()
        self.layoutMTH.setObjectName(u"layoutMTH")

        self.layout.addLayout(self.layoutMTH)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layout.addItem(self.horizontalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout.addWidget(self.scrollArea)


        self.retranslateUi(MTHList)

        QMetaObject.connectSlotsByName(MTHList)
    # setupUi

    def retranslateUi(self, MTHList):
        MTHList.setWindowTitle(QCoreApplication.translate("MTHList", u"MTHList", None))
    # retranslateUi

