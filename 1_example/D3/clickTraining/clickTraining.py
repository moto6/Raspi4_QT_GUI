from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtTest
from PyQt5.uic import *
import random

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("clickTraining.ui", self)        
        
        self.timer = QBasicTimer()
        self.timer.start(600, self)
        
    def timerEvent(self, e):
        x = random.randint(0, self.frame.size().width())
        y = random.randint(0, self.frame.size().height())
        self.label.move(x, y)
        
    def showDialog(self):
        sender = self.sender()
        if sender.text() == "이름변경":
            name, ok = QInputDialog.getText(self, '이름입력', '너의 이름은?')
            if ok:
                self.label.setText(name)
                self.label.adjustSize()
            
        if sender.text() == "컬러변경":
            color = QColorDialog.getColor()
            if color.isValid():
                self.frame.setStyleSheet("background-color:%s" % color.name())
        
    def mousePressEvent(self, e):
        x = e.x()
        y = e.y()
        
        tx = self.label.x()
        ty = self.label.y()
        twidth = self.label.width()
        theight = self.label.height()
        
        if tx <= x <= tx + twidth:
            if ty <= y <= ty + theight:
                self.frame.setStyleSheet("background-color:#FF3256")
                QtTest.QTest.qWait(200)
                self.frame.setStyleSheet("background-color:#FFFFFF")
        
        
        
        
app = QApplication([])
win = MyApp()
win.show()
app.exec()