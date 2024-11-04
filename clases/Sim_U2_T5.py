from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
import pyqtgraph as pg
from pyqtgraph.opengl import GLScatterPlotItem, GLLinePlotItem
from numpy import array, hstack, vstack, eye, linspace
from math import sqrt
from clases.ui_sim_U2_T5 import Ui_sim_U2_T5
from clases.Robot3D import Rejilla, RobotCilindrico, SistemaCoordenadas3D
from clases.Hilos_Unidad_2 import LinealPuntoPunto, DirectaQs, GetXYZ_From_MTHs, InterpolarLinealR3, GenerarMTHs, InversaMTHs
from functions.unidad_2 import cinematicaInversa, generaMTH, limitesQ, longitudes

class Sim_U2_T5(QWidget,Ui_sim_U2_T5):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
    def init(self):
        self.nPuntos = 100
        puntos = [[186,-55],
                  [112,132],
                  [170,338],
                  [-90, 90],
                  [0,    1]]
        self.ct_puntos.setTable(puntos)
        self.ct_puntos.set_column_prefix('P_')
        nombresFilas = ['X(cm)','Y(cm)','Z(cm)','q4(°)','t(s)']
        self.ct_puntos.setVerticalHeaderLabels(nombresFilas)
        self.ct_puntos.setAxisLabelsVisible(True)
        self.ct_Qs.setSize(5,2)
        self.ct_Qs.setEditable(False)
        self.ct_Qs.set_column_prefix('P_')
        nombresFilas = ['q1(°)','q2(cm)','q3(cm)','q4(°)','t(s)']
        self.ct_Qs.setVerticalHeaderLabels(nombresFilas)
        self.ct_Qs.setAxisLabelsVisible(True)
        
        flecha = QPixmap("resources/images/MainWindow/arrow_right_icon.svg")
        flecha = flecha.scaled(70, 70, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.lb_flecha.setPixmap(flecha)
        
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
        
        self.gv_1.glView.setCameraPosition(distance=1900, azimuth=45)
        self.rejillas1 = Rejilla(-500,500,-500,500,-20,500,100)
        self.rejillas1.loadOnGlView(self.gv_1.glView)
        
        self.sistema_1 = SistemaCoordenadas3D(eye(4),90,5,'1')
        self.sistema_2 = SistemaCoordenadas3D(eye(4),90,5,'2')
        self.sistema_1.hide()
        self.sistema_2.hide()
        self.sistema_1.loadOnGlView(self.gv_1.glView)
        self.sistema_2.loadOnGlView(self.gv_1.glView)
        
        self.robot_1 = RobotCilindrico(0,0,0,0)
        self.robot_1.loadOnGlView(self.gv_1.glView)
        
        size = 10
        color = (1,0,0,1)
        self.scatterPuntos = GLScatterPlotItem(size=size,color=color,pxMode=False)
        self.gv_1.glView.addItem(self.scatterPuntos)
        self.lineTrayectory = GLLinePlotItem(color=pg.mkColor((30,200)), width=5, mode='line_strip', antialias=True)
        self.gv_1.glView.addItem(self.lineTrayectory)
        
        self.cb_tipoTrayec.currentIndexChanged.connect(self.tipoTrayecCurrentIndexChanged)
        
        self.bt_generarTrayec.clicked.connect(self.generarTrayecClicked)
        self.bt_iniciarAnimacion.clicked.connect(self.iniciarAnimacionClicked)
        
        self.linealPuntoPunto = LinealPuntoPunto()
        self.linealPuntoPunto.trayectoriaCalculada.connect(self.trayecCalculada)
        self.directas = DirectaQs()
        self.directas.directasCalculadas.connect(self.directasCalculadas)
        self.getXYZ = GetXYZ_From_MTHs()
        self.getXYZ.XYZExtraidos.connect(self.xyzExtraidos)
        self.interpolarR3 = InterpolarLinealR3()
        self.interpolarR3.puntosInterpolados.connect(self.puntosInterpolados)
        self.generarMTHs = GenerarMTHs()
        self.generarMTHs.listMTHsGenerada.connect(self.mthsGeneradas)
        self.inversasMTHs = InversaMTHs()
        self.inversasMTHs.inversasCalculadas.connect(self.inversasCalculadas)
        
        self.robot_1.animacionTerminada.connect(self.animacionTerminada)
        
    def tipoTrayecCurrentIndexChanged(self, index):
        if index==0:
            self.fr_tipoMovimiento.show()
        elif index==1:
            self.fr_tipoMovimiento.hide()
        
    def generarTrayecClicked(self):
        dato,i = self.validarPuntos()
        qMin,qMax,_,_ = limitesQ()
        L1,_,_ = longitudes()
        if dato==0:
            table = self.ct_puntos.getTable()
            self.tiempos = [float(i) for i in table[-1]]
            table = array([[float(j) for j in i] for i in table])
            p_1 = table[0:3,0:1].T[0]
            p_2 = table[0:3,1:2].T[0]
            mth_1 = generaMTH(p_1,table[3,0])
            mth_2 = generaMTH(p_2,table[3,1])
            self.sistema_1.setA(mth_1)
            self.sistema_2.setA(mth_2)
            self.sistema_1.show()
            self.sistema_2.show()
            pq_1 = cinematicaInversa(mth_1)
            pq_2 = cinematicaInversa(mth_2)
            Qs = hstack((array([pq_1]).T,array([pq_2]).T)).tolist()
            self.robot_1.setPosQ(Qs[0][0],Qs[1][0],Qs[2][0],Qs[3][0])
            puntos = vstack((array(Qs),array([self.tiempos]))).tolist()
            self.ct_Qs.setTable([[round(j,2) for j in i] for i in puntos])
            self.Qs = Qs
            tipoTr = self.cb_tipoTrayec.currentIndex()
            if tipoTr==0:
                tipoMov = self.cb_tipoMov.currentIndex()
                self.linealPuntoPunto.setQs(Qs[0],Qs[1],Qs[2],Qs[3],self.nPuntos,tipoMov)
                self.linealPuntoPunto.start()
            elif tipoTr==1:
                self.interpolarR3.setPuntos(table,self.nPuntos)
                self.interpolarR3.start()
        elif dato==1:
            QMessageBox().critical(self,'Punto '+str(i+1)+' inalcanzable','Velifique las coordenadas (X,Y). Están muy cerca al origen del plano X,Y. Esto hace que sea inalcanzable por el robot.')
        elif dato==2:
            QMessageBox().critical(self,'Punto '+str(i+1)+' inalcanzable','Velifique las coordenadas (X,Y). Están muy lejos del origen del plano X,Y. Es inalcanzable para la articulación 3 del robot.')
        elif dato==3:
            QMessageBox().critical(self,'Punto '+str(i+1)+' inalcanzable','Velifique la coordenada (Z). Está en un valor muy bajo. El valor mínimo alcanzable es '+str(L1)+' cm.')
        elif dato==4:
            QMessageBox().critical(self,'Punto '+str(i+1)+' inalcanzable','Velifique la coordenada (Z). Está en un valor muy alto. El valor máximo alcanzable es '+str(L1+qMax[1])+' cm.')
        elif dato==5:
            QMessageBox().critical(self,'Punto '+str(i+1)+' inalcanzable','Velifique el valor de q4. El valor mínimo alcanzable es '+str(qMin[3])+'°')
        elif dato==6:
            QMessageBox().critical(self,'Punto '+str(i+1)+' inalcanzable','Velifique el valor de q4. El valor máximo alcanzable es '+str(qMax[3])+'°')
        elif dato==7:
            QMessageBox().critical(self,'Tiempos incorrectos','Verifique que todos los tiempos estén en orden ascendente y no se repitan')
        
    def validarPuntos(self):
        puntos = self.ct_puntos.getTable()
        puntos = [[float(j) for j in i] for i in puntos]
        tiempos = puntos[-1]
        qMin,qMax,_,_ = limitesQ()
        L1,L2,L4 = longitudes()
        for i in range(len(tiempos)):
            x=puntos[0][i]
            y=puntos[1][i]
            z=puntos[2][i]
            q4=puntos[3][i]
            if sqrt(x**2+y**2)<sqrt(L2**2+L4**2):
                return 1, i
            elif sqrt(x**2+y**2)>sqrt(L2**2+(qMax[2]+L4)**2):
                return 2, i
            elif z<L1:
                return 3, i
            elif z>L1+qMax[1]:
                return 4, i
            elif q4<qMin[3]:
                return 5, i
            elif q4>qMax[3]:
                return 6, i
        if not all(tiempos[i] < tiempos[i + 1] for i in range(len(tiempos) - 1)):
            return 7, 0
        return 0, 0
    
    def trayecCalculada(self,tm,q,qp,tqi):
        self.tm = tm
        self.qInt = q
        self.cp_q_1.setData(tm,q[0],[1,2])
        self.cp_q_2.setData(tm,q[1],[1,2])
        self.cp_q_3.setData(tm,q[2],[1,2])
        self.cp_q_4.setData(tm,q[3],[1,2])
        self.cp_q_1.setData(tqi[0],self.Qs[0],[0])
        self.cp_q_2.setData(tqi[1],self.Qs[1],[0])
        self.cp_q_3.setData(tqi[2],self.Qs[2],[0])
        self.cp_q_4.setData(tqi[3],self.Qs[3],[0])
        
        self.directas.setQs(q[0],q[1],q[2],q[3])
        self.directas.start()
        if not self.bt_iniciarAnimacion.isEnabled():
            self.bt_iniciarAnimacion.setEnabled(True)
        
    def directasCalculadas(self,MTHs):
        self.getXYZ.setMTHs(MTHs)
        self.getXYZ.start()
    
    def xyzExtraidos(self,xyz):
        self.scatterPuntos.setData(pos=xyz)
        self.lineTrayectory.setData(pos=xyz)
    
    def puntosInterpolados(self,puntos):
        self.generarMTHs.setPuntos(puntos)
        self.generarMTHs.start()
    
    def mthsGeneradas(self,MTHs):
        self.inversasMTHs.setMTHs(MTHs)
        self.inversasMTHs.start()
        self.getXYZ.setMTHs(MTHs)
        self.getXYZ.start()
    
    def inversasCalculadas(self,q1,q2,q3,q4):
        self.qInt = [q1,q2,q3,q4]
        tm = linspace(self.tiempos[0],self.tiempos[1],self.nPuntos)
        self.tm = tm
        self.cp_q_1.setData(tm,q1,[1,2])
        self.cp_q_2.setData(tm,q2,[1,2])
        self.cp_q_3.setData(tm,q3,[1,2])
        self.cp_q_4.setData(tm,q4,[1,2])
        self.cp_q_1.setData(self.tiempos,self.Qs[0],[0])
        self.cp_q_2.setData(self.tiempos,self.Qs[1],[0])
        self.cp_q_3.setData(self.tiempos,self.Qs[2],[0])
        self.cp_q_4.setData(self.tiempos,self.Qs[3],[0])
        self.bt_iniciarAnimacion.setEnabled(True)
    
    def iniciarAnimacionClicked(self):
        puntos = hstack((array([self.tm]).T*1000,array(self.qInt).T))
        self.robot_1.iniciarAinimacion(puntos)
        
    def animacionTerminada(self):
        
        pass