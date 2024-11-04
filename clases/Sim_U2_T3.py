from PySide6.QtWidgets import QWidget, QMessageBox
from clases.ui_sim_U2_T3 import Ui_sim_U2_T3
from clases.Hilos_Unidad_2 import InterpolarLineal
from math import floor

class Sim_U2_T3(QWidget,Ui_sim_U2_T3):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
    def init(self):
        self.dT = 0.05
        self.iniTable = [[ 0, 50,200,  45,   0,-190,150],
                         [20,150,100, 200,   0, 280,200],
                         [60,150, 80, 200, 400, 420,250],
                         [45,180,  0, -90,-180, 100, 50],
                         [ 0,0.5,  1, 1.5,   2, 2.5,  3]]
        self.ct_puntos.setTable(self.iniTable)
        self.ct_puntos.set_column_prefix('P_')
        nombresFilas = ['q1(°)','q2(cm)','q3(cm)','q4(°)','t(s)']
        self.ct_puntos.setVerticalHeaderLabels(nombresFilas)
        self.ct_puntos.setAxisLabelsVisible(True)
        
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
        
        self.sb_nPuntos.valueChanged.connect(self.ct_puntos.setColumnS)
        
        self.bt_calcularTrayectoria.clicked.connect(self.calcularTrayectoriaClicked)
        
        self.interpolarLineal = InterpolarLineal()
        self.interpolarLineal.qInterpolado.connect(self.qInterpolado)
        
    def calcularTrayectoriaClicked(self):
        self.bt_calcularTrayectoria.setEnabled(False)
        q = self.ct_puntos.getTable()
        q = [[float(i) for i in j] for j in q]
        t = q.pop()
        self.q = q
        self.t = t
        if all(t[i] < t[i + 1] for i in range(len(t) - 1)):
            self.interpolarLineal.setQ(q,t,floor((t[-1]-t[0])/self.dT))
            self.interpolarLineal.start()
        else:
            QMessageBox().critical(self,'Valores de tiempos incorrectos','Verifique que los tiempos sean siempre de forma ascendente y no se repitan')
            self.bt_calcularTrayectoria.setEnabled(True)
    
    def qInterpolado(self,q,qp,t):
        self.cp_q_1.setData(t,q[0],[1,2])
        self.cp_q_2.setData(t,q[1],[1,2])
        self.cp_q_3.setData(t,q[2],[1,2])
        self.cp_q_4.setData(t,q[3],[1,2])
        self.cp_q_1.setData(self.t,self.q[0],[0])
        self.cp_q_2.setData(self.t,self.q[1],[0])
        self.cp_q_3.setData(self.t,self.q[2],[0])
        self.cp_q_4.setData(self.t,self.q[3],[0])
        self.bt_calcularTrayectoria.setEnabled(True)