import sys
import time
import datetime as dt

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel, QTextEdit
from PyQt5.QtWidgets import QWidget, QDesktopWidget
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QStatusBar
from PyQt5.QtWidgets import QToolBar
from PyQt5.QtGui import QColor
# from PyQt5.QtWidgets import * 
from PyQt5 import QtCore 
from PyQt5 import QtGui 


whiteColor = QColor(255, 255, 255)
blackColor = QColor(0, 0, 0)

class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Dark Theme Text Editor')
        self.setCentralWidget(QTextEdit())
        self.setStyleSheet("background-color: rgb(0, 0, 0); color: rgb(255,255,255);")
        self._createMenu()
        self._createToolBar()
        self._createStatusBar()

    def _createMenu(self):
        self.menu = self.menuBar().addMenu("&Menu")
        self.options = self.menuBar().addMenu("&Options")
        self.menu.addAction('&About', self.about)
        self.menu.addAction('&Exit', self.close)

    def _createToolBar(self):
        tools = QToolBar()
        self.addToolBar(tools)
        tools.addAction('Exit', self.close)

    def _createStatusBar(self):
        self.status = QStatusBar()
        self.status.showMessage('New file')
        self.setStatusBar(status)

    def about(self):
        # TODO! Create an about window refering to the Github repo
        print('about')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('blackicon.svg')) 

    win = Window()
    win.show()

    sys.exit(app.exec_())