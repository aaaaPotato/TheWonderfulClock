from PySide6 import QtCore, QtGui, QtWidgets
import weatherWindowUI
import requests
class weatherWindow(weatherWindowUI.Ui_Form, QtWidgets.QWidget):
    def __init__(self, parent=None):
        self.sugs = ["mood","sport","ac","allergy","comfort","dressing","flu","uv"]
        self.sug1 = ["心情","运动","空调","过敏","舒适度","穿衣","感冒","紫外线"]
        self.sugmd = """"""
        super(weatherWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("天气")
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.updateWeather)
        self.timer.start(60000)  # Update every minute
        self.updateWeather()
        self.parentWidget = parent
    def updateWeather(self):
        try:
            response = requests.get("https://api.seniverse.com/v3/weather/now.json?key=SQ-vSmTyW07Gbnv0H&location=chongqing&language=zh-Hans&unit=c")
            data = response.json()
            if 'results' in data and len(data['results']) > 0:
                weather = data['results'][0]['now']
                self.twInfo.setText(f"{weather['text']}  {weather['temperature']}°C")
                self.twLogo.setPixmap(QtGui.QPixmap(f"weatherLogo/{weather['code']}@2x.png"))
            response = requests.get("https://api.seniverse.com/v3/weather/daily.json?key=SQ-vSmTyW07Gbnv0H&location=chongqing&language=zh-Hans&unit=c&start=0&days=3")
            data = response.json()
            if 'results' in data and len(data['results']) > 0:
                weather = data['results'][0]['daily']
                self.fwInfo.setText(f"{weather[0]['text_day']}转{weather[0]['text_night']}  {weather[0]['high']}°C~ {weather[0]['low']}°C\n{weather[0]['rainfall']}mm的降雨 {weather[0]['wind_direction']}风{weather[0]['wind_scale']}级")
                self.fwInfo_2.setText(f"{weather[1]['text_day']}转{weather[1]['text_night']}  {weather[1]['high']}°C~ {weather[1]['low']}°C\n{weather[1]['rainfall']}mm的降雨 {weather[1]['wind_direction']}风{weather[1]['wind_scale']}级")
                self.fwInfo_3.setText(f"{weather[2]['text_day']}转{weather[2]['text_night']}  {weather[2]['high']}°C~ {weather[2]['low']}°C\n{weather[2]['rainfall']}mm的降雨 {weather[2]['wind_direction']}风{weather[2]['wind_scale']}级")
                self.fwdLogo.setPixmap(QtGui.QPixmap(f"weatherLogo/{weather[0]['code_day']}@2x.png"))
                self.fwdLogo_2.setPixmap(QtGui.QPixmap(f"weatherLogo/{weather[1]['code_day']}@2x.png"))
                self.fwdLogo_3.setPixmap(QtGui.QPixmap(f"weatherLogo/{weather[2]['code_day']}@2x.png"))
                self.fwnLogo.setPixmap(QtGui.QPixmap(f"weatherLogo/{weather[0]['code_night']}@2x.png"))
                self.fwnLogo_2.setPixmap(QtGui.QPixmap(f"weatherLogo/{weather[1]['code_night']}@2x.png"))
                self.fwnLogo_3.setPixmap(QtGui.QPixmap(f"weatherLogo/{weather[2]['code_night']}@2x.png"))
            response = requests.get("https://api.seniverse.com/v3/life/suggestion.json?key=SQ-vSmTyW07Gbnv0H&location=chongqing&language=zh-Hans&days=1")
            data = response.json()
            if 'results' in data and len(data['results']) > 0:
                suggestions = data['results'][0]['suggestion'][0]
                self.sugmd = """|建议|简要|详情|\n|---|---|---|\n"""
                for i in self.sugs:
                    self.sugmd += f"|{self.sug1[self.sugs.index(i)]}|{suggestions[i]['brief']}|{suggestions[i]['details']}|\n"
                self.textBrowser.setMarkdown(self.sugmd)
        except Exception as e:
            self.twInfo.setText("天气信息获取失败")
            self.fwInfo.setText("天气信息获取失败")
            self.fwInfo_2.setText("天气信息获取失败")
            self.fwInfo_3.setText("天气信息获取失败")
            print(f"Error fetching weather data: {e}")