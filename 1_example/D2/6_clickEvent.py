#6_clickEvent.py
from PyQt5.QtWidgets import *
app = QApplication([])
bot = QPushButton('Click')

def on_bot_click():
    alert = QMessageBox()
    alert.setText('you clicked the button')
    alert.exec()

bot.clicked.connect(on_bot_click)
bot.show()
app.exec()