import sys
import os
import math
from clases.ui_PdfView import Ui_PdfView
from PySide6.QtWidgets import QFileDialog, QMessageBox, QWidget, QPushButton, QApplication, QFrame
from PySide6.QtPdf import QPdfDocument
from PySide6.QtPdfWidgets import QPdfView
from PySide6.QtCore import QPoint, QStandardPaths, QUrl, Slot, Qt
import shutil

ZOOM_MULTIPLIER = math.sqrt(2.0)

class PdfView(QWidget,Ui_PdfView):
    def __init__(self, pdfView):
        super().__init__()
        self.setupUi(self)
        
        self.folder_location = None
        
        mode = QPdfView.PageMode.MultiPage
        self.pdfView.setPageMode(mode)
        
        self.m_document = QPdfDocument(self)
        self.m_fileDialog = None
        
        self.m_pageSelector.valueChanged.connect(self.page_selected)
        self.nav = self.pdfView.pageNavigator()
        self.nav.currentPageChanged.connect(self.m_pageSelector_setValue)
        
        self.m_zoomSelector.zoom_mode_changed.connect(self.pdfView.setZoomMode)
        self.m_zoomSelector.zoom_factor_changed.connect(self.pdfView.setZoomFactor)
        self.m_zoomSelector.reset()
        self.m_zoomSelector.setCurrentIndex(1)
        
        self.pdfView.setDocument(self.m_document)
        
        self.pdfView.zoomFactorChanged.connect(self.m_zoomSelector.set_zoom_factor)
        
        self.actionZoom_In.clicked.connect(self.on_actionZoom_In_triggered)
        self.actionZoom_Out.clicked.connect(self.on_actionZoom_Out_triggered)
        self.actionBack.clicked.connect(self.on_actionBack_triggered)
        self.actionForward.clicked.connect(self.on_actionForward_triggered)
        
        self.bt_descargar.clicked.connect(self.save_pdf)
        
    @Slot(str)
    def open(self, folder_location):
        self.folder_location = folder_location
        doc_location = QUrl.fromLocalFile(folder_location + "tema.pdf")
        if doc_location.isLocalFile():
            self.m_document.load(doc_location.toLocalFile())
            self.page_selected(1)
            self.pages = self.m_document.pageCount()
            self.m_pageSelector.setMaximum(self.pages)
            if self.pages >= 1:
                self.actionForward.setEnabled(True)
            self.m_pageSelector.setValue(1)
            self.m_pageSelector.setEnabled(True)
            cantidad_Codigos = len([archivo for archivo in os.listdir(folder_location) if archivo.endswith('.txt')])
            self.setCantidadCodigos(cantidad_Codigos)
        else:
            message = f"{doc_location} is not a valid local file"
            print(message, file=sys.stderr)
            QMessageBox.critical(self, "Failed to open", message)
        
    @Slot(int)
    def page_selected(self, page):
        self.nav.jump(page-1, QPoint(), self.nav.currentZoom())
        
    @Slot()
    def on_actionZoom_In_triggered(self):
        factor = self.pdfView.zoomFactor() * ZOOM_MULTIPLIER
        self.pdfView.setZoomFactor(factor)

    @Slot()
    def on_actionZoom_Out_triggered(self):
        factor = self.pdfView.zoomFactor() / ZOOM_MULTIPLIER
        self.pdfView.setZoomFactor(factor)

    @Slot()
    def on_actionBack_triggered(self):
        self.nav.jump(self.nav.currentPage() - 1, QPoint(), self.nav.currentZoom())

    @Slot()
    def on_actionForward_triggered(self):
        self.nav.jump(self.nav.currentPage() + 1, QPoint(), self.nav.currentZoom())
        
    def m_pageSelector_setValue(self, value):
        self.m_pageSelector.setValue(value+1)
        if self.nav.currentPage() == 0:
            self.actionBack.setEnabled(False)
        else:
            self.actionBack.setEnabled(True)
        if self.nav.currentPage()+1 == self.pages:
            self.actionForward.setEnabled(False)
        else:
            self.actionForward.setEnabled(True)
            
    def save_pdf(self):
        if self.folder_location != None:
            # Suponiendo que la ruta original del PDF está almacenada en algún lugar
            original_pdf_path = self.folder_location + "tema.pdf"
            
            file_path, _ = QFileDialog.getSaveFileName(self, "Guardar PDF", QStandardPaths.writableLocation(QStandardPaths.DocumentsLocation), "PDF Files (*.pdf)")
            if file_path:
                try:
                    shutil.copy2(original_pdf_path, file_path)
                    QMessageBox.information(self, "Guardado", "PDF guardado con éxito.")
                    
                    
                except Exception as e:
                    QMessageBox.critical(self, "Error", f"No se pudo guardar el PDF: {e}")
            
    def setCantidadCodigos(self,n:int):
        if self.folder_location != None:
            line = QFrame(self.controlPdf)
            # line.setObjectName(u"line_2")
            line.setFrameShape(QFrame.VLine)
            line.setFrameShadow(QFrame.Sunken)
            self.controlesLayout.addWidget(line)
            for i in range(n):
                text = 'Código '+str(i+1)
                file_path = self.folder_location+'codigo '+str(i+1)+'.txt'
                self.controlesLayout.addWidget(BotonCopiarCodigo(text,file_path))
    
class BotonCopiarCodigo(QPushButton):
    def __init__(self,text:str,file_path:str):
        super().__init__(text=text)
        self.file_path = file_path
        self.clicked.connect(self.copy_text_to_clipboard)
        # Se establece el cursor para el botón
        self.setCursor(Qt.PointingHandCursor)
        
    def copy_text_to_clipboard(self):
        file_path = self.file_path
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                text_to_copy = file.read()
            clipboard = QApplication.clipboard()
            clipboard.setText(text_to_copy)
            QMessageBox.information(self, "Copiado", "Código copiado al portapapeles.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo leer el archivo: {e}")