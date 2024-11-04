from PySide6.QtCore import QThread, Signal
from functions.unidad_2 import (generaMTH, interpolarLinealR3, cinematicaInversa, interpoladorLineal, cinematicaDirecta,
                                limitesQ, int_trapezoidal_tmin, int_trapezoidal_vec_t, int_lineal_vec_t, interpoladorCubicoMuestreo)
from numpy import array, eye, zeros, ndarray, linspace, sign
from math import floor

class GenerarMTHs(QThread):
    listMTHsGenerada = Signal(list)
    ocurrioError = Signal()
    def __init__(self) -> None:
        super().__init__()
        self.puntosCargados = False
        
    def setPuntos(self,Puntos):
        self.Puntos = array(Puntos)
        self.puntosCargados = True
        
    def run(self):
        if self.puntosCargados:
            MTHs = []
            columns = self.Puntos.shape[1]
            try:
                for i in range(columns):
                    try:
                        mth = generaMTH(self.Puntos[0:3,i],self.Puntos[3,i])
                    except:
                        pass
                    MTHs.append(mth.tolist())
                self.listMTHsGenerada.emit(MTHs)
            except Exception as e:
                self.ocurrioError.emit()
        else:
            self.listMTHsGenerada.emit([eye(4).tolist()])

class InterpolarLinealR3(QThread):
    puntosInterpolados = Signal(list)
    ocurrioError = Signal()
    def __init__(self):
        super().__init__()
        self.puntosCargados = False
        
    def setPuntos(self,puntosR3,nPuntos):
        self.puntosR3 = puntosR3
        self.nPuntos = nPuntos
        self.puntosCargados = True
        
    def run(self):
        if self.puntosCargados:
            puntosInt = interpolarLinealR3(self.puntosR3,self.nPuntos)
            self.puntosInterpolados.emit(puntosInt)

class InterpolarLineal(QThread):
    qInterpolado = Signal(list,list,list)
    def __init__(self):
        super().__init__()
        self.puntosCargados = False
        
    def setQ(self,q:list,t:list,nPuntos:int):
        self.q1 = q[0]
        self.q2 = q[1]
        self.q3 = q[2]
        self.q4 = q[3]
        self.t = t
        self.nPuntos = nPuntos
        self.puntosCargados = True
        
    def run(self):
        if self.puntosCargados:
            q1,qp1,_ = interpoladorLineal(self.q1,self.t,self.nPuntos)
            q2,qp2,_ = interpoladorLineal(self.q2,self.t,self.nPuntos)
            q3,qp3,_ = interpoladorLineal(self.q3,self.t,self.nPuntos)
            q4,qp4,t = interpoladorLineal(self.q4,self.t,self.nPuntos)
            self.qInterpolado.emit([q1,q2,q3,q4],[qp1,qp2,qp3,qp4],t)

class InterpolarCubico(QThread):
    qInterpolado = Signal(list,list,list,list,list)
    def __init__(self):
        super().__init__()
        self.puntosCargados = False
        
    def setQ(self,q:list,t:list,nPuntos:int):
        self.q1 = q[0]
        self.q2 = q[1]
        self.q3 = q[2]
        self.q4 = q[3]
        self.t = t
        self.nPuntos = nPuntos
        self.puntosCargados = True
        
    def run(self):
        if self.puntosCargados:
            _,q1,q1p,q1pp,q1ppp = interpoladorCubicoMuestreo(self.t,self.nPuntos,self.q1,2)
            _,q2,q2p,q2pp,q2ppp = interpoladorCubicoMuestreo(self.t,self.nPuntos,self.q2,2)
            _,q3,q3p,q3pp,q3ppp = interpoladorCubicoMuestreo(self.t,self.nPuntos,self.q3,2)
            t,q4,q4p,q4pp,q4ppp = interpoladorCubicoMuestreo(self.t,self.nPuntos,self.q4,2)
        self.qInterpolado.emit([q1,q2,q3,q4],[q1p,q2p,q3p,q4p],[q1pp,q2pp,q3pp,q4pp],[q1ppp,q2ppp,q3ppp,q4ppp],t)

class InversaMTHs(QThread):
    inversasCalculadas = Signal(list,list,list,list)
    def __init__(self):
        super().__init__()
        self.MTHsCargadas = False
        
    def setMTHs(self,MTHs):
        self.MTHs = MTHs
        self.MTHsCargadas = True
        
    def run(self):
        if self.MTHsCargadas:
            q_1 = []
            q_2 = []
            q_3 = []
            q_4 = []
            for i in range(len(self.MTHs)):
                try:
                    q1,q2,q3,q4 = cinematicaInversa(array(self.MTHs[i]))
                except:
                    pass
                q_1.append(q1)
                q_2.append(q2)
                q_3.append(q3)
                q_4.append(q4)
            self.inversasCalculadas.emit(q_1,q_2,q_3,q_4)

class DirectaQs(QThread):
    directasCalculadas = Signal(list)
    def __init__(self):
        super().__init__()
        self.QsCargadas = False
        
    def setQs(self,q1:list,q2:list,q3:list,q4:list):
        self.q1 = q1
        self.q2 = q2
        self.q3 = q3
        self.q4 = q4
        self.QsCargadas = True
        
    def run(self):
        if self.QsCargadas:
            MTHs = []
            for i in range(len(self.q1)):
                try:
                    mth = cinematicaDirecta(self.q1[i],self.q2[i],self.q3[i],self.q4[i]).tolist()
                except:
                    pass
                MTHs.append(mth)
            self.directasCalculadas.emit(MTHs)
        else:
            print('No se cargaron Qs')

class GetXYZ_From_MTHs(QThread):
    XYZExtraidos = Signal(ndarray)
    def __init__(self):
        super().__init__()
        self.MTHsCargadas = False
        
    def setMTHs(self,MTHs):
        self.MTHs = MTHs
        self.MTHsCargadas = True
        
    def run(self):
        if self.MTHsCargadas:
            n = len(self.MTHs)
            puntos = zeros((n,3))
            MTHs = [array(elemento) for elemento in self.MTHs]
            for i in range(n):
                puntos[i,:] = MTHs[i][0:3,3].T
            self.XYZExtraidos.emit(puntos)
        else:
            print('No se cargaron MTHs')

class TrayectoriaPuntoPunto(QThread):
    trayectoriaCalculada = Signal(list,list,list,list,list)
    valueError = Signal()
    def __init__(self):
        super().__init__()
        self.valoresCargados = False
        self.dT = 0.05
        
    def setQs(self,q1:list,q2:list,q3:list,q4:list,tipo:int):
        self.q1 = q1
        self.q2 = q2
        self.q3 = q3
        self.q4 = q4
        self.q = [q1,q2,q3,q4]
        self.tipo = tipo
        self.valoresCargados = True
        
    def run(self):
        if self.valoresCargados:
            _,_,qpMax,qppMax = limitesQ()
            if self.tipo == 0:
                T = [int_trapezoidal_tmin(self.q[i][0],self.q[i][1],qppMax[i],qpMax[i]) for i in range(4)]
                n = floor(sum(T)/self.dT)
                tm = linspace(0,sum(T),n).tolist()
                tq1 = [0,T[0]]
                tq2 = [T[0],sum([T[i] for i in range(2)])]
                tq3 = [sum([T[i] for i in range(2)]),sum([T[i] for i in range(3)])]
                tq4 = [sum([T[i] for i in range(3)]),sum(T)]
                q1,qp1,qpp1 = int_trapezoidal_vec_t(self.q1[0],self.q1[1],qppMax[0],qpMax[0],tm,tq1[0])
                q2,qp2,qpp2 = int_trapezoidal_vec_t(self.q2[0],self.q2[1],qppMax[1],qpMax[1],tm,tq2[0])
                q3,qp3,qpp3 = int_trapezoidal_vec_t(self.q3[0],self.q3[1],qppMax[2],qpMax[2],tm,tq3[0])
                q4,qp4,qpp4 = int_trapezoidal_vec_t(self.q4[0],self.q4[1],qppMax[3],qpMax[3],tm,tq4[0])
                q = [q1,q2,q3,q4]
                qp = [qp1,qp2,qp3,qp4]
                qpp = [qpp1,qpp2,qpp3,qpp4]
            elif self.tipo == 1:
                T = [int_trapezoidal_tmin(self.q[i][0],self.q[i][1],qppMax[i],qpMax[i]) for i in range(4)]
                n = floor(max(T)/self.dT)
                tm = linspace(0,max(T),n).tolist()
                tq1 = [0,T[0]]
                tq2 = [0,T[1]]
                tq3 = [0,T[2]]
                tq4 = [0,T[3]]
                q1,qp1,qpp1 = int_trapezoidal_vec_t(self.q1[0],self.q1[1],qppMax[0],qpMax[0],tm,0)
                q2,qp2,qpp2 = int_trapezoidal_vec_t(self.q2[0],self.q2[1],qppMax[1],qpMax[1],tm,0)
                q3,qp3,qpp3 = int_trapezoidal_vec_t(self.q3[0],self.q3[1],qppMax[2],qpMax[2],tm,0)
                q4,qp4,qpp4 = int_trapezoidal_vec_t(self.q4[0],self.q4[1],qppMax[3],qpMax[3],tm,0)
                q = [q1,q2,q3,q4]
                qp = [qp1,qp2,qp3,qp4]
                qpp = [qpp1,qpp2,qpp3,qpp4]
            elif self.tipo == 2:
                T = [int_trapezoidal_tmin(self.q[i][0],self.q[i][1],qppMax[i],qpMax[i],True) for i in range(4)]
                maxT=max(T)
                n = floor(maxT/self.dT)
                tm = linspace(0,maxT,n).tolist()
                tq1 = [0,maxT]
                tq2 = [0,maxT]
                tq3 = [0,maxT]
                tq4 = [0,maxT]
                q1,qp1,qpp1 = int_trapezoidal_vec_t(self.q1[0],self.q1[1],qppMax[0],qpMax[0],tm,0,maxT)
                q2,qp2,qpp2 = int_trapezoidal_vec_t(self.q2[0],self.q2[1],qppMax[1],qpMax[1],tm,0,maxT)
                q3,qp3,qpp3 = int_trapezoidal_vec_t(self.q3[0],self.q3[1],qppMax[2],qpMax[2],tm,0,maxT)
                q4,qp4,qpp4 = int_trapezoidal_vec_t(self.q4[0],self.q4[1],qppMax[3],qpMax[3],tm,0,maxT)
                q = [q1,q2,q3,q4]
                qp = [qp1,qp2,qp3,qp4]
                qpp = [qpp1,qpp2,qpp3,qpp4]
            else:
                self.valueError.emit()
            tqi = [tq1,tq2,tq3,tq4]
            self.trayectoriaCalculada.emit(tm,q,qp,qpp,tqi)

class LinealPuntoPunto(QThread):
    trayectoriaCalculada = Signal(list,list,list,list)
    valueError = Signal()
    def __init__(self):
        super().__init__()
        self.valoresCargados = False
        
    def setQs(self,q1:list,q2:list,q3:list,q4:list,nPuntos:list,tipo:int):
        self.q1 = q1
        self.q2 = q2
        self.q3 = q3
        self.q4 = q4
        self.q = [q1,q2,q3,q4]
        self.nPuntos = nPuntos
        self.tipo = tipo
        self.valoresCargados = True
        
    def run(self):
        if self.valoresCargados:
            _,_,qpMax,_ = limitesQ()
            T = [(self.q[i][1]-self.q[i][0])/(sign(self.q[i][1]-self.q[i][0])*qpMax[i]) for i in range(4)]
            n = int(self.nPuntos)
            if self.tipo == 0:
                tm = linspace(0,sum(T),n).tolist()
                tq1 = [0,T[0]]
                tq2 = [T[0],sum([T[i] for i in range(2)])]
                tq3 = [sum([T[i] for i in range(2)]),sum([T[i] for i in range(3)])]
                tq4 = [sum([T[i] for i in range(3)]),sum(T)]
                q1,qp1 = int_lineal_vec_t(self.q1[0],self.q1[1],qpMax[0],tm,tq1[0])
                q2,qp2 = int_lineal_vec_t(self.q2[0],self.q2[1],qpMax[1],tm,tq2[0])
                q3,qp3 = int_lineal_vec_t(self.q3[0],self.q3[1],qpMax[2],tm,tq3[0])
                q4,qp4 = int_lineal_vec_t(self.q4[0],self.q4[1],qpMax[3],tm,tq4[0])
            elif self.tipo == 1:
                tm = linspace(0,max(T),n).tolist()
                tq1 = [0,T[0]]
                tq2 = [0,T[1]]
                tq3 = [0,T[2]]
                tq4 = [0,T[3]]
                q1,qp1 = int_lineal_vec_t(self.q1[0],self.q1[1],qpMax[0],tm,0)
                q2,qp2 = int_lineal_vec_t(self.q2[0],self.q2[1],qpMax[1],tm,0)
                q3,qp3 = int_lineal_vec_t(self.q3[0],self.q3[1],qpMax[2],tm,0)
                q4,qp4 = int_lineal_vec_t(self.q4[0],self.q4[1],qpMax[3],tm,0)
            elif self.tipo == 2:
                tm = linspace(0,max(T),n).tolist()
                tq1 = [0,max(T)]
                tq2 = [0,max(T)]
                tq3 = [0,max(T)]
                tq4 = [0,max(T)]
                q1,qp1 = int_lineal_vec_t(self.q1[0],self.q1[1],qpMax[0],tm,0,max(T))
                q2,qp2 = int_lineal_vec_t(self.q2[0],self.q2[1],qpMax[1],tm,0,max(T))
                q3,qp3 = int_lineal_vec_t(self.q3[0],self.q3[1],qpMax[2],tm,0,max(T))
                q4,qp4 = int_lineal_vec_t(self.q4[0],self.q4[1],qpMax[3],tm,0,max(T))
            else:
                self.valueError.emit()
            if self.tipo in [0,1,2]:
                q = [q1,q2,q3,q4]
                qp = [qp1,qp2,qp3,qp4]
                tqi = [tq1,tq2,tq3,tq4]
                self.trayectoriaCalculada.emit(tm,q,qp,tqi)
