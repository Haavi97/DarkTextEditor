import sys
import time
import datetime as dt

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget, QDesktopWidget

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('Dark Theme Text Editor')
window.setGeometry(100, 100, 280, 80)
window.move(60, 15)
helloMsg = QLabel('<h1>Dark Theme Text Editor</h1>', parent=window)
helloMsg.move(60, 15)

window.show()

centerPoint = QDesktopWidget().availableGeometry().center()
window2 = QWidget()
window2.setWindowTitle('Extra window')
window2.setGeometry(100, 100, 280, 80)
window2.move(centerPoint)
helloMsg2 = QLabel('<p>p text</p>', parent=window2)
helloMsg2.move(60, 15)

window2.show()

sys.exit(app.exec_())