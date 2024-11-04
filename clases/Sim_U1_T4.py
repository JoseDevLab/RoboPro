from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QTimer
from numpy import eye, linspace
from clases.ui_sim_U1_T4 import Ui_Sim_U1_T4
from clases.Robot3D import Solido, Rejilla
from functions.unidad_1 import rotX, rotY, rotZ

class Sim_U1_T4(QWidget,Ui_Sim_U1_T4):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        
    def init(self):
        self.glView_1.glView.setCameraPosition(distance=600, azimuth=45)
        self.glView_2.glView.setCameraPosition(distance=600, azimuth=45)
        self.glView_3.glView.setCameraPosition(distance=600, azimuth=45)
        self.rejillas1 = Rejilla(-500,500,-500,500,-20,500,100)
        self.rejillas2 = Rejilla(-500,500,-500,500,-20,500,100)
        self.rejillas3 = Rejilla(-500,500,-500,500,-20,500,100)
        self.rejillas1.loadOnGlView(self.glView_1.glView)
        self.rejillas2.loadOnGlView(self.glView_2.glView)
        self.rejillas3.loadOnGlView(self.glView_3.glView)
            
        ###############################################  Simulación animación  ####################################################
        self.solido_1 = Solido(eye(4))
        self.solido_1.loadOnGlView(self.glView_1.glView)
        self.sl_rotX_1.valueChanged.connect(self.asignarA_1)
        self.sl_rotY_1.valueChanged.connect(self.asignarA_1)
        self.sl_rotZ_1.valueChanged.connect(self.asignarA_1)
        self.sl_despX_1.valueChanged.connect(self.asignarA_1)
        self.sl_despY_1.valueChanged.connect(self.asignarA_1)
        self.sl_despZ_1.valueChanged.connect(self.asignarA_1)
        self.timer = QTimer()
        self.timer.timeout.connect(self.avanzarCuadro)
        self.bt_iniciarAnimacion.clicked.connect(self.iniciarAnimación)
        ###########################################################################################################################
        ############################################  Simulación localización 1  ##################################################
        self.solido_2 = Solido(eye(4))
        self.solido_2.loadOnGlView(self.glView_2.glView)
        self.sl_rotX_1.valueChanged.connect(lambda value:(self.asignarA_2(),self.sb_rX.setValue(value)))
        self.sl_rotY_1.valueChanged.connect(lambda value:(self.asignarA_2(),self.sb_rY.setValue(value)))
        self.sl_rotZ_1.valueChanged.connect(lambda value:(self.asignarA_2(),self.sb_rZ.setValue(value)))
        self.sl_despX_1.valueChanged.connect(lambda value:(self.asignarA_2(),self.sb_dX.setValue(value)))
        self.sl_despY_1.valueChanged.connect(lambda value:(self.asignarA_2(),self.sb_dY.setValue(value)))
        self.sl_despZ_1.valueChanged.connect(lambda value:(self.asignarA_2(),self.sb_dZ.setValue(value)))
        ###########################################################################################################################
        ############################################  Simulación localización 2  ##################################################
        self.solido_3 = Solido(eye(4))
        self.solido_3.loadOnGlView(self.glView_3.glView)
        self.sl_rotX_2.valueChanged.connect(lambda value:(self.asignarA_3(),self.sb_rX_2.setValue(value)))
        self.sl_rotY_2.valueChanged.connect(lambda value:(self.asignarA_3(),self.sb_rY_2.setValue(value)))
        self.sl_rotZ_2.valueChanged.connect(lambda value:(self.asignarA_3(),self.sb_rZ_2.setValue(value)))
        self.sl_despX_2.valueChanged.connect(lambda value:(self.asignarA_3(),self.sb_dX_2.setValue(value)))
        self.sl_despY_2.valueChanged.connect(lambda value:(self.asignarA_3(),self.sb_dY_2.setValue(value)))
        self.sl_despZ_2.valueChanged.connect(lambda value:(self.asignarA_3(),self.sb_dZ_2.setValue(value)))
        ###########################################################################################################################
        self.cb_ecuaciones.currentIndexChanged.connect(lambda index:(self.asignarA_2(),self.asignarA_3()))
    
    ## Método que se llama cuando se pulsa el botón de iniciar animación
    def iniciarAnimación(self):
        self.bt_iniciarAnimacion.setEnabled(False)
        rX0 = self.sl_rotX_1.value()
        rY0 = self.sl_rotY_1.value()
        rZ0 = self.sl_rotZ_1.value()
        x0 = self.sl_despX_1.value()
        y0 = self.sl_despY_1.value()
        z0 = self.sl_despZ_1.value()
        rXf = self.sl_rotX_2.value()
        rYf = self.sl_rotY_2.value()
        rZf = self.sl_rotZ_2.value()
        xf = self.sl_despX_2.value()
        yf = self.sl_despY_2.value()
        zf = self.sl_despZ_2.value()
        n = self.sb_nPuntos.value()
        tf = self.sb_tFinal.value()*1000
        
        self.vrX = linspace(rX0, rXf, n)
        self.vrY = linspace(rY0, rYf, n)
        self.vrZ = linspace(rZ0, rZf, n)
        self.vX = linspace(x0, xf, n)
        self.vY = linspace(y0, yf, n)
        self.vZ = linspace(z0, zf, n)
        self.t = linspace(0, tf, n)
        self.n = n
        
        self.i = 1
        self.asignarA_1(rX0,rY0,rZ0,x0,y0,z0)
        self.dt = self.t[1]-self.t[0]
        self.timer.start(self.dt)
        
    ## Método que se llama cada vez que se desborda el timer
    def avanzarCuadro(self):
        self.asignarA_1(self.vrX[self.i],self.vrY[self.i],self.vrZ[self.i],self.vX[self.i],self.vY[self.i],self.vZ[self.i])
        if self.i != self.n-1:
            self.i+=1
            if round(self.dt) != round(self.t[self.i]-self.t[self.i-1]):
                self.dt = self.t[self.i]-self.t[self.i-1]
                self.timer.setInterval(self.dt)
        else:
            self.timer.stop()
            self.bt_iniciarAnimacion.setEnabled(True)
    
    def asignarA_1(self, angX=None,angY=None,angZ=None,despX=None,despY=None,despZ=None):
        if angY == None:
            desplazamiento = eye(4)
            desplazamiento[0,3] = self.sl_despX_1.value()
            desplazamiento[1,3] = self.sl_despY_1.value()
            desplazamiento[2,3] = self.sl_despZ_1.value()
            rX = rotX(self.sl_rotX_1.value())
            rY = rotY(self.sl_rotY_1.value())
            rZ = rotZ(self.sl_rotZ_1.value())
        else:
            desplazamiento = eye(4)
            desplazamiento[0,3] = despX
            desplazamiento[1,3] = despY
            desplazamiento[2,3] = despZ
            rX = rotX(angX)
            rY = rotY(angY)
            rZ = rotZ(angZ)
        A = self.calcularA(rX,rY,rZ,desplazamiento)
        self.solido_1.setA(A)
        
    def asignarA_2(self, value=None):
        desplazamiento = eye(4)
        desplazamiento[0,3] = self.sl_despX_1.value()
        desplazamiento[1,3] = self.sl_despY_1.value()
        desplazamiento[2,3] = self.sl_despZ_1.value()
        rX = rotX(self.sl_rotX_1.value())
        rY = rotY(self.sl_rotY_1.value())
        rZ = rotZ(self.sl_rotZ_1.value())
        A = self.calcularA(rX,rY,rZ,desplazamiento)
        self.solido_2.setA(A)
        
    def asignarA_3(self, value=None):
        desplazamiento = eye(4)
        desplazamiento[0,3] = self.sl_despX_2.value()
        desplazamiento[1,3] = self.sl_despY_2.value()
        desplazamiento[2,3] = self.sl_despZ_2.value()
        rX = rotX(self.sl_rotX_2.value())
        rY = rotY(self.sl_rotY_2.value())
        rZ = rotZ(self.sl_rotZ_2.value())
        A = self.calcularA(rX,rY,rZ,desplazamiento)
        self.solido_3.setA(A)
        
    def calcularA(self,rX,rY,rZ,desplazamiento):
        currentIndex = self.cb_ecuaciones.currentIndex()
        if currentIndex == 0:
            A = rX @ rY @ rZ @ desplazamiento
        elif currentIndex == 1:
            A = rX @ rZ @ rY @ desplazamiento
        elif currentIndex == 2:
            A = rY @ rZ @ rX @ desplazamiento
        elif currentIndex == 3:
            A = rY @ rX @ rZ @ desplazamiento
        elif currentIndex == 4:
            A = rZ @ rX @ rY @ desplazamiento
        elif currentIndex == 5:
            A = rZ @ rY @ rX @ desplazamiento
        return A