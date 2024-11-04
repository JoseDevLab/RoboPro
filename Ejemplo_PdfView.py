import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QUrl
from clases.ui_Ejemplo_pdfView import Ui_Ejemplo_pdfView

class Ejemplo_pdfView(QMainWindow,Ui_Ejemplo_pdfView):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pdfView_1.open(QUrl('file:resources/test.pdf'))
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ejemplo = Ejemplo_pdfView()
    ejemplo.show()
    sys.exit(app.exec())