from PyQt5.QtWidgets import *
from PyQt5.uic import *
from PyQt5.QtGui import *
import cv2
from PyQt5.QtTest import *
from PyQt5.QtCore import *
from time import sleep

class MyThread(QThread):
    mySignal = pyqtSignal(QPixmap, QPixmap)
    def __init__(self):
        super().__init__()
        #self.cam = cv2.VideoCapture(0)
        self.cam = cv2.VideoCapture('s1.mp4')
        self.cam.set(3, 480) #width(3)
        self.cam.set(4, 320) #height(4)

    def run(self):
        while True:
            ret, self.img = self.cam.read()
            self.printImage(self.img)
            sleep(0.1)

    def printImage(self, imgBGR):
        imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)
        h, w, byte = imgRGB.shape
        img = QImage(imgRGB, w, h, byte * w, QImage.Format_RGB888)
        img = QPixmap(img)
        
        imgGray = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2GRAY)
        imgCanny = cv2.Canny(imgGray, 100, 100)
        img2 = QImage(imgCanny, w, h, imgCanny.strides[0], QImage.Format_Grayscale8)
        img2 = QPixmap(img2)

        self.mySignal.emit(img, img2)
                
    
class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("hi.ui", self)
        self.main()
    
    def main(self):
        self.th = MyThread()
        self.th.mySignal.connect(self.setImage)
    
    def getPicture(self):
        self.th.start()
            
    def setImage(self, img, img2):
        self.pic1.setPixmap(img)
        self.pic2.setPixmap(img2)
        
    
app = QApplication([])
win = MyApp()
win.show()
app.exec()