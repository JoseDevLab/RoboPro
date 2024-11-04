from PySide6.QtWidgets import QWidget, QMessageBox
from pyqtgraph.opengl import GLScatterPlotItem, GLLinePlotItem
import pyqtgraph as pg
from clases.ui_sim_U2_T1 import Ui_sim_U2_T1
from clases.Robot3D import RobotCilindrico, Rejilla, SistemaCoordenadas3D
from clases.Hilos_Unidad_2 import GenerarMTHs, InterpolarLinealR3, InversaMTHs, InterpolarLineal, DirectaQs, GetXYZ_From_MTHs
from functions.unidad_2 import cinematicaInversa, limitesQ
from numpy import array, hstack
from math import floor

pg.setConfigOptions(antialias=True)

class Sim_U2_T1(QWidget,Ui_sim_U2_T1):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
    
    def init(self):
        self.sistemas_1 = []
        self.sistemas_2 = []
        self.sistemas_3 = []
        self.MTHs_1 = []
        self.MTHs_2 = []
        self.MTHs_3 = []
        self.nPuntosR3_2 = 19
        self.nPuntosArt = 100
        
        self.plot_pos_q1.plotWidget.setLabel('left', 'Posición', units='° , cm')
        self.plot_pos_q1_2.plotWidget.setLabel('left', 'Posición', units='° , cm')
        self.plot_vel_q1_2.plotWidget.setLabel('left', 'Velocidad', units='°/s , cm/s')
        qMin,qMax,qpMax,_ = limitesQ()
        self.plot_pos_q1.setLimits(qMin[0],qMax[0])
        self.plot_pos_q2.setLimits(qMin[1],qMax[1])
        self.plot_pos_q3.setLimits(qMin[2],qMax[2])
        self.plot_pos_q4.setLimits(qMin[3],qMax[3])
        self.plot_pos_q1_2.setLimits(qMin[0],qMax[0])
        self.plot_pos_q2_2.setLimits(qMin[1],qMax[1])
        self.plot_pos_q3_2.setLimits(qMin[2],qMax[2])
        self.plot_pos_q4_2.setLimits(qMin[3],qMax[3])
        self.plot_vel_q1_2.setLimits(-qpMax[0],qpMax[0])
        self.plot_vel_q2_2.setLimits(-qpMax[1],qpMax[1])
        self.plot_vel_q3_2.setLimits(-qpMax[2],qpMax[2])
        self.plot_vel_q4_2.setLimits(-qpMax[3],qpMax[3])
        
        self.bt_basadoTiempo.hide()
        self.bt_basadoTiempo_2.hide()
        self.fr_deltaT.hide()
        self.fr_deltaT_2.hide()
        self.bt_verEn3D.hide()
        self.bt_ocultar.hide()
        
        puntos = [[186,-55,-241,186],
                  [112,132, 323,112],
                  [170,338, 224,170],
                  [-90, 90,   0, 45],
                  [0,    1,   2,  3]]
        self.ct_puntosR3.setAxisLabelsVisible(True)
        self.ct_puntosR3_2.setAxisLabelsVisible(True)
        self.ct_puntosR3.setSize(5,4)
        self.ct_puntosR3.setTable(puntos)
        self.ct_puntosR3_2.setSize(5,20)
        self.ct_puntosR3.set_column_prefix('P_')
        self.ct_puntosR3_2.set_column_prefix('P_')
        nombresFilas = ['X','Y','Z','q4','t']
        self.ct_puntosR3.setVerticalHeaderLabels(nombresFilas)
        self.ct_puntosR3_2.setVerticalHeaderLabels(nombresFilas)
        self.ct_puntosR3_2.setEditable(False)
        
        self.sb_nPuntosR3_1.valueChanged.connect(self.nPuntosR3_1ValueChanged)
        self.sb_nPuntosR3_2.valueChanged.connect(self.nPuntosR3_2ValueChanged)
        self.sb_dT_1.valueChanged.connect(self.dT_1ValueChanged)
        self.sb_dT_2.valueChanged.connect(self.dT_2ValueChanged)
        self.sb_nPuntosArt.valueChanged.connect(self.nPuntosArtValueChanged)
        
        self.bt_basadoPuntos.clicked.connect(self.basadoPuntosClicked)
        self.bt_basadoTiempo.clicked.connect(self.basadoTiempoClicked)
        self.bt_basadoPuntos_2.clicked.connect(self.basadoPuntos_2Clicked)
        self.bt_basadoTiempo_2.clicked.connect(self.basadoTiempo_2Clicked)
        self.bt_verEn3D.clicked.connect(self.verEn3DClicked)
        self.bt_verEnLineas.clicked.connect(self.verEnLineasClicked)
        self.bt_ocultar.clicked.connect(self.ocultarClicked)
        self.bt_interpolarR3.clicked.connect(self.interpolarR3Clicked)
        self.bt_transformarInversa.clicked.connect(self.transformarInversaClicked)
        self.bt_interpolarArt.clicked.connect(self.interpolarArtClicked)
        self.bt_transformarDirecta.clicked.connect(self.transformarDirectaClicked)
        self.bt_iniciarAnimacion.clicked.connect(self.iniciarAnimacionClicked)
        
        # Configuración inicial de las listas de MTH
        self.mthList_1.setEditable(False)
        self.mthList_1.setNTablas(4)
        self.mthList_2.setEditable(False)
        self.mthList_2.setNTablas(20)
        self.mthList_3.setEditable(False)
        self.mthList_3.setNTablas(100)
        
        self.glView_1.glView.setCameraPosition(distance=1900, azimuth=45)
        self.glView_2.glView.setCameraPosition(distance=1900, azimuth=45)
        self.glView_3.glView.setCameraPosition(distance=1900, azimuth=45)
        self.rejilla_1 = Rejilla(-500,500,-500,500,-20,500,100)
        self.rejilla_2 = Rejilla(-500,500,-500,500,-20,500,100)
        self.rejilla_3 = Rejilla(-500,500,-500,500,-20,500,100)
        self.rejilla_1.loadOnGlView(self.glView_1.glView)
        self.rejilla_2.loadOnGlView(self.glView_2.glView)
        self.rejilla_3.loadOnGlView(self.glView_3.glView)
        
        self.robot_1 = RobotCilindrico(0,0,0,0)
        self.robot_2 = RobotCilindrico(0,0,0,0)
        self.robot_3 = RobotCilindrico(0,0,0,0)
        self.robot_1.loadOnGlView(self.glView_1.glView)
        self.robot_2.loadOnGlView(self.glView_2.glView)
        self.robot_3.loadOnGlView(self.glView_3.glView)
        self.robot_3.animacionTerminada.connect(self.animacionTerminada)
        
        self.scatterPuntos = GLScatterPlotItem()
        self.scatterPuntos_2 = GLScatterPlotItem()
        self.glView_2.glView.addItem(self.scatterPuntos)
        self.glView_3.glView.addItem(self.scatterPuntos_2)
        
        self.lineTrayectory = GLLinePlotItem(color=pg.mkColor((30,200)), width=5, mode='line_strip', antialias=True)
        self.glView_3.glView.addItem(self.lineTrayectory)
        
        self.generarMTHs = GenerarMTHs()
        self.generarMTHs.listMTHsGenerada.connect(self.listMTHsGenerada)
        self.generarMTHs.ocurrioError.connect(lambda:(QMessageBox().critical( self,'Ocurrió un error','Verifica que los datos ingresados sean correctos'),self.bt_generarMTHs.setEnabled(True)))
        self.generarMTHs_2 = GenerarMTHs()
        self.generarMTHs_2.listMTHsGenerada.connect(self.listMTHsGenerada_2)
        self.interpolarLinealR3 = InterpolarLinealR3()
        self.interpolarLinealR3.puntosInterpolados.connect(self.puntosInterpolados)
        self.inversaMTHs = InversaMTHs()
        self.inversaMTHs.inversasCalculadas.connect(self.inversasCalculadas)
        self.interpolarLineal = InterpolarLineal()
        self.interpolarLineal.qInterpolado.connect(self.qInterpolado)
        self.directaQs = DirectaQs()
        self.directaQs.directasCalculadas.connect(self.directasCalculadas)
        self.getXYZ_from_MTHs = GetXYZ_From_MTHs()
        self.getXYZ_from_MTHs.XYZExtraidos.connect(self.xyzExtraidos)
                
        self.bt_generarMTHs.clicked.connect(self.generarMTHsClicked)
        self.mthList_1.MTHClicked.connect(self.MTHList_1Clicked)
        self.mthList_2.MTHClicked.connect(self.MTHList_2Clicked)
        self.mthList_3.MTHClicked.connect(self.MTHList_3Clicked)
    
    def MTHList_1Clicked(self, index):
        if len(self.MTHs_1) > 0:
            if index+1 <= len(self.MTHs_1):
                q1,q2,q3,q4 = cinematicaInversa(array(self.MTHs_1[index]))
                self.robot_1.setPosQ(q1,q2,q3,q4)
    
    def MTHList_2Clicked(self, index):
        if len(self.MTHs_2) > 0:
            if index+1 <= len(self.MTHs_2):
                q1,q2,q3,q4 = cinematicaInversa(array(self.MTHs_2[index]))
                self.robot_2.setPosQ(q1,q2,q3,q4)
    
    def MTHList_3Clicked(self, index):
        if len(self.MTHs_3) > 0:
            if index+1 <= len(self.MTHs_3):
                q1,q2,q3,q4 = cinematicaInversa(array(self.MTHs_3[index]))
                self.robot_3.setPosQ(q1,q2,q3,q4)
    
    def listMTHsGenerada(self, MTHs:list):
        self.MTHs_1 = MTHs
        self.bt_generarMTHs.setEnabled(True)
        self.bt_interpolarR3.setEnabled(True)
        self.bt_basadoPuntos.setEnabled(True)
        self.sb_nPuntosR3_2.setEnabled(True)
        self.mthList_1.setListMTH(MTHs)
        for sistema in self.sistemas_1:
            sistema.removeItem()
        for sistema in self.sistemas_2:
            sistema.removeItem()
        self.sistemas_1=[]
        self.sistemas_2=[]
        self.sistemas_3=[]
        for i in range(len(MTHs)):
            self.sistemas_1.append(SistemaCoordenadas3D(array(MTHs[i]),90,5,str(i+1)))
            self.sistemas_1[i].loadOnGlView(self.glView_1.glView)
            self.sistemas_2.append(SistemaCoordenadas3D(array(MTHs[i]),90,5,str(i+1)))
            self.sistemas_2[i].loadOnGlView(self.glView_2.glView)
            self.sistemas_3.append(SistemaCoordenadas3D(array(MTHs[i]),90,5,str(i+1)))
            self.sistemas_3[i].loadOnGlView(self.glView_3.glView)
        q1,q2,q3,q4 = cinematicaInversa(array(MTHs[0]))
        self.robot_1.setPosQ(q1,q2,q3,q4)
        self.robot_2.setPosQ(q1,q2,q3,q4)
        self.robot_3.setPosQ(q1,q2,q3,q4)
    
    def listMTHsGenerada_2(self, MTHs:list):
        self.MTHs_2 = MTHs
        self.mthList_2.setListMTH(MTHs)
    
    def generarMTHsClicked(self):
        self.bt_generarMTHs.setEnabled(False)
        puntos = self.ct_puntosR3.getTable()
        # Convertir los puntos a tipo float
        puntos = [[float(elemento) for elemento in sublista] for sublista in puntos]
        tiempos = puntos[-1]
        # Validar si los tiempos son correctos
        if all(tiempos[i] < tiempos[i + 1] for i in range(len(tiempos) - 1)):
            self.puntosR3 = puntos
            nPuntos = self.sb_nPuntosR3_1.value()
            tTotal = (tiempos[-1] - tiempos[0])*1000
            self.tTotal = tTotal
            Tmax = floor(tTotal/nPuntos)
            self.sb_nPuntosR3_2.setMinimum(nPuntos)
            self.sb_dT_1.setMaximum(Tmax)
            self.generarMTHs.setPuntos(puntos)
            self.generarMTHs.start()
        else:
            QMessageBox().critical(self,'Valores de tiempos incorrectos','Verifique que los tiempos sean siempre de forma ascendente y no se repitan')
            self.bt_generarMTHs.setEnabled(True)
        
    def nPuntosR3_1ValueChanged(self, value):
        self.ct_puntosR3.setColumnS(value)
        
    def nPuntosR3_2ValueChanged(self, value):
        self.ct_puntosR3_2.setColumnS(value)
        self.nPuntosR3_2 = value
        
    def dT_1ValueChanged(self, value):
        nPuntos = round(self.tTotal/value)
        self.ct_puntosR3_2.setColumnS(nPuntos)
        self.nPuntosR3_2 = nPuntos
        
    def interpolarR3Clicked(self):
        self.bt_interpolarR3.setEnabled(False)
        self.interpolarLinealR3.setPuntos(self.puntosR3,self.nPuntosR3_2)
        self.interpolarLinealR3.start()
        
    def puntosInterpolados(self,puntos):
        self.tTotal_2 = self.tTotal
        self.puntosR3Int = puntos
        puntos = [[round(elemento,2) for elemento in sublista] for sublista in puntos]
        self.tiempoInt_1 = array(puntos)[-1,:]
        self.ct_puntosR3_2.setTable(puntos)
        self.bt_interpolarR3.setEnabled(True)
        self.bt_transformarInversa.setEnabled(True)
        self.generarMTHs_2.setPuntos(puntos)
        self.generarMTHs_2.start()
        puntos = array(puntos)
        puntos = puntos[0:3,:].T
        size = 15
        color = (1,0,0,1)
        self.scatterPuntos.setData(pos=puntos,size=size,color=color,pxMode=False)
        self.scatterPuntos_2.setData(pos=puntos,size=size,color=color,pxMode=False)
        self.bt_interpolarR3.setEnabled(True)
    
    def transformarInversaClicked(self):
        self.bt_transformarInversa.setEnabled(False)
        self.inversaMTHs.setMTHs(self.MTHs_2)
        self.inversaMTHs.start()
        
    def inversasCalculadas(self, q1,q2,q3,q4):
        self.tTotal_3 = self.tTotal_2
        nPuntos = len(q1)
        self.sb_nPuntosArt.setMinimum(nPuntos)
        self.sb_dT_2.setMaximum(floor(self.tTotal_2/nPuntos))
        self.q = [q1,q2,q3,q4]
        self.plot_pos_q1.setData(self.tiempoInt_1,q1,[0])
        self.plot_pos_q2.setData(self.tiempoInt_1,q2,[0])
        self.plot_pos_q3.setData(self.tiempoInt_1,q3,[0])
        self.plot_pos_q4.setData(self.tiempoInt_1,q4,[0])
        self.plot_pos_q1_2.setData(self.tiempoInt_1,q1,[0])
        self.plot_pos_q2_2.setData(self.tiempoInt_1,q2,[0])
        self.plot_pos_q3_2.setData(self.tiempoInt_1,q3,[0])
        self.plot_pos_q4_2.setData(self.tiempoInt_1,q4,[0])
        
        self.bt_transformarInversa.setEnabled(True)
        self.bt_interpolarArt.setEnabled(True)
        self.bt_basadoPuntos_2.setEnabled(True)
        self.sb_nPuntosArt.setEnabled(True)
        
    def interpolarArtClicked(self):
        self.bt_interpolarArt.setEnabled(False)
        self.interpolarLineal.setQ(self.q,self.tiempoInt_1,self.nPuntosArt)
        self.interpolarLineal.start()
    
    def qInterpolado(self,q:list,qp:list,t:list):
        self.qInt = q
        self.qpInt = qp
        self.tInt = t
        self.plot_pos_q1_2.setData(t,q[0],[1,2])
        self.plot_pos_q2_2.setData(t,q[1],[1,2])
        self.plot_pos_q3_2.setData(t,q[2],[1,2])
        self.plot_pos_q4_2.setData(t,q[3],[1,2])
        self.plot_vel_q1_2.setData(t,qp[0],[1,2])
        self.plot_vel_q2_2.setData(t,qp[1],[1,2])
        self.plot_vel_q3_2.setData(t,qp[2],[1,2])
        self.plot_vel_q4_2.setData(t,qp[3],[1,2])
        self.bt_interpolarArt.setEnabled(True)
        self.bt_transformarDirecta.setEnabled(True)
        
    def transformarDirectaClicked(self):
        self.bt_transformarDirecta.setEnabled(False)
        self.directaQs.setQs(self.qInt[0],self.qInt[1],self.qInt[2],self.qInt[3])
        self.directaQs.start()
    
    def directasCalculadas(self,MTHs):
        self.MTHs_3 = MTHs
        self.getXYZ_from_MTHs.setMTHs(MTHs)
        self.getXYZ_from_MTHs.start()
        MTHs = [[[round(elemento,2) for elemento in sublista] for sublista in sublista_1] for sublista_1 in MTHs]
        self.mthList_3.setListMTH(MTHs)
        self.bt_transformarDirecta.setEnabled(True)
        self.bt_iniciarAnimacion.setEnabled(True)
        self.bt_verEnLineas.setEnabled(True)
        
    def xyzExtraidos(self, puntos):
        self.lineTrayectory.setData(pos=puntos)
        
    def iniciarAnimacionClicked(self):
        self.bt_iniciarAnimacion.setEnabled(False)
        t = array([self.tInt]).T
        q1 = array([self.qInt[0]]).T
        q2 = array([self.qInt[1]]).T
        q3 = array([self.qInt[2]]).T
        q4 = array([self.qInt[3]]).T
        puntos = hstack((t,q1,q2,q3,q4))
        self.robot_3.iniciarAinimacion(puntos)
    
    def animacionTerminada(self):
        self.bt_iniciarAnimacion.setEnabled(True)
        
    def nPuntosArtValueChanged(self, value):
        self.nPuntosArt = value
        
    def dT_2ValueChanged(self, value):
        nPuntos = round(self.tTotal_3/value)
        self.nPuntosArt = nPuntos
        
    def basadoPuntosClicked(self):
        nPuntos = self.sb_nPuntosR3_2.value()
        self.sb_dT_1.setValue(floor(self.tTotal/nPuntos))
        self.bt_basadoPuntos.hide()
        self.bt_basadoTiempo.show()
        self.fr_nPuntos.hide()
        self.fr_deltaT.show()
        
    def basadoTiempoClicked(self):
        dT = self.sb_dT_1.value()
        nPuntos = round(self.tTotal/dT)
        self.sb_nPuntosR3_2.setValue(nPuntos)
        self.bt_basadoTiempo.hide()
        self.bt_basadoPuntos.show()
        self.fr_deltaT.hide()
        self.fr_nPuntos.show()
    
    def basadoPuntos_2Clicked(self):
        nPuntos = self.sb_nPuntosArt.value()
        self.sb_dT_2.setValue(floor(self.tTotal_3/nPuntos))
        self.bt_basadoPuntos_2.hide()
        self.bt_basadoTiempo_2.show()
        self.fr_nPuntos_2.hide()
        self.fr_deltaT_2.show()
    
    def basadoTiempo_2Clicked(self):
        dT = self.sb_dT_2.value()
        nPuntos = round(self.tTotal_3/dT)
        self.sb_nPuntosArt.setValue(nPuntos)
        self.bt_basadoTiempo_2.hide()
        self.bt_basadoPuntos_2.show()
        self.fr_deltaT_2.hide()
        self.fr_nPuntos_2.show()
    
    def verEn3DClicked(self):
        self.verticalScrollVarValue = self.scrollArea.verticalScrollBar().value()
        self.robot_3.setEn3D(2)
        self.bt_verEn3D.hide()
        self.bt_verEnLineas.show()
        self.scrollArea.verticalScrollBar().setValue(self.verticalScrollVarValue)
    
    def verEnLineasClicked(self):
        self.verticalScrollVarValue = self.scrollArea.verticalScrollBar().value()
        self.robot_3.setEn3D(1)
        self.bt_verEnLineas.hide()
        self.bt_ocultar.show()
        self.scrollArea.verticalScrollBar().setValue(self.verticalScrollVarValue)
    
    def ocultarClicked(self):
        self.verticalScrollVarValue = self.scrollArea.verticalScrollBar().value()
        self.robot_3.setEn3D(0)
        self.bt_ocultar.hide()
        self.bt_verEn3D.show()
        self.scrollArea.verticalScrollBar().setValue(self.verticalScrollVarValue)
        
