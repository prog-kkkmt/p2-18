#Выполнил Щепкин П2-18
#Импортирование библиотек
from PyQt5 import QtCore, QtGui, QtWidgets
class WinGui(object):
    def Win2(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        #Размер окна
        MainWindow.resize(470, 290)
        self.Widget = QtWidgets.QWidget(MainWindow)
        self.Widget.setObjectName("Widget")
        self.Pb = QtWidgets.QPushButton(self.Widget)
        #Размер кнопки
        self.Pb.setGeometry(QtCore.QRect(30, 90, 150, 50))
        self.Pb.setObjectName("PushButton")
        self.Text = QtWidgets.QTextEdit(self.Widget)
        #Размер окна вывода 
        self.Text.setGeometry(QtCore.QRect(200, 40, 220, 180))
        self.Text.setObjectName("TextEdit")
        MainWindow.setCentralWidget(self.Widget)
        self.WinText(MainWindow)
    def WinText(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        #Название окна
        MainWindow.setWindowTitle(_translate("MainWindow", "KeyGeneragion"))
        #Название кнопки
        self.Pb.setText(_translate("MainWindow", "Сгенерировать ключ"))
