from PySide6.QtWidgets import QWidget
from clases.ui_sim_U2_T4 import Ui_sim_U2_T4
from clases.Robot3D import Rejilla, SistemaCoordenadas3D
from functions.unidad_2 import interpoladorLineal
from functions.unidad_1 import rotX,rotY,rotZ
from numpy import eye, array, linspace

class Sim_U2_T4(QWidget,Ui_sim_U2_T4):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    
    def init(self):
        self.t = [0,3000]
        self.n = 150
        self.dist = 300
        
        self.cp_1.heightScale = 1/7
        self.cp_2.heightScale = 1/7
        self.cp_3.heightScale = 1/7
        self.cp_1.plotWidget.setLabel('left', 'Ángulo W', units='°')
        self.cp_2.plotWidget.setLabel('left', 'Ángulo U', units='°')
        self.cp_3.plotWidget.setLabel('left', 'Ángulo W', units='°')
        self.cp_1.plotWidget.setLabel('bottom', 'Tiempo', units='s')
        self.cp_2.plotWidget.setLabel('bottom', 'Tiempo', units='s')
        self.cp_3.plotWidget.setLabel('bottom', 'Tiempo', units='s')
        
        self.ct_orientacionIni.setTable([[0,-50,0]])
        self.ct_orientacionFin.setTable([[30,60,150]])
        self.ct_orientacionIni.setHLabelsVisible(True)
        self.ct_orientacionFin.setHLabelsVisible(True)
        nombresFilas = ['W','U','W']
        self.ct_orientacionIni.setHorizontalHeaderLabels(nombresFilas)
        self.ct_orientacionFin.setHorizontalHeaderLabels(nombresFilas)
        self.ct_matrizIni.setTable(eye(3).tolist())
        self.ct_matrizFin.setTable(eye(3).tolist())
        self.ct_matrizIni.setEditable(False)
        self.ct_matrizFin.setEditable(False)
        
        self.gv_1.glView.setCameraPosition(distance=800, azimuth=90)
        self.rejilla_1 = Rejilla(-500,500,-500,500,-100,200,100)
        self.rejilla_1.loadOnGlView(self.gv_1.glView)
        self.pos_1 = eye(4)
        self.pos_2 = eye(4)
        self.pos_1[0:3,3:4] = array([[self.dist,0,0]]).T
        self.pos_2[0:3,3:4] = array([[-self.dist,0,0]]).T
        self.sistema_1 = SistemaCoordenadas3D(self.pos_1,90,5,'0')
        self.sistema_2 = SistemaCoordenadas3D(self.pos_2,90,5,'1')
        self.sistema_3 = SistemaCoordenadas3D(self.pos_1,90,5,'0')
        self.sistema_3.hide()
        self.sistema_1.loadOnGlView(self.gv_1.glView)
        self.sistema_2.loadOnGlView(self.gv_1.glView)
        self.sistema_3.loadOnGlView(self.gv_1.glView)
        self.sistema_3.animacionTerminada.connect(self.animacionTerminada)
        
        self.cb_angulosEuler.currentIndexChanged.connect(self.angulosEulerCurrentIndexChanged)
        
        self.ct_orientacionIni.cellChanged.connect(self.orientacionIniCellChanged)
        self.ct_orientacionFin.cellChanged.connect(self.orientacionFinCellChanged)
        
        self.bt_interpolarEuler.clicked.connect(self.interpolarEulerClicked)
        self.bt_iniciarAnimacion.clicked.connect(self.iniciarAnimacionClicked)
        
        self.orientacionIniCellChanged()
        self.orientacionFinCellChanged()
        
    def angulosEulerCurrentIndexChanged(self, value):
        if value==0:
            self.cp_2.plotWidget.setLabel('left', 'Ángulo U', units='°')
            nombresFilas = ['W','U','W']
            self.ct_orientacionIni.setHorizontalHeaderLabels(nombresFilas)
            self.ct_orientacionFin.setHorizontalHeaderLabels(nombresFilas)
        elif value==1:
            self.cp_2.plotWidget.setLabel('left', 'Ángulo V', units='°')
            nombresFilas = ['W','V','W']
            self.ct_orientacionIni.setHorizontalHeaderLabels(nombresFilas)
            self.ct_orientacionFin.setHorizontalHeaderLabels(nombresFilas)
        self.orientacionIniCellChanged()
        self.orientacionFinCellChanged()
            
    def orientacionIniCellChanged(self, row=None, column=None):
        orientIni = self.ct_orientacionIni.getTable()[0]
        orientIni = [float(i) for i in orientIni]
        angulosEuler = self.cb_angulosEuler.currentIndex()
        if angulosEuler==0:
            mth = rotZ(orientIni[0])@rotX(orientIni[1])@rotZ(orientIni[2])
            matrixIni = mth[0:3,0:3].tolist()
        elif angulosEuler==1:
            mth = rotZ(orientIni[0])@rotY(orientIni[1])@rotZ(orientIni[2])
            matrixIni = mth[0:3,0:3].tolist()
        matrixIni = [[round(i,2) for i in j] for j in matrixIni]
        self.ct_matrizIni.setTable(matrixIni)
        mth[0:3,3:4] = array([[self.dist,0,0]]).T
        self.sistema_1.setA(mth)
        
    def orientacionFinCellChanged(self, row=None, column=None):
        orientFin = self.ct_orientacionFin.getTable()[0]
        orientFin = [float(i) for i in orientFin]
        angulosEuler = self.cb_angulosEuler.currentIndex()
        if angulosEuler==0:
            mth = rotZ(orientFin[0])@rotX(orientFin[1])@rotZ(orientFin[2])
            matrixFin = mth[0:3,0:3].tolist()
        elif angulosEuler==1:
            mth = rotZ(orientFin[0])@rotY(orientFin[1])@rotZ(orientFin[2])
            matrixFin = mth[0:3,0:3].tolist()
        matrixFin = [[round(i,2) for i in j] for j in matrixFin]
        self.ct_matrizFin.setTable(matrixFin)
        mth[0:3,3:4] = array([[-self.dist,0,0]]).T
        self.sistema_2.setA(mth)
            
    def interpolarEulerClicked(self):
        orientIni = self.ct_orientacionIni.getTable()[0]
        orientFin = self.ct_orientacionFin.getTable()[0]
        orientIni = [float(i) for i in orientIni]
        orientFin = [float(i) for i in orientFin]
        ang1 = [orientIni[0],orientFin[0]]
        ang2 = [orientIni[1],orientFin[1]]
        ang3 = [orientIni[2],orientFin[2]]
        ang1Int,_,_  = interpoladorLineal(ang1,self.t,self.n)
        ang2Int,_,_  = interpoladorLineal(ang2,self.t,self.n)
        ang3Int,_,tm = interpoladorLineal(ang3,self.t,self.n)
        self.cp_1.setData(tm,ang1Int,[2,1])
        self.cp_2.setData(tm,ang2Int,[2,1])
        self.cp_3.setData(tm,ang3Int,[2,1])
        self.cp_1.setData(self.t,ang1,[0])
        self.cp_2.setData(self.t,ang2,[0])
        self.cp_3.setData(self.t,ang3,[0])
        self.bt_iniciarAnimacion.setEnabled(True)
        
    def iniciarAnimacionClicked(self):
        # self.bt_iniciarAnimacion.setEnabled(False)
        t = linspace(self.t[0],self.t[1],self.n).tolist()
        d = linspace(self.dist,-self.dist,self.n)
        orientIni = self.ct_orientacionIni.getTable()[0]
        orientFin = self.ct_orientacionFin.getTable()[0]
        orientIni = [float(i) for i in orientIni]
        orientFin = [float(i) for i in orientFin]
        ang1Int = linspace(orientIni[0],orientFin[0],self.n)
        ang2Int = linspace(orientIni[1],orientFin[1],self.n)
        ang3Int = linspace(orientIni[2],orientFin[2],self.n)
        
        MTHs = []
        angulosEuler = self.cb_angulosEuler.currentIndex()
        for i in range(self.n):
            if angulosEuler==0:
                mth = rotZ(ang1Int[i])@rotX(ang2Int[i])@rotZ(ang3Int[i])
            elif angulosEuler==1:
                mth = rotZ(ang1Int[i])@rotY(ang2Int[i])@rotZ(ang3Int[i])
            mth[0:3,3:4] = array([[d[i],0,0]]).T
            MTHs.append(mth)
        self.sistema_3.show()
        self.sistema_3.iniciarAnimacion(MTHs,t)
        
    def animacionTerminada(self):
        self.sistema_3.hide()
        # self.bt_iniciarAnimacion.setEnabled(True)