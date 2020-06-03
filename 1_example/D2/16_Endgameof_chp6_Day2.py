#15 day2 Final
from PyQt5.QtWidgets import *

app = QApplication([])
win = QMainWindow()


#52================
app.setApplicationName("MyFriends")
win.resize(400,400)
bar = win.statusBar()
bar.showMessage("인맥을 관리합시다")
#52================


#win.resize(300,300)
mb = win.menuBar()
menu = mb.addMenu('메뉴')

menuAdd = QAction('추가',win)
menuRemove = QAction('제거',win)
bye = QAction('종료',win)


menu.addAction(menuAdd)
menu.addAction(menuRemove)
mb.addAction(bye)


#53==================
main = QWidget()
win.setCentralWidget(main)
#53==================




#54=================
addBtn = QPushButton("추가")
removeBtn = QPushButton("제거")

btnLayout = QHBoxLayout()
btnLayout.addWidget(addBtn)
btnLayout.addWidget(removeBtn)

form = QFormLayout()
name = QLineEdit()
form.addWidget(QLabel("인맥을 관리합시다."))
form.addRow("name",name)
form.addRow(btnLayout)

main.setLayout(form)
#54=================





#55================
def add():
    print("ADD")
    #56================
    str = name.text()
    if len(str) == 0:return

    global names
    if names.count(str) == 1:
        bar.showMessage("이미 친구입니다")
    else:
        bar.showMessage("환영합니다 나의 인맥")
        names.append(str)
        print(names)
    #56================

def remove():
    print("REMOVE")
    #57================
    str = name.text()
    if len(str) == 0:return

    global names
    if names.count(str) == 0:
        bar.showMessage(str+",그는내친구아냐")
    else: 
        bar.showMessage(str+",더이상내친구아냐")
        names.remove(str)
        print(names)
    #57================

def byebye():
    print("BYE")
    app.quit()


names = ["inho","dongHun","cart","hwan"]
addBtn.clicked.connect(add)
removeBtn.clicked.connect(remove)

menuAdd.triggered.connect(add)
menuRemove.triggered.connect(remove)
bye.triggered.connect(byebye)
#55================



win.show()
#app.quit()
app.exec()