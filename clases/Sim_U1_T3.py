from PySide6.QtWidgets import QWidget
import pyqtgraph as pg
from numpy import eye
from clases.ui_sim_U1_T3 import Ui_sim_U1_T3
from clases.Robot3D import Solido, RobotCilindrico, Rejilla
from functions.unidad_1 import rotX, rotY, rotZ

# Activar antialiasing globalmente
pg.setConfigOptions(antialias=True)


class Sim_U1_T3(QWidget,Ui_sim_U1_T3):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
    
    def init(self):
        self.glView_1.glView.setCameraPosition(distance=600, azimuth=45)
        self.glView_2.glView.setCameraPosition(distance=1900, azimuth=45)
        self.glView_1.glView.opts['rotationMode'] = 'quaternion'
        self.glView_2.glView.opts['rotationMode'] = 'quaternion'
        self.rejillas1 = Rejilla(-500,500,-500,500,-20,500,100)
        self.rejillas2 = Rejilla(-500,500,-500,500,-20,500,100)
        self.rejillas1.loadOnGlView(self.glView_1.glView)
        self.rejillas2.loadOnGlView(self.glView_2.glView)
        ############################################  Simulación localización de solidos  #########################################
        self.solido = Solido(eye(4))
        self.solido.loadOnGlView(self.glView_1.glView)
        self.sl_rotX.valueChanged.connect(lambda value: (self.asignarA(),self.sb_rX.setValue(value)))
        self.sl_rotY.valueChanged.connect(lambda value: (self.asignarA(),self.sb_rY.setValue(value)))
        self.sl_rotZ.valueChanged.connect(lambda value: (self.asignarA(),self.sb_rZ.setValue(value)))
        self.sl_despX.valueChanged.connect(lambda value: (self.asignarA(),self.sb_dX.setValue(value)))
        self.sl_despY.valueChanged.connect(lambda value: (self.asignarA(),self.sb_dY.setValue(value)))
        self.sl_despZ.valueChanged.connect(lambda value: (self.asignarA(),self.sb_dZ.setValue(value)))
        self.cb_ecuaciones.currentIndexChanged.connect(self.asignarA)
        ###########################################################################################################################
        ##############################################  Simulación robot cilíndrico 3D  ###########################################
        self.robotCilindrico = RobotCilindrico(0,0,0,0)
        self.robotCilindrico.loadOnGlView(self.glView_2.glView)
        self.sl_q1.valueChanged.connect(lambda value:(self.asignarPosicion(),self.sb_q1.setValue(value)))
        self.sl_q2.valueChanged.connect(lambda value:(self.asignarPosicion(),self.sb_q2.setValue(value)))
        self.sl_q3.valueChanged.connect(lambda value:(self.asignarPosicion(),self.sb_q3.setValue(value)))
        self.sl_q4.valueChanged.connect(lambda value:(self.asignarPosicion(),self.sb_q4.setValue(value)))
        
        self.bt_ver3D.hide()
        self.bt_ver3D.clicked.connect(lambda:(self.robotCilindrico.setEn3D(2),self.bt_ver3D.hide(),self.bt_verLineas.show()))
        self.bt_verLineas.clicked.connect(lambda:(self.robotCilindrico.setEn3D(0),self.bt_ver3D.show(),self.bt_verLineas.hide()))
        
        ###########################################################################################################################
        
    def asignarPosicion(self,value=None):
        self.robotCilindrico.setPosQ(self.sl_q1.value(),self.sl_q2.value(),self.sl_q3.value(),self.sl_q4.value())
        
    def asignarA(self, value=None):
        desplazamiento = eye(4)
        desplazamiento[0,3] = self.sl_despX.value()
        desplazamiento[1,3] = self.sl_despY.value()
        desplazamiento[2,3] = self.sl_despZ.value()
        rX = rotX(self.sl_rotX.value())
        rY = rotY(self.sl_rotY.value())
        rZ = rotZ(self.sl_rotZ.value())
        if self.cb_ecuaciones.currentIndex() == 0:
            A = rX @ rY @ rZ @ desplazamiento
        elif self.cb_ecuaciones.currentIndex() == 1:
            A = rX @ rZ @ rY @ desplazamiento
        elif self.cb_ecuaciones.currentIndex() == 2:
            A = rY @ rZ @ rX @ desplazamiento
        elif self.cb_ecuaciones.currentIndex() == 3:
            A = rY @ rX @ rZ @ desplazamiento
        elif self.cb_ecuaciones.currentIndex() == 4:
            A = rZ @ rX @ rY @ desplazamiento
        elif self.cb_ecuaciones.currentIndex() == 5:
            A = rZ @ rY @ rX @ desplazamiento
        self.solido.setA(A)
        
        