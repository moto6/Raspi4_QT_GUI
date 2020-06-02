#14-1
from PyQt5.QtWidgets import *

app = QApplication([])
win = QMainWindow()

win.resize(300,300)
menu = win.menuBar()
menuFILE = menu.addMenu('FILE')
menuEXIT = menu.addMenu('EXIT')


bye = QAction("NEW",win)
menuFILE.addAction(bye)

def run():
    bar.showMessage("메뉴 버튼을 눌렀습니다")


bar = win.statusBar()
menuFILE.triggered.connect(run)

win.show()
app.exec()