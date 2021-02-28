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

style = ''.join(open("style.css", "r").read().split("\n"))
about_file = "about.html"


class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._autosaveText = 'Enable autosave'
        self._autosave = False
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
        tools.addAction(self._autosaveText, self.autosave)

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
        name = self._fileDialog.getSaveFileName(self)[0]
        if name != '':
            print(name)
            file = open(name,'w')
            text = self._editBox.toPlainText()
            file.write(text)
            file.close()
    
    def autosave(self):
        if self._autosave:
            self._autosaveText = 'Enable autosave'
        else:
            self._autosaveText = 'Disable autosave'
        self._autosave = not self._autosave


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
