# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WebViewbHTmzC.ui'
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
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(579, 395)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setMinimumSize(QSize(0, 25))
        self.frame.setMaximumSize(QSize(16777215, 35))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(294, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.bt_Title_Page = QPushButton(self.frame)
        self.bt_Title_Page.setObjectName(u"bt_Title_Page")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.bt_Title_Page.sizePolicy().hasHeightForWidth())
        self.bt_Title_Page.setSizePolicy(sizePolicy2)
        self.bt_Title_Page.setLayoutDirection(Qt.RightToLeft)
        self.bt_Title_Page.setStyleSheet(u"QPushButton#bt_Title_Page{\n"
"font: 15pt \"Britannic Bold\";\n"
"color: white;\n"
"background-color:rgba(25, 25, 25,220);\n"
"border-radius:13px;\n"
"}\n"
"QPushButton#bt_Title_Page:hover{\n"
"background-color:rgba(15, 15, 15,250);\n"
"}")
        icon = QIcon()
        icon.addFile(u"resources/images/MainWindow/youtube.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_Title_Page.setIcon(icon)
        self.bt_Title_Page.setIconSize(QSize(35, 35))

        self.horizontalLayout.addWidget(self.bt_Title_Page)

        self.horizontalSpacer = QSpacerItem(294, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addWidget(self.frame)

        self.frame_webView = QFrame(Form)
        self.frame_webView.setObjectName(u"frame_webView")
        self.frame_webView.setFrameShape(QFrame.StyledPanel)
        self.frame_webView.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_webView)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.webEngineView = QWebEngineView(self.frame_webView)
        self.webEngineView.setObjectName(u"webEngineView")
        sizePolicy1.setHeightForWidth(self.webEngineView.sizePolicy().hasHeightForWidth())
        self.webEngineView.setSizePolicy(sizePolicy1)
        self.webEngineView.setUrl(QUrl(u"about:blank"))

        self.verticalLayout_2.addWidget(self.webEngineView)


        self.verticalLayout.addWidget(self.frame_webView)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.bt_Title_Page.setText("")
#if QT_CONFIG(shortcut)
        self.bt_Title_Page.setShortcut("")
#endif // QT_CONFIG(shortcut)
    # retranslateUi

