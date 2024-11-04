from PySide6.QtWidgets import QWidget
from pyqtgraph import mkPen
from clases.ui_sim_U3_T3 import Ui_sim_U3_T3
from functions.unidad_3 import controlPrealimentado

class Sim_U3_T3(QWidget,Ui_sim_U3_T3):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
    def init(self):
        self.bt_pertOn.hide()
        self.cp.plotWidget.setLabel('left', 'Posición')
        self.cp.plotWidget.setLabel('bottom', 'Tiempo',units='s')
        legend=self.cp.plotWidget.addLegend(pen=mkPen('gray',width=3))
        legend.addItem(self.cp.linea,'Entrada')
        pen = mkPen('y',width=3)
        self.salida = self.cp.plotWidget.plot(name='Salida',pen=pen)
        pen = mkPen('r',width=3)
        self.perturbacion = self.cp.plotWidget.plot(name='Perturbación',pen=pen)
        self.bt_pertOn.clicked.connect(self.pertOnClicked)
        self.bt_pertOff.clicked.connect(self.pertOffClicked)
        self.sb_Je.valueChanged.connect(self.update)
        self.sb_Be.valueChanged.connect(self.update)
        self.sb_Ke.valueChanged.connect(self.update)
        self.sb_amplitud.valueChanged.connect(self.update)
        self.update()
        
    def update(self):
        Je = self.sb_Je.value()
        Be = self.sb_Be.value()
        Ke = self.sb_Ke.value()
        amplitud = self.sb_amplitud.value()
        conPert = self.bt_pertOn.isVisible()
        t,entrada,salida,perturbacion=controlPrealimentado(10,Je,Be,Ke,conPert,amplitud)
        self.cp.setData(t,entrada,[2])
        self.salida.setData(t,salida)
        self.perturbacion.setData(t,perturbacion)
        
    def pertOnClicked(self):
        self.bt_pertOn.hide()
        self.bt_pertOff.show()
        self.update()
    
    def pertOffClicked(self):
        self.bt_pertOff.hide()
        self.bt_pertOn.show()
        self.update()