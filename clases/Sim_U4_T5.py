from PySide6.QtWidgets import QWidget
from clases.ui_sim_U4_T5 import Ui_sim_U4_T5
from PIL import Image
from scipy.signal import convolve2d
from scipy.ndimage import median_filter
from numpy import array,clip,ones,stack
from pyqtgraph import ImageItem

class Sim_U4_T5(QWidget,Ui_sim_U4_T5):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
    def init(self):
        # Invertir el eje Y de los PlotWidget
        self.cp_1.plotWidget.getPlotItem().invertY()
        self.cp_2.plotWidget.getPlotItem().invertY()
        # Bloquear la relación de aspecto de los ejes a 1:1
        self.cp_1.plotWidget.getPlotItem().setAspectLocked(ratio=1)
        self.cp_2.plotWidget.getPlotItem().setAspectLocked(ratio=1)
        # Ocultar ambos ejes
        self.cp_1.plotWidget.getPlotItem().hideAxis('bottom')
        self.cp_1.plotWidget.getPlotItem().hideAxis('left')
        self.cp_2.plotWidget.getPlotItem().hideAxis('bottom')
        self.cp_2.plotWidget.getPlotItem().hideAxis('left')
        
        # Abrir una imagen
        self.imagen = Image.open("resources/images/MainWindow/unidad 4/Canotaje_24.jpg")
        ancho, alto = self.imagen.size
        imagenA = self.imagen.load()
        imagenA = array([[[imagenA[i,j][k] for k in range(3)] for j in range(alto)] for i in range(ancho)])
        self.imagenA = imagenA
        
        # Se crean los items de las imagenes
        self.img_1 = ImageItem(imagenA)
        self.img_2 = ImageItem()
        self.cp_1.plotWidget.addItem(self.img_1)
        self.cp_2.plotWidget.addItem(self.img_2)
        self.img_1.hoverEvent = self.imageHoverEvent
        
        self.cb_filtros.currentIndexChanged.connect(self.update)
        self.sl_realce.valueChanged.connect(self.update)
        
        self.update()
        
    def update(self, index=None):
        index = self.cb_filtros.currentIndex()
        r=self.imagenA[:,:,0]
        g=self.imagenA[:,:,1]
        b=self.imagenA[:,:,2]
        if index==0:
            s = ones((3,3))*(1/9)
            Hr = clip(convolve2d(r, s, mode='same', boundary='symm'),0,255)
            Hg = clip(convolve2d(g, s, mode='same', boundary='symm'),0,255)
            Hb = clip(convolve2d(b, s, mode='same', boundary='symm'),0,255)
            H = stack((Hr,Hg,Hb),2)
        elif index==1:
            s = (1/16) * array([ [1, 2, 1], 
                                 [2, 4, 2], 
                                 [1, 2, 1] ])
            Hr = clip(convolve2d(r, s, mode='same', boundary='symm'),0,255)
            Hg = clip(convolve2d(g, s, mode='same', boundary='symm'),0,255)
            Hb = clip(convolve2d(b, s, mode='same', boundary='symm'),0,255)
            H = stack((Hr,Hg,Hb),2)
        elif index==2:
            s = (1/249) * array([[3, 6, 8, 6,3],
                                 [6,14,19,14,6],
                                 [8,19,25,19,8],
                                 [6,14,19,14,6],
                                 [3, 6, 8, 6,3]])
            Hr = clip(convolve2d(r, s, mode='same', boundary='symm'),0,255)
            Hg = clip(convolve2d(g, s, mode='same', boundary='symm'),0,255)
            Hb = clip(convolve2d(b, s, mode='same', boundary='symm'),0,255)
            H = stack((Hr,Hg,Hb),2)
        elif index==3:
            Hr = clip(median_filter(r, size=3),0,255)
            Hg = clip(median_filter(g, size=3),0,255)
            Hb = clip(median_filter(b, size=3),0,255)
            H = stack((Hr,Hg,Hb),2)
        elif index==4:
            a=self.sl_realce.value()/100
            self.sb_realce.setValue(a)
            s = array([[-a,    -a, -a],
                       [-a, 1+8*a, -a],
                       [-a,    -a, -a] ])
            Hr = clip(convolve2d(r, s),0,255)
            Hg = clip(convolve2d(g, s),0,255)
            Hb = clip(convolve2d(b, s),0,255)
            H = stack((Hr,Hg,Hb),2)
        if index==4:
            self.fr_realce.show()
        else:
            self.fr_realce.hide()
        self.img_2.setImage(H)
        
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