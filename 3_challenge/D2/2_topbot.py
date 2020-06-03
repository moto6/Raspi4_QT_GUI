from PyQt5.QtWidgets import *

app = QApplication([])# QApp class instace make
window = QWidget()
layout = QVBoxLayout()
layout.addWidget(QPushButton('top'))
layout.addWidget(QPushButton('bot'))
window.setLayout(layout)
window.show()
app.exec_()