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

bodyLayout.addWidget(QPushButton('111'))
bodyLayout.addWidget(QPushButton('222'))
bodyLayout.addWidget(QPushButton('333'))


window.setLayout(mainLayout)
window.show()
app.exec()


