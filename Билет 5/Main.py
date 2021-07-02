import sqlite3

class main: # Создаем класс
    def fun(): # Создаем метод
        conn = sqlite3.connect('Table') # Открываем db файл
        curs = conn.cursor()
        # Сортируем базу
        *grid, = curs.execute("""SELECT *
                                 FROM Размещение""")
        return grid

mas = main.fun() # Записываем отсортированные базы в списки
copy = []
for i in mas:
    copy.append(i[4])
print(copy.count(0))
