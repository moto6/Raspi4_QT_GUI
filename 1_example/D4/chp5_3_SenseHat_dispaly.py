#5_3
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
        #self.sense.show_message(self.lineEdit.text())
        for y in range(8):
            for x in range(8):
                self.sense.set_pixel(x,y,255,255,255)
                sleep(0.1)
        sleep(3)
        self.sense.clear() 

app = QApplication([]) 
win = MyApp()
win.show()
app.exec()
