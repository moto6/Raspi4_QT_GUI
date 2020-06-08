#chp
from PyQt5.QtWidgets import *
from PyQt5.uic import *
from PyQt5.QtGui import *
#from matplotlib import pyplot
#from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
#from PyQt5.QtCore import *

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("test2.ui",self)
        self.main()

        '''
        self.readImg = cv2.imread('')
        self.new
        '''

    def main(self):
        img = QImage('')
        label = QLabel(self)
        label.setPixmap(QPixmap(img))
        label.adjustSize()

app = QApplication([])
win = MyApp()
win.show()
app.exec()