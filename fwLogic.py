from PySide6 import QtCore, QtGui, QtWidgets
import floatingWindowUI
import time
class floatingWindow(floatingWindowUI.Ui_Form, QtWidgets.QWidget):
    def __init__(self,parent=None):
        super(floatingWindow, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint | QtCore.Qt.Tool)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setGeometry(1350,50,172,138)
        self.classTimeBar.setRange(0, 2400)
        self.classTimeBar.setValue(2400)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(lambda: self.timeLabel.setText(time.strftime("%H:%M:%S")))
        self.timer.start(100)
        self.transparencySlider.valueChanged.connect(self.changeTransparency)
        self.backButton.clicked.connect(self.back)
        self.parentWidget = parent
        self.classTimer = QtCore.QTimer()
        self.classTimer.timeout.connect(self.updateClassTime)
        self.classTimer.start(3000)
    def changeTransparency(self, value):
        self.setWindowOpacity(value / 100.0)
    def back(self):
        self.parentWidget.show()
        self.close()
    def updateClassTime(self):
        self.classTimeBar.setValue(self.parentWidget.ptime)