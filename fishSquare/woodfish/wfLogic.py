from PySide6 import QtCore, QtGui, QtWidgets
from .wfWindowUI import Ui_Form
class wfWindow(Ui_Form, QtWidgets.QWidget):
    def __init__(self, parent=None):
        self.merit = 0
        super(wfWindow, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint | QtCore.Qt.Tool)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setGeometry(1100, 50, 172, 138)
        self.pushButton.pressed.connect(self.giveGavel)
        self.pushButton.released.connect(self.stopGavel)
        self.pushButton.setIcon(QtGui.QIcon("fishSquare/woodfish/up.png"))
        self.backButton.clicked.connect(self.close1)
        self.parentWidget = parent
    def giveGavel(self):
        self.pushButton.setIcon(QtGui.QIcon("fishSquare/woodfish/down.png"))
    def stopGavel(self):
        self.pushButton.setIcon(QtGui.QIcon("fishSquare/woodfish/up.png"))
        self.merit += 1
        self.label.setText(f"功德: {self.merit}")
    def close1(self):
        self.parentWidget.pushButton.setEnabled(True)
        self.parentWidget.show()
        self.close()
        self.deleteLater()
        