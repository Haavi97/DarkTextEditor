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
import json

with open('conf.json', 'r') as conf_file:
    conf = json.load(conf_file)


whiteColor = QColor(255, 255, 255)
blackColor = QColor(0, 0, 0)

about_file = conf['about_file']
style_file = conf['style_file']
style = ''.join(open(style_file, 'r').read().split('\n'))


class Window(QMainWindow):
    def __init__(self, w, h, parent=None):
        super().__init__(parent)
        self._autosaveText = 'Enable autosave'
        self._autosave = False
        self.name = ''
        self.font_size = conf['default-font-size']
        self.font = 'font-size: ' +  str(conf['default-font-size'])
        self.background_color = 'background-color: ' + conf['background-color']
        self.font_color = 'color: ' +  conf['font-color']
        self.style = ''
        self.updateStyle()
        self.setWindowTitle('Dark Theme Text Editor')
        self._editBox = QTextEdit()
        self.setCentralWidget(self._editBox)
        self._createMenu()
        self._createToolBar()
        self._createStatusBar()
        self.about_window = About(w*0.5, h*0.5)
        self._fileDialog = QFileDialog()
        self.resize(int(w), int(h))

    def _createMenu(self):
        self.menu = self.menuBar().addMenu("&Menu")
        self.menu.addAction('&About', self.about)
        self.menu.addAction('&Exit', self.close)
        self.options = self.menuBar().addMenu("&Options")
        self.options.addAction('&Font', self.fontMenu)

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

    def updateStatusBar(self, text):
        self.status.showMessage(text)
        self.setStatusBar(self.status)

    def about(self):
        self.about_window.show()
    
    def saveFile(self):
        file = open(self.name, 'w')
        text = self._editBox.toPlainText()
        file.write(text)
        file.close()

    def save(self):
        print(self._editBox.toPlainText())
        if self.name != '':
            self.updateStatusBar(self.name)
            self.saveFile()
        else:
            self.name = self._fileDialog.getSaveFileName(self)[0]
            if self.name != '':
                self.saveFile()


    def autosave(self):
        if self._autosave:
            self._autosaveText = 'Enable autosave'
        else:
            self._autosaveText = 'Disable autosave'
        self._autosave = not self._autosave

    def changeFontSize(self, size):
        self.font = 'font-size:{}px'.format(int(size))
        self.updateStyle()

    def wheelEvent(self, event):
        self.font_size += event.angleDelta().y()/280
        self.changeFontSize(self.font_size)

    def fontMenu(self):
        print('Font menu to be implemented')
    
    def updateStyle(self):
        self.style = ''
        self.style += self.font + ';'
        self.style += self.background_color + ';'
        self.style += self.font_color + ';'
        self.setStyleSheet(self.style)


class About(QMainWindow):
    def __init__(self, w, h, parent=None):
        super().__init__(parent)
        self.setWindowTitle('About page')
        with open(about_file, "r") as f:
            self.about_text = f.read()
        f.close()
        self.setCentralWidget(QLabel(self.about_text))
        self.setStyleSheet(style)
        self.resize(int(w), int(h))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('blackicon.svg'))

    screen = app.primaryScreen()
    size = screen.size()
    rect = screen.availableGeometry()

    p = 0.7

    win = Window(int(rect.width()*p), int(rect.height()*p))
    win.show()

    sys.exit(app.exec_())
