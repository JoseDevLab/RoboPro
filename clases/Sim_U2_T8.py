from PySide6.QtWidgets import QWidget
from clases.ui_sim_U2_T8 import Ui_sim_U2_T8
import pyqtgraph as pg
from numpy import linspace
from functions.unidad_2 import int_trapezoidal_vec_t, int_trapezoidal_tmin

class Sim_U2_T8(QWidget,Ui_sim_U2_T8):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
    def init(self):
        self.updateActivado = True
        self.cp_p.heightScale = 1/2.5
        self.cp_v.heightScale = 1/2.5
        self.cp_a.heightScale = 1/2.5
        self.cp_p.plotWidget.setLabel('left', 'Posición', units='°')
        self.cp_v.plotWidget.setLabel('left', 'Velocidad', units='°/s')
        self.cp_a.plotWidget.setLabel('left', 'Aceleración', units='°/s^2')
        self.cp_p.plotWidget.setLabel('bottom', 'Tiempo', units='s')
        self.cp_v.plotWidget.setLabel('bottom', 'Tiempo', units='s')
        self.cp_a.plotWidget.setLabel('bottom', 'Tiempo', units='s')
        self.cp_p.puntos_1.setData(size=12)
        self.textError = pg.TextItem()
        self.textError.setVisible(False)
        self.cp_p.plotWidget.addItem(self.textError)
        
        self.cp_p.plotWidget.setYRange(0,400)
        self.cp_p.plotWidget.setXRange(0,3.4)
        self.cp_v.plotWidget.setXRange(0,3.4)
        self.cp_a.plotWidget.setXRange(0,3.4)
        
        t=[0,3.4]
        q=[0,400]
        self.cp_p.polyLine.addSegment = self.desactivaSegmentos
        self.cp_p.setData(t,q,[3])
        
        self.cp_p.polyLine.sigRegionChanged.connect(self.update)
        self.sb_nPuntos.valueChanged.connect(self.update)
        self.sb_vMax.valueChanged.connect(self.update)
        self.sb_a.valueChanged.connect(self.update)
        self.cb_tipoT.currentIndexChanged.connect(self.update)
        self.update()
        
    def update(self, value=None):
        t,q=self.cp_p.getPolyData()
        n = self.sb_nPuntos.value()
        self.cp_p.setData(t,q,[0])
        qi = q[0]
        qf = q[1]
        vMax = self.sb_vMax.value()
        a = self.sb_a.value()
        ti = t[0]
        tf = t[1]
        vec_t = linspace(ti,tf,n).tolist()
        
        tMin = int_trapezoidal_tmin(qi,qf,a,vMax)
        try:
            if self.cb_tipoT.currentIndex()==0:
                tMin = int_trapezoidal_tmin(qi,qf,a,vMax)
                if t[1]-t[0]<tMin:
                    self.textError.setPos(t[1],q[1])
                    self.textError.setHtml('<div style="font-size: 25px; color: rgb(255, 255, 0);">Visualización incompleta</div>')
                    self.textError.setVisible(True)
                else:
                    self.textError.setVisible(False)
                qInt,qpInt,qppInt=int_trapezoidal_vec_t(qi,qf,a,vMax,vec_t,ti)
            else:
                qInt,qpInt,qppInt=int_trapezoidal_vec_t(qi,qf,a,vMax,vec_t,ti,tf)
                self.textError.setVisible(False)
            self.cp_p.setData(vec_t,qInt,[1,2])
            self.cp_v.setData(vec_t,qpInt,[1,2])
            self.cp_a.setData(vec_t,qppInt,[1,2])
        except ValueError as e:
            self.textError.setPos(t[1],q[1])
            self.textError.setHtml('<div style="font-size: 25px; color: rgb(255, 0, 0);">Error: Tiempo insuficiente</div>')
            self.textError.setVisible(True)
        
    def desactivaSegmentos(self,h1, h2, index=None):
        pass
    