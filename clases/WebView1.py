from PySide6.QtWidgets import QVBoxLayout, QWidget
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWebEngineCore import QWebEngineSettings, QWebEnginePage
from PySide6.QtCore import QUrl
from PySide6.QtGui import QDesktopServices

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

class CustomWebViewWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0,0,0,0)
        
        self.web_view = QWebEngineView()
        
        # Establecer nuestra propia clase de página web personalizada en el QWebEngineView
        self.web_view.setPage(MyWebEnginePage(self.web_view))

        # Habilitar el soporte de pantalla completa y otros ajustes
        self.web_view.settings().setAttribute(QWebEngineSettings.FullScreenSupportEnabled, True)
        self.web_view.settings().setAttribute(QWebEngineSettings.WebGLEnabled, True)
        self.web_view.settings().setAttribute(QWebEngineSettings.JavascriptEnabled, True)
        self.web_view.settings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
        self.web_view.settings().setAttribute(QWebEngineSettings.AllowRunningInsecureContent, True)
        self.web_view.settings().setAttribute(QWebEngineSettings.LinksIncludedInFocusChain, True)
        self.web_view.settings().setAttribute(QWebEngineSettings.PlaybackRequiresUserGesture, False)
        
        # Mantener relación de aspecto
        self.web_view.resizeEvent = lambda event: self.web_view.setMinimumHeight(int(self.web_view.width()/2.1))
        
        # # Mostrar los mensajes de la consola de JavaScript
        # self.web_view.page().setInspectedPage(self.web_view.page())


        # Conectar la señal de pantalla completa
        self.web_view.page().fullScreenRequested.connect(self.handle_full_screen)

        # Añadir el QWebEngineView al layout
        self.layout.addWidget(self.web_view)
        self.setLayout(self.layout)

    def handle_full_screen(self, request):
        if request.toggleOn():
            # Lógica para entrar en modo de pantalla completa
            request.accept()
            self.parentWidget().showFullScreen()
        else:
            # Lógica para salir del modo de pantalla completa
            request.accept()
            self.parentWidget().showNormal()
            
    def setUrl(self, url:str):
        self.web_view.load(QUrl(url))

# Ahora puedes usar tu CustomWebViewWidget en cualquier lugar donde usarías un QWidget,
# por ejemplo, en una QMainWindow o en cualquier otro tipo de contenedor de widgets.