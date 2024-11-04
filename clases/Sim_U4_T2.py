from PySide6.QtWidgets import QWidget
from clases.ui_sim_U4_T2 import Ui_sim_U4_T2
from PIL import Image
from scipy.signal import convolve2d
from numpy import array,clip, zeros, uint8, stack
from pyqtgraph import ImageItem

class Sim_U4_T2(QWidget,Ui_sim_U4_T2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
    def init(self):
        # Invertir el eje Y de los PlotWidget
        self.cp_1.plotWidget.getPlotItem().invertY()
        self.cp_2.plotWidget.getPlotItem().invertY()
        self.cp_3.plotWidget.getPlotItem().invertY()
        self.cp_4.plotWidget.getPlotItem().invertY()
        self.cp_5.plotWidget.getPlotItem().invertY()
        # Bloquear la relación de aspecto de los ejes a 1:1
        self.cp_1.plotWidget.getPlotItem().setAspectLocked(ratio=1)
        self.cp_2.plotWidget.getPlotItem().setAspectLocked(ratio=1)
        self.cp_3.plotWidget.getPlotItem().setAspectLocked(ratio=1)
        self.cp_4.plotWidget.getPlotItem().setAspectLocked(ratio=1)
        self.cp_5.plotWidget.getPlotItem().setAspectLocked(ratio=1)
        # Ocultar ambos ejes
        self.cp_1.plotWidget.getPlotItem().hideAxis('bottom')
        self.cp_1.plotWidget.getPlotItem().hideAxis('left')
        self.cp_2.plotWidget.getPlotItem().hideAxis('bottom')
        self.cp_2.plotWidget.getPlotItem().hideAxis('left')
        self.cp_3.plotWidget.getPlotItem().hideAxis('bottom')
        self.cp_3.plotWidget.getPlotItem().hideAxis('left')
        self.cp_4.plotWidget.getPlotItem().hideAxis('bottom')
        self.cp_4.plotWidget.getPlotItem().hideAxis('left')
        self.cp_5.plotWidget.getPlotItem().hideAxis('bottom')
        self.cp_5.plotWidget.getPlotItem().hideAxis('left')
        
        # Abrir una imagen
        self.imagen = Image.open("resources/images/MainWindow/unidad 4/Canotaje_24.jpg")
        ancho, alto = self.imagen.size
        imagenA = self.imagen.load()
        imagenA = array([[[imagenA[i,j][k] for k in range(3)] for j in range(alto)] for i in range(ancho)])
        self.imagenA = imagenA
        
        # Se crean los items de las imagenes
        self.img_1 = ImageItem()
        self.img_2 = ImageItem()
        self.img_3 = ImageItem()
        self.img_4 = ImageItem()
        self.img_5 = ImageItem()
        self.cp_1.plotWidget.addItem(self.img_1)
        self.cp_2.plotWidget.addItem(self.img_2)
        self.cp_3.plotWidget.addItem(self.img_3)
        self.cp_4.plotWidget.addItem(self.img_4)
        self.cp_5.plotWidget.addItem(self.img_5)
        self.img_1.hoverEvent = self.imageHoverEvent
        
        self.sl_r.valueChanged.connect(self.update)
        self.sl_g.valueChanged.connect(self.update)
        self.sl_b.valueChanged.connect(self.update)
        
        self.update()
        
    def update(self, value=None):
        l_r=self.sl_r.value()
        l_g=self.sl_g.value()
        l_b=self.sl_b.value()
        n,m = self.imagenA.shape[0],self.imagenA.shape[1]
        nulo = zeros((n,m), dtype=uint8)
        r = clip(self.imagenA[:, :, 0]+l_r,0,255)
        g = clip(self.imagenA[:, :, 1]+l_g,0,255)
        b = clip(self.imagenA[:, :, 2]+l_b,0,255)
        img_r = stack((r,nulo,nulo),2)
        img_g = stack((nulo,g,nulo),2)
        img_b = stack((nulo,nulo,b),2)
        img_color = uint8(stack((r,g,b),2))
        img_gray = Image.fromarray(img_color).convert('L').load()
        img_gray = array([[img_gray[i,j] for i in range(m)] for j in range(n)])
        self.img_1.setImage(img_color)
        self.img_2.setImage(img_r)
        self.img_3.setImage(img_g)
        self.img_4.setImage(img_b)
        self.img_5.setImage(img_gray)
        
    def imageHoverEvent(self,event):
        """Show the position, pixel, and value under the mouse cursor.
        """
        if event.isExit():
            self.cp_1.plotWidget.setTitle("")
            return
        pos = event.pos()
        i, j =  pos.x(),pos.y()
        i = int(clip(i, 0, self.imagenA.shape[0] - 1))
        j = int(clip(j, 0, self.imagenA.shape[1] - 1))
        r = self.imagenA[i, j, 0]
        g = self.imagenA[i, j, 1]
        b = self.imagenA[i, j, 2]
        ppos = self.img_1.mapToParent(pos)
        x, y = ppos.x(), ppos.y()
        self.cp_1.plotWidget.setTitle("pos: (%0.1f, %0.1f)  pixel: (%d, %d)  RGB: (%.3g, %.3g, %.3g)" % (x, y, i, j, r, g, b))
