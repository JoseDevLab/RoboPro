from PySide6.QtWidgets import QWidget
from pyqtgraph import mkPen
from clases.ui_sim_U3_T4 import Ui_sim_U3_T4
from functions.unidad_3 import controlRealimentadoD

class Sim_U3_T4(QWidget,Ui_sim_U3_T4):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
    def init(self):
        self.bt_perturbOn.hide()
        self.cp.plotWidget.setLabel('left', 'Posición')
        self.cp.plotWidget.setLabel('bottom', 'Tiempo',units='s')
        legend=self.cp.plotWidget.addLegend(pen=mkPen('gray',width=3))
        legend.addItem(self.cp.linea,'Entrada')
        legend.setOffset((-30, 10))
        pen = mkPen('r',width=3)
        self.perturbacion = self.cp.plotWidget.plot(name='Perturbación',pen=pen)
        pen = mkPen('y',width=3)
        self.salida = self.cp.plotWidget.plot(name='Salida',pen=pen)
        self.sb_ref.valueChanged.connect(self.update)
        self.sb_Kp.valueChanged.connect(self.update)
        self.sb_Ki.valueChanged.connect(self.update)
        self.sb_Kd.valueChanged.connect(self.update)
        self.sb_tPerturb.valueChanged.connect(self.update)
        self.sb_aPerturb.valueChanged.connect(self.update)
        self.bt_perturbOn.clicked.connect(self.perturbOnClicked)
        self.bt_perturbOff.clicked.connect(self.perturbOffClicked)
        self.update()
    
    def update(self,value=None):
        Kp=self.sb_Kp.value()
        Ki=self.sb_Ki.value()
        Kd=self.sb_Kd.value()
        ref=self.sb_ref.value()
        pert=self.bt_perturbOn.isVisible()
        tPer=self.sb_tPerturb.value()
        aPer=self.sb_aPerturb.value()
        t,entrada,salida,perturbacion=controlRealimentadoD(250,Kp,Ki,Kd,ref,pert,tPer,aPer)
        self.cp.setData(t,entrada,[2])
        self.salida.setData(t,salida)
        self.perturbacion.setData(t,perturbacion)
    
    def perturbOnClicked(self):
        self.bt_perturbOn.hide()
        self.bt_perturbOff.show()
        self.update()
    
    def perturbOffClicked(self):
        self.bt_perturbOff.hide()
        self.bt_perturbOn.show()
        self.update()