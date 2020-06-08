#chp
from PyQt5.QtWidgets import *
from PyQt5.uic import *
from PyQt5.QtGui import *
#from matplotlib import pyplot
#from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
#from PyQt5.QtCore import *

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("test2.ui",self)
        self.main()

    def main(self):
        self.img = cv2.imread('')
        self.img = self.processingImage(self.img)
        self.printImage(self.img, self.pic)

    def processingImage(self, img):

        #img = cv2.blur(img,(55,55))
        
        #img = cv2.
        

        img = cv2.cvtColor(img,cv2.COLOR_RGB2RRAY)
        kernal = numpy.ones((3,3), numpy.uint8)
        img = cv2.morphologyEx(img,cv2.MORPH_GRADIENT, kernal)
        
        
        
        return img

    def printImage(self, img):
        imgRGB = cv2.cvtColor(imgRGB, cv2.COLOR_RGB2RGB)
        h, w, byte = imgRGB.shape
        img = QImage(imgRGB,w,h,byte *w, QImage.Format_RGB888)
        pic.setPixmap(QPixmap(img))
        
app = QApplication([])
win = MyApp()
win.show()
app.exec()