#13_menu Bar
from PyQt5.QtWidgets import *

app = QApplication([])
win = QMainWindow()

win.resize(300,300)
#bar = win.statusBar()
#bar.showMessage("now you empty stomic")
menu = win.menuBars()
menu.addMenu('menu')
menu.addMenu('BYE')

win.show()
app.exec()