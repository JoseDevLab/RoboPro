from PySide6.QtWidgets import QWidget
from numpy import linspace, transpose, concatenate
from clases.ui_sim_U1_T5 import Ui_sim_U1_T5
from clases.Robot3D import RobotCilindrico, Rejilla

class Sim_U1_T5(QWidget,Ui_sim_U1_T5):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        
    def init(self):
        self.glView_1.glView.setCameraPosition(distance=1900, azimuth=45)
        self.glView_2.glView.setCameraPosition(distance=1900, azimuth=45)
        self.glView_3.glView.setCameraPosition(distance=1900, azimuth=45)
        self.rejillas1 = Rejilla(-500,500,-500,500,-20,500,100)
        self.rejillas2 = Rejilla(-500,500,-500,500,-20,500,100)
        self.rejillas3 = Rejilla(-500,500,-500,500,-20,500,100)
        self.rejillas1.loadOnGlView(self.glView_1.glView)
        self.rejillas2.loadOnGlView(self.glView_2.glView)
        self.rejillas3.loadOnGlView(self.glView_3.glView)
        
        ##################################################  Simulación robot 1 3D  ###############################################
        self.robot_1 = RobotCilindrico(0,0,0,0)
        self.robot_1.loadOnGlView(self.glView_1.glView)
        self.sl_q1_1.valueChanged.connect(lambda value:(self.asignarPosicion_1(),self.sb_q1.setValue(value)))
        self.sl_q2_1.valueChanged.connect(lambda value:(self.asignarPosicion_1(),self.sb_q2.setValue(value)))
        self.sl_q3_1.valueChanged.connect(lambda value:(self.asignarPosicion_1(),self.sb_q3.setValue(value)))
        self.sl_q4_1.valueChanged.connect(lambda value:(self.asignarPosicion_1(),self.sb_q4.setValue(value)))
        ###########################################################################################################################
        ##################################################  Simulación robot 2 3D  ###############################################
        self.robot_2 = RobotCilindrico(0,0,0,0)
        self.robot_2.loadOnGlView(self.glView_2.glView)
        self.sl_q1_2.valueChanged.connect(lambda value:(self.asignarPosicion_2(),self.sb_q1_2.setValue(value)))
        self.sl_q2_2.valueChanged.connect(lambda value:(self.asignarPosicion_2(),self.sb_q2_2.setValue(value)))
        self.sl_q3_2.valueChanged.connect(lambda value:(self.asignarPosicion_2(),self.sb_q3_2.setValue(value)))
        self.sl_q4_2.valueChanged.connect(lambda value:(self.asignarPosicion_2(),self.sb_q4_2.setValue(value)))
        ###########################################################################################################################
        ##################################################  Simulación robot 3 3D  ###############################################
        self.robot_3 = RobotCilindrico(0,0,0,0)
        self.robot_3.loadOnGlView(self.glView_3.glView)
        self.sl_q1_1.valueChanged.connect(self.asignarPosicion_3)
        self.sl_q2_1.valueChanged.connect(self.asignarPosicion_3)
        self.sl_q3_1.valueChanged.connect(self.asignarPosicion_3)
        self.sl_q4_1.valueChanged.connect(self.asignarPosicion_3)
        self.bt_iniciarAnimacion.clicked.connect(self.iniciarAnimacion)
        self.robot_3.animacionTerminada.connect(lambda: self.bt_iniciarAnimacion.setEnabled(True))
        ###########################################################################################################################
        
    def asignarPosicion_1(self,value=None):
        self.robot_1.setPosQ(self.sl_q1_1.value(),self.sl_q2_1.value(),self.sl_q3_1.value(),self.sl_q4_1.value())
        
    def asignarPosicion_2(self,value=None):
        self.robot_2.setPosQ(self.sl_q1_2.value(),self.sl_q2_2.value(),self.sl_q3_2.value(),self.sl_q4_2.value())
    
    def asignarPosicion_3(self,value=None):
        self.robot_3.setPosQ(self.sl_q1_1.value(),self.sl_q2_1.value(),self.sl_q3_1.value(),self.sl_q4_1.value())
        
    def iniciarAnimacion(self):
        self.bt_iniciarAnimacion.setEnabled(False)
        n = self.sb_nPuntos.value()
        t = transpose([linspace(0,self.sb_tFinal.value()*1000,n)])
        vq1 = transpose([linspace(self.sl_q1_1.value(),self.sl_q1_2.value(),n)])
        vq2 = transpose([linspace(self.sl_q2_1.value(),self.sl_q2_2.value(),n)])
        vq3 = transpose([linspace(self.sl_q3_1.value(),self.sl_q3_2.value(),n)])
        vq4 = transpose([linspace(self.sl_q4_1.value(),self.sl_q4_2.value(),n)])
        puntos = concatenate((t,vq1,vq2,vq3,vq4),1)
        self.robot_3.iniciarAinimacion(puntos)