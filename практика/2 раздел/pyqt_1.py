#Выполнил Толоконников А.М., Джабраилов Т. А.                       
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QSize
import random



# Наследуемся от QMainWindow
class MainWindow(QMainWindow):
    # Создаём диалоговое окно, которое открывается при нажатии на кнопку
    def dialog(self, lineEdit, strList, secretList):
        mbox = QMessageBox() # Создаём диалоговое окно
        mbox.setWindowTitle('Окно')
        # Условия вывода определённого текста в окне
        if(lineEdit.text() in strList):
            mbox.setText(lineEdit.text() + " krut!")
        elif(lineEdit.text() in secretList):
            mbox.setText(lineEdit.text() + "\nЭто правда")
        else:
            mbox.setText("prosto text")
            mbox.setDetailedText("Наберите одно из этих слов\n'Python', 'PyQt5', 'Qt', 'Django', 'QML'")
        mbox.exec()

    	# Переопределяем конструктор класса
    	def __init__(self):
        # Обязательно нужно вызвать метод супер класса
        QMainWindow.__init__(self)

 
        self.setWindowTitle("Проверка автодополнения")  # Устанавливаем заголо-вок окна
        central_widget = QWidget(self)  # Создаём центральный виджет
        self.setCentralWidget(central_widget)  # Устанавливаем центральный ви-джет

        grid_layout = QGridLayout()  # Создаём QGridLayout
        central_widget.setLayout(grid_layout)  # Устанавливаем данное размещение в #центральный виджет


        grid_layout.addWidget(QLabel("Проверка автодополнения", self), 0, 0)

        # Создаём поле ввода
        lineEdit = QLineEdit(self)
        strList = ['Python', 'PyQt5', 'Qt', 'Django', 'QML']  # Создаём список слов
        secretList = ['Хочу домой', 'Я сделал домашку', 'ККМТ - сила'] # Создаём секретный список
        rand = random.randint(1,10)
        # Создаём QCompleter, в который устанавливаем список, а также указатель на родителя
        # С вероятностью 50% в QCompleter может добавиться секретный список
        if(rand % 2 == 0):
            completer = QCompleter(strList, lineEdit)
        else:
            completer = QCompleter(strList + secretList, lineEdit)
        lineEdit.setCompleter(completer)  # Устанавливает QCompleter в поле вво-да
        grid_layout.addWidget(lineEdit, 0, 1)  # Добавляем поле ввода в сетку
        qb = QPushButton("Submit") # Создаём кнопку
        # Создаём действие для кнопки
        qb.clicked.connect(lambda : self.dialog(lineEdit, strList, secretList))
        grid_layout.addWidget(qb, 0, 2)

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec())
