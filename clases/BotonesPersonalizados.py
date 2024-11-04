from PySide6.QtWidgets import QPushButton, QVBoxLayout, QLabel
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QMovie

class AnimatedButton(QPushButton):
    def __init__(self, text='', parent=None):
        super(AnimatedButton, self).__init__(text, parent)

        # Establecer el fondo del botón como transparente
        # self.setStyleSheet("background-color: transparent;")

        # Configurar un QLabel interno para mostrar el GIF animado
        self.gif_label = QLabel(self)
        self.gif_label.setAlignment(Qt.AlignCenter)
        self.gif_label.setStyleSheet("QLabel {background-color: transparent;}")  # Fondo transparente
        self.movie = None
        
        # Layout para organizar el QLabel y el QPushButton
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.gif_label)
        self.layout.addWidget(self, alignment=Qt.AlignCenter)
        self.layout.setContentsMargins(1,1,1,1)
        
        
    def enterEvent(self, event):
        if self.movie != None:
            self.movie.start()
        
    def leaveEvent(self, event):
        if self.movie != None:
            self.movie.stop()
            self.movie.jumpToFrame(0)
        
    def setGifFileName(self, fileName:str):
        self.movie = QMovie(fileName)
        self.gif_label.setMovie(self.movie)
        self.movie.jumpToFrame(0)
        
        # Se captura la relación de aspecto del gif cargado
        gifSize = self.movie.frameRect().size()
        self.heightScale = gifSize.height()/gifSize.width()
        
    def resizeEvent(self, event):
        if self.movie != None:
            width = self.width()
            height = int(width*self.heightScale)
            self.movie.setScaledSize(QSize(width,height))
            self.movie.start()
            self.movie.stop()