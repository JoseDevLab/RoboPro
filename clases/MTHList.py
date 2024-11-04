from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QWidget, QFrame, QVBoxLayout, QLabel, QSizePolicy
from clases.ui_MTHList import Ui_MTHList
from clases.CustomTable import CustomTable
import numpy as np

class MTHList(QWidget,Ui_MTHList):
    MTHClicked = Signal(int)
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.isEditable = True
        self.nTablas = 0
        self.Tablas = []
        self.setMinimumHeight(226)
        self.scrollArea.setMinimumHeight(226)
        
    def setNTablas(self,nTablas):
        if nTablas - self.nTablas >= 1:
            for i in range(self.nTablas,nTablas,1):
                mth = MTH(i+1)
                mth.setEditable(self.isEditable)
                mth.MTHClicked.connect(lambda index: self.MTHClicked.emit(index))
                self.layoutMTH.addWidget(mth)
        elif nTablas - self.nTablas <= -1:
            for i in range(self.nTablas,nTablas,-1):
                self.eliminar_MTH(i-1)
        self.nTablas = nTablas
    
    def eliminar_MTH(self, posicion):
        if posicion < 0 or posicion >= self.layoutMTH.count():
            return  # Posición inválida
        
        layout_item = self.layoutMTH.takeAt(posicion)
        if layout_item:
            fr_MTH = layout_item.widget()
            if fr_MTH:
                fr_MTH.deleteLater()
            else:
                # Si el elemento no es un widget, eliminarlo
                layout_item.deleteLater()
    
    def setListMTH(self, listMTH:list):
        n = len(listMTH)
        self.setNTablas(n)
        for i in range(n):
            layout_item = self.layoutMTH.itemAt(i)
            mth = layout_item.widget()
            if mth:
                mth.setMTH(listMTH[i])
    
    def addMTH(self,mth):
        n = self.layoutMTH.count()
        fr_mth = MTH(n+1,mth)
        fr_mth.setEditable(self.isEditable)
        fr_mth.MTHClicked.connect(lambda index: self.MTHClicked.emit(index))
        self.layoutMTH.addWidget(fr_mth)
        self.nTablas+=1
    
    def setEditable(self, editable:bool):
        self.isEditable = editable
        for i in range(self.layoutMTH.count()):
            layout_item = self.layoutMTH.itemAt(i)
            mth = layout_item.widget()
            if mth:
                mth.setEditable(editable)
            
        
class MTH(QFrame):
    MTHClicked = Signal(int)
    def __init__(self,indice,MTH=None):
        super().__init__()
        self.indice = indice
        self.isEditable = True
        # Configura el layout vertical
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0,0,0,0)
        self.setLayout(self.layout)
        
        # Se crea la etiqueta con el título de la MTH
        self.label  = QLabel()
        self.label.setText('MTH '+str(indice))
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        self.layout.addWidget(self.label)
        
        # Se crea la tabla de la MTH
        self.ct = CustomTable()
        if MTH==None:
            self.ct.setTable(np.eye(4).tolist())
        else:
            self.ct.setTable(MTH)
        self.layout.addWidget(self.ct)
        self.ct.setHorizontalHeaderLabels(['n','o','a','p'])
        self.ct.setHLabelsVisible(True)
        self.ct.cellClicked.connect(lambda row, column:self.MTHClicked.emit(self.indice-1))
    
    def setMTH(self,MTH):
        self.ct.setTable(MTH)
        
    def setEditable(self, editable:bool):
        self.isEditable = editable
        self.ct.setEditable(editable)