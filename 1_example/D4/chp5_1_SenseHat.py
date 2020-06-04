#5_1
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("hi.ui",self)
        self.main()

    def main(self):
        pass

app = QApplication([]) 
win = MyApp()
win.show()
app.exec()
