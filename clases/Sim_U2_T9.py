from PySide6.QtWidgets import QWidget, QMessageBox
from pyqtgraph.opengl import GLScatterPlotItem, GLLinePlotItem
from pyqtgraph import mkColor
from numpy import array, sign, vstack, zeros, floor, hstack
from math import sqrt
from clases.ui_sim_U2_T9 import Ui_sim_U2_T9
from clases.Robot3D import Rejilla, RobotCilindrico, SistemaCoordenadas3D
from clases.Hilos_Unidad_2 import (GenerarMTHs, InterpolarLinealR3, InversaMTHs, InterpolarLineal, DirectaQs, GetXYZ_From_MTHs,
                                   LinealPuntoPunto, TrayectoriaPuntoPunto, InterpolarCubico)
from functions.unidad_2 import limitesQ, longitudes, cinematicaInversa, generaMTH, V_AceleracionContinua

class Sim_U2_T9(QWidget,Ui_sim_U2_T9):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
    def init(self):
        self.sistemas = []
        
        self.fr_nPuntosR3.hide()
        self.bt_detRob.hide()
        
        self.cp_q_1.plotWidget.setLabel('left', 'Posición')
        self.cp_qp_1.plotWidget.setLabel('left', 'Velocidad')
        self.cp_qpp_1.plotWidget.setLabel('left', 'Aceleración')
        self.cp_qppp_1.plotWidget.setLabel('left', 'JERK')
        self.cp_qppp_1.plotWidget.setLabel('bottom', 'Tiempo', units='s')
        self.cp_qppp_2.plotWidget.setLabel('bottom', 'Tiempo', units='s')
        self.cp_qppp_3.plotWidget.setLabel('bottom', 'Tiempo', units='s')
        self.cp_qppp_4.plotWidget.setLabel('bottom', 'Tiempo', units='s')
        self.cp_qppp_1.heightScale = 1/1.6
        self.cp_qppp_2.heightScale = 1/1.6
        self.cp_qppp_3.heightScale = 1/1.6
        self.cp_qppp_4.heightScale = 1/1.6
        qMin,qMax,qpMax,qppMax = limitesQ()
        self.cp_q_1.setLimits(qMin[0],qMax[0])
        self.cp_q_2.setLimits(qMin[1],qMax[1])
        self.cp_q_3.setLimits(qMin[2],qMax[2])
        self.cp_q_4.setLimits(qMin[3],qMax[3])
        self.cp_qp_1.setLimits(-qpMax[0],qpMax[0])
        self.cp_qp_2.setLimits(-qpMax[1],qpMax[1])
        self.cp_qp_3.setLimits(-qpMax[2],qpMax[2])
        self.cp_qp_4.setLimits(-qpMax[3],qpMax[3])
        self.cp_qpp_1.setLimits(-qppMax[0],qppMax[0])
        self.cp_qpp_2.setLimits(-qppMax[1],qppMax[1])
        self.cp_qpp_3.setLimits(-qppMax[2],qppMax[2])
        self.cp_qpp_4.setLimits(-qppMax[3],qppMax[3])
        self.cp_q = [self.cp_q_1,self.cp_q_2,self.cp_q_3,self.cp_q_4]
        self.cp_qp = [self.cp_qp_1,self.cp_qp_2,self.cp_qp_3,self.cp_qp_4]
        self.cp_qpp = [self.cp_qpp_1,self.cp_qpp_2,self.cp_qpp_3,self.cp_qpp_4]
        self.cp_qppp = [self.cp_qppp_1,self.cp_qppp_2,self.cp_qppp_3,self.cp_qppp_4]
        
        puntos = [[186,-55],
                  [112,132],
                  [170,338],
                  [-90, 90],
                  [  0,  1]]
        self.puntosContinua = [[186,-55,-241,186],
                               [112,132, 323,112],
                               [170,338, 224,170],
                               [-90, 90,   0, 45],
                               [  0,  1,   2,  3]]
        self.ct_puntos.setAxisLabelsVisible(True)
        self.ct_puntos.setTable(puntos)
        self.ct_puntos.set_column_prefix('P_')
        nombresFilas = ['X','Y','Z','q4','t']
        self.ct_puntos.setVerticalHeaderLabels(nombresFilas)
        self.ct_puntos.cellChanged.connect(lambda row,column: (self.bt_genTrayec.setEnabled(False),self.sb_nPuntosR3.setEnabled(False)))
        self.ct_puntos.cellClicked.connect(self.puntosClicked)
        
        self.gv_1.glView.setCameraPosition(distance=1900, azimuth=45)
        self.rejilla = Rejilla(-500,500,-500,500,-20,500,100)
        self.rejilla.loadOnGlView(self.gv_1.glView)
        
        self.robot = RobotCilindrico(0,0,0,0)
        self.robot.animacionTerminada.connect(self.animacionTerminada)
        self.robot.loadOnGlView(self.gv_1.glView)
        
        size = 15
        color = (1,0,0,1)
        pxMode=False
        self.scatterPuntos = GLScatterPlotItem(size=size,color=color,pxMode=pxMode)
        size = 4
        color = (0,1,0,1)
        self.scatterPuntos_1 = GLScatterPlotItem(size=size,color=color,pxMode=pxMode)
        self.gv_1.glView.addItem(self.scatterPuntos)
        self.gv_1.glView.addItem(self.scatterPuntos_1)
        
        self.lineTrayectory = GLLinePlotItem(color=mkColor((30,200)), width=5, mode='line_strip', antialias=True)
        self.gv_1.glView.addItem(self.lineTrayectory)
        
        self.sb_nPuntosEnt.valueChanged.connect(self.nPuntosEntChanged)
        self.sb_nPuntosR3.valueChanged.connect(self.nPuntosR3Changed)
        self.cb_tipoTrayec.currentIndexChanged.connect(self.tipoTrayeChanged)
        
        self.bt_ValidarPuntos.clicked.connect(self.validarPuntosClicked)
        self.bt_genTrayec.clicked.connect(self.genTrayecClicked)
        self.bt_movRob.clicked.connect(self.moverRobotClicked)
        self.bt_detRob.clicked.connect(self.robot.detenerAnimacion)
        
        self.generarMTHs = GenerarMTHs()
        self.generarMTHs.listMTHsGenerada.connect(self.mthsGeneradas)
        self.generarMTHs_2 = GenerarMTHs()
        self.generarMTHs_2.listMTHsGenerada.connect(self.mthsGeneradas_2)
        self.interpolarR3 = InterpolarLinealR3()
        self.interpolarR3.puntosInterpolados.connect(self.puntosInterpolados)
        self.linealP_P = LinealPuntoPunto()
        self.linealP_P.trayectoriaCalculada.connect(self.linealP_PGenerada)
        self.trapezoidalP_P = TrayectoriaPuntoPunto()
        self.trapezoidalP_P.trayectoriaCalculada.connect(self.trapezoidalP_PGenerada)
        self.directasQs = DirectaQs()
        self.directasQs.directasCalculadas.connect(self.directasCalc)
        self.getXYZ = GetXYZ_From_MTHs()
        self.getXYZ.XYZExtraidos.connect(self.xyzExtraidos)
        self.interpolarLineal = InterpolarLineal()
        self.interpolarLineal.qInterpolado.connect(self.linealContInterpolado)
        self.inversaMTHs = InversaMTHs()
        self.inversaMTHs.inversasCalculadas.connect(self.inversasCalculadas)
        self.interpolarCubico = InterpolarCubico()
        self.interpolarCubico.qInterpolado.connect(self.cubicoCalculado)

    def genTrayecClicked(self):
        dT = self.sb_Tm.value()/1000
        tipoTrayec = self.cb_tipoTrayec.currentIndex()
        tipoInt = self.cb_tipoInt.currentIndex()
        puntos = self.ct_puntos.getTable()
        puntos = array([[float(j) for j in i] for i in puntos])
        if tipoTrayec==0:
            tipoMov = self.cb_tipoMov.currentIndex()
            _,_,qpMax,_ = limitesQ()
            mth1 = generaMTH(puntos[0:3,0],puntos[3,0])
            mth2 = generaMTH(puntos[0:3,1],puntos[3,1])
            q1i,q2i,q3i,q4i = cinematicaInversa(mth1)
            q1f,q2f,q3f,q4f = cinematicaInversa(mth2)
            qi = [q1i,q2i,q3i,q4i]
            qf = [q1f,q2f,q3f,q4f]
            if tipoInt==0:
                T = [(qf[i]-qi[i])/(sign(qf[i]-qi[i])*qpMax[i]) for i in range(4)]
                if tipoMov==0:
                    nPuntos = int(floor(sum(T)/dT))
                else:
                    nPuntos = int(floor(max(T)/dT))
                q = vstack((array([qi]),array([qf]))).T.tolist()
                self.linealP_P.setQs(q[0],q[1],q[2],q[3],nPuntos,tipoMov)
                self.linealP_P.start()
            elif tipoInt==1:
                q = vstack((array([qi]),array([qf]))).T.tolist()
                self.trapezoidalP_P.dT = dT
                self.trapezoidalP_P.setQs(q[0],q[1],q[2],q[3],tipoMov)
                self.trapezoidalP_P.start()
        elif tipoTrayec==1:
            self.generarMTHs_2.setPuntos(self.puntosInt)
            self.generarMTHs_2.start()
        if self.cb_tipoInt.currentText()=='Cúbico':
            for i in range(4):
                self.cp_qp[i].puntos_1.setVisible(True)
        else:
            for i in range(4):
                self.cp_qp[i].puntos_1.setVisible(False)
            
    def linealContInterpolado(self,q,qp,tm):
        self.q = hstack(((array([tm])*1000).T,array(q).T))
        self.graficar(tm,q,qp)
        self.directasQs.setQs(q[0],q[1],q[2],q[3])
        self.directasQs.start()
        
    def cubicoCalculado(self,q,qp,qpp,qppp,t):
        self.q = hstack(((array([t])*1000).T,array(q).T))
        self.graficar(t,q,qp,qpp,qppp)
        self.directasQs.setQs(q[0],q[1],q[2],q[3])
        self.directasQs.start()
    
    def linealP_PGenerada(self,tm,q,qp,tqi):
        self.q = hstack(((array([tm])*1000).T,array(q).T))
        self.graficar(tm,q,qp)
        self.directasQs.setQs(q[0],q[1],q[2],q[3])
        self.directasQs.start()
        puntos = self.ct_puntos.getTable()
        puntos = array([[float(j) for j in i] for i in puntos])
        mth1 = generaMTH(puntos[0:3,0],puntos[3,0])
        mth2 = generaMTH(puntos[0:3,1],puntos[3,1])
        q1i,q2i,q3i,q4i = cinematicaInversa(mth1)
        q1f,q2f,q3f,q4f = cinematicaInversa(mth2)
        qi = [q1i,q2i,q3i,q4i]
        qf = [q1f,q2f,q3f,q4f]
        q = vstack((array([qi]),array([qf]))).T.tolist()
        for i in range(4):
            self.cp_q[i].setData(tqi[i],q[i],[0])
        
    def trapezoidalP_PGenerada(self,tm,q,qp,qpp,tqi):
        self.q = hstack(((array([tm])*1000).T,array(q).T))
        self.graficar(tm,q,qp,qpp)
        self.directasQs.setQs(q[0],q[1],q[2],q[3])
        self.directasQs.start()
        puntos = self.ct_puntos.getTable()
        puntos = array([[float(j) for j in i] for i in puntos])
        mth1 = generaMTH(puntos[0:3,0],puntos[3,0])
        mth2 = generaMTH(puntos[0:3,1],puntos[3,1])
        q1i,q2i,q3i,q4i = cinematicaInversa(mth1)
        q1f,q2f,q3f,q4f = cinematicaInversa(mth2)
        qi = [q1i,q2i,q3i,q4i]
        qf = [q1f,q2f,q3f,q4f]
        q = vstack((array([qi]),array([qf]))).T.tolist()
        for i in range(4):
            self.cp_q[i].setData(tqi[i],q[i],[0])
    
    def graficar(self,tm,q,qp,qpp=None,qppp=None):
        if type(qpp)==type(None):
            qpp = [zeros(len(tm)) for i in range(4)]
        if type(qppp)==type(None):
            qppp = [zeros(len(tm)) for i in range(4)]
        for i in range(4):
            self.cp_q[i].setData(tm,q[i],[1,2])
            self.cp_qp[i].setData(tm,qp[i],[1,2])
            self.cp_qpp[i].setData(tm,qpp[i],[1,2])
            self.cp_qppp[i].setData(tm,qppp[i],[1,2])
        
    def directasCalc(self,MTHs):
        self.getXYZ.setMTHs(MTHs)
        self.getXYZ.start()
    
    def xyzExtraidos(self,puntos):
        self.lineTrayectory.setData(pos=puntos)
        self.scatterPuntos_1.setData(pos=puntos)
        self.bt_movRob.setEnabled(True)
    
    def mthsGeneradas(self,MTHs):
        self.MTHs_1 = MTHs
        for sistema in self.sistemas:
            sistema.removeItem()
        self.sistemas=[]
        for i in range(len(MTHs)):
            self.sistemas.append(SistemaCoordenadas3D(array(MTHs[i]),90,5,str(i+1)))
            self.sistemas[i].loadOnGlView(self.gv_1.glView)
        q1,q2,q3,q4 = cinematicaInversa(array(MTHs[0]))
        self.robot.setPosQ(q1,q2,q3,q4)
        puntos = self.ct_puntos.getTable()
        puntos = [[float(j) for j in i] for i in puntos]
        if self.cb_tipoTrayec.currentIndex()==0:
            puntos = array(puntos)
            puntos = puntos[0:3,:].T
            self.scatterPuntos.setData(pos=puntos)
        else:
            self.sb_nPuntosR3.valueChanged.disconnect(self.nPuntosR3Changed)
            self.sb_nPuntosR3.setMinimum(len(puntos[0]))
            self.sb_nPuntosR3.valueChanged.connect(self.nPuntosR3Changed)
            self.interpolarR3.setPuntos(puntos,self.sb_nPuntosR3.value())
            self.interpolarR3.start()
        
    def mthsGeneradas_2(self,MTHs):
        self.MTHs_2 = MTHs
        self.inversaMTHs.setMTHs(MTHs)
        self.inversaMTHs.start()
        
    def inversasCalculadas(self,q1,q2,q3,q4):
        t = self.puntosInt[-1]
        q = [q1,q2,q3,q4]
        for i in range(4):
            self.cp_q[i].setData(t,q[i],[0])
        nPuntos = int(floor((t[-1]-t[0])/(self.sb_Tm.value()/1000)))
        tipoInt=self.cb_tipoInt.currentIndex()
        if tipoInt==0:
            self.interpolarLineal.setQ(q,t,nPuntos)
            self.interpolarLineal.start()
        elif tipoInt==1:
            v = [V_AceleracionContinua(t,q[i]) for i in range(4)]
            for i in range(4):
                self.cp_qp[i].setData(t,v[i],[0])
            self.interpolarCubico.setQ(q,t,nPuntos)
            self.interpolarCubico.start()
        
    def puntosInterpolados(self,puntos):
        self.puntosInt = puntos
        puntos = array(puntos)
        puntos = puntos[0:3,:].T
        self.scatterPuntos.setData(pos=puntos)
    
    def moverRobotClicked(self):
        self.bt_movRob.hide()
        self.bt_detRob.show()
        self.robot.iniciarAinimacion(self.q)
        
    def animacionTerminada(self):
        self.bt_detRob.hide()
        self.bt_movRob.show()
    
    def validarPuntosClicked(self):
        dato,i = self.validarPuntos()
        qMin,qMax,_,_ = limitesQ()
        L1,_,_ = longitudes()
        if dato==0:
            QMessageBox().information(self,'Puntos correctos','Todos los puntos son alcanzables por el robot.')
            puntos = self.ct_puntos.getTable()
            puntos = [[float(j) for j in i] for i in puntos]
            self.bt_genTrayec.setEnabled(True)
            self.sb_nPuntosR3.setEnabled(True)
            self.generarMTHs.setPuntos(puntos)
            self.generarMTHs.start()
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
    
    def puntosClicked(self,row,column):
        if self.bt_genTrayec.isEnabled():
            puntos = self.ct_puntos.getTable()
            puntos = array([[float(j) for j in i] for i in puntos])
            P = puntos[0:3,column]
            q4 = puntos[3,column]
            mth = generaMTH(P,q4)
            q1,q2,q3,q4 = cinematicaInversa(mth)
            self.robot.setPosQ(q1,q2,q3,q4)
    
    def nPuntosR3Changed(self,value):
        puntos = self.ct_puntos.getTable()
        puntos = [[float(j) for j in i] for i in puntos]
        self.interpolarR3.setPuntos(puntos,self.sb_nPuntosR3.value())
        self.interpolarR3.start()
    
    def nPuntosEntChanged(self,value):
        self.ct_puntos.setColumnS(value)
        self.bt_genTrayec.setEnabled(False)
        self.sb_nPuntosR3.setEnabled(False)
    
    def tipoTrayeChanged(self,index):
        if index==0:
            self.fr_nPuntosR3.hide()
            self.fr_tipoMov.show()
            self.cb_tipoInt.setItemText(1,'Trapezoidal')
            self.puntosContinua = self.ct_puntos.getTable()
            self.sb_nPuntosEnt.setEnabled(False)
            self.sb_nPuntosEnt.setValue(2)
        else:
            self.fr_nPuntosR3.show()
            self.fr_tipoMov.hide()
            self.cb_tipoInt.setItemText(1,'Cúbico')
            self.sb_nPuntosEnt.setValue(len(self.puntosContinua[0]))
            self.ct_puntos.setTable(self.puntosContinua)
            self.sb_nPuntosEnt.setEnabled(True)
    