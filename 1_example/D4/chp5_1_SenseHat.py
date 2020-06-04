from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import *
from gpiozero import *


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("hat.ui",self)
        self.main()

    def main(self):
        pass

app = QApplication([]) 
win = MyApp()
win.show()
app.exec()
