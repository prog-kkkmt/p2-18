'''
В каждой строке файла хранится информация о пунктах и их координатах
относительно некоторого центра.
Требуется
1. Прочесть файл в список кортежей
2. Найти диаметр множества точек, то есть расстояние между наиболее удалёнными точками.
Указать наиболее удалённые пары
3. Сформировать список пар городов, имеющих одинаковое расстояние до центра
4. Отсортировать список одним из методов, реализованных в предыдущих работах
Результаты вывести на экран

Пример входного файла
Москва 0 0
Ивантеевка 20 15
Щёлково 10 30
Пушкино 15 5
'''
from math import sqrt
def abc(s:str):
    try:
        int(s)
        return True
    except ValueError:
        return False

def distance(x1, y1, x2, y2):
    dx = x1 - x2 if x1 > x2 else x2 - x1
    dy = y1 - y2 if y1 > y2 else y2 - y1
    return sqrt(dx * dx + dy * dy)

def distancee(x1,y1):
    return sqrt(x1*x1+y1*y1)


# 1 Прочесть файл в список кортежей
li= {}
f = open('goroda.txt', encoding='utf-8')
cities = list(tuple(int(item.replace('\n', '')) if abc(item.replace('\n', ''))
                    else item.replace('\n', '') for item in line.split(' ')) for line in f)
# 2 Найти диаметр множества точек, то есть расстояние между наиболее удалёнными точками.
# Указать наиболее удалённые пары
for i in range(0,len(cities)-1,+1):
    x1=cities[i][1]
    y1=cities[i][2]
    for j in range(i+1, len(cities), +1):
        x2=cities[j][1]
        y2=cities[j][2]
        if li.get(distance(x1, y1, x2, y2)) is None:
            li[distance(x1, y1, x2, y2)] = cities[i][0] + "-" + cities[j][0]
        else:
            li[distance(x1, y1, x2, y2)] += ' '+cities[i][0]+"-"+cities[j][0]
max = 0
for k in li.keys():
    if max < k:
        max = k
for l in li.keys():
    if max == l:
        print(li[l])
# 3 Сформировать список пар городов, имеющих одинаковое расстояние до центра
lii={}
for i in range(0,len(cities),+1):
    x1=cities[i][1]
    y1=cities[i][2]
    if lii.get(distancee(x1, y1)) is None:
        lii[distancee(x1, y1)] = cities[i][0]
    else:
        lii[distancee(x1, y1)] += ' '+cities[i][0]
print(lii.values())
# 4 Отсортировать список одним из методов, реализованных в предыдущих работах
# Результаты вывести на экран
liii=[]
for j in range(0,len(cities),+1):
    max = 0
    for i in range(0,len(cities),+1):
        x1=cities[i][1]
        y1=cities[i][2]
        if distancee(x1, y1)>max and liii.count(distancee(x1, y1))== 0:
            max=distancee(x1, y1)
    if liii.count(max)== 0:
        liii.append(max)
print("От большего к меньшему",liii)
