#chp2_4
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import *

class MyThread(QThread):
    mySignal = pyqtSignal(int, int) #param (int, int) <= twice of integear number are accomped
    def __init__(self):
        super().__init__()
        self.isRun = False

    def run(self):
        for i in range(0,101):
            self.mySignal.emit(i,x)
            time.sleep(0.001)
        self.isRun = True 

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("hi.ui".self)

        self.pros = []
        for i in range(0,10):
            self.pros.append(self.lay.itemAt(i).Widget())
            self.pros[i].setValue(0)
        self.th = MyThread()
        self.th.mySignal.connect(self.setValue)

    def go(self):
        #10개의 Progress Bar를 0 ~ 100 까지 setValue 수행
        for i in range(10):
            for x in range(0,101,10):
                self.pros[i].setValue(x)

    def setValue(self, i, x):
        self.pros[i].setValue(x)

app = QApplication([]) 
win = MyApp()
win.show()
app.exec()

