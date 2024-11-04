from PySide6.QtWidgets import QWidget
from clases.ui_sim_U4_T3 import Ui_sim_U4_T3
from PIL import Image
import cv2
from numpy import array, clip, uint8, logical_and, logical_or, logical_xor, logical_not
from pyqtgraph import ImageItem

class Sim_U4_T3(QWidget,Ui_sim_U4_T3):
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
        self.cp_6.plotWidget.getPlotItem().invertY()
        self.cp_7.plotWidget.getPlotItem().invertY()
        self.cp_8.plotWidget.getPlotItem().invertY()
        # Bloquear la relación de aspecto de los ejes a 1:1
        self.cp_1.plotWidget.getPlotItem().setAspectLocked(ratio=1)
        self.cp_2.plotWidget.getPlotItem().setAspectLocked(ratio=1)
        self.cp_3.plotWidget.getPlotItem().setAspectLocked(ratio=1)
        self.cp_4.plotWidget.getPlotItem().setAspectLocked(ratio=1)
        self.cp_5.plotWidget.getPlotItem().setAspectLocked(ratio=1)
        self.cp_6.plotWidget.getPlotItem().setAspectLocked(ratio=1)
        self.cp_7.plotWidget.getPlotItem().setAspectLocked(ratio=1)
        self.cp_8.plotWidget.getPlotItem().setAspectLocked(ratio=1)
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
        self.cp_6.plotWidget.getPlotItem().hideAxis('bottom')
        self.cp_6.plotWidget.getPlotItem().hideAxis('left')
        self.cp_7.plotWidget.getPlotItem().hideAxis('bottom')
        self.cp_7.plotWidget.getPlotItem().hideAxis('left')
        self.cp_8.plotWidget.getPlotItem().hideAxis('bottom')
        self.cp_8.plotWidget.getPlotItem().hideAxis('left')
        
        # Abrir una imagen
        self.imagen = Image.open("resources/images/MainWindow/unidad 4/cara.png")
        ancho, alto = self.imagen.size
        imagenA = self.imagen.load()
        imagenA = array([[[imagenA[i,j][k] for k in range(3)] for j in range(alto)] for i in range(ancho)])
        self.imagenA = imagenA
        
        # Se crean los items de las imagenes
        self.img_1 = ImageItem(imagenA)
        self.img_2 = ImageItem()
        self.img_3 = ImageItem()
        self.img_4 = ImageItem()
        self.img_5 = ImageItem()
        self.img_6 = ImageItem()
        self.img_7 = ImageItem()
        self.img_8 = ImageItem()
        self.cp_1.plotWidget.addItem(self.img_1)
        self.cp_2.plotWidget.addItem(self.img_2)
        self.cp_3.plotWidget.addItem(self.img_3)
        self.cp_4.plotWidget.addItem(self.img_4)
        self.cp_5.plotWidget.addItem(self.img_5)
        self.cp_6.plotWidget.addItem(self.img_6)
        self.cp_7.plotWidget.addItem(self.img_7)
        self.cp_8.plotWidget.addItem(self.img_8)
        self.img_1.hoverEvent = self.imageHoverEvent
        
        r = imagenA[:,:,0].astype(uint8)
        g = imagenA[:,:,1].astype(uint8)
        b = imagenA[:,:,2].astype(uint8)
        _, self.r = cv2.threshold(r, 120, 255, cv2.THRESH_BINARY)
        _, self.g = cv2.threshold(g, 120, 255, cv2.THRESH_BINARY)
        _, self.b = cv2.threshold(b, 25, 255, cv2.THRESH_BINARY)
        self.r_N = logical_not(self.r)
        self.g_N = logical_not(self.g)
        self.b_N = logical_not(self.b)
        self.binarias = [self.r,self.g,self.b,self.r_N,self.g_N,self.b_N]
        self.img_3.setImage(self.r)
        self.img_4.setImage(self.g)
        self.img_5.setImage(self.b)
        self.img_6.setImage(self.r_N)
        self.img_7.setImage(self.g_N)
        self.img_8.setImage(self.b_N)
        self.cb_imgBin_1.currentIndexChanged.connect(self.update)
        self.cb_imgBin_2.currentIndexChanged.connect(self.update)
        self.cb_imgBin_3.currentIndexChanged.connect(self.update)
        self.cb_opLog_1.currentIndexChanged.connect(self.update)
        self.cb_opLog_2.currentIndexChanged.connect(self.update)
        self.update()
        
    def update(self,index=None):
        imgBin_1 = self.cb_imgBin_1.currentIndex()
        imgBin_2 = self.cb_imgBin_2.currentIndex()
        imgBin_3 = self.cb_imgBin_3.currentIndex()
        opLog_1 = self.cb_opLog_1.currentIndex()
        opLog_2 = self.cb_opLog_2.currentIndex()
        if opLog_1==0:
            imgBin = logical_and(self.binarias[imgBin_1],self.binarias[imgBin_2])
        elif opLog_1==1:
            imgBin = logical_or(self.binarias[imgBin_1],self.binarias[imgBin_2])
        elif opLog_1==2:
            imgBin = logical_xor(self.binarias[imgBin_1],self.binarias[imgBin_2])
        if imgBin_3!=0:
            if opLog_2==0:
                imgBin = logical_and(imgBin,self.binarias[imgBin_3-1])
            elif opLog_2==1:
                imgBin = logical_or(imgBin,self.binarias[imgBin_3-1])
            elif opLog_2==2:
                imgBin = logical_xor(imgBin,self.binarias[imgBin_3-1])
        self.img_2.setImage(imgBin)
        
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