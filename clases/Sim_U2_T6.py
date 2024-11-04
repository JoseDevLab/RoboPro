from PySide6.QtWidgets import QWidget
from clases.ui_sim_U2_T6 import Ui_sim_U2_T6
from numpy import array
import pyqtgraph as pg
from functions.unidad_2 import interpoladorLineal

class Sim_U2_T6(QWidget,Ui_sim_U2_T6):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
    def init(self):
        self.cp_p.heightScale = 1/2.5
        self.cp_v.heightScale = 1/2.5
        self.cp_p.plotWidget.setLabel('left', 'Posición', units='°')
        self.cp_v.plotWidget.setLabel('left', 'Velocidad', units='°/s')
        self.cp_p.plotWidget.setLabel('bottom', 'Tiempo', units='s')
        self.cp_v.plotWidget.setLabel('bottom', 'Tiempo', units='s')
        self.cp_p.puntos_1.setData(size=12)
        
        self.cp_p.plotWidget.setYRange(-10,180)
        
        self.cp_p.setData([0,1,2,3,4],[0,50,180,-10,30],[3])
        self.cp_p.polyLine.sigRegionChanged.connect(self.update)
        self.sb_nPuntos.valueChanged.connect(self.update)
        self.update()
        
    def update(self,value=None):
        t,q=self.cp_p.getPolyData()
        self.cp_p.setData(t,q,[0])
        # Validar si los tiempos son correctos
        if all(t[i] < t[i + 1] for i in range(len(t) - 1)):
            qInt, qpInt, tm = interpoladorLineal(q,t,self.sb_nPuntos.value())
            self.cp_p.setData(tm,qInt,[1,2])
            self.cp_v.setData(tm,qpInt,[1,2])
            self.sb_nPuntos.setMinimum(len(t))