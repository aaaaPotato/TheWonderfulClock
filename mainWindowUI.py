# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
    QSpacerItem, QTextBrowser, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setEnabled(True)
        Form.resize(920, 642)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMouseTracking(False)
        self.horizontalLayout_5 = QHBoxLayout(Form)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.countdownToCEE = QGroupBox(Form)
        self.countdownToCEE.setObjectName(u"countdownToCEE")
        self.verticalLayout_8 = QVBoxLayout(self.countdownToCEE)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.CEETime = QLabel(self.countdownToCEE)
        self.CEETime.setObjectName(u"CEETime")
        font = QFont()
        font.setFamilies([u"\u7b49\u7ebf"])
        font.setPointSize(48)
        font.setBold(True)
        self.CEETime.setFont(font)
        self.CEETime.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.CEETime)


        self.verticalLayout_6.addWidget(self.countdownToCEE)

        self.classesGB = QGroupBox(Form)
        self.classesGB.setObjectName(u"classesGB")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.classesGB.sizePolicy().hasHeightForWidth())
        self.classesGB.setSizePolicy(sizePolicy1)
        self.verticalLayout_5 = QVBoxLayout(self.classesGB)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.classesBrowser = QTextEdit(self.classesGB)
        self.classesBrowser.setObjectName(u"classesBrowser")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.classesBrowser.sizePolicy().hasHeightForWidth())
        self.classesBrowser.setSizePolicy(sizePolicy2)
        font1 = QFont()
        font1.setFamilies([u"\u7b49\u7ebf"])
        font1.setPointSize(18)
        self.classesBrowser.setFont(font1)
        self.classesBrowser.setReadOnly(True)

        self.verticalLayout_5.addWidget(self.classesBrowser)


        self.verticalLayout_6.addWidget(self.classesGB)

        self.classGB = QGroupBox(Form)
        self.classGB.setObjectName(u"classGB")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.classGB.sizePolicy().hasHeightForWidth())
        self.classGB.setSizePolicy(sizePolicy3)
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
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy4)
        self.pushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.pushButton)


        self.verticalLayout_6.addWidget(self.classGB)


        self.horizontalLayout_5.addLayout(self.verticalLayout_6)

        self.timeGB = QGroupBox(Form)
        self.timeGB.setObjectName(u"timeGB")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.timeGB.sizePolicy().hasHeightForWidth())
        self.timeGB.setSizePolicy(sizePolicy5)
        self.verticalLayout_2 = QVBoxLayout(self.timeGB)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.timeGB)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setFamilies([u"\u7b49\u7ebf"])
        font2.setPointSize(72)
        font2.setBold(True)
        self.label.setFont(font2)
        self.label.setCursor(QCursor(Qt.CursorShape.ForbiddenCursor))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.label_2 = QLabel(self.timeGB)
        self.label_2.setObjectName(u"label_2")
        font3 = QFont()
        font3.setFamilies([u"\u7b49\u7ebf"])
        font3.setPointSize(26)
        self.label_2.setFont(font3)
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


        self.horizontalLayout_5.addWidget(self.timeGB)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy4.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy4)
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.weatherLogo = QLabel(self.groupBox)
        self.weatherLogo.setObjectName(u"weatherLogo")
        sizePolicy.setHeightForWidth(self.weatherLogo.sizePolicy().hasHeightForWidth())
        self.weatherLogo.setSizePolicy(sizePolicy)
        self.weatherLogo.setPixmap(QPixmap(u"weatherLogo/0@2x.png"))
        self.weatherLogo.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.weatherLogo)

        self.weatherInfo = QLabel(self.groupBox)
        self.weatherInfo.setObjectName(u"weatherInfo")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.weatherInfo.sizePolicy().hasHeightForWidth())
        self.weatherInfo.setSizePolicy(sizePolicy6)
        font4 = QFont()
        font4.setFamilies([u"\u7b49\u7ebf"])
        font4.setPointSize(20)
        self.weatherInfo.setFont(font4)

        self.horizontalLayout_3.addWidget(self.weatherInfo)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.pushButton_2 = QPushButton(self.groupBox)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout.addWidget(self.pushButton_2)


        self.verticalLayout_7.addWidget(self.groupBox)

        self.stopwatchGB = QGroupBox(Form)
        self.stopwatchGB.setObjectName(u"stopwatchGB")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.stopwatchGB.sizePolicy().hasHeightForWidth())
        self.stopwatchGB.setSizePolicy(sizePolicy7)
        self.verticalLayout_4 = QVBoxLayout(self.stopwatchGB)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_3 = QLabel(self.stopwatchGB)
        self.label_3.setObjectName(u"label_3")
        font5 = QFont()
        font5.setFamilies([u"\u7b49\u7ebf"])
        font5.setPointSize(24)
        self.label_3.setFont(font5)
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
        sizePolicy4.setHeightForWidth(self.countsBrowser.sizePolicy().hasHeightForWidth())
        self.countsBrowser.setSizePolicy(sizePolicy4)

        self.verticalLayout_4.addWidget(self.countsBrowser)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.SPButton = QPushButton(self.stopwatchGB)
        self.SPButton.setObjectName(u"SPButton")
        sizePolicy4.setHeightForWidth(self.SPButton.sizePolicy().hasHeightForWidth())
        self.SPButton.setSizePolicy(sizePolicy4)
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
        sizePolicy4.setHeightForWidth(self.countingButton.sizePolicy().hasHeightForWidth())
        self.countingButton.setSizePolicy(sizePolicy4)
        self.countingButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.countingButton)

        self.toZeroButton = QPushButton(self.stopwatchGB)
        self.toZeroButton.setObjectName(u"toZeroButton")
        sizePolicy4.setHeightForWidth(self.toZeroButton.sizePolicy().hasHeightForWidth())
        self.toZeroButton.setSizePolicy(sizePolicy4)

        self.horizontalLayout_2.addWidget(self.toZeroButton)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)


        self.verticalLayout_7.addWidget(self.stopwatchGB)

        self.fsButton = QPushButton(Form)
        self.fsButton.setObjectName(u"fsButton")

        self.verticalLayout_7.addWidget(self.fsButton)

        self.windowSettingGB = QGroupBox(Form)
        self.windowSettingGB.setObjectName(u"windowSettingGB")
        sizePolicy4.setHeightForWidth(self.windowSettingGB.sizePolicy().hasHeightForWidth())
        self.windowSettingGB.setSizePolicy(sizePolicy4)
        self.horizontalLayout_4 = QHBoxLayout(self.windowSettingGB)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.fullscreenButton = QPushButton(self.windowSettingGB)
        self.fullscreenButton.setObjectName(u"fullscreenButton")
        self.fullscreenButton.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.fullscreenButton)

        self.activateFWButton = QPushButton(self.windowSettingGB)
        self.activateFWButton.setObjectName(u"activateFWButton")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.activateFWButton.sizePolicy().hasHeightForWidth())
        self.activateFWButton.setSizePolicy(sizePolicy8)

        self.horizontalLayout_4.addWidget(self.activateFWButton)


        self.verticalLayout_7.addWidget(self.windowSettingGB)


        self.horizontalLayout_5.addLayout(self.verticalLayout_7)

        QWidget.setTabOrder(self.pushButton, self.hourDial)
        QWidget.setTabOrder(self.hourDial, self.minDial)
        QWidget.setTabOrder(self.minDial, self.secDial)
        QWidget.setTabOrder(self.secDial, self.swDial)
        QWidget.setTabOrder(self.swDial, self.countsBrowser)
        QWidget.setTabOrder(self.countsBrowser, self.SPButton)
        QWidget.setTabOrder(self.SPButton, self.countingButton)
        QWidget.setTabOrder(self.countingButton, self.toZeroButton)
        QWidget.setTabOrder(self.toZeroButton, self.fullscreenButton)
        QWidget.setTabOrder(self.fullscreenButton, self.activateFWButton)
        QWidget.setTabOrder(self.activateFWButton, self.classesBrowser)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.countdownToCEE.setTitle(QCoreApplication.translate("Form", u"\u8ddd\u79bb\u9ad8\u8003", None))
        self.CEETime.setText(QCoreApplication.translate("Form", u"1000 \u5929", None))
        self.classesGB.setTitle(QCoreApplication.translate("Form", u"\u8bfe\u7a0b", None))
        self.classGB.setTitle(QCoreApplication.translate("Form", u"\u8bfe\u5802", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u4e0a\u8bfe\uff01", None))
        self.timeGB.setTitle(QCoreApplication.translate("Form", u"\u65f6\u95f4", None))
        self.label.setText(QCoreApplication.translate("Form", u"[TIME]", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"[DATE]", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u5929\u6c14", None))
        self.weatherLogo.setText("")
        self.weatherInfo.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u66f4\u591a\u4fe1\u606f\u2026", None))
        self.stopwatchGB.setTitle(QCoreApplication.translate("Form", u"\u79d2\u8868", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"[TIME]", None))
        self.SPButton.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb/\u6682\u505c", None))
        self.countingButton.setText(QCoreApplication.translate("Form", u"\u8ba1\u6b21", None))
        self.toZeroButton.setText(QCoreApplication.translate("Form", u"\u5f52\u96f6", None))
#if QT_CONFIG(tooltip)
        self.fsButton.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.fsButton.setText(QCoreApplication.translate("Form", u"\u6478  \u9c7c  \u5e7f  \u573a", None))
        self.windowSettingGB.setTitle(QCoreApplication.translate("Form", u"\u7a97\u53e3", None))
        self.fullscreenButton.setText(QCoreApplication.translate("Form", u"\u5168\u5c4f", None))
        self.activateFWButton.setText(QCoreApplication.translate("Form", u"\u542f\u52a8\u6d6e\u7a97", None))
    # retranslateUi

