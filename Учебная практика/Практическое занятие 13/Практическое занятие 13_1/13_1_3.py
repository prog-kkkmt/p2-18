# Гусятинер Л.Б.
# Задание 3
# Выполнили: Воронцов А.А. Бурлаев З.С Щепкин М.В П2-18

"""
 В каждой строке файла хранится информация о пунктах и их координатах
относительно некоторого центра.
Требуется
1. Прочесть файл в список кортежей
2. Найти диаметр множества точек, то есть расстояние между наиболее удалёнными точками. 
Указать наиболее удалённые пары
3. Сформировать список пар городов, имеющих одинаковое расстояние до центра
4. Отсортировать список одним из методов, реализованных в предыдущих работах
Результаты вывести на экран
"""
a = [] 
f = open('zad 3.txt', 'r')
for line in f:
    lst = line.split()
    cort = (lst[0], int(lst[1]), int(lst[2]))
    a.append(cort)    
print(a)

f.close()
