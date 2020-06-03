#chp1_1_QTimer.py
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.main()

    def main(self):
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.run)
        self.timer.start()

    def run(self):
        print("#")

app = QApplication([]) 
win = MyApp()
win.show()
app.exec()

