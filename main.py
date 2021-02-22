import sys
import time
import datetime as dt
import threading

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel, QTextEdit
from PyQt5.QtWidgets import QWidget, QDesktopWidget
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QStatusBar
from PyQt5.QtWidgets import QToolBar
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QColor
# from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5 import QtGui


whiteColor = QColor(255, 255, 255)
blackColor = QColor(0, 0, 0)

style = "background-color: rgb(0, 0, 0); color: rgb(255,255,255);"
about_file = "about.html"


class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Dark Theme Text Editor')
        self._editBox = QTextEdit()
        self.setCentralWidget(self._editBox)
        self.setStyleSheet(style)
        self._createMenu()
        self._createToolBar()
        self._createStatusBar()
        self.about_window = About()
        self._fileDialog = QFileDialog()

    def _createMenu(self):
        self.menu = self.menuBar().addMenu("&Menu")
        self.menu.addAction('&About', self.about)
        self.menu.addAction('&Exit', self.close)

        
        self.options = self.menuBar().addMenu("&Options")

        self.options.addAction('&Font', self.font)

    def _createToolBar(self):
        tools = QToolBar()
        self.addToolBar(tools)
        tools.addAction('Save', self.save)
        tools.addAction('Exit', self.close)

    def _createStatusBar(self):
        self.status = QStatusBar()
        self.status.showMessage('New file')
        self.setStatusBar(self.status)

    def about(self):
        self.about_window.show()

    def font(self):
        print("To be implemented")

    def save(self):
        print(self._editBox.toPlainText())
        name = self._fileDialog.getSaveFileName(self)
        print(name[0])
        file = open(name[0],'w')
        text = self._editBox.toPlainText()
        file.write(text)
        file.close()


class About(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('About page')
        f = open(about_file, "r")
        self.about_text = f.read()
        f.close()
        self.setCentralWidget(QLabel(self.about_text))
        self.setStyleSheet(style)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('blackicon.svg'))

    win = Window()
    win.show()

    sys.exit(app.exec_())
