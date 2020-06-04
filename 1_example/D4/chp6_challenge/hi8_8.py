from PyQt5.QtWidgets import *
from PyQt5.uic import *
from sense_emu import SenseHat
from time import sleep

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("hi.ui", self)
        self.main()
    
    def main(self):        
        self.sense = SenseHat()
    
    def click(self, x, y):
        print(x, y)
    
    def flash(self):
        pass
    
    def clear(self):
        pass
        
    def rslide(self, value):
        print(value)
    
    def gslide(self, value):
        print(value)
    
    def bslide(self, value):
        print(value)
        
app = QApplication([])
win = MyApp()
win.show()
app.exec()
