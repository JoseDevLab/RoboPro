from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6 import QtCore
from PySide6.QtCore import QSize
import sys
from clases.Sim_U4_T4 import Sim_U4_T4

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.resize(900,650)
        self.sim = Sim_U4_T4()
        self.setCentralWidget(self.sim)
        self.sim.init()
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
