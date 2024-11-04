from PySide6.QtWidgets import QWidget
from clases.ui_sim_U2_T2 import Ui_sim_U2_T2
from clases.Hilos_Unidad_2 import TrayectoriaPuntoPunto
class Sim_U2_T2(QWidget,Ui_sim_U2_T2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
    def init(self):
        self.cp_q_1.heightScale = 1/7
        self.cp_q_2.heightScale = 1/7
        self.cp_q_3.heightScale = 1/7
        self.cp_q_4.heightScale = 1/7
        self.cp_q_1.plotWidget.setLabel('left', 'Articulación 1', units='°')
        self.cp_q_2.plotWidget.setLabel('left', 'Articulación 2', units='cm')
        self.cp_q_3.plotWidget.setLabel('left', 'Articulación 3', units='cm')
        self.cp_q_4.plotWidget.setLabel('left', 'Articulación 4', units='°')
        self.cp_q_1.plotWidget.setLabel('bottom', 'Tiempo', units='s')
        self.cp_q_2.plotWidget.setLabel('bottom', 'Tiempo', units='s')
        self.cp_q_3.plotWidget.setLabel('bottom', 'Tiempo', units='s')
        self.cp_q_4.plotWidget.setLabel('bottom', 'Tiempo', units='s')
        
        self.sl_q1Min.valueChanged.connect(self.sb_q1Min.setValue)
        self.sl_q2Min.valueChanged.connect(self.sb_q2Min.setValue)
        self.sl_q3Min.valueChanged.connect(self.sb_q3Min.setValue)
        self.sl_q4Min.valueChanged.connect(self.sb_q4Min.setValue)
        self.sl_q1Max.valueChanged.connect(self.sb_q1Max.setValue)
        self.sl_q2Max.valueChanged.connect(self.sb_q2Max.setValue)
        self.sl_q3Max.valueChanged.connect(self.sb_q3Max.setValue)
        self.sl_q4Max.valueChanged.connect(self.sb_q4Max.setValue)
        
        self.bt_CalcularTrayectoria.clicked.connect(self.calcularTraayectoriaClicked)
        self.trapezoidalPuntoPunto = TrayectoriaPuntoPunto()
        self.trapezoidalPuntoPunto.trayectoriaCalculada.connect(self.trayectoriaCalculada)
        
    def calcularTraayectoriaClicked(self):
        self.bt_CalcularTrayectoria.setEnabled(False)
        self.q1 = [self.sl_q1Min.value(),self.sl_q1Max.value()]
        self.q2 = [self.sl_q2Min.value(),self.sl_q2Max.value()]
        self.q3 = [self.sl_q3Min.value(),self.sl_q3Max.value()]
        self.q4 = [self.sl_q4Min.value(),self.sl_q4Max.value()]
        
        tipo = self.cb_tiposMovimiento.currentIndex()
        self.trapezoidalPuntoPunto.setQs(self.q1,self.q2,self.q3,self.q4,tipo)
        self.trapezoidalPuntoPunto.start()
    
    def trayectoriaCalculada(self,tm,q,qp,qpp,tqi):
        self.cp_q_1.setData(tm,q[0],[1,2])
        self.cp_q_2.setData(tm,q[1],[1,2])
        self.cp_q_3.setData(tm,q[2],[1,2])
        self.cp_q_4.setData(tm,q[3],[1,2])
        self.cp_q_1.setData(tqi[0],self.q1,[0])
        self.cp_q_2.setData(tqi[1],self.q2,[0])
        self.cp_q_3.setData(tqi[2],self.q3,[0])
        self.cp_q_4.setData(tqi[3],self.q4,[0])
        self.bt_CalcularTrayectoria.setEnabled(True)
        
        