from PyQt5.QtWidgets import *

app = QApplication([])
win = QMainWindow()


app.setApplicationName("My InMAC")
win.resize(400,400)
bar = win.statusBar()
bar.showMessage("인맥을 관리합시다~!")


mb = win.menuBar()
menu = mb.addMenu('메뉴')


menuAdd = QAction("추가",win)
menuRemove = QAction("제거",win)
bye = QAction("종료",win)

menu.addAction(menuAdd)
menu.addAction(menuRemove)
mb.addAction(bye)

main = QWidget()
win.setCentralWidget(main)

addBtn = QPushButton("추가")
removeBtn = QPushButton("제거")

btnLayout = QHBoxLayout()
btnLayout.addWidget(addBtn)
btnLayout.addWidget(removeBtn)

form = QFormLayout()
name = QLineEdit()

form.addWidget(QLabel("인맥을 관리."))
form.addRow("name",name)
form.addRow(btnLayout)

main.setLayout(form)



def add():
    pass
def remove():
    pass

def byebye():
    print("BYE")
    quit()



names = ["SSAFY", "SAMSA", "HYINDAI", "SKSKS"]

addBtn.clicked.connect(add)
removeBtn.clicked.connect(remove)


menuAdd.triggered.connect(add)
menuRemove.triggered.connect(remove)
bye.triggered.connect(byebye)

win.show()
app.exec()
