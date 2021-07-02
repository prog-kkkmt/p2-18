import sqlite3

class main: # Создаем класс
    def fun(): # Создаем метод
        conn = sqlite3.connect('library') # Открываем db файл 
        curs = conn.cursor()
        # Сортируем базу
        *grid, = curs.execute("""SELECT Автор
                                 FROM Книги""")
        conn = sqlite3.connect('library')
        curs = conn.cursor()
        *grid1, = curs.execute("""SELECT Дата_выдачи, Код_книги
                                 FROM Выдача""")
        return grid, grid1

mas1, mas2 = main.fun() # Записываем отсортированные базы в списки
coun = 0
num = *mas1[0],
for i in *mas1,: # Проверка на повторяющиеся эллементы
    a = mas1.count(i)
    if a > coun:
        coun = a
        num = i
print(*num) # Вывод результата

lib = {} # Создаем dict
lib.update({mas2[0][0]: mas2[0][1]})
for i in range(1, len(mas2)): # Цикл для прохода по всему списку
    if mas2[i][0] in lib.keys(): # Проверка на повторяющиеся эллементы
        a = [lib[mas2[i][0]], mas2[i][1]]
        lib.update({mas2[i][0]: a})
    else:
        lib.update({mas2[i][0]: mas2[i][1]})

for i, j in lib.items(): # Вывод результата
    print(i, ' - ', j)
