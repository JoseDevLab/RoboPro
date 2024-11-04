from PySide6.QtWidgets import QDialog, QFileDialog, QDialogButtonBox
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtCore import QPoint, QStandardPaths, Signal, QSize
from clases.ui_Personalizar import Ui_Personalizar
from typing import Optional

class Personalizar(QDialog, Ui_Personalizar):
    
    actualizarAceptado = Signal(str,str,bool)
    
    def __init__(self,mainWindow):
        super().__init__()
        self.setupUi(self)
        self.photo_url = 'sinCambio'
        self.esFoto = False
        
        self.bt_foto.setIcon(mainWindow.fotoPerfil)
        self.le_userName.setText(mainWindow.lb_userName.text())
        
        self.bt_avatar_1.clicked.connect(self.selectAvatar_1)
        self.bt_avatar_2.clicked.connect(self.selectAvatar_2)
        self.bt_avatar_3.clicked.connect(self.selectAvatar_3)
        self.bt_avatar_4.clicked.connect(self.selectAvatar_4)
        self.bt_avatar_5.clicked.connect(self.selectAvatar_5)
        self.bt_avatar_6.clicked.connect(self.selectAvatar_6)
        self.bt_avatar_7.clicked.connect(self.selectAvatar_7)
        self.bt_avatar_8.clicked.connect(self.selectAvatar_8)
        self.bt_avatar_9.clicked.connect(self.selectAvatar_9)
        self.bt_avatar_10.clicked.connect(self.selectAvatar_10)
        self.bt_avatar_0.clicked.connect(self.selectAvatar_0)
        self.bt_subirFoto.clicked.connect(self.subirFoto)
        self.buttonBox.accepted.connect(self.actualizarPerfil)
        self.actualizarAceptado.connect(mainWindow.actualizarPerfil)
        self.le_userName.textEdited.connect(lambda text:self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(True))
        
        # Se cambian los textos de los botones 'Ok' y 'Cancel'
        self.buttonBox.button(QDialogButtonBox.Ok).setText('Actualizar')
        self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)
        self.buttonBox.button(QDialogButtonBox.Cancel).setText('Cancelar')
        
    def selectAvatar_1(self):
        icon = QIcon()
        icon.addFile("resources/images/MainWindow/perfiles/avatar_1.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_foto.setIcon(icon)
        self.photo_url='https://1'
        self.esFoto = False
        self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(True)
    def selectAvatar_2(self):
        icon = QIcon()
        icon.addFile("resources/images/MainWindow/perfiles/avatar_2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_foto.setIcon(icon)
        self.photo_url='https://2'
        self.esFoto = False
        self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(True)
    def selectAvatar_3(self):
        icon = QIcon()
        icon.addFile("resources/images/MainWindow/perfiles/avatar_3.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_foto.setIcon(icon)
        self.photo_url='https://3'
        self.esFoto = False
        self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(True)
    def selectAvatar_4(self):
        icon = QIcon()
        icon.addFile("resources/images/MainWindow/perfiles/avatar_4.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_foto.setIcon(icon)
        self.photo_url='https://4'
        self.esFoto = False
        self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(True)
    def selectAvatar_5(self):
        icon = QIcon()
        icon.addFile("resources/images/MainWindow/perfiles/avatar_5.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_foto.setIcon(icon)
        self.photo_url='https://5'
        self.esFoto = False
        self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(True)
    def selectAvatar_6(self):
        icon = QIcon()
        icon.addFile("resources/images/MainWindow/perfiles/avatar_6.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_foto.setIcon(icon)
        self.photo_url='https://6'
        self.esFoto = False
        self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(True)
    def selectAvatar_7(self):
        icon = QIcon()
        icon.addFile("resources/images/MainWindow/perfiles/avatar_7.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_foto.setIcon(icon)
        self.photo_url='https://7'
        self.esFoto = False
        self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(True)
    def selectAvatar_8(self):
        icon = QIcon()
        icon.addFile("resources/images/MainWindow/perfiles/avatar_8.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_foto.setIcon(icon)
        self.photo_url='https://8'
        self.esFoto = False
        self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(True)
    def selectAvatar_9(self):
        icon = QIcon()
        icon.addFile("resources/images/MainWindow/perfiles/avatar_9.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_foto.setIcon(icon)
        self.photo_url='https://9'
        self.esFoto = False
        self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(True)
    def selectAvatar_10(self):
        icon = QIcon()
        icon.addFile("resources/images/MainWindow/perfiles/avatar_10.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_foto.setIcon(icon)
        self.photo_url='https://10'
        self.esFoto = False
        self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(True)
    def selectAvatar_0(self):
        icon = QIcon()
        icon.addFile("resources/images/MainWindow/perfiles/avatar_0.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_foto.setIcon(icon)
        self.photo_url='https://0'
        self.esFoto = False
        self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(True)
        
    def subirFoto(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, 
            "Abrir archivo", 
            QStandardPaths.writableLocation(QStandardPaths.DocumentsLocation), 
            "Todos los archivos soportados (*.jpg *.jpeg *.png *.svg);;Archivos JPEG (*.jpg *.jpeg);;Archivos PNG (*.png);;Archivos SVG (*.svg)"
        )
        if file_path!='':
            icon = QIcon()
            icon.addFile(file_path, QSize(), QIcon.Normal, QIcon.Off)
            self.bt_foto.setIcon(icon)
            self.photo_url = file_path
            self.esFoto = True
            self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(True)
        
    def actualizarPerfil(self):
        self.actualizarAceptado.emit(self.photo_url,self.le_userName.text(),self.esFoto)
        