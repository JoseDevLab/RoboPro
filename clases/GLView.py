from PySide6.QtWidgets import QFrame, QVBoxLayout
from PySide6.QtCore import QTimer
import pyqtgraph.opengl as gl

class GLView(QFrame):
    def __init__(self, parent=None):
        super(GLView, self).__init__(parent)

        # Configura el layout vertical
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0,0,0,0)
        self.setLayout(self.layout)

        # Crea el GLViewWidget
        self.glView = gl.GLViewWidget()
        self.layout.addWidget(self.glView)
        
        # cambia el color de fondo
        self.setBackgroundColor((0,0,0))
        
        # Mantener relación de aspecto
        self.heightScale = 1/2.1
        self.resizeEvent = self.escalarTamaio
        
    def showEvent(self, event):
        super().showEvent(event)
        self.glView.updateGeometry()
        
    def escalarTamaio(self, event=None):
        self.setMinimumHeight(int(self.width()*self.heightScale))
        
    def setBackgroundColor(self,color):
        self.glView.setBackgroundColor(color)