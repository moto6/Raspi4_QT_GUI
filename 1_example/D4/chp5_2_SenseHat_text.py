#5_2
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import *
from gpiozero import *
from time import *
from sense_hat import SenseHat
#from sense_emu import SenseHat


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("hat.ui",self)
        self.main()

    def main(self):
        self.sense = SenseHat()

    def go(self):
        self.sense.show_message(self.lineEdit.text())

app = QApplication([]) 
win = MyApp()
win.show()
app.exec()
