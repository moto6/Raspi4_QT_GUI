#12_status Bar
from PyQt5.QtWidgets import *

app = QApplication([])
win = QMainWindow()

win.resize(500,500)
bar = win.statusBar()
bar.showMessage("now you empty stomic")

win.show()
app.exec()