from PyQt5.QtWidgets import *
from PyQt5.QtGui import QKeySequence

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.main()

    def main(self):
        self.resize(400,400)
        self.btn = QPushButton()

        #not Yet