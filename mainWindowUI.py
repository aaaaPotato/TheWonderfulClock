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
        Form.resize(867, 467)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMouseTracking(False)
        self.horizontalLayout_3 = QHBoxLayout(Form)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.classGB = QGroupBox(Form)
        self.classGB.setObjectName(u"classGB")
        sizePolicy.setHeightForWidth(self.classGB.sizePolicy().hasHeightForWidth())
        self.classGB.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QVBoxLayout(self.classGB)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.passedTime = QProgressBar(self.classGB)
        self.passedTime.setObjectName(u"passedTime")
        sizePolicy.setHeightForWidth(self.passedTime.sizePolicy().hasHeightForWidth())
        self.passedTime.setSizePolicy(sizePolicy)
        self.passedTime.setCursor(QCursor(Qt.CursorShape.BusyCursor))
        self.passedTime.setValue(24)
        self.passedTime.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.passedTime.setTextVisible(True)
        self.passedTime.setOrientation(Qt.Orientation.Horizontal)
        self.passedTime.setTextDirection(QProgressBar.Direction.TopToBottom)

        self.verticalLayout_3.addWidget(self.passedTime)

        self.pushButton = QPushButton(self.classGB)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)
        self.pushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.pushButton)


        self.horizontalLayout_3.addWidget(self.classGB)

        self.timeGB = QGroupBox(Form)
        self.timeGB.setObjectName(u"timeGB")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.timeGB.sizePolicy().hasHeightForWidth())
        self.timeGB.setSizePolicy(sizePolicy2)
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

        self.stopwatchGB = QGroupBox(Form)
        self.stopwatchGB.setObjectName(u"stopwatchGB")
        sizePolicy.setHeightForWidth(self.stopwatchGB.sizePolicy().hasHeightForWidth())
        self.stopwatchGB.setSizePolicy(sizePolicy)
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

        self.swDial = QDial(self.stopwatchGB)
        self.swDial.setObjectName(u"swDial")
        self.swDial.setEnabled(False)
        self.swDial.setCursor(QCursor(Qt.CursorShape.ForbiddenCursor))
        self.swDial.setMaximum(60)
        self.swDial.setPageStep(5)
        self.swDial.setWrapping(True)
        self.swDial.setNotchesVisible(True)

        self.verticalLayout_4.addWidget(self.swDial)

        self.countsBrowser = QTextBrowser(self.stopwatchGB)
        self.countsBrowser.setObjectName(u"countsBrowser")
        sizePolicy1.setHeightForWidth(self.countsBrowser.sizePolicy().hasHeightForWidth())
        self.countsBrowser.setSizePolicy(sizePolicy1)

        self.verticalLayout_4.addWidget(self.countsBrowser)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.SPButton = QPushButton(self.stopwatchGB)
        self.SPButton.setObjectName(u"SPButton")
        sizePolicy1.setHeightForWidth(self.SPButton.sizePolicy().hasHeightForWidth())
        self.SPButton.setSizePolicy(sizePolicy1)
        self.SPButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.SPButton.setMouseTracking(False)
        self.SPButton.setTabletTracking(False)
        self.SPButton.setCheckable(True)
        self.SPButton.setChecked(False)
        self.SPButton.setAutoRepeat(False)
        self.SPButton.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.SPButton)

        self.countingButton = QPushButton(self.stopwatchGB)
        self.countingButton.setObjectName(u"countingButton")
        sizePolicy1.setHeightForWidth(self.countingButton.sizePolicy().hasHeightForWidth())
        self.countingButton.setSizePolicy(sizePolicy1)
        self.countingButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.countingButton)

        self.toZeroButton = QPushButton(self.stopwatchGB)
        self.toZeroButton.setObjectName(u"toZeroButton")
        sizePolicy1.setHeightForWidth(self.toZeroButton.sizePolicy().hasHeightForWidth())
        self.toZeroButton.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.toZeroButton)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_3.addWidget(self.stopwatchGB)

        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.tempBar = QProgressBar(self.groupBox)
        self.tempBar.setObjectName(u"tempBar")
        self.tempBar.setValue(24)
        self.tempBar.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_4.addWidget(self.tempBar)

        self.humBar = QProgressBar(self.groupBox)
        self.humBar.setObjectName(u"humBar")
        self.humBar.setValue(24)
        self.humBar.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_4.addWidget(self.humBar)

        self.preBar = QProgressBar(self.groupBox)
        self.preBar.setObjectName(u"preBar")
        self.preBar.setValue(24)
        self.preBar.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_4.addWidget(self.preBar)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.tempLabel = QLabel(self.groupBox)
        self.tempLabel.setObjectName(u"tempLabel")

        self.verticalLayout.addWidget(self.tempLabel)

        self.humLabel = QLabel(self.groupBox)
        self.humLabel.setObjectName(u"humLabel")

        self.verticalLayout.addWidget(self.humLabel)

        self.preLabel = QLabel(self.groupBox)
        self.preLabel.setObjectName(u"preLabel")

        self.verticalLayout.addWidget(self.preLabel)


        self.horizontalLayout_3.addWidget(self.groupBox)

        QWidget.setTabOrder(self.pushButton, self.hourDial)
        QWidget.setTabOrder(self.hourDial, self.minDial)
        QWidget.setTabOrder(self.minDial, self.secDial)
        QWidget.setTabOrder(self.secDial, self.swDial)
        QWidget.setTabOrder(self.swDial, self.countsBrowser)
        QWidget.setTabOrder(self.countsBrowser, self.SPButton)
        QWidget.setTabOrder(self.SPButton, self.countingButton)
        QWidget.setTabOrder(self.countingButton, self.toZeroButton)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.classGB.setTitle(QCoreApplication.translate("Form", u"\u8bfe\u5802", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u4e0a\u8bfe\uff01", None))
        self.timeGB.setTitle(QCoreApplication.translate("Form", u"\u65f6\u95f4", None))
        self.label.setText(QCoreApplication.translate("Form", u"[TIME]", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"[DATE]", None))
        self.stopwatchGB.setTitle(QCoreApplication.translate("Form", u"\u79d2\u8868", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"[TIME]", None))
        self.SPButton.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb/\u6682\u505c", None))
        self.countingButton.setText(QCoreApplication.translate("Form", u"\u8ba1\u6b21", None))
        self.toZeroButton.setText(QCoreApplication.translate("Form", u"\u5f52\u96f6", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u73af\u5883", None))
        self.tempLabel.setText(QCoreApplication.translate("Form", u"Temp.", None))
        self.humLabel.setText(QCoreApplication.translate("Form", u"Humi.", None))
        self.preLabel.setText(QCoreApplication.translate("Form", u"Pres.", None))
    # retranslateUi

