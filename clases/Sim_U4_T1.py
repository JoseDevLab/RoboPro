from PySide6.QtWidgets import QWidget
from clases.ui_sim_U4_T1 import Ui_sim_U4_T1
from PIL import Image
from scipy.signal import convolve2d
from numpy import array,linspace, clip, zeros, uint8, stack
from pyqtgraph import ImageItem, ROI

class Sim_U4_T1(QWidget,Ui_sim_U4_T1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
    def init(self):
        # Invertir el eje Y de los PlotWidget
        self.cp_1.plotWidget.getPlotItem().invertY()
        self.cp_2.plotWidget.getPlotItem().invertY()
        self.cp_3.plotWidget.getPlotItem().invertY()
        self.cp_4.plotWidget.getPlotItem().invertY()
        # Bloquear la relación de aspecto de los ejes a 1:1
        self.cp_1.plotWidget.getPlotItem().setAspectLocked(ratio=1)
        self.cp_2.plotWidget.getPlotItem().setAspectLocked(ratio=1)
        self.cp_3.plotWidget.getPlotItem().setAspectLocked(ratio=1)
        self.cp_4.plotWidget.getPlotItem().setAspectLocked(ratio=1)
        # Ocultar ambos ejes
        self.cp_1.plotWidget.getPlotItem().hideAxis('bottom')
        self.cp_1.plotWidget.getPlotItem().hideAxis('left')
        self.cp_2.plotWidget.getPlotItem().hideAxis('bottom')
        self.cp_2.plotWidget.getPlotItem().hideAxis('left')
        self.cp_3.plotWidget.getPlotItem().hideAxis('bottom')
        self.cp_3.plotWidget.getPlotItem().hideAxis('left')
        self.cp_4.plotWidget.getPlotItem().hideAxis('bottom')
        self.cp_4.plotWidget.getPlotItem().hideAxis('left')
        
        
        # Abrir una imagen
        self.imagen = Image.open("resources/images/MainWindow/unidad 4/Canotaje_24.jpg")
        ancho, alto = self.imagen.size
        imagenA = self.imagen.load()
        imagenA = array([[[imagenA[i,j][k] for k in range(3)] for j in range(alto)] for i in range(ancho)])
        self.imagenA = imagenA
        
        self.imv.setImage(imagenA,xvals=linspace(1., 3., imagenA.shape[0]))
        self.imv.setHistogramLabel("Histograma, Imagen a color")
        self.imv.ui.roiBtn.setChecked(True)
        self.imv.roiClicked()
        self.imv.roi.setPos([50, 150], update=False)
        self.imv.roi.setSize([400, 30], update=True)
        self.imv.ui.menuBtn.hide()
        
        self.img_1 = ImageItem(imagenA)
        self.img_2 = ImageItem()
        self.img_3 = ImageItem()
        self.img_4 = ImageItem()
        self.cp_1.plotWidget.addItem(self.img_1)
        self.cp_2.plotWidget.addItem(self.img_2)
        self.cp_3.plotWidget.addItem(self.img_3)
        self.cp_4.plotWidget.addItem(self.img_4)
        self.img_1.hoverEvent = self.imageHoverEvent
        
        
        # Custom ROI for selecting an image region
        roi = ROI([103, 184], [85, 42])
        self.roi=roi
        roi.addScaleHandle([0.5, 1], [0.5, 0.5])
        roi.addScaleHandle([0, 0.5], [0.5, 0.5])
        self.cp_1.plotWidget.addItem(roi)
        roi.setZValue(10)  # make sure ROI is drawn above image
        
        roi.sigRegionChanged.connect(self.update)
        self.update()
        
    def update(self):
        selected = self.roi.getArrayRegion(self.imagenA, self.img_1)
        n,m = selected.shape[0],selected.shape[1]
        Az = zeros((n*2,m*2,3), dtype=uint8)
        for i in range(n):
            for j in range(m):
                Az[i*2,j*2,:] = selected[i,j,:]
        self.img_3.setImage(Az)
        s = array([[ 1, 1],
                    [1, 1]])
        r = Az[:,:,0]
        g = Az[:,:,1]
        b = Az[:,:,2]
        Hr = clip(convolve2d(r, s, mode='same', boundary='symm'),0,255)
        Hg = clip(convolve2d(g, s, mode='same', boundary='symm'),0,255)
        Hb = clip(convolve2d(b, s, mode='same', boundary='symm'),0,255)
        H = stack((Hr,Hg,Hb),2)
        self.img_2.setImage(H)
        s = array([ [1/4, 1/2, 1/4], 
                    [1/2,   1, 1/2], 
                    [1/4, 1/2, 1/4] ])
        Hr = clip(convolve2d(r, s, mode='same', boundary='symm'),0,255)
        Hg = clip(convolve2d(g, s, mode='same', boundary='symm'),0,255)
        Hb = clip(convolve2d(b, s, mode='same', boundary='symm'),0,255)
        H = stack((Hr,Hg,Hb),2)
        self.img_4.setImage(H)
    
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
        