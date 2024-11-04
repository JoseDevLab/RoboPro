import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_Ejemplo_pdfView import Ui_Ejemplo_pdfView

class Ejemplo_pdfView(QMainWindow,Ui_Ejemplo_pdfView):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ejemplo = Ejemplo_pdfView()
    ejemplo.show()
    sys.exit(app.exec())