
from PyQt5.QtWidgets import *

app = QApplication([])
win = QWidget()

#form = QFormLayout()
#Swin.setLayout(form)

#formEdit = QLineEdit()
#form.addRow("name", formEdit)

## ?!?!?
win.setWindowTitle("My First QT APP!") #메시지 변경!!
lineEdit = QLineEdit(win)
button = QPushButton("OKAY",win) #메시지 변경!!
mainLayout = QHBoxLayout()
mainLayout.addWidget(lineEdit)
mainLayout.addWidget(button)
win.setLayout(mainLayout)

mainLayout = QHBoxLayout()
win.show()
app.exec()
