from PySide6.QtWidgets import QWidget
from clases.ui_ContenidosTema import Ui_contenidosTema

class ContenidosTemas(QWidget, Ui_contenidosTema):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        
    def setColor(self,color:int):
        if color == 1:
            self.pdfView.frame.setStyleSheet(u"QFrame#frame{\n"
                                            "background-color:rgba(0,0,0,0);\n"
                                            "border-radius:10px\n"
                                            "}\n"
                                            "QFrame#controlPdf, \n"
                                            "QFrame#controlPdf QFrame{\n"
                                            "background-color:rgba(173, 51, 51,255);\n"
                                            "}")
        elif color == 2:
            self.pdfView.frame.setStyleSheet(u"QFrame#frame{\n"
                                            "background-color:rgba(0,0,0,0);\n"
                                            "border-radius:10px\n"
                                            "}\n"
                                            "QFrame#controlPdf, \n"
                                            "QFrame#controlPdf QFrame{\n"
                                            "background-color: rgb(0, 51, 102);\n"
                                            "}")
        elif color == 3:
            self.pdfView.frame.setStyleSheet(u"QFrame#frame{\n"
                                            "background-color:rgba(0,0,0,0);\n"
                                            "border-radius:10px\n"
                                            "}\n"
                                            "QFrame#controlPdf, \n"
                                            "QFrame#controlPdf QFrame{\n"
                                            "background-color:rgb(218, 218, 218);\n"
                                            "}")
        elif color == 4:
            self.pdfView.frame.setStyleSheet(u"QFrame#frame{\n"
                                            "background-color:rgba(0,0,0,0);\n"
                                            "border-radius:10px\n"
                                            "}\n"
                                            "QFrame#controlPdf, \n"
                                            "QFrame#controlPdf QFrame{\n"
                                            "background-color:rgb(239, 184, 16);\n"
                                            "}")
            