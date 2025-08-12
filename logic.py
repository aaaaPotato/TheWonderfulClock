from PySide6 import QtCore, QtGui, QtWidgets
import mainWindowUI
import time
class window(mainWindowUI.Ui_Form, QtWidgets.QWidget):
    def __init__(self):
        super(window,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("WHAT A CLOCK!")
        self.timer = QtCore.QTimer()
        self.timer.start(100)
        self.timer.timeout.connect(self.updateTime)
    def updateTime(self):
        self.label.setText(time.strftime("%H:%M:%S"))
        self.hourDial.setValue(int(time.strftime("%H")))
        self.minDial.setValue(int(time.strftime("%M")))
        self.secDial.setValue(int(time.strftime("%S")))