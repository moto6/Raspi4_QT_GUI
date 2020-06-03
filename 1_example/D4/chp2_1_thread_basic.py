#chp2_1_thread_basic.py
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import *

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("chp2_1_thread_basic.ui",self)
        #self.main()

    def go(self):
        print("Very good! you just cilcked btn, but we must do something")
        pass


app = QApplication([]) 
win = MyApp()
win.show()
app.exec()

