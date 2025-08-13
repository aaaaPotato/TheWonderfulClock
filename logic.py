from PySide6 import QtCore, QtGui, QtWidgets
import mainWindowUI
import time
class window(mainWindowUI.Ui_Form, QtWidgets.QWidget):
    def __init__(self):
        self.ptime = 0
        super(window,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("WHAT A CLOCK!")
        self.timer = QtCore.QTimer()
        self.timer.start(100)
        self.timer.timeout.connect(self.updateTime)
        self.classTimer = QtCore.QTimer()
        self.pushButton.clicked.connect(self.classTimerStart)
        self.passedTime.setValue(100)
    def updateTime(self):
        self.label.setText(time.strftime("%H:%M:%S"))
        self.hourDial.setValue(int(time.strftime("%H"))+12)
        self.minDial.setValue(int(time.strftime("%M"))+30)
        self.secDial.setValue(int(time.strftime("%S"))+30)
    def updateClassTime(self):
        self.passedTime.setValue(self.ptime/144000)
        self.ptime += 10
        if self.ptime >= 144000:
            self.classTimer.stop()
    def classTimerStart(self):
        self.classTimer.timeout.connect(self.updateClassTime)
        self.classTimer.start(10000)