from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6 import QtCore
import sys
from clases.ui_pruebaSim_1 import Ui_pruebaSim_1
from clases.Sim_U1_T2 import Sim_U1_T2
from clases.Videos import V_U1_T1

class PruebaSim_1(QMainWindow, Ui_pruebaSim_1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self.webView.setUrl('https://www.youtube.com/embed/i-EHZt-xRnw?si=Hw07WNudJ9yFCl3X')
        # self.webView.setVisible(False)
        self.v_U1_T1 = V_U1_T1(self,self.frame_video,self.tabWidget,self.pushButton)
        
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PruebaSim_1()
    window.show()
    window.update()
    sys.exit(app.exec())