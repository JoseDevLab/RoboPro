from PySide6.QtWidgets import QWidget, QApplication
from PySide6.QtWebEngineCore import QWebEngineSettings, QWebEnginePage
from PySide6.QtCore import QUrl, Qt
from PySide6.QtGui import QDesktopServices
from clases.ui_WebView import Ui_Form


class MyWebEnginePage(QWebEnginePage):
    def __init__(self, parent=None):
        super(MyWebEnginePage, self).__init__(parent)
        self.newWindowRequested.connect(self.on_new_window_requested)

    def on_new_window_requested(self, request):
        # Aquí manejas la petición de una nueva ventana abriendo el enlace en un navegador externo
        QDesktopServices.openUrl(request.requestedUrl())
        
    # def certificateError(self, error):
    #     # Advertencia: Permitir errores de certificado puede ser riesgoso y solo se debe usar para desarrollo.
    #     if error.isOverridable():
    #         error.ignoreCertificateError()
    #         return True
    #     return False

class WebView(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        
        self.window = None
        self.mainWindow = None
        self.verticalScrollBarValue = 0
        self.heightScale = 642/1337
        
        
        # Establecer nuestra propia clase de página web personalizada en el QWebEngineView
        self.webEngineView.setPage(MyWebEnginePage(self.webEngineView))
        
        self.webEngineView.page().titleChanged.connect(self.setTitle)

        # Habilitar el soporte de pantalla completa y otros ajustes
        self.webEngineView.settings().setAttribute(QWebEngineSettings.FullScreenSupportEnabled, True)
        self.webEngineView.settings().setAttribute(QWebEngineSettings.WebGLEnabled, True)
        self.webEngineView.settings().setAttribute(QWebEngineSettings.JavascriptEnabled, True)
        self.webEngineView.settings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
        self.webEngineView.settings().setAttribute(QWebEngineSettings.AllowRunningInsecureContent, True)
        self.webEngineView.settings().setAttribute(QWebEngineSettings.LinksIncludedInFocusChain, True)
        self.webEngineView.settings().setAttribute(QWebEngineSettings.PlaybackRequiresUserGesture, False)
        
        # Mantener relación de aspecto
        self.frame_webView.resizeEvent = lambda event: self.frame_webView.setMinimumHeight(int(self.frame_webView.width()*self.heightScale))
        
        # Se conecta la señal del click del botón para abrir la url en el navegador externo
        self.bt_Title_Page.clicked.connect(self.openUrl)

        # Se establece el cursor para el botón
        self.bt_Title_Page.setCursor(Qt.PointingHandCursor)

        # Conectar la señal de pantalla completa
        self.webEngineView.page().fullScreenRequested.connect(self.handle_full_screen)

    def handle_full_screen(self, request):
        if request.toggleOn():
            # Lógica para entrar en modo de pantalla completa
            request.accept()
            self.frame.hide()
            screen = QApplication.primaryScreen()
            screen_size = screen.size()
            self.heightScale = screen_size.height()/(screen_size.width())
            if self.window!=None:
                self.window.showFullScreen()
            ############## Se ocultan todos los demás videos ###############
            for i in range(self.window.layoutVideos.count()):
                item = self.window.layoutVideos.itemAt(i)
                widget = item.widget()
                if widget is not None and widget != self:
                    widget.hide()
            self.verticalScrollBarValue = self.window.scrollArea.verticalScrollBar().value()
        else:
            # Lógica para salir del modo de pantalla completa
            request.accept()
            self.frame.show()
            self.heightScale = 642/1337
            if self.window!=None:
                self.window.showNormal()
            ############## Se muestran todos los demás videos ###############
            for i in range(self.window.layoutVideos.count()):
                item = self.window.layoutVideos.itemAt(i)
                widget = item.widget()
                if widget is not None and widget != self:
                    widget.show()
            self.window.widgetContentsCambioTamanio.connect(self.scrollBarSetValue)
            self.window.scrollArea.verticalScrollBar().valueChanged.connect(self.desconectarSeñal)
            
    ############# Desconecta la señal widgetContentsCambioTamanio y valueChanged #############
    def desconectarSeñal(self,value):
            self.window.widgetContentsCambioTamanio.disconnect(self.scrollBarSetValue)
            self.window.scrollArea.verticalScrollBar().valueChanged.disconnect(self.desconectarSeñal)
    
    def scrollBarSetValue(self):
        self.window.scrollArea.verticalScrollBar().setValue(self.verticalScrollBarValue)
    
    def setUrl(self, url:str):
        self.webEngineView.load(QUrl(url))
        self.url = url
        
    def setTitle(self, title):
        if title[-7:]=='YouTube':
            title = title[:-9]
        self.bt_Title_Page.setText(title)
        
    def openUrl(self):
        url = 'https://www.youtube.com/watch?v=' + self.url[30:]
        QDesktopServices.openUrl(url)
        
    def setWindow(self, window):
        self.window = window
        # Conectar la señal de pantalla completa
        self.webEngineView.page().fullScreenRequested.connect(self.handle_full_screen)
        
    def setMainWindow(self, mainWindow):
        self.mainWindow = mainWindow
        # Conecta el evento del click en el botón de titulo con minimizar la ventana principal
        self.bt_Title_Page.clicked.connect(lambda: mainWindow.showMinimized())
        # Conectar el evento de abrir un enlace para ocultar la ventana
        self.webEngineView.page().newWindowRequested.connect(lambda request: mainWindow.showMinimized())
        
        

# Ahora puedes usar tu CustomWebViewWidget en cualquier lugar donde usarías un QWidget,
# por ejemplo, en una QMainWindow o en cualquier otro tipo de contenedor de widgets.
        