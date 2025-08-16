from PySide6.QtWidgets import *
from mwLogic import window
import sys
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = window()
    mainWindow.show()
    sys.exit(app.exec())