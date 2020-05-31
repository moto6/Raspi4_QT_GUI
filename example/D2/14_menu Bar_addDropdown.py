#13_menu Bar
from PyQt5.QtWidgets import *

app = QApplication([])
win = QMainWindow()

win.resize(300,300)
menu = win.menuBar()
menuFILE = menu.addMenu('FILE')
menuEXIT = menu.addMenu('EXIT')


bye = QAction("NEW",win)
menuFILE.addAction(bye)

win.show()
app.exec()