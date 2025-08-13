# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QDial, QGroupBox, QHBoxLayout,
    QLabel, QProgressBar, QPushButton, QSizePolicy,
    QTextBrowser, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setEnabled(True)
        Form.resize(783, 467)
        Form.setMouseTracking(False)
        self.horizontalLayout_3 = QHBoxLayout(Form)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.timeGB = QGroupBox(Form)
        self.timeGB.setObjectName(u"timeGB")
        self.verticalLayout_2 = QVBoxLayout(self.timeGB)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.timeGB)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"\u7b49\u7ebf"])
        font.setPointSize(72)
        self.label.setFont(font)
        self.label.setCursor(QCursor(Qt.CursorShape.ForbiddenCursor))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.label_2 = QLabel(self.timeGB)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamilies([u"\u7b49\u7ebf"])
        font1.setPointSize(26)
        self.label_2.setFont(font1)
        self.label_2.setCursor(QCursor(Qt.CursorShape.ForbiddenCursor))
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2.setWordWrap(False)

        self.verticalLayout_2.addWidget(self.label_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.hourDial = QDial(self.timeGB)
        self.hourDial.setObjectName(u"hourDial")
        self.hourDial.setEnabled(False)
        self.hourDial.setCursor(QCursor(Qt.CursorShape.ForbiddenCursor))
        self.hourDial.setMaximum(24)
        self.hourDial.setPageStep(6)
        self.hourDial.setWrapping(True)
        self.hourDial.setNotchTarget(3.699999999999999)
        self.hourDial.setNotchesVisible(True)

        self.horizontalLayout.addWidget(self.hourDial)

        self.minDial = QDial(self.timeGB)
        self.minDial.setObjectName(u"minDial")
        self.minDial.setEnabled(False)
        self.minDial.setCursor(QCursor(Qt.CursorShape.ForbiddenCursor))
        self.minDial.setMaximum(60)
        self.minDial.setPageStep(5)
        self.minDial.setWrapping(True)
        self.minDial.setNotchesVisible(True)

        self.horizontalLayout.addWidget(self.minDial)

        self.secDial = QDial(self.timeGB)
        self.secDial.setObjectName(u"secDial")
        self.secDial.setEnabled(False)
        self.secDial.setCursor(QCursor(Qt.CursorShape.ForbiddenCursor))
        self.secDial.setMaximum(60)
        self.secDial.setPageStep(5)
        self.secDial.setWrapping(True)
        self.secDial.setNotchesVisible(True)

        self.horizontalLayout.addWidget(self.secDial)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.horizontalLayout_3.addWidget(self.timeGB)

        self.classGB = QGroupBox(Form)
        self.classGB.setObjectName(u"classGB")
        self.verticalLayout_3 = QVBoxLayout(self.classGB)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.passedTime = QProgressBar(self.classGB)
        self.passedTime.setObjectName(u"passedTime")
        self.passedTime.setCursor(QCursor(Qt.CursorShape.BusyCursor))
        self.passedTime.setValue(24)
        self.passedTime.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.passedTime.setTextVisible(True)
        self.passedTime.setOrientation(Qt.Orientation.Horizontal)
        self.passedTime.setTextDirection(QProgressBar.Direction.TopToBottom)

        self.verticalLayout_3.addWidget(self.passedTime)

        self.pushButton = QPushButton(self.classGB)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.pushButton)


        self.horizontalLayout_3.addWidget(self.classGB)

        self.stopwatchGB = QGroupBox(Form)
        self.stopwatchGB.setObjectName(u"stopwatchGB")
        self.verticalLayout_4 = QVBoxLayout(self.stopwatchGB)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_3 = QLabel(self.stopwatchGB)
        self.label_3.setObjectName(u"label_3")
        font2 = QFont()
        font2.setFamilies([u"\u7b49\u7ebf"])
        font2.setPointSize(24)
        self.label_3.setFont(font2)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_3)

        self.dial = QDial(self.stopwatchGB)
        self.dial.setObjectName(u"dial")
        self.dial.setEnabled(False)
        self.dial.setCursor(QCursor(Qt.CursorShape.ForbiddenCursor))
        self.dial.setMaximum(60)
        self.dial.setPageStep(5)
        self.dial.setWrapping(True)
        self.dial.setNotchesVisible(True)

        self.verticalLayout_4.addWidget(self.dial)

        self.countsBrowser = QTextBrowser(self.stopwatchGB)
        self.countsBrowser.setObjectName(u"countsBrowser")

        self.verticalLayout_4.addWidget(self.countsBrowser)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.SPButton = QPushButton(self.stopwatchGB)
        self.SPButton.setObjectName(u"SPButton")
        self.SPButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.SPButton)

        self.countingButton = QPushButton(self.stopwatchGB)
        self.countingButton.setObjectName(u"countingButton")
        self.countingButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.countingButton)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_3.addWidget(self.stopwatchGB)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.timeGB.setTitle(QCoreApplication.translate("Form", u"\u65f6\u95f4", None))
        self.label.setText(QCoreApplication.translate("Form", u"[TIME]", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"[DATE]", None))
        self.classGB.setTitle(QCoreApplication.translate("Form", u"\u8bfe\u5802", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u4e0a\u8bfe\uff01", None))
        self.stopwatchGB.setTitle(QCoreApplication.translate("Form", u"\u79d2\u8868", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"[TIME]", None))
        self.SPButton.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb/\u6682\u505c", None))
        self.countingButton.setText(QCoreApplication.translate("Form", u"\u8ba1\u6b21", None))
    # retranslateUi

