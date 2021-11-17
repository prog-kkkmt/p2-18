import sys
'''этот модуль отвечает за определение среды запуска приложения'''
from Design import *
'''импортируем наш разработанный дизайн'''

class MyWin(QtWidgets.QMainWindow):
    '''создаем класс приложения,который наследуется от qMainWindow'''
    def __init__(self):
        '''создаем конструктор для экземпляра'''
        QtWidgets.QWidget.__init__(self)
        '''импортируем все методы библиотеки pyQt'''
        self.ui = Ui_MainWindow()
        '''связываем дизайн с кнопками'''
        self.ui.setupUi(self)
        '''функция отрисовки главного окна'''
        self.ui.pushButton_3.clicked.connect(self.setZero)
        '''назначаем функционал для кнопок...'''
        self.ui.pushButton_4.clicked.connect(self.setSix)
        self.ui.pushButton_8.clicked.connect(self.setFour)
        self.ui.pushButton_9.clicked.connect(self.setFive)
        self.ui.pushButton_10.clicked.connect(self.setEight)
        self.ui.pushButton_6.clicked.connect(self.setThree)
        self.ui.pushButton_11.clicked.connect(self.setSub)
        self.ui.pushButton_13.clicked.connect(self.setTwo)
        self.ui.pushButton_5.clicked.connect(self.setEnter)
        self.ui.pushButton_14.clicked.connect(self.setMult)
        self.ui.pushButton_18.clicked.connect(self.setOne)
        self.ui.pushButton_17.clicked.connect(self.setSeven)
        self.ui.pushButton_16.clicked.connect(self.setNine)
        self.ui.pushButton_15.clicked.connect(self.setDif)
        self.ui.pushButton_7.clicked.connect(self.setAdd)
        self.ui.pushButton_12.clicked.connect(self.setClear)

    def setZero(self):                          
        '''определяем функции...'''
        a = self.ui.lineEdit.text()             
        '''создаем локальную переменную и сохраняем в нее строку из "lineEdit"'''
        self.ui.lineEdit.setText(a + '0')       
        '''к "a" прибавляем '0' и сохраняем в "lineEdit"'''
        
    def setOne(self):
        a = self.ui.lineEdit.text()
        self.ui.lineEdit.setText(a + '1')
        
    def setTwo(self):
        a = self.ui.lineEdit.text()
        self.ui.lineEdit.setText(a + '2')
        
    def setThree(self):
        a = self.ui.lineEdit.text()
        self.ui.lineEdit.setText(a + '3')
        
    def setFour(self):
        a = self.ui.lineEdit.text()
        self.ui.lineEdit.setText(a + '4')
        
    def setFive(self):
        a = self.ui.lineEdit.text()
        self.ui.lineEdit.setText(a + '5')
        
    def setSix(self):
        a = self.ui.lineEdit.text()
        self.ui.lineEdit.setText(a + '6')
        
    def setSeven(self):
        a = self.ui.lineEdit.text()
        self.ui.lineEdit.setText(a + '7')
        
    def setEight(self):
        a = self.ui.lineEdit.text()
        self.ui.lineEdit.setText(a + '8')
        
    def setNine(self):
        a = self.ui.lineEdit.text()
        self.ui.lineEdit.setText(a + '9')
        
    def setSub(self):
        a = self.ui.lineEdit.text()
        self.ui.lineEdit.setText(a + '-')
        
    def setMult(self):
        a = self.ui.lineEdit.text()
        self.ui.lineEdit.setText(a + '*')
        
    def setDif(self):
        a = self.ui.lineEdit.text()
        self.ui.lineEdit.setText(a + '/')
        
    def setAdd(self):
        a = self.ui.lineEdit.text()
        self.ui.lineEdit.setText(a + '+')
        
    def setClear(self):
        self.ui.lineEdit.setText('')

    def setEnter(self):
        a = self.ui.lineEdit.text()
        b = str(eval(a))
        '''функция "eval" преобразует строку в математическую операцию'''
        self.ui.lineEdit.setText(b)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    '''определение в среде виндовс'''
    myapp = MyWin()
    '''создание экземпляра окна'''
    myapp.show()
    '''отрисовка окна на экране'''
    sys.exit(app.exec_())
    '''устанавливает параметр завершения работы окна'''
