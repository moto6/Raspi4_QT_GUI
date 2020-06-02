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
formLabel.setVisible(False)
formButton2 = QPushButton("회원가입")
form.addRow(formButton2)

app.setApplicationName("My World!!")


#35
def checkAge():
    # 36
    age = formED2.text()
    if age.isdigit() == False: return
    age = int(age)
    if age >= 25: formLabel.setVisible(True)
    else: formLabel.setVisible(False)

def checkName():
    # name check
    #36
    name = formED1.text()
    n = len(name)
    if 1 <= n <= 4 : pass
    else: 
        msg = QMessageBox()
        msg.setText("이름은 1~4글자로 지정해야 합니다")
        msg.exec()

formButton.clicked.connect(checkAge)
formButton2.clicked.connect(checkName)




#####################
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