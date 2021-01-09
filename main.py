import sys
import time
import datetime as dt

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget, QDesktopWidget
# from PyQt5.QtWidgets import * 
from PyQt5 import QtCore 
from PyQt5 import QtGui 

app = QApplication(sys.argv)

app.setWindowIcon(QtGui.QIcon('blackicon.svg')) 

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
window2.setGeometry(100, 100, centerPoint.x(), centerPoint.y()*2)
window2.move(centerPoint.x(),0)
helloMsg2 = QLabel('<p>p text</p>', parent=window2)
helloMsg2.move(60, 15)


if __name__ == "__main__":
  
    window2.show()

    sys.exit(app.exec_())