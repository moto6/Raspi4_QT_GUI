#4 QMSG_Box
from PyQt5.QtWidgets import *

app = QApplication([])
win = QWidget()

alert = QMessageBox()
alert.setText("Father Touch")
alert.exec()

win.show()
app.exex()