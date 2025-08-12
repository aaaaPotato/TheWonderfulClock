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
from PySide6.QtWidgets import (QApplication, QDial, QHBoxLayout, QLabel,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setEnabled(True)
        Form.resize(505, 348)
        Form.setMouseTracking(False)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"\u7b49\u7ebf"])
        font.setPointSize(72)
        self.label.setFont(font)
        self.label.setCursor(QCursor(Qt.CursorShape.ForbiddenCursor))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.hourDial = QDial(Form)
        self.hourDial.setObjectName(u"hourDial")
        self.hourDial.setEnabled(False)
        self.hourDial.setCursor(QCursor(Qt.CursorShape.ForbiddenCursor))
        self.hourDial.setMaximum(24)
        self.hourDial.setPageStep(6)
        self.hourDial.setWrapping(True)
        self.hourDial.setNotchTarget(3.699999999999999)
        self.hourDial.setNotchesVisible(True)

        self.horizontalLayout.addWidget(self.hourDial)

        self.minDial = QDial(Form)
        self.minDial.setObjectName(u"minDial")
        self.minDial.setEnabled(False)
        self.minDial.setCursor(QCursor(Qt.CursorShape.ForbiddenCursor))
        self.minDial.setMaximum(60)
        self.minDial.setPageStep(5)
        self.minDial.setWrapping(True)
        self.minDial.setNotchesVisible(True)

        self.horizontalLayout.addWidget(self.minDial)

        self.secDial = QDial(Form)
        self.secDial.setObjectName(u"secDial")
        self.secDial.setEnabled(False)
        self.secDial.setCursor(QCursor(Qt.CursorShape.ForbiddenCursor))
        self.secDial.setMaximum(60)
        self.secDial.setPageStep(5)
        self.secDial.setWrapping(True)
        self.secDial.setNotchesVisible(True)

        self.horizontalLayout.addWidget(self.secDial)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"[TIME]", None))
    # retranslateUi

