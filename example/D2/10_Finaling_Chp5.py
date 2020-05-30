#10_Finaling_Chp5.py
from PyQt5.QtWidgets import *

app = QApplication([])
win = QWidget()


form = QFormLayout()
win.setLayout(form)

#31
formED1 = QLineEdit()
form.addRow('name',formED1)


#32
formED2 = QLineEdit()
formButton = QPushButton("나이확인")

formLayout = QHBoxLayout()
formLayout.addWidget(formED2)
formLayout.addWidget(formButton)
form.addRow("age",formLayout)

#33p
formLabel = QLabel("경고 : 나이")
form.addWidget(formLabel)

#Form 완성하기 34p


win.show()
app.exec()


'''

win.setWindowTitle("Hi QT world!")
lineEdit = QLineEdit(win)
button = QPushButton("OKAY",win)
mainLayout = QHBoxLayout()
mainLayout.addWidget(lineEdit)
mainLayout.addWidget(button)
win.setLayout(mainLayout)

'''