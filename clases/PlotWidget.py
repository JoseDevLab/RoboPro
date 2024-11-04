from PySide6.QtWidgets import QFrame, QVBoxLayout, QLabel, QSizePolicy
from PySide6.QtCore import QRect, QSize
from numpy import array, hstack
import pyqtgraph as pg
pg.setConfigOptions(antialias=True)

class CustomPlotWidget(QFrame):
    def __init__(self, parent=None):
        super().__init__()
        
        # Configura el layout vertical
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0,0,0,0)
        self.setLayout(self.layout)

        # Crea el frame que contiene el PlotWidget
        self.frame = QFrame()
        self.layout_1 = QVBoxLayout()
        self.layout_1.setContentsMargins(0,0,0,0)
        self.frame.setLayout(self.layout_1)
        self.frame.setSizePolicy(QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Ignored))
        self.layout.addWidget(self.frame)
        
        # Crea el PlotWidget
        self.plotWidget = pg.PlotWidget()
        self.plotWidget.showGrid(x=True,y=True)
        self.minLine = pg.InfiniteLine(angle=0, pen=pg.mkPen('r', width=1))
        self.maxLine = pg.InfiniteLine(angle=0, pen=pg.mkPen('r', width=1))
        self.minLine.setVisible(False)
        self.maxLine.setVisible(False)
        self.plotWidget.addItem(self.minLine)
        self.plotWidget.addItem(self.maxLine)
        
        # Añadir una línea interactiva (PolyLineROI)
        pen = {'color': (0, 0, 0, 0), 'width': 1}
        hoverPen = {'color': 'y', 'width': 1}
        handlePen = {'color': (0, 0, 0, 0), 'width': 1}
        handleHoverPen = {'color': 'r', 'width': 8}
        self.polyLine = pg.PolyLineROI([[0,0]],pen=pen, movable=False,hoverPen=hoverPen,handlePen=handlePen,handleHoverPen=handleHoverPen)
        self.polyLine.setVisible(False)
        self.plotWidget.addItem(self.polyLine)
        
        hoverable = True
        hoverPen = pg.mkPen('g')
        hoverSize = -1
        size = 8
        pen = {'color': 'w', 'width': 2}
        brush = pg.intColor(2, 100)
        self.puntos_1 = pg.ScatterPlotItem(hoverable=hoverable,hoverPen=hoverPen,hoverSize=hoverSize,size=size,pen=pen,brush=brush)
        hoverPen = pg.mkPen('g')
        size = 6
        pen = {'color': 'w', 'width': 1}
        brush = pg.intColor(55, 100)
        self.puntos_2 = pg.ScatterPlotItem(hoverable=hoverable,hoverPen=hoverPen,hoverSize=hoverSize,size=size,pen=pen,brush=brush)
        self.plotWidget.addItem(self.puntos_2)
        self.plotWidget.addItem(self.puntos_1)
        pen = pg.mkPen('b',width=3)
        self.linea = self.plotWidget.plot(pen=pen)
        
        self.layout_1.addWidget(self.plotWidget)
        
        # Mantener relación de aspecto
        self.heightScale = 1/1.8
        self.resizeEvent = self.escalarTamaio
        
    def escalarTamaio(self, event=None):
        self.setMinimumHeight(int(self.width()*self.heightScale))
        
    def setLimits(self,Min=None,Max=None):
        if Min!=None:
            self.minLine.setValue(Min)
            if not self.minLine.isVisible():
                self.minLine.setVisible(True)
        if Max!=None:
            self.maxLine.setValue(Max)
            if not self.maxLine.isVisible():
                self.maxLine.setVisible(True)
    
    def setData(self,t:list,q:list,graficos:list):
        if len(graficos)<=4:
            for grafico in graficos:
                if grafico == 0:
                    self.puntos_1.setData(pos=hstack((array([t]).T,array([q]).T)))
                if grafico == 1:
                    self.puntos_2.setData(pos=hstack((array([t]).T,array([q]).T)))
                if grafico == 2:
                    self.linea.setData(t,q)
                if grafico == 3:
                    puntos = hstack((array([t]).T,array([q]).T)).tolist()
                    self.polyLine.setPoints(puntos)
                    if not self.polyLine.isVisible():
                        self.polyLine.setVisible(True)
                        
    def getPolyData(self):
        puntos = array([array(list(pt)) for pt in self.polyLine.getState()['points']])
        n = puntos.shape[0]
        t = puntos[0:n,0].tolist()
        q = puntos[0:n,1].tolist()
        return t,q