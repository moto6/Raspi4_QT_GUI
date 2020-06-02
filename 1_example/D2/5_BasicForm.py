from PyQt5.QtWidgets import *

app = QApplication([])
win = QWidget()

win.setWindowTitle("Hi QT world!")
lineEdit = QLineEdit(win)
button = QPushButton("OKAY",win)
mainLayout = QHBoxLayout()
mainLayout.addWidget(lineEdit)
mainLayout.addWidget(button)
win.setLayout(mainLayout)

win.show()
app.exec()
