from PyQt5.QtWidgets import *
app = QApplication([])
window = QWidget()


mainLayout = QVBoxLayout()
HeadLayout = QHBoxLayout()
bodyLayout = QVBoxLayout()
mainLayout.addLayout(HeadLayout)
mainLayout.addLayout(bodyLayout)

HeadLayout.addWidget(QPushButton('ONE'))
HeadLayout.addWidget(QPushButton('TWO'))
HeadLayout.addWidget(QPushButton('TRE'))

bodyLayout.addWidget(QPushButton('1'))
bodyLayout.addWidget(QPushButton('2'))
bodyLayout.addWidget(QPushButton('3'))


window.setLayout(mainLayout)
window.show()
app.exec()


