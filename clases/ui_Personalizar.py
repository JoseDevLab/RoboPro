# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PersonalizarqJxfGY.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Personalizar(object):
    def setupUi(self, Personalizar):
        if not Personalizar.objectName():
            Personalizar.setObjectName(u"Personalizar")
        Personalizar.setWindowModality(Qt.WindowModal)
        Personalizar.setEnabled(True)
        Personalizar.resize(482, 721)
        icon = QIcon()
        icon.addFile(u"resources/images/icon.jpeg", QSize(), QIcon.Normal, QIcon.Off)
        Personalizar.setWindowIcon(icon)
        Personalizar.setSizeGripEnabled(False)
        Personalizar.setModal(False)
        self.verticalLayout_2 = QVBoxLayout(Personalizar)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Personalizar)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame#frame{\n"
"background-image: url(resources/images/resized_background.png);\n"
"}\n"
"QPushButton{\n"
"background-color:rgba(218,218,218,100);\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(0, 51, 102,150)\n"
"}\n"
"QPushButton#bt_foto{\n"
"background-color:rgba(218,218,218,0);\n"
"}\n"
"QPushButton#bt_foto:hover{\n"
"background-color:rgba(0, 51, 102,100)\n"
"}\n"
"\n"
"QDialogButtonBox QPushButton{\n"
"background-color:None\n"
"}\n"
"QDialogButtonBox QPushButton:hover{\n"
"background-color:None\n"
"}\n"
"\n"
"QLineEdit{\n"
"	background-color: rgba(0, 0, 0, 200);\n"
"	border-radius: 10px;\n"
"	font: 12pt \"Arial\";\n"
"	color: rgb(255, 255, 254);\n"
"	border: 2px solid rgb(255, 255, 255)\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	background-color: rgba(0, 0, 0, 200);\n"
"	border-radius: 10px;\n"
"	font: 12pt \"Arial\";\n"
"	border: 2px solid rgb(0, 51, 102)\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	background-color: rgb(0, 0, 0);\n"
"	border-radius: 10px;\n"
"	font: 12pt \"Arial\";\n"
"	border: 2px solid rg"
                        "b(173, 51, 51);\n"
"}\n"
"QLabel{\n"
"	color: rgb(255, 255, 254);\n"
"	font: 12pt \"Arial\";\n"
"	background-color: rgba(0, 0, 0, 200);\n"
"	border-radius:10px\n"
"}\n"
"QLabel#titulo{\n"
"	color: rgb(255, 255, 254);\n"
"	font: 700 14pt \"Arial\";\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.titulo = QLabel(self.frame)
        self.titulo.setObjectName(u"titulo")
        self.titulo.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.titulo)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.bt_foto = QPushButton(self.frame)
        self.bt_foto.setObjectName(u"bt_foto")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bt_foto.sizePolicy().hasHeightForWidth())
        self.bt_foto.setSizePolicy(sizePolicy)
        icon1 = QIcon()
        icon1.addFile(u"resources/images/MainWindow/perfiles/avatar_0.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_foto.setIcon(icon1)
        self.bt_foto.setIconSize(QSize(200, 200))

        self.horizontalLayout.addWidget(self.bt_foto)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.le_userName = QLineEdit(self.frame)
        self.le_userName.setObjectName(u"le_userName")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.le_userName.sizePolicy().hasHeightForWidth())
        self.le_userName.setSizePolicy(sizePolicy1)
        self.le_userName.setMinimumSize(QSize(200, 30))
        self.le_userName.setFocusPolicy(Qt.ClickFocus)
        self.le_userName.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.le_userName)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_7)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_4)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_8)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.bt_avatar_5 = QPushButton(self.frame)
        self.bt_avatar_5.setObjectName(u"bt_avatar_5")
        sizePolicy.setHeightForWidth(self.bt_avatar_5.sizePolicy().hasHeightForWidth())
        self.bt_avatar_5.setSizePolicy(sizePolicy)
        icon2 = QIcon()
        icon2.addFile(u"resources/images/MainWindow/perfiles/avatar_5.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_avatar_5.setIcon(icon2)
        self.bt_avatar_5.setIconSize(QSize(100, 100))

        self.gridLayout.addWidget(self.bt_avatar_5, 1, 1, 1, 1)

        self.bt_avatar_8 = QPushButton(self.frame)
        self.bt_avatar_8.setObjectName(u"bt_avatar_8")
        sizePolicy.setHeightForWidth(self.bt_avatar_8.sizePolicy().hasHeightForWidth())
        self.bt_avatar_8.setSizePolicy(sizePolicy)
        icon3 = QIcon()
        icon3.addFile(u"resources/images/MainWindow/perfiles/avatar_8.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_avatar_8.setIcon(icon3)
        self.bt_avatar_8.setIconSize(QSize(100, 100))

        self.gridLayout.addWidget(self.bt_avatar_8, 2, 0, 1, 1)

        self.bt_avatar_0 = QPushButton(self.frame)
        self.bt_avatar_0.setObjectName(u"bt_avatar_0")
        sizePolicy.setHeightForWidth(self.bt_avatar_0.sizePolicy().hasHeightForWidth())
        self.bt_avatar_0.setSizePolicy(sizePolicy)
        self.bt_avatar_0.setIcon(icon1)
        self.bt_avatar_0.setIconSize(QSize(100, 100))

        self.gridLayout.addWidget(self.bt_avatar_0, 2, 3, 1, 1)

        self.bt_avatar_1 = QPushButton(self.frame)
        self.bt_avatar_1.setObjectName(u"bt_avatar_1")
        sizePolicy.setHeightForWidth(self.bt_avatar_1.sizePolicy().hasHeightForWidth())
        self.bt_avatar_1.setSizePolicy(sizePolicy)
        icon4 = QIcon()
        icon4.addFile(u"resources/images/MainWindow/perfiles/avatar_1.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_avatar_1.setIcon(icon4)
        self.bt_avatar_1.setIconSize(QSize(100, 100))

        self.gridLayout.addWidget(self.bt_avatar_1, 0, 1, 1, 1)

        self.bt_avatar_7 = QPushButton(self.frame)
        self.bt_avatar_7.setObjectName(u"bt_avatar_7")
        sizePolicy.setHeightForWidth(self.bt_avatar_7.sizePolicy().hasHeightForWidth())
        self.bt_avatar_7.setSizePolicy(sizePolicy)
        icon5 = QIcon()
        icon5.addFile(u"resources/images/MainWindow/perfiles/avatar_7.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_avatar_7.setIcon(icon5)
        self.bt_avatar_7.setIconSize(QSize(100, 100))

        self.gridLayout.addWidget(self.bt_avatar_7, 1, 3, 1, 1)

        self.bt_avatar_2 = QPushButton(self.frame)
        self.bt_avatar_2.setObjectName(u"bt_avatar_2")
        sizePolicy.setHeightForWidth(self.bt_avatar_2.sizePolicy().hasHeightForWidth())
        self.bt_avatar_2.setSizePolicy(sizePolicy)
        icon6 = QIcon()
        icon6.addFile(u"resources/images/MainWindow/perfiles/avatar_2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_avatar_2.setIcon(icon6)
        self.bt_avatar_2.setIconSize(QSize(100, 100))

        self.gridLayout.addWidget(self.bt_avatar_2, 0, 2, 1, 1)

        self.bt_avatar_9 = QPushButton(self.frame)
        self.bt_avatar_9.setObjectName(u"bt_avatar_9")
        sizePolicy.setHeightForWidth(self.bt_avatar_9.sizePolicy().hasHeightForWidth())
        self.bt_avatar_9.setSizePolicy(sizePolicy)
        icon7 = QIcon()
        icon7.addFile(u"resources/images/MainWindow/perfiles/avatar_9.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_avatar_9.setIcon(icon7)
        self.bt_avatar_9.setIconSize(QSize(100, 100))

        self.gridLayout.addWidget(self.bt_avatar_9, 2, 1, 1, 1)

        self.bt_avatar_3 = QPushButton(self.frame)
        self.bt_avatar_3.setObjectName(u"bt_avatar_3")
        sizePolicy.setHeightForWidth(self.bt_avatar_3.sizePolicy().hasHeightForWidth())
        self.bt_avatar_3.setSizePolicy(sizePolicy)
        icon8 = QIcon()
        icon8.addFile(u"resources/images/MainWindow/perfiles/avatar_3.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_avatar_3.setIcon(icon8)
        self.bt_avatar_3.setIconSize(QSize(100, 100))

        self.gridLayout.addWidget(self.bt_avatar_3, 0, 3, 1, 1)

        self.bt_avatar_4 = QPushButton(self.frame)
        self.bt_avatar_4.setObjectName(u"bt_avatar_4")
        sizePolicy.setHeightForWidth(self.bt_avatar_4.sizePolicy().hasHeightForWidth())
        self.bt_avatar_4.setSizePolicy(sizePolicy)
        icon9 = QIcon()
        icon9.addFile(u"resources/images/MainWindow/perfiles/avatar_4.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_avatar_4.setIcon(icon9)
        self.bt_avatar_4.setIconSize(QSize(100, 100))

        self.gridLayout.addWidget(self.bt_avatar_4, 1, 0, 1, 1)

        self.bt_avatar_10 = QPushButton(self.frame)
        self.bt_avatar_10.setObjectName(u"bt_avatar_10")
        sizePolicy.setHeightForWidth(self.bt_avatar_10.sizePolicy().hasHeightForWidth())
        self.bt_avatar_10.setSizePolicy(sizePolicy)
        icon10 = QIcon()
        icon10.addFile(u"resources/images/MainWindow/perfiles/avatar_10.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_avatar_10.setIcon(icon10)
        self.bt_avatar_10.setIconSize(QSize(100, 100))

        self.gridLayout.addWidget(self.bt_avatar_10, 2, 2, 1, 1)

        self.bt_subirFoto = QPushButton(self.frame)
        self.bt_subirFoto.setObjectName(u"bt_subirFoto")
        sizePolicy.setHeightForWidth(self.bt_subirFoto.sizePolicy().hasHeightForWidth())
        self.bt_subirFoto.setSizePolicy(sizePolicy)
        icon11 = QIcon()
        icon11.addFile(u"resources/images/MainWindow/upload.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_subirFoto.setIcon(icon11)
        self.bt_subirFoto.setIconSize(QSize(100, 100))

        self.gridLayout.addWidget(self.bt_subirFoto, 0, 0, 1, 1)

        self.bt_avatar_6 = QPushButton(self.frame)
        self.bt_avatar_6.setObjectName(u"bt_avatar_6")
        sizePolicy.setHeightForWidth(self.bt_avatar_6.sizePolicy().hasHeightForWidth())
        self.bt_avatar_6.setSizePolicy(sizePolicy)
        icon12 = QIcon()
        icon12.addFile(u"resources/images/MainWindow/perfiles/avatar_6.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_avatar_6.setIcon(icon12)
        self.bt_avatar_6.setIconSize(QSize(100, 100))

        self.gridLayout.addWidget(self.bt_avatar_6, 1, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.buttonBox = QDialogButtonBox(self.frame)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setLocale(QLocale(QLocale.Spanish, QLocale.Colombia))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.verticalLayout_2.addWidget(self.frame)


        self.retranslateUi(Personalizar)
        self.buttonBox.accepted.connect(Personalizar.accept)
        self.buttonBox.rejected.connect(Personalizar.reject)

        QMetaObject.connectSlotsByName(Personalizar)
    # setupUi

    def retranslateUi(self, Personalizar):
        Personalizar.setWindowTitle(QCoreApplication.translate("Personalizar", u"Personalizar", None))
        self.titulo.setText(QCoreApplication.translate("Personalizar", u"Personaliza tu perfil", None))
        self.bt_foto.setText("")
        self.label_3.setText(QCoreApplication.translate("Personalizar", u" Elige un nombre para mostrar ", None))
        self.label_4.setText(QCoreApplication.translate("Personalizar", u" Elige una foto de perfil ", None))
#if QT_CONFIG(tooltip)
        self.bt_avatar_5.setToolTip(QCoreApplication.translate("Personalizar", u"Avatar 5", None))
#endif // QT_CONFIG(tooltip)
        self.bt_avatar_5.setText("")
#if QT_CONFIG(tooltip)
        self.bt_avatar_8.setToolTip(QCoreApplication.translate("Personalizar", u"Avatar 8", None))
#endif // QT_CONFIG(tooltip)
        self.bt_avatar_8.setText("")
#if QT_CONFIG(tooltip)
        self.bt_avatar_0.setToolTip(QCoreApplication.translate("Personalizar", u"Sin avatar", None))
#endif // QT_CONFIG(tooltip)
        self.bt_avatar_0.setText("")
#if QT_CONFIG(tooltip)
        self.bt_avatar_1.setToolTip(QCoreApplication.translate("Personalizar", u"Avatar 1", None))
#endif // QT_CONFIG(tooltip)
        self.bt_avatar_1.setText("")
#if QT_CONFIG(tooltip)
        self.bt_avatar_7.setToolTip(QCoreApplication.translate("Personalizar", u"Avatar 7", None))
#endif // QT_CONFIG(tooltip)
        self.bt_avatar_7.setText("")
#if QT_CONFIG(tooltip)
        self.bt_avatar_2.setToolTip(QCoreApplication.translate("Personalizar", u"Avatar 2", None))
#endif // QT_CONFIG(tooltip)
        self.bt_avatar_2.setText("")
#if QT_CONFIG(tooltip)
        self.bt_avatar_9.setToolTip(QCoreApplication.translate("Personalizar", u"Avatar 9", None))
#endif // QT_CONFIG(tooltip)
        self.bt_avatar_9.setText("")
#if QT_CONFIG(tooltip)
        self.bt_avatar_3.setToolTip(QCoreApplication.translate("Personalizar", u"Avatar 3", None))
#endif // QT_CONFIG(tooltip)
        self.bt_avatar_3.setText("")
#if QT_CONFIG(tooltip)
        self.bt_avatar_4.setToolTip(QCoreApplication.translate("Personalizar", u"Avatar 4", None))
#endif // QT_CONFIG(tooltip)
        self.bt_avatar_4.setText("")
#if QT_CONFIG(tooltip)
        self.bt_avatar_10.setToolTip(QCoreApplication.translate("Personalizar", u"Avatar 10", None))
#endif // QT_CONFIG(tooltip)
        self.bt_avatar_10.setText("")
#if QT_CONFIG(tooltip)
        self.bt_subirFoto.setToolTip(QCoreApplication.translate("Personalizar", u"Subir foto", None))
#endif // QT_CONFIG(tooltip)
        self.bt_subirFoto.setText("")
#if QT_CONFIG(tooltip)
        self.bt_avatar_6.setToolTip(QCoreApplication.translate("Personalizar", u"Avatar 6", None))
#endif // QT_CONFIG(tooltip)
        self.bt_avatar_6.setText("")
    # retranslateUi

