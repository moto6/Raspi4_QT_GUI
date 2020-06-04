#chp3_8
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import *


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("",self)
        self.maia()

    def main(self):
        pass

    def ledOn(self):
        print("ON")

    def ledOff(self):
        print("OFF")

    def setDial(self):
        print(value)

app = QApplication([])
win = MyApp()
win.show()
app.exec()