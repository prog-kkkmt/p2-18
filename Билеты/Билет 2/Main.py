import sqlite3

class main: # Создаем класс
    def fun(): # Создаем метод
        conn = sqlite3.connect('Table') # Открываем db файл
        curs = conn.cursor()
        # Сортируем базу
        *grid, = curs.execute("""SELECT *
                                 FROM Продажи""")
        conn = sqlite3.connect('Table')
        curs = conn.cursor()
        *grid1, = curs.execute("""SELECT *
                                 FROM Автомобили""")
        return grid, grid1

mas, mas1 = main.fun() # Записываем отсортированные базы в списки

copy = []
summ = 0
for i in range(len(mas)): # Расчет общей суммы
    summ += mas[i][5]
    copy.append(mas[i][1])
print(summ//len(mas), 'руб') # Вывод результата

copy1 = tuple(set(copy)) # Создание копий списков
mas = list(copy1)

for i in range(len(mas)): # Замена эллементов
    mas[mas.index(mas1[i][0])] = mas1[i][1]
    
for i in range(len(copy1)): # Вовод результата
    print(mas[i], copy.count(copy1[i]))
