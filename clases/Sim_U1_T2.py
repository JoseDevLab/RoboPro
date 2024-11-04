from PySide6.QtWidgets import QWidget
import numpy as np
from math import sqrt
from clases.ui_sim_U1_T2 import Ui_sim_U1_T2
from clases.Robot3D import Cono, Flecha, SistemaCoordenadas3D, Rejilla
from functions.unidad_1 import rotX, rotY, rotZ


class Sim_U1_T2(QWidget, Ui_sim_U1_T2):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        
    def init(self):
        self.glView_1.glView.setCameraPosition(distance=30, azimuth=0)
        self.glView_2.glView.setCameraPosition(distance=15, azimuth=-40)
        self.glView_3.glView.setCameraPosition(distance=40, azimuth=45)
        self.glView_1.glView.opts['rotationMode'] = 'quaternion'
        self.glView_2.glView.opts['rotationMode'] = 'quaternion'
        self.glView_3.glView.opts['rotationMode'] = 'quaternion'
        self.rejillas1 = Rejilla(-10,10,-10,10,0,20,2)
        self.rejillas2 = Rejilla(-10,10,-10,10,0,20,2)
        self.rejillas3 = Rejilla(-10,10,-10,10,-2,20,2)
        self.rejillas1.loadOnGlView(self.glView_1.glView)
        self.rejillas2.loadOnGlView(self.glView_2.glView)
        self.rejillas3.loadOnGlView(self.glView_3.glView)
        #######################################   Simulación del cono  ##########################################
        pos_cono_1 = np.array([0,0,4])
        vec_cono_1 = np.array([1,1,1])
        t_cono_1 = self.sl_lCono_1.value()
        d_cono_1 = self.sl_dCono_1.value()
        n_cono = self.sl_n.value()
        self.sl_nCaras.setMaximum(2*n_cono)
        self.sl_nCaras.setValue(1)
        caras_cono = self.sl_nCaras.value()
        color = [1,0,0,1]
        drawEdges = True
        color_borde = [0,0,0,1]
        shader = 'edgeHilight'  # 'balloon', 'normalColor', 'viewNormalColor', 'shaded', 'edgeHilight', 'heightColor'
                
        self.cono = Cono(n_cono,pos_cono_1,vec_cono_1,t_cono_1,d_cono_1,color,drawEdges,color_borde)
        self.cono.dibujarVertices(self.glView_1.glView)
        self.cono.dibujarLinea(self.glView_1.glView)
        self.cono.loadOnGlView(self.glView_1.glView)
        self.cono.setCarasVisibles(caras_cono)
        self.cono.setShader(shader)
        
        self.sl_n.valueChanged.connect(self.cono.setN)
        self.sl_n.valueChanged.connect(lambda value: self.sl_nCaras.setMaximum(2*value))
        self.sl_lCono_1.valueChanged.connect(self.cono.setT)
        self.sl_nCaras.valueChanged.connect(self.cono.setCarasVisibles)
        self.sl_dCono_1.valueChanged.connect(self.cono.setD)
        ########################################################################################################
        
        #########################################  Simulación flecha  ##########################################
        pos = np.array([1,1,1])
        vec = np.array([1,1,1])
        tflecha = 2
        tpunta = 1
        dcil = 1
        dcono = 2
        color = [0,0,1,1]
        shader = 'edgeHilight'  # 'balloon', 'normalColor', 'viewNormalColor', 'shaded', 'edgeHilight', 'heightColor'
        
        self.flecha = Flecha(pos[:],vec[:],tflecha,tpunta,dcil,dcono,color)
        self.flecha.loadOnGlView(self.glView_2.glView)
        self.flecha.setShader(shader)
        
        self.sl_lFlecha_1.valueChanged.connect(self.flecha.setTFlecha)
        self.sl_lFlecha_1.valueChanged.connect(lambda value: self.sl_lCono_2.setMaximum(value-1))
        self.sl_lCono_2.valueChanged.connect(self.flecha.setTPunta)
        self.sl_dCilindro.valueChanged.connect(self.flecha.setDCil)
        self.sl_dCono_2.valueChanged.connect(self.flecha.setDcono)
        #########################################################################################################
        
        ##############################  Simulación sistema de ejes coordenados 3D  ##############################
        Sn =  np.array([[sqrt(2)/2 , -sqrt(2)/2 , 0 , 0],
                        [0         , 0          , 1 , 0],
                        [sqrt(2)/2 , sqrt(2)/2  , 0 , 0],
                        [0         , 0          , 0 , 1] ])
        self.Sn = Sn

        self.sistema3D = SistemaCoordenadas3D(Sn, 10, 2, '0')
        self.sistema3D.loadOnGlView(self.glView_3.glView)
        
        self.sl_lFlecha_2.valueChanged.connect(self.sistema3D.setL)
        self.sl_dFlecha.valueChanged.connect(self.sistema3D.setG)
        self.sb_subindice.valueChanged.connect(self.sistema3D.setText)
        
        self.sl_rotX.valueChanged.connect(lambda ang: (self.sistema3D.setA(self.rotar()),self.sb_X.setValue(ang)))
        self.sl_rotY.valueChanged.connect(lambda ang: (self.sistema3D.setA(self.rotar()),self.sb_Y.setValue(ang)))
        self.sl_rotZ.valueChanged.connect(lambda ang: (self.sistema3D.setA(self.rotar()),self.sb_Z.setValue(ang)))
        self.cb_ecuaciones.currentIndexChanged.connect(lambda index: self.sistema3D.setA(self.rotar()))
        #########################################################################################################
        
    def rotar(self):
        if self.cb_ecuaciones.currentIndex() == 0:
            A = ((self.Sn@rotX(self.sl_rotX.value()))@rotY(self.sl_rotY.value()))@rotZ(self.sl_rotZ.value())
        elif self.cb_ecuaciones.currentIndex() == 1:
            A = ((self.Sn@rotX(self.sl_rotX.value()))@rotZ(self.sl_rotZ.value()))@rotY(self.sl_rotY.value())
        elif self.cb_ecuaciones.currentIndex() == 2:
            A = ((self.Sn@rotY(self.sl_rotY.value()))@rotZ(self.sl_rotZ.value()))@rotX(self.sl_rotX.value())
        elif self.cb_ecuaciones.currentIndex() == 3:
            A = ((self.Sn@rotY(self.sl_rotY.value()))@rotX(self.sl_rotX.value()))@rotZ(self.sl_rotZ.value())
        elif self.cb_ecuaciones.currentIndex() == 4:
            A = ((self.Sn@rotZ(self.sl_rotZ.value()))@rotX(self.sl_rotX.value()))@rotY(self.sl_rotY.value())
        elif self.cb_ecuaciones.currentIndex() == 5:
            A = ((self.Sn@rotZ(self.sl_rotZ.value()))@rotY(self.sl_rotY.value()))@rotX(self.sl_rotX.value())
        return A