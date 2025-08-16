# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'floatingWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QProgressBar, QPushButton,
    QSizePolicy, QSlider, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(176, 140)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.timeLabel = QLabel(Form)
        self.timeLabel.setObjectName(u"timeLabel")
        font = QFont()
        font.setFamilies([u"\u7b49\u7ebf"])
        font.setPointSize(26)
        font.setBold(True)
        self.timeLabel.setFont(font)
        self.timeLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.timeLabel)

        self.classTimeBar = QProgressBar(Form)
        self.classTimeBar.setObjectName(u"classTimeBar")
        self.classTimeBar.setValue(100)
        self.classTimeBar.setTextVisible(False)

        self.verticalLayout.addWidget(self.classTimeBar)

        self.transparencySlider = QSlider(Form)
        self.transparencySlider.setObjectName(u"transparencySlider")
        self.transparencySlider.setMinimum(20)
        self.transparencySlider.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout.addWidget(self.transparencySlider)

        self.backButton = QPushButton(Form)
        self.backButton.setObjectName(u"backButton")
        self.backButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout.addWidget(self.backButton)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.timeLabel.setText(QCoreApplication.translate("Form", u"[TIME]", None))
        self.backButton.setText(QCoreApplication.translate("Form", u"\u8fd4\u56de", None))
    # retranslateUi

