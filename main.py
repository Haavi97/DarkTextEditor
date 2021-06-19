import sys
import os
import time
import datetime as dt
import threading

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QLabel, QTextEdit, QShortcut
from PyQt5.QtWidgets import QWidget, QDesktopWidget
from PyQt5.QtWidgets import QStatusBar, QToolBar
from PyQt5.QtWidgets import QFileDialog, QFontDialog
from PyQt5.QtGui import QColor, QKeySequence
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
        # Inheritance
        super().__init__(parent)

        # Basic parameters
        self.name = ''

        # Style parameters
        self.font_size = conf['default-font-size']
        self.font = 'font-size: ' + str(conf['default-font-size'])
        self.background_color = 'background-color: ' + conf['background-color']
        self.font_color = 'color: ' + conf['font-color']
        self.font_family = ''
        self.style = ''

        self._autosaveText = 'Enable autosave'
        self._autosave = False

        self.encoding = 'utf-8'

        # Main widgets
        self._editBox = QTextEdit()
        self.about_window = About(w*0.5, h*0.5)
        self._fileDialog = QFileDialog()

        # Setting edit box main properties
        self.setCentralWidget(self._editBox)
        self.resize(int(w), int(h))
        self.setFocusPolicy(QtCore.Qt.StrongFocus)
        self._editBox.setFocusPolicy(QtCore.Qt.StrongFocus)
        self._editBox.setAcceptRichText(False)  # Erase format when pasting

        # Timer for the autosave
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.save)

        # Shortcuts (https://zetcode.com/pyqt/qshortcut/)
        self.ctrlsave = QShortcut(QKeySequence('Ctrl+S'), self)
        self.ctrlsave.activated.connect(self.save)
        self.quitSc = QShortcut(QKeySequence('Ctrl+Q'), self)
        self.quitSc.activated.connect(QApplication.instance().quit)

        # Initial functions
        self.updateStyle()
        self.setWindowTitle('Dark Theme Text Editor')
        self._createMenu()
        self._createToolBar()
        self._createStatusBar()

    def _createMenu(self):
        self.menu = self.menuBar().addMenu("&Menu")
        self.menu.addAction('&Open file', self.openFile)
        self.menu.addAction('&Save copy as', self.save_as)
        self.menu.addAction('&Change encoding', self.changeEncoding)
        self.menu.addAction('&About', self.about)
        self.menu.addAction('&Exit', self.close)
        self.options = self.menuBar().addMenu("&Options")
        self.options.addAction('&Font', self.fontMenu)

    def _createToolBar(self):
        tools = QToolBar()
        self.addToolBar(tools)
        tools.addAction('Save', self.save)
        tools.addAction('Exit', self.close)
        self.saveAction = tools.addAction(self._autosaveText, self.autosave)

    def _createStatusBar(self):
        self.status = QStatusBar()
        self.status.showMessage('New file')
        self.setStatusBar(self.status)

    def about(self):
        self.about_window.show()

    def updateStatusBar(self, text):
        self.status.showMessage(text)
        self.setStatusBar(self.status)

    # SAVE METHODS
    def saveFile(self):
        file = open(self.name, 'wb')
        text = (self._editBox.toPlainText()).encode(self.encoding)
        file.write(text)
        file.close()

    def save(self, bypass=False):
        if self.name != '':
            self.updateStatusBar(self.name)
            self.saveFile()
        else:
            self.name = self._fileDialog.getSaveFileName(self)[0]
            if self.name != '':
                self.saveFile()
                self.updateStatusBar(self.name)
            else:
                self.updateStatusBar('Unsaved file')

    def save_as(self):
        self.save(bypass=True)

    def autosave(self):
        if self._autosave:
            self._autosaveText = 'Enable autosave'
            self._autosave = True
            self.timer.stop()
        else:
            self._autosaveText = 'Disable autosave'
            self._autosave = False
            self.timer.start(1000)
        self.saveAction.setText(self._autosaveText)

    # STYLE METHODS
    def changeFontSize(self, size):
        self.font = 'font-size:{}px'.format(int(size))
        self.updateStyle()

    def fontMenu(self):
        font, valid = QFontDialog.getFont()
        if valid:
            self.font_family = 'font-family:"{}";'.format(font)
        self.updateStyle()

    def updateStyle(self):
        self.style = ''
        self.style += self.font + ';'
        self.style += self.background_color + ';'
        self.style += self.font_color + ';'
        self.style += self.font_family + ';'
        self.setStyleSheet(self.style)

    # OTHER METHODS
    def openFile(self):
        self.name = QFileDialog.getOpenFileName(self, 'Open file')[0]
        try:
            with open(self.name, 'rb') as fn:
                self._editBox.setText(fn.read().decode(self.encoding))
        except:
            print('To add message box of wrong encoding')
            with open(self.name, 'r') as fn:
                self._editBox.setText(fn.read())
        self.save()

    def changeEncoding(self):
        print('To do. Change encoding')

    def wheelEvent(self, event):
        self.font_size += event.angleDelta().y()/280
        self.changeFontSize(self.font_size)


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
    # If the os is Windows there is need to do some
    # trick for the icon to appear in the taskbar.
    if os.name == 'nt':
        import ctypes
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
            "myappid")
    
    app = QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('blackicon.svg'))

    screen = app.primaryScreen()
    size = screen.size()
    rect = screen.availableGeometry()

    # Proportion of the windows size the application takes on launch
    p = 0.7

    win = Window(int(rect.width()*p), int(rect.height()*p))
    win.show()

    sys.exit(app.exec_())
