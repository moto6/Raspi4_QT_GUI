#14-2_QWigetProblem.py
from PyQt5.QtWidgets import *

app = QApplication([])
win = QMainWindow()

menu = win.menuBar()

# added code
menu.addMenu("ABC")
menu.addMenu("BTS")
#occur prob
label = QLabel("HI SSAFY",win)


#label.show()
win.show()
app.exec()