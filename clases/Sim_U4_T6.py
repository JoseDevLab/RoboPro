from PySide6.QtWidgets import QWidget
from clases.ui_sim_U4_T6 import Ui_sim_U4_T6
from PIL import Image
from scipy.signal import convolve2d
from scipy.ndimage import median_filter
from numpy import array,clip,stack
from pyqtgraph import ImageItem

class Sim_U4_T6(QWidget,Ui_sim_U4_T6):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
    def init(self):
        self.ct_oper.setEditable(False)
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
        
        self.cb_oper.currentIndexChanged.connect(self.update)
        self.update(0)
        
    def update(self, index):
        if index==0:
            s=[[-1],
               [ 1]]
        elif index==1:
            s=[[-1,1]]
        elif index==2:
            s=[[-1, 0],
               [ 0, 1]]
        elif index==3:
            s=[[0, -1],
               [1,  0]]
        elif index==4:
            s=[[0, 1,0],
               [1,-4,1],
               [0, 1,0]]
        elif index==5:
            s=[[1, 1,1],
               [1,-8,1],
               [1, 1,1]]
        elif index==6:
            s=[[-1,-1,-1],
               [ 0, 0, 0],
               [ 1, 1, 1]]
        elif index==7:
            s=[[-1,0,1],
               [-1,0,1],
               [-1,0,1]]
        elif index==8:
            s=[[1, 1, 0],
               [1, 0,-1],
               [0,-1,-1]]
        elif index==9:
            s=[[ 0, 1,1],
               [-1, 0,1],
               [-1,-1,0]]
        elif index==10:
            s=[[-1,-2,-1],
               [ 0, 0, 0],
               [ 1, 2, 1]]
        elif index==11:
            s=[[-1,0,1],
               [-2,0,2],
               [-1,0,1]]
        self.ct_oper.setTable(s)
        s = array(s)
        r=self.imagenA[:,:,0]
        g=self.imagenA[:,:,1]
        b=self.imagenA[:,:,2]
        Hr = clip(convolve2d(r, s, mode='same', boundary='symm'),0,255)
        Hg = clip(convolve2d(g, s, mode='same', boundary='symm'),0,255)
        Hb = clip(convolve2d(b, s, mode='same', boundary='symm'),0,255)
        H = stack((Hr,Hg,Hb),2)
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