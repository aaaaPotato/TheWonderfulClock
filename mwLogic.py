from PySide6 import QtCore, QtGui, QtWidgets
from fwLogic import floatingWindow
from wwLogic import weatherWindow
import mainWindowUI
import time,datetime,json,requests
class window(mainWindowUI.Ui_Form, QtWidgets.QWidget):
    def __init__(self):
        self.ptime = 2400
        self.pdtime = 0
        self.counts = 0
        self.weekdays = ["time","Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        self.classesMd = """"""
        self.CEETime1 = datetime.date(2028,6,6)
        super(window,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("WonderfulClock")
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.timer = QtCore.QTimer()
        self.timer.start(100)
        self.timer.timeout.connect(self.updateTime)
        self.classTimer = QtCore.QTimer()
        self.pushButton.clicked.connect(self.classTimerStart)
        self.passedTime.setRange(0, 2400)
        self.passedTime.setValue(2400)
        self.swTimer = QtCore.QTimer()
        self.now = time.time()
        self.beginTime = time.time()
        self.toZeroButton.setEnabled(True)
        self.countingButton.setEnabled(False)
        self.swTimer.timeout.connect(self.updateSWTime)
        self.swTimer.start(15)
        self.SPButton.clicked.connect(self.beginSW)
        self.toZeroButton.clicked.connect(self.toZero)
        self.countingButton.clicked.connect(self.countOne)
        self.label_3.setText("0:0.0")
        self.udCEETime = QtCore.QTimer()
        self.udCEETime.timeout.connect(self.updateCEETime)
        self.udCEETime.start(1000*60*60)
        self.now1 = datetime.date.today()
        self.CEETime.setText(str(self.CEETime1.__sub__(self.now1).days)+" 天")
        self.clsTimer = QtCore.QTimer()
        self.clsTimer.timeout.connect(self.updateClasses)
        with open("classes.json","r",encoding="utf-8") as f:
            self.classes = json.load(f)
        self.clsTimer.start(1000*60*60)
        self.updateClasses()
        self.activateFWButton.clicked.connect(self.showFloating)
        self.flsTimer = QtCore.QTimer()
        self.flsTimer.timeout.connect(self.checkFullscreen)
        self.flsTimer.start(100)
        self.weatherTimer = QtCore.QTimer()
        self.weatherTimer.timeout.connect(self.updateWeather)
        self.weatherTimer.start(1000*60*60)
        self.updateWeather()
        self.pushButton_2.clicked.connect(self.showWeather)
    def updateTime(self):
        self.label.setText(time.strftime("%H:%M:%S"))
        self.label_2.setText(time.strftime("%Y-%m-%d %a"))
        self.hourDial.setValue(int(time.strftime("%H"))+12)
        self.minDial.setValue(int(time.strftime("%M"))+30)
        self.secDial.setValue(int(time.strftime("%S"))+30)
    def updateClassTime(self):
        self.passedTime.setValue(self.ptime)
        self.ptime += 3
        if self.ptime >= 2400:
            self.classTimer.stop()
            self.pushButton.setEnabled(True)
    def classTimerStart(self):
        self.pushButton.setEnabled(False)
        self.ptime = 0
        self.classTimer.timeout.connect(self.updateClassTime)
        self.classTimer.start(3000)
    def updateSWTime(self):
        self.swDial.setValue(self.pdtime)
        if self.SPButton.isChecked():
            self.toZeroButton.setEnabled(False)
            self.countingButton.setEnabled(True)
            self.now = time.time()
            self.pdtime += self.now - self.beginTime
            self.strpdtime = str(int(self.pdtime//60))+":"+str(int(self.pdtime%60))+"."+str(round((self.pdtime*100)%100))
            self.label_3.setText(self.strpdtime)
            self.beginTime = self.now
        else:
            self.swTimer.stop()
            self.toZeroButton.setEnabled(True)
            self.countingButton.setEnabled(False)
    def beginSW(self):
        self.swTimer.start(15)
        self.beginTime = time.time()
    def toZero(self):
        self.pdtime = 0
        self.strpdtime = "0:0.0"
        self.label_3.setText(self.strpdtime)
        self.countsBrowser.clear()
        self.swDial.setValue(0)
        self.counts = 0
    def countOne(self):
        self.counts += 1
        self.countsBrowser.append("["+str(self.counts)+"]  "+self.strpdtime)
    def updateCEETime(self):
        self.now1 = datetime.date.today()
        self.CEETime.setText(str(self.CEETime1.__sub__(self.now1).days+" 天"))
    def updateClasses(self):
        self.classesBrowser.clear()
        self.classesMd = f"""|时间|{time.strftime("%a")}|
                             |---|---|"""
        for i in range(3):
            self.classesMd += f"\n|{self.classes[0][i]}|{self.classes[self.weekdays.index(time.strftime("%a"))][i]}|"
        self.classesBrowser.setMarkdown(self.classesMd)
    def showFloating(self):
        self.fullscreenButton.setChecked(False)
        self.floating = floatingWindow(parent=self)
        self.floating.show()
        self.hide()
    def checkFullscreen(self):
        if self.fullscreenButton.isChecked():
            self.showFullScreen()
            self.activateFWButton.setEnabled(False)
        else:
            self.activateFWButton.setEnabled(True)
            if self.isFullScreen():
                self.showNormal()
    def updateWeather(self):
        try:
            response = requests.get("https://api.seniverse.com/v3/weather/now.json?key=SQ-vSmTyW07Gbnv0H&location=chongqing&language=zh-Hans&unit=c")
            data = response.json()
            if data and 'results' in data and len(data['results']) > 0:
                weather = data['results'][0]['now']
                temperature = weather['temperature']
                text = weather['text']
                index = weather['code']
                self.weatherInfo.setText(f"{text}  {temperature}°C")
                self.weatherLogo.setPixmap(QtGui.QPixmap(f"weatherLogo/{index}@2x.png"))
        except Exception as e:
            self.weatherInfo.setText("天气信息获取失败")
            print(f"Error fetching weather data: {e}")
    def showWeather(self):
        self.fullscreenButton.setChecked(False)
        self.weatherW = weatherWindow(parent=self)
        self.weatherW.show()