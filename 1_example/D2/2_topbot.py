from PyQt5.QtWidgets import *
app = QApplication([])
window = QWidget()
layout = QVBoxLayout()
layout.addWidget(QPushButton('top'))
layout.addWidget(QPushButton('bot'))
window.setLayout(layout)
window.show()
app.exec()