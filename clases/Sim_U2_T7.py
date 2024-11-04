from PySide6.QtWidgets import QWidget
from clases.ui_sim_U2_T7 import Ui_sim_U2_T7
from functions.unidad_2 import v_criterioHeuristico,V_AceleracionContinua,interpoladorCubicoMuestreo

class Sim_U2_T7(QWidget,Ui_sim_U2_T7):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
    def init(self):
        self.cp_p_activado = True
        self.cp_v_activado = True
        self.cp_p.heightScale = 1/2.5
        self.cp_v.heightScale = 1/2.5
        self.cp_a.heightScale = 1/2.5
        self.cp_sa.heightScale = 1/2.5
        self.cp_p.plotWidget.setLabel('left', 'Posición', units='°')
        self.cp_v.plotWidget.setLabel('left', 'Velocidad', units='°/s')
        self.cp_a.plotWidget.setLabel('left', 'Aceleración', units='°/s^2')
        self.cp_sa.plotWidget.setLabel('left', 'JERK', units='°/s^3')
        self.cp_p.plotWidget.setLabel('bottom', 'Tiempo', units='s')
        self.cp_v.plotWidget.setLabel('bottom', 'Tiempo', units='s')
        self.cp_a.plotWidget.setLabel('bottom', 'Tiempo', units='s')
        self.cp_sa.plotWidget.setLabel('bottom', 'Tiempo', units='s')
        self.cp_p.puntos_1.setData(size=12)
        self.cp_v.puntos_1.setData(size=12)
        
        self.cp_p.plotWidget.setYRange(-10,180)
        
        t=[0,1,2,3,4]
        q=[0,50,180,-10,30]
        self.cp_p.setData(t,q,[3])
        self.cp_p.polyLine.sigRegionChanged.connect(self.posicionChanged)
        self.sb_nPuntos.valueChanged.connect(self.update)
        self.cp_v.polyLine.sigRegionChanged.connect(self.velocidadChanged)
        self.cb_velocidades.currentIndexChanged.connect(self.velocidadesCurrentIndexChanged)
        self.update()
    
    def update(self):
        nPuntos=self.sb_nPuntos.value()
        t,q=self.cp_p.getPolyData()
        tipoVel = self.cb_velocidades.currentIndex()
        if tipoVel==0:
            t_v,v=self.cp_v.getPolyData()
            self.cp_v.setData(t_v,v,[0])
        self.cp_p.setData(t,q,[0])
        if all(t[i] < t[i + 1] for i in range(len(t) - 1)):
            if tipoVel==1:
                v=v_criterioHeuristico(t,q)
            elif tipoVel==2:
                v=V_AceleracionContinua(t,q)
            self.v=v
            self.cp_v.setData(t,v,[0])
            tInt,qInt,qpInt,qppInt,qpppInt=interpoladorCubicoMuestreo(t,nPuntos,q,0,v)
            self.cp_p.setData(tInt,qInt,[1,2])
            self.cp_v.setData(tInt,qpInt,[1,2])
            self.cp_a.setData(tInt,qppInt,[1,2])
            self.cp_sa.setData(tInt,qpppInt,[1,2])
            self.sb_nPuntos.setMinimum(len(t))
            
    def posicionChanged(self):
        if self.cp_p_activado:
            if self.cb_velocidades.currentIndex()==0:
                t_v,q_v=self.cp_v.getPolyData()
                t_p,q_p=self.cp_p.getPolyData()
                if len(q_p)>len(q_v):
                    for i in range(len(q_p)):
                        if i<=len(q_v)-1:
                            if t_p[i]!=t_v[i]:
                                newDato = ((q_v[i]-q_v[i-1])/(t_v[i]-t_v[i-1]))*(t_p[i]-t_v[i-1])+q_v[i-1]
                                q_v.insert(i,newDato)
                                break
                        else:
                            q_v.append(0)
                elif len(q_p)<len(q_v):
                    for i in range(len(q_v)):
                        if i<=len(q_p)-1:
                            if t_p[i]!=t_v[i]:
                                del q_v[i]
                                break
                        else:
                            del q_v[-1]
                self.cp_v_activado=False
                self.cp_v.setData(t_p,q_v,[3])
                self.cp_v_activado=True
            self.update()
    
    def velocidadChanged(self):
        if self.cp_v_activado:
            if self.cb_velocidades.currentIndex()==0:
                t_v,q_v=self.cp_v.getPolyData()
                t_p,q_p=self.cp_p.getPolyData()
                if len(q_v)>len(q_p):
                    for i in range(len(q_v)):
                        if i<=len(q_p)-1:
                            if t_p[i]!=t_v[i]:
                                newDato = ((q_p[i]-q_p[i-1])/(t_p[i]-t_p[i-1]))*(t_v[i]-t_p[i-1])+q_p[i-1]
                                q_p.insert(i,newDato)
                                break
                        else:
                            q_p.append(0)
                elif len(q_v)<len(q_p):
                    for i in range(len(q_p)):
                        if i<=len(q_v)-1:
                            if t_p[i]!=t_v[i]:
                                del q_p[i]
                                break
                        else:
                            del q_p[-1]
                self.cp_p_activado=False
                self.cp_p.setData(t_v,q_p,[3])
                self.cp_p_activado=True
            self.update()
    
    def velocidadesCurrentIndexChanged(self, index):
        if index==0:
            t,_=self.cp_p.getPolyData()
            self.cp_v_activado = False
            self.cp_v.setData(t,self.v,[3])
            self.cp_v_activado = True
        else:
            if self.cp_v.polyLine.isVisible():
                self.cp_v.polyLine.setVisible(False)
            self.update()
