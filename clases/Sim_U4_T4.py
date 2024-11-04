from PySide6.QtWidgets import QWidget
from clases.ui_sim_U4_T4 import Ui_sim_U4_T4
from PIL import Image
from scipy.signal import convolve2d
from scipy.ndimage import binary_dilation, binary_erosion, binary_opening, binary_closing
from skimage.morphology import disk, square, rectangle,diamond
from skimage.draw import line
from numpy import array,clip,zeros,ones,uint8,stack,sin,radians,cos,bincount,absolute
from pyqtgraph import ImageItem
from clases.Hilos_Unidad_4 import DilatarErosionar

class Sim_U4_T4(QWidget,Ui_sim_U4_T4):
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
        # Bloquear la relación de aspecto de los ejes a 1:1
        self.cp_1.plotWidget.getPlotItem().setAspectLocked(ratio=1)
        self.cp_2.plotWidget.getPlotItem().setAspectLocked(ratio=1)
        self.cp_3.plotWidget.getPlotItem().setAspectLocked(ratio=1)
        self.cp_4.plotWidget.getPlotItem().setAspectLocked(ratio=1)
        self.cp_5.plotWidget.getPlotItem().setAspectLocked(ratio=1)
        self.cp_6.plotWidget.getPlotItem().setAspectLocked(ratio=1)
        self.cp_7.plotWidget.getPlotItem().setAspectLocked(ratio=1)
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
        
        # Cambiar relación de aspecto de los CustomPlotWidget
        self.cp_1.heightScale = 1
        self.cp_2.heightScale = 1
        self.cp_3.heightScale = 1
        self.cp_4.heightScale = 1/3
        self.cp_5.heightScale = 1
        self.cp_6.heightScale = 1
        self.cp_7.heightScale = 1
        
        self.cp_4.plotWidget.setTitle('Elemento Estructurante')
        
        # Abrir una imagen
        imagen = Image.open("resources/images/MainWindow/unidad 4/formas.bmp")
        ancho, alto = imagen.size
        imagen_1 = imagen.load()
        imagen_1 = array([[imagen_1[i,j] for j in range(alto)] for i in range(ancho)])
        self.imagen_1 = imagen_1
        imagen = Image.open("resources/images/MainWindow/unidad 4/circles_2.bmp")
        ancho, alto = imagen.size
        imagen_2 = imagen.load()
        imagen_2 = array([[imagen_2[i,j] for j in range(alto)] for i in range(ancho)])
        self.imagen_2 = imagen_2
        imagen = Image.open("resources/images/MainWindow/unidad 4/imagenE.bmp")
        ancho, alto = imagen.size
        imagen_3 = imagen.load()
        imagen_3 = array([[imagen_3[i,j] for j in range(alto)] for i in range(ancho)])
        self.imagen_3 = imagen_3
        
        # Se crean los items de las imagenes
        self.img_1 = ImageItem(imagen_1)
        self.img_2 = ImageItem(imagen_2)
        self.img_3 = ImageItem(imagen_3)
        self.img_4 = ImageItem()
        self.img_5 = ImageItem()
        self.img_6 = ImageItem()
        self.img_7 = ImageItem()
        self.cp_1.plotWidget.addItem(self.img_1)
        self.cp_2.plotWidget.addItem(self.img_2)
        self.cp_3.plotWidget.addItem(self.img_3)
        self.cp_4.plotWidget.addItem(self.img_4)
        self.cp_5.plotWidget.addItem(self.img_5)
        self.cp_6.plotWidget.addItem(self.img_6)
        self.cp_7.plotWidget.addItem(self.img_7)
        
        self.cb_estruc.currentIndexChanged.connect(self.update)
        self.cb_oper.currentIndexChanged.connect(self.update)
        self.sb_r.valueChanged.connect(self.update)
        self.sb_deg.valueChanged.connect(self.update)
        self.sb_ancho.valueChanged.connect(self.update)
        
        self.dilatarErosionar = DilatarErosionar()
        self.dilatarErosionar.terminado.connect(self.terminado)
        self.bt_aplicar.clicked.connect(self.aplicarClicked)
        self.update()
        
    def update(self,index=None):
        estruc = self.cb_estruc.currentIndex()
        if estruc==2:
            self.fr_ancho.hide()
            self.fr_grados.show()
            self.lb_r.setText('Longitud')
        elif estruc==4:
            self.fr_grados.hide()
            self.fr_ancho.show()
            self.lb_r.setText('Alto')
        else:
            self.fr_grados.hide()
            self.fr_ancho.hide()
            self.lb_r.setText('Radio')
        r = self.sb_r.value()
        if estruc==0:
            se = diamond(r)
        elif estruc==1:
            se = disk(r)
        elif estruc==2:
            deg = self.sb_deg.value()
            rows,cols = line(0, 0, int(r * sin(radians(deg))), int(r * cos(radians(deg))))
            rowsp = absolute(rows)
            colsp = absolute(cols)
            n = max(rowsp)
            m = max(colsp)
            se = zeros((n+1,m+1),dtype=int)
            for i in range(rows.shape[0]):
                se[rowsp[i],colsp[i]] = 1
            if cols[-1]<0:
                se = array([fila[::-1] for fila in se.tolist()])
            if rows[-1]<0:
                se = array(se[::-1])
            se = array(se[::-1])
        elif estruc==3:
            se = square(r)
        elif estruc==4:
            ancho = self.sb_ancho.value()
            se = rectangle(r,ancho)
        x = se.shape[0]
        y = se.shape[1]
        seb = zeros((x+2,y+2))
        seb[1:x+1,1:y+1]=se[:,:]
        self.img_4.setImage(seb.T)
        
        self.se = se
        
    def aplicarClicked(self):
        self.bt_aplicar.setEnabled(False)
        self.dilatarErosionar.setDatos(self.imagen_1,self.imagen_2,self.imagen_3,self.se,self.cb_oper.currentIndex())
        self.dilatarErosionar.start()
        
    def terminado(self,img_1,img_2,img_3):
        self.img_5.setImage(img_1)
        self.img_6.setImage(img_2)
        self.img_7.setImage(img_3)
        self.bt_aplicar.setEnabled(True)