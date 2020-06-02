#14-4_QWigetProblemsol.py
from PyQt5.QtWidgets import *

app = QApplication([])
win = QMainWindow()

menu = win.menuBar()

menu.addMenu("ABC")
menu.addMenu("BTS")

#added========================
main = QWidget()
win.setCentralWidget(main)
#added========================

#error case
#label = QLabel("HI SSAFY",win)

#good case
label = QLabel("HI SSAFY",main)


#label.show()
win.show()
app.exec()