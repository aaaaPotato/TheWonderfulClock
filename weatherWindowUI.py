# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'weatherWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QSizePolicy, QTextBrowser, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(221, 440)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.twLogo = QLabel(self.groupBox)
        self.twLogo.setObjectName(u"twLogo")
        self.twLogo.setPixmap(QPixmap(u"weatherLogo/0@2x.png"))

        self.horizontalLayout.addWidget(self.twLogo)

        self.twInfo = QLabel(self.groupBox)
        self.twInfo.setObjectName(u"twInfo")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.twInfo.setFont(font)

        self.horizontalLayout.addWidget(self.twInfo)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout = QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.fwdLogo = QLabel(self.groupBox_2)
        self.fwdLogo.setObjectName(u"fwdLogo")
        self.fwdLogo.setPixmap(QPixmap(u"weatherLogo/5@2x.png"))

        self.horizontalLayout_2.addWidget(self.fwdLogo)

        self.fwnLogo = QLabel(self.groupBox_2)
        self.fwnLogo.setObjectName(u"fwnLogo")
        self.fwnLogo.setPixmap(QPixmap(u"weatherLogo/18@2x.png"))

        self.horizontalLayout_2.addWidget(self.fwnLogo)

        self.fwInfo = QLabel(self.groupBox_2)
        self.fwInfo.setObjectName(u"fwInfo")

        self.horizontalLayout_2.addWidget(self.fwInfo)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.fwdLogo_2 = QLabel(self.groupBox_2)
        self.fwdLogo_2.setObjectName(u"fwdLogo_2")
        self.fwdLogo_2.setPixmap(QPixmap(u"weatherLogo/5@2x.png"))

        self.horizontalLayout_3.addWidget(self.fwdLogo_2)

        self.fwnLogo_2 = QLabel(self.groupBox_2)
        self.fwnLogo_2.setObjectName(u"fwnLogo_2")
        self.fwnLogo_2.setPixmap(QPixmap(u"weatherLogo/18@2x.png"))

        self.horizontalLayout_3.addWidget(self.fwnLogo_2)

        self.fwInfo_2 = QLabel(self.groupBox_2)
        self.fwInfo_2.setObjectName(u"fwInfo_2")

        self.horizontalLayout_3.addWidget(self.fwInfo_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.fwdLogo_3 = QLabel(self.groupBox_2)
        self.fwdLogo_3.setObjectName(u"fwdLogo_3")
        self.fwdLogo_3.setPixmap(QPixmap(u"weatherLogo/5@2x.png"))

        self.horizontalLayout_4.addWidget(self.fwdLogo_3)

        self.fwnLogo_3 = QLabel(self.groupBox_2)
        self.fwnLogo_3.setObjectName(u"fwnLogo_3")
        self.fwnLogo_3.setPixmap(QPixmap(u"weatherLogo/18@2x.png"))

        self.horizontalLayout_4.addWidget(self.fwnLogo_3)

        self.fwInfo_3 = QLabel(self.groupBox_2)
        self.fwInfo_3.setObjectName(u"fwInfo_3")

        self.horizontalLayout_4.addWidget(self.fwInfo_3)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.verticalLayout_2.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(Form)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.textBrowser = QTextBrowser(self.groupBox_3)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setLineWrapMode(QTextEdit.LineWrapMode.NoWrap)

        self.verticalLayout_3.addWidget(self.textBrowser)


        self.verticalLayout_2.addWidget(self.groupBox_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u5f53\u65e5\u5929\u6c14", None))
        self.twLogo.setText("")
        self.twInfo.setText(QCoreApplication.translate("Form", u"weatherInfo", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"\u672a\u6765\u5929\u6c14", None))
        self.fwdLogo.setText("")
        self.fwnLogo.setText("")
        self.fwInfo.setText(QCoreApplication.translate("Form", u"0~0\u2103", None))
        self.fwdLogo_2.setText("")
        self.fwnLogo_2.setText("")
        self.fwInfo_2.setText(QCoreApplication.translate("Form", u"0~0\u2103", None))
        self.fwdLogo_3.setText("")
        self.fwnLogo_3.setText("")
        self.fwInfo_3.setText(QCoreApplication.translate("Form", u"0~0\u2103", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"\u751f\u6d3b\u6307\u6570", None))
    # retranslateUi

