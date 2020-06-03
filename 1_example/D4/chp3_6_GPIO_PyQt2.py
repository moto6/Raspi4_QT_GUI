#5_GPIO_PyQt.py
from gpiozero import LED, Button
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import *

led = LED(18)
led2 = LED(15)
button = Button(24)

app = QApplication([])
win = QMainWindow()

app.setApplicationName("GPIO Control With GUI")
win.resize(400,250)
bar = win.statusBar()
bar.showMessage("copyright(c) 2020 All rights reserved")


win.resize(300,300)
mb = win.menuBar()
bye = QAction('EXIT',win)
mb.addAction(bye)


main = QWidget()
win.setCentralWidget(main)


onBtn = QPushButton("LED ON")
offBtn = QPushButton("LED OFF")
swBtn = QPushButton("Swtich Check")
#remove ; off
btnLayout = QHBoxLayout()
btnLayout.addWidget(onBtn)
btnLayout.addWidget(offBtn)
btnLayout.addWidget(swBtn)
form = QFormLayout()
#name = QLineEdit()

#//pwform = QFormLayout()
pwname = QLineEdit()
#pwform.addWidget(QLabel("pwform"))

form.addRow(btnLayout)

main.setLayout(form)

        


#================
def onnled():
    print("LED ON!")
    #================
    led.on()
    led2.on()
    #================

def offled():
    print("LED OFF")
    #================
    led.off()
    led2.off()
    #================
    
def swcheck():
    if button.is_pressed:
        print("pressed!!!!")
    else:
        print("released...")

def byebye():
    print("EXIT")
    quit()


onBtn.clicked.connect(onnled)
offBtn.clicked.connect(offled)
swBtn.clicked.connect(swcheck)

#menuAdd.triggered.connect(onnled)
#menuRemove.triggered.connect(offled)
bye.triggered.connect(byebye)
#


win.show()
app.exec()
