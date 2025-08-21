from PySide6 import QtCore, QtGui, QtWidgets
from .fsWindowUI import Ui_Form
class fsWindow(Ui_Form, QtWidgets.QWidget):
    def __init__(self,parent=None):
        super(fsWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("摸鱼广场")
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.showNormal()
        self.timer = QtCore.QTimer()
        self.timer.start(1000)
        self.pushButton.clicked.connect(self.openWoodfish)
        self.pushButton_2.clicked.connect(self.openBalls)
        self.pushButton_3.clicked.connect(self.openFans)
        self.pushButton_4.clicked.connect(self.openButton)
        self.parentWidget = parent
    def openWoodfish(self):
        from .woodfish.wfLogic import wfWindow
        self.wfWindow = wfWindow(self)
        self.wfWindow.show()
        self.pushButton.setEnabled(False)
    def openBalls(self):
        pass
    def openFans(self):
        pass
    def openButton(self):
        pass