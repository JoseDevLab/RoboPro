import sympy as sp
from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6.QtCore import QThread, Signal, Slot
from clases.ui_sim_U1_T1 import Ui_sim_U1_T1
from functions.unidad_1 import modeloDinamico

class Sim_U1_T1(QWidget,Ui_sim_U1_T1):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        
    def init(self):
        Par = [['q1','0' ,'0','-pi/2'],
               ['0' ,'q2','0','0'    ]]
        jrj = [[0   , 0],
               [0   , 0],
               ['L1', 0]]
        g = [[0, 0, -9.80665]]
        self.tb_par.setTable(Par)
        self.tb_jrj.setTable(jrj)
        self.tb_g.setTable(g)
        self.sb_n.valueChanged.connect(self.nChanged)
        self.bt_ejecutar.clicked.connect(self.iniciarAlgoritmo)
        
        self.tb_fuerzas.setSize(2,1)
        self.tb_D.setSize(2,2)
        self.tb_ddq.setSize(2,1)
        self.tb_H.setSize(2,1)
        self.tb_C.setSize(2,1)
        
    def nChanged(self, n):
        self.tb_par.setSize(n,4)
        self.tb_jrj.setSize(3,n)
        
    def iniciarAlgoritmo(self):
        try:
            self.bt_ejecutar.setEnabled(False)
            self.bt_ejecutar.setText('Calculando...')
            par = self.tb_par.getTable()
            jrj = self.tb_jrj.getTable()
            g = self.tb_g.getTable()
            g = g[0]
            par = sp.Matrix(sp.sympify(par))
            jrj = sp.Matrix(sp.sympify(jrj))
            g = sp.Matrix(sp.sympify(g))
            
            # Iniciar el proceso en un hilo
            self.thread = ModeloDinamicoThread(par, jrj, g)
            self.thread.resultado.connect(self.actualizarUI)
            # Llamar a la función modeloDinamico en un hilo diferente
            self.thread.start()
        except Exception as e:
            dialogo = QMessageBox.critical(self,'Error','Por favor ingrese correctamente los datos, sin dejar celdas en blanco y siguiendo las indicaciones.')
            self.bt_ejecutar.setEnabled(True)
            self.bt_ejecutar.setText('Ejecutar algoritmo')
        
    @Slot(object, object, object, object, object)
    def actualizarUI(self, t, ddq, D, H, C):
        if t != 'e':
            # Convertir las matrices simbólicas en matrices str
            t = [[str(t[row, col]) for col in range(t.cols)] for row in range(t.rows)]
            D = [[str(D[row, col]) for col in range(D.cols)] for row in range(D.rows)]
            H = [[str(H[row, col]) for col in range(H.cols)] for row in range(H.rows)]
            C = [[str(C[row, col]) for col in range(C.cols)] for row in range(C.rows)]
            
            # Asignar las matrices str a las tablas
            self.tb_fuerzas.setTable(t)
            self.tb_D.setTable(D)
            self.tb_ddq.setTable(ddq)
            self.tb_H.setTable(H)
            self.tb_C.setTable(C)
        else:
            dialogo = QMessageBox.critical(self,'Error','Ocurrió un error en la función modeloDinamico: \n'+str(ddq))
            
        # Habilitar el boton de ejecutar el algoritmo
        self.bt_ejecutar.setEnabled(True)
        self.bt_ejecutar.setText('Ejecutar algoritmo')
        
class ModeloDinamicoThread(QThread):
    # Señal para emitir los resultados
    resultado = Signal(object, object, object, object, object)

    def __init__(self, par, jrj, g):
        super().__init__()
        self.par = par
        self.jrj = jrj
        self.g = g

    def run(self):
        # Reemplaza esto con la llamada a tu función real y sus argumentos
        try:
            t, ddq, D, H, C = modeloDinamico(self.par, self.jrj, self.g)
            # Emite los resultados al terminar
            self.resultado.emit(t, ddq, D, H, C)
        except Exception as e:
            self.resultado.emit('e',e,'e','e','e')