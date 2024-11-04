from PySide6.QtCore import QThread, Signal
from scipy.ndimage import binary_dilation, binary_erosion, binary_opening, binary_closing
from numpy import array, ndarray

class DilatarErosionar(QThread):
    terminado = Signal(ndarray,ndarray,ndarray)
    def __init__(self):
        super().__init__()
        self.datosCargados = False
        
    def setDatos(self,imagen_1:ndarray,imagen_2:ndarray,imagen_3:ndarray,el_estruc:ndarray,oper:int):
        self.imagen_1 = imagen_1
        self.imagen_2 = imagen_2
        self.imagen_3 = imagen_3
        self.el_estruct = array(el_estruc,dtype=bool)
        self.oper = oper
        self.datosCargados = True
        
    def run(self):
        if self.datosCargados:
            if self.oper==0:
                img_1 = binary_erosion(self.imagen_1, self.el_estruct)
                img_2 = binary_erosion(self.imagen_2, self.el_estruct)
                img_3 = binary_erosion(self.imagen_3, self.el_estruct)
            elif self.oper==1:
                img_1 = binary_dilation(self.imagen_1, self.el_estruct)
                img_2 = binary_dilation(self.imagen_2, self.el_estruct)
                img_3 = binary_dilation(self.imagen_3, self.el_estruct)
            elif self.oper==2:
                img_1 = binary_closing(self.imagen_1, self.el_estruct)
                img_2 = binary_closing(self.imagen_2, self.el_estruct)
                img_3 = binary_closing(self.imagen_3, self.el_estruct)
            elif self.oper==3:
                img_1 = binary_opening(self.imagen_1, self.el_estruct)
                img_2 = binary_opening(self.imagen_2, self.el_estruct)
                img_3 = binary_opening(self.imagen_3, self.el_estruct)
            self.terminado.emit(img_1,img_2,img_3)
        