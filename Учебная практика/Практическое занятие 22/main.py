# Выполниили: Бурлаев Захар, Воронцов Александр

"""
Данная программа создает приложение с графическим интерфейсом, приложение предоставляет возможность выбрать папку и просмотреть все файлы находящиеся в ней.
"""

from PyQt5 import QtWidgets
import sys # sys нужен для передачи argv в QApplication
import os
import app1 # Это наш конвертированный файл дизайна

class ExampleApp(QtWidgets.QMainWindow, app1.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self) # Это нужно для инициализации нашего дизайна
        self.pushButton.clicked.connect(self.browse_folder)# Выполнить функцию browse_folder при нажатии кнопки
        
    def browse_folder(self):
        self.listWidget.clear() # На случай, если в списке уже есть элементы
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку")

        if directory: # не продолжать выполнение, если пользователь не выбрал директорию
            for file_name in os.listdir(directory): # для каждого файла в директории
                self.listWidget.addItem(file_name) # добавить файл в listWidget

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp() # Создаём объект класса ExampleApp
    window.show() # Показываем окно
    app.exec_() # запускаем приложение

if __name__ == '__main__':
    main()
