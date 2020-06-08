from PyQt5.QtWidgets import *
from PyQt5.uic import *
from PyQt5.QtGui import *
import cv2
import numpy

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("pic.ui",self)
        print("sd")
        self.main()
        
    def main(self):
        ##img = QImage('bg.jpg')
        self.img = cv2.imread('bg.jpg')
        
        self.img = self.imp0(self.img)
        ##self.img = cv2.imp2(self,img)
        ##self.img = cv2.imp3(self,img)
        ##self.img = cv2.imp4(self,img)
        ##self.img = cv2.imp5(self,img)
        self.printImage(self.img, self.pic)
        
        # pyqt call
        #label = QLabel(self)
        #label.setPixmap(QPixmap(img))
        #label.adjustSize()
        print("##")
        
        
        
    def imp0(self, img):
        #img = cv2.blur(img,(22,22))
        return img
        
        
    def imp1(self, img):
        img = cv2.blur(img,(22,22))
        return img
    
    def imp2(self, img):
        img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        return img
    
    
    def imp3(self, img):
        img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        kernal = numpy.ones((3,3), numpy.uint8)
        img = cv2.morphologyEx(img,cv2.MORPH_GRADIENT, kernal)
        return img
    
    
    def imp4(self, img):
        img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        ret, img = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)
        return img
    
    
    def imp5(self, img):
        ##img =
        return img
    def printImage(self, imgBGR, pic) :
        imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)
        h,w,byte = imgRGB.shape
        img = QImage(imgRGB, w, h, byte*w, QImage.Format_RGB888)
        pic.setPixmap(QPixmap(img))
                
        
app = QApplication([])
win = MyApp()
win.show()
app.exec()
print("##ss")
                        
    