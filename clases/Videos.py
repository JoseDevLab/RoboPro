from PySide6.QtWidgets import QMainWindow, QFrame, QTabWidget, QPushButton
from PySide6.QtCore import Qt, QRect, QEvent, Signal
import os
from clases.ui_abstractVideos import Ui_abstractVideos
from clases.WebView import WebView

################################################################################################################
#!#### Se crea la clase de la ventana que contendrá los videos con las interacciones a la ventana prncipal #####
################################################################################################################
class AbstractVideos(QMainWindow, Ui_abstractVideos):
    widgetContentsCambioTamanio = Signal()
    def __init__(self,ventana:QMainWindow,frame:QFrame,tabWidget:QTabWidget,bt_retorno:QPushButton):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowOpacity(1)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.frame = frame
        self.ventana = ventana
        self.tabWidget = tabWidget
        self.bt_retormo = bt_retorno
        self.isClosed = False
        
        self.connectVentana(ventana,frame,tabWidget,bt_retorno)
        
        if tabWidget.currentIndex() == 1:
            self.show()
        
        #! Se conecta la ventana con el WebView
        self.video_1.setWindow(self)
        #! Se conecta la ventana principal con el WebView
        self.video_1.setMainWindow(ventana)
        
        ###### Se emite una señal cuando el scrollAreaWidgetContents cambia de tamaño #######
        self.scrollAreaWidgetContents.resizeEvent = lambda event: self.widgetContentsCambioTamanio.emit()
        
    def connectVentana(self,ventana:QMainWindow,frame:QFrame,tabWidget:QTabWidget,bt_retorno:QPushButton):
        frame.resizeEvent = self.resizeEvent_frame
        ventana.moveEvent = self.moveEvent_Ventana
        tabWidget.currentChanged.connect(self.mostrar)
        ventana.closeEvent = lambda event: self.close()
        ventana.changeEvent = self.changeEvent_Ventana
        bt_retorno.clicked.connect(self.cerrar)
        ventana.bt_cerrarSesion.clicked.connect(lambda: self.hide())
        ventana.bt_perfilClicado.connect(lambda: self.hide())
        
        
    def setSize(self,size,oldSize=None):
        self.ancho = size.width()
        self.alto = size.height()
        pos = self.frame.mapToGlobal(self.frame.pos())
        self.setGeometry(QRect(pos.x(),pos.y(),size.width(),size.height()))
        
    def resizeEvent_frame(self, event):
        if not self.isClosed:
            self.setSize(event.size())
            
    def moveEvent_Ventana(self, event):
        if not self.isClosed:
            self.move(self.frame.mapToGlobal(self.frame.pos()))
        
    def mostrar(self, index):
        if index == 1:
            self.show()
        else:
            self.hide()
        
    def changeEvent_Ventana(self, event):
        if not self.isClosed:
            if event.type() == QEvent.WindowStateChange:
                if self.ventana.isMinimized():
                    self.hide()
                else:
                    self.mostrar(self.tabWidget.currentIndex())
                
    def cerrar(self):
        self.close()
        self.isClosed = True
        
    def abrir(self):
        self.mostrar(self.tabWidget.currentIndex())
        self.setSize(self.frame.size())
        self.isClosed = False
        
    #!########################### Busca los id de videos en la ruta path #############################
    def setPathVideos(self,path:str):
        cantidad_Videos = len([archivo for archivo in os.listdir(path) if archivo.endswith('.txt')])
        self.videos = []
        for i in range(cantidad_Videos):
            if i == 0:
                self.videos.append(self.video_1)
            else:
                self.videos.append(WebView())
                self.layoutVideos.addWidget(self.videos[i])
                self.videos[i].setWindow(self)
                self.videos[i].setMainWindow(self.ventana)
            file_path = path+'video '+str(i+1)+'.txt'
            with open(file_path, 'r', encoding='utf-8') as file:
                videoID = file.read()
            self.videos[i].setUrl('https://www.youtube.com/embed/'+videoID)
        
        
################################################################################################################
#!####### Se crean las clases de las ventanas con los videos de cada tema que heredan de AbstractVideos ########
################################################################################################################
class V_U1_T1(AbstractVideos):
    def __init__(self,ventana:QMainWindow,frame:QFrame,tabWidget:QTabWidget,bt_retorno:QPushButton):
        super().__init__(ventana,frame,tabWidget,bt_retorno)
        
        self.setPathVideos('resources/videos/unidad 1/tema 1/')
        
class V_U1_T2(AbstractVideos):
    def __init__(self,ventana:QMainWindow,frame:QFrame,tabWidget:QTabWidget,bt_retorno:QPushButton):
        super().__init__(ventana,frame,tabWidget,bt_retorno)
        
        self.setPathVideos('resources/videos/unidad 1/tema 2/')
        
class V_U1_T3(AbstractVideos):
    def __init__(self,ventana:QMainWindow,frame:QFrame,tabWidget:QTabWidget,bt_retorno:QPushButton):
        super().__init__(ventana,frame,tabWidget,bt_retorno)
        
        self.setPathVideos('resources/videos/unidad 1/tema 3/')
        
class V_U1_T4(AbstractVideos):
    def __init__(self,ventana:QMainWindow,frame:QFrame,tabWidget:QTabWidget,bt_retorno:QPushButton):
        super().__init__(ventana,frame,tabWidget,bt_retorno)
        
        self.setPathVideos('resources/videos/unidad 1/tema 4/')
        
class V_U1_T5(AbstractVideos):
    def __init__(self,ventana:QMainWindow,frame:QFrame,tabWidget:QTabWidget,bt_retorno:QPushButton):
        super().__init__(ventana,frame,tabWidget,bt_retorno)
        
        self.setPathVideos('resources/videos/unidad 1/tema 5/')
        
class V_U2_T1(AbstractVideos):
    def __init__(self,ventana:QMainWindow,frame:QFrame,tabWidget:QTabWidget,bt_retorno:QPushButton):
        super().__init__(ventana,frame,tabWidget,bt_retorno)
        
        self.setPathVideos('resources/videos/unidad 2/tema 1/')
        
class V_U2_T2(AbstractVideos):
    def __init__(self,ventana:QMainWindow,frame:QFrame,tabWidget:QTabWidget,bt_retorno:QPushButton):
        super().__init__(ventana,frame,tabWidget,bt_retorno)
        
        self.setPathVideos('resources/videos/unidad 2/tema 2/')
        
class V_U2_T3(AbstractVideos):
    def __init__(self,ventana:QMainWindow,frame:QFrame,tabWidget:QTabWidget,bt_retorno:QPushButton):
        super().__init__(ventana,frame,tabWidget,bt_retorno)
        
        self.setPathVideos('resources/videos/unidad 2/tema 3/')
        
class V_U2_T4(AbstractVideos):
    def __init__(self,ventana:QMainWindow,frame:QFrame,tabWidget:QTabWidget,bt_retorno:QPushButton):
        super().__init__(ventana,frame,tabWidget,bt_retorno)
        
        self.setPathVideos('resources/videos/unidad 2/tema 4/')
        
class V_U2_T5(AbstractVideos):
    def __init__(self,ventana:QMainWindow,frame:QFrame,tabWidget:QTabWidget,bt_retorno:QPushButton):
        super().__init__(ventana,frame,tabWidget,bt_retorno)
        
        self.setPathVideos('resources/videos/unidad 2/tema 5/')
        
class V_U2_T6(AbstractVideos):
    def __init__(self,ventana:QMainWindow,frame:QFrame,tabWidget:QTabWidget,bt_retorno:QPushButton):
        super().__init__(ventana,frame,tabWidget,bt_retorno)
        
        self.setPathVideos('resources/videos/unidad 2/tema 6/')
        
class V_U2_T7(AbstractVideos):
    def __init__(self,ventana:QMainWindow,frame:QFrame,tabWidget:QTabWidget,bt_retorno:QPushButton):
        super().__init__(ventana,frame,tabWidget,bt_retorno)
        
        self.setPathVideos('resources/videos/unidad 2/tema 7/')
        
class V_U2_T8(AbstractVideos):
    def __init__(self,ventana:QMainWindow,frame:QFrame,tabWidget:QTabWidget,bt_retorno:QPushButton):
        super().__init__(ventana,frame,tabWidget,bt_retorno)
        
        self.setPathVideos('resources/videos/unidad 2/tema 8/')
        
class V_U2_T9(AbstractVideos):
    def __init__(self,ventana:QMainWindow,frame:QFrame,tabWidget:QTabWidget,bt_retorno:QPushButton):
        super().__init__(ventana,frame,tabWidget,bt_retorno)
        
        self.setPathVideos('resources/videos/unidad 2/tema 9/')
        
class V_U3_T1(AbstractVideos):
    def __init__(self,ventana:QMainWindow,frame:QFrame,tabWidget:QTabWidget,bt_retorno:QPushButton):
        super().__init__(ventana,frame,tabWidget,bt_retorno)
        
        self.setPathVideos('resources/videos/unidad 3/tema 1/')
        
class V_U3_T2(AbstractVideos):
    def __init__(self,ventana:QMainWindow,frame:QFrame,tabWidget:QTabWidget,bt_retorno:QPushButton):
        super().__init__(ventana,frame,tabWidget,bt_retorno)
        
        self.setPathVideos('resources/videos/unidad 3/tema 2/')
        
class V_U3_T3(AbstractVideos):
    def __init__(self,ventana:QMainWindow,frame:QFrame,tabWidget:QTabWidget,bt_retorno:QPushButton):
        super().__init__(ventana,frame,tabWidget,bt_retorno)
        
        self.setPathVideos('resources/videos/unidad 3/tema 3/')
        
        
class V_U3_T4(AbstractVideos):
    def __init__(self,ventana:QMainWindow,frame:QFrame,tabWidget:QTabWidget,bt_retorno:QPushButton):
        super().__init__(ventana,frame,tabWidget,bt_retorno)
        
        self.setPathVideos('resources/videos/unidad 3/tema 4/')
        
        
class V_U3_T5(AbstractVideos):
    def __init__(self,ventana:QMainWindow,frame:QFrame,tabWidget:QTabWidget,bt_retorno:QPushButton):
        super().__init__(ventana,frame,tabWidget,bt_retorno)
        
        self.setPathVideos('resources/videos/unidad 3/tema 5/')
        
        
class V_U3_T6(AbstractVideos):
    def __init__(self,ventana:QMainWindow,frame:QFrame,tabWidget:QTabWidget,bt_retorno:QPushButton):
        super().__init__(ventana,frame,tabWidget,bt_retorno)
        
        self.setPathVideos('resources/videos/unidad 3/tema 6/')
        
        
class V_U3_T7(AbstractVideos):
    def __init__(self,ventana:QMainWindow,frame:QFrame,tabWidget:QTabWidget,bt_retorno:QPushButton):
        super().__init__(ventana,frame,tabWidget,bt_retorno)
        
        self.setPathVideos('resources/videos/unidad 3/tema 7/')
        
        
class V_U3_T8(AbstractVideos):
    def __init__(self,ventana:QMainWindow,frame:QFrame,tabWidget:QTabWidget,bt_retorno:QPushButton):
        super().__init__(ventana,frame,tabWidget,bt_retorno)
        
        self.setPathVideos('resources/videos/unidad 3/tema 8/')
        
        
class V_U3_T9(AbstractVideos):
    def __init__(self,ventana:QMainWindow,frame:QFrame,tabWidget:QTabWidget,bt_retorno:QPushButton):
        super().__init__(ventana,frame,tabWidget,bt_retorno)
        
        self.setPathVideos('resources/videos/unidad 3/tema 9/')
        
        
class V_U4_T1(AbstractVideos):
    def __init__(self,ventana:QMainWindow,frame:QFrame,tabWidget:QTabWidget,bt_retorno:QPushButton):
        super().__init__(ventana,frame,tabWidget,bt_retorno)
        
        self.setPathVideos('resources/videos/unidad 4/tema 1/')
        
        
class V_U4_T2(AbstractVideos):
    def __init__(self,ventana:QMainWindow,frame:QFrame,tabWidget:QTabWidget,bt_retorno:QPushButton):
        super().__init__(ventana,frame,tabWidget,bt_retorno)
        
        self.setPathVideos('resources/videos/unidad 4/tema 2/')
        
        
class V_U4_T3(AbstractVideos):
    def __init__(self,ventana:QMainWindow,frame:QFrame,tabWidget:QTabWidget,bt_retorno:QPushButton):
        super().__init__(ventana,frame,tabWidget,bt_retorno)
        
        self.setPathVideos('resources/videos/unidad 4/tema 3/')
        
        
class V_U4_T4(AbstractVideos):
    def __init__(self,ventana:QMainWindow,frame:QFrame,tabWidget:QTabWidget,bt_retorno:QPushButton):
        super().__init__(ventana,frame,tabWidget,bt_retorno)
        
        self.setPathVideos('resources/videos/unidad 4/tema 4/')
        
        
class V_U4_T5(AbstractVideos):
    def __init__(self,ventana:QMainWindow,frame:QFrame,tabWidget:QTabWidget,bt_retorno:QPushButton):
        super().__init__(ventana,frame,tabWidget,bt_retorno)
        
        self.setPathVideos('resources/videos/unidad 4/tema 5/')
        
        
class V_U4_T6(AbstractVideos):
    def __init__(self,ventana:QMainWindow,frame:QFrame,tabWidget:QTabWidget,bt_retorno:QPushButton):
        super().__init__(ventana,frame,tabWidget,bt_retorno)
        
        self.setPathVideos('resources/videos/unidad 4/tema 6/')
        
        
class V_U4_T7(AbstractVideos):
    def __init__(self,ventana:QMainWindow,frame:QFrame,tabWidget:QTabWidget,bt_retorno:QPushButton):
        super().__init__(ventana,frame,tabWidget,bt_retorno)
        
        self.setPathVideos('resources/videos/unidad 4/tema 7/')
        
        
class V_U4_T8(AbstractVideos):
    def __init__(self,ventana:QMainWindow,frame:QFrame,tabWidget:QTabWidget,bt_retorno:QPushButton):
        super().__init__(ventana,frame,tabWidget,bt_retorno)
        
        self.setPathVideos('resources/videos/unidad 4/tema 8/')
        
        