#Выполнил Щепкин П2-18
#Импорт библиотек
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

import random
import string
import sys

import gui
class GenKey(QMainWindow, gui.WinGui):
    def __init__(self):
        super().__init__()
        self.Win2(self)
        self.Pb.clicked.connect(self.button)
#Создание функциий, которые генерируют до 10 символов с использованием цифр и букв верхнего регистра.  
    def Random(self, RmSize = 6, chars = string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for x in range(RmSize))
    def button(self):
        self.Text.append(self.Random(10))
        
if __name__ == '__main__':
    AppMain = QApplication(sys.argv)
    window = GenKey()
    window.show()
    AppMain.exec()



