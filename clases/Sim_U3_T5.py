from PySide6.QtWidgets import QWidget
from pyqtgraph import mkPen
from clases.ui_sim_U3_T5 import Ui_sim_U3_T5
from functions.unidad_3 import prealimentadoMRealimentado

class Sim_U3_T5(QWidget,Ui_sim_U3_T5):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
    def init(self):
        self.bt_pertOn.hide()
        self.cp_1.plotWidget.setLabel('left', 'Posición')
        self.cp_1.plotWidget.setLabel('bottom', 'Tiempo',units='s')
        self.cp_2.plotWidget.setLabel('left', 'Perturbación')
        self.cp_2.plotWidget.setLabel('bottom', 'Tiempo',units='s')
        legend=self.cp_1.plotWidget.addLegend(pen=mkPen('gray',width=3))
        legend.addItem(self.cp_1.linea,'Entrada')
        # legend.setOffset((-30, 10))
        pen = mkPen('y',width=3)
        self.salida = self.cp_1.plotWidget.plot(name='Salida',pen=pen)
        pen = mkPen('r',width=3)
        self.cp_2.linea.setData(pen=pen)
        self.sb_Je.valueChanged.connect(self.update)
        self.sb_Be.valueChanged.connect(self.update)
        self.sb_Ke.valueChanged.connect(self.update)
        self.sb_Kp.valueChanged.connect(self.update)
        self.sb_Ki.valueChanged.connect(self.update)
        self.sb_Kd.valueChanged.connect(self.update)
        self.sb_aPert.valueChanged.connect(self.update)
        self.bt_pertOn.clicked.connect(self.pertOnClicked)
        self.bt_pertOff.clicked.connect(self.pertOffClicked)
        self.update()
        
    def update(self,value=None):
        Je=self.sb_Je.value()
        Be=self.sb_Be.value()
        Ke=self.sb_Ke.value()
        Kp=self.sb_Kp.value()
        Ki=self.sb_Ki.value()
        Kd=self.sb_Kd.value()
        pert=self.bt_pertOn.isVisible()
        aPert=self.sb_aPert.value()
        t,entrada,salida,perturbacion=prealimentadoMRealimentado(10,Kp,Ki,Kd,Je,Be,Ke,pert,aPert)
        self.cp_1.setData(t,entrada,[2])
        self.salida.setData(t,salida)
        self.cp_2.setData(t,perturbacion,[2])
    
    def pertOnClicked(self):
        self.bt_pertOn.hide()
        self.bt_pertOff.show()
        self.update()
    
    def pertOffClicked(self):
        self.bt_pertOff.hide()
        self.bt_pertOn.show()
        self.update()
    