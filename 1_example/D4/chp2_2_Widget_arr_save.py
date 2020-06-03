#chp2_2
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import *
from random import *

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("chp2_1_thread_basic.ui",self)
        #self.main()

        #progress bar value settting 0
        self.pros = []
        for i in range(0,8):
            self.pros.append(self.lay.itemAt(i).widget())
            self.pros[i].setValue(0)

    def go(self):
        for i in range(0,8):
            self.pros.append(self.lay.itemAt(i).widget())
            self.pros[i].setValue(randint(1, 65))
        pass


app = QApplication([]) 
win = MyApp()
win.show()
app.exec()

