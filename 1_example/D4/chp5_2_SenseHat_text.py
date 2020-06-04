#5_2
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
#from senst_hat import SenseHat
from senst_emu import SenseHat


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("hi.ui",self)
        self.main()

    def main(self):
        self.sense = SenseHat()

    def go(slef):
        self.sense.show_message(self.lineEdit.text())

app = QApplication([]) 
win = MyApp()
win.show()
app.exec()
