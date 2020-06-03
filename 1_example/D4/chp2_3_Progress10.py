#chp2_3
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import *
from time import sleep

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("chp2_1_thread_basic.ui",self)

        self.pros = []
        for i in range(0,8):
            self.pros.append(self.lay.itemAt(i).widget())
            #(self.lay.itemAt(i).widget())
            self.pros[i].setValue(0)

    
    def go(self):
        #10개의 Progress Bar를 0 ~ 100 까지 setValue 수행
        for i in range(8):
            for x in range(0,101,10):
                self.pros[i].setValue(x)
                sleep(0.01)


app = QApplication([]) 
win = MyApp()
win.show()
app.exec()

