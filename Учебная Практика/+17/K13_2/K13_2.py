#Выполнил: Зайцев Никита
#Группа: П2-18
'''
К13_2. Техника работы с кортежами

Задание 1. Класс namedtuple() модуля collections в Python.
https://docs-python.ru/standart-library/modul-collections-python/klass-namedtuple-modulja-collections/

По приведённым примерам подготовить свои.
'''


print("Именнованные кортежи")

#Подключаем модуль namedtuple
print("#Подключаем модуль namedtuple")
print("from collections import namedtuple")
from collections import namedtuple
print()
#Создаем именнованый кортеж
print("#Создаем именнованый кортеж")
print("pos = namedtuple('pos', ['x', 'y'])")
pos = namedtuple('pos', ['x', 'y'])
print()

print("#Кортеж с позиционным параметром")
print("p1 = pos(20, 15)")
p1 = pos(20, 15)
print("print(p1)")
print(p1)
print('print("	Сумма: ", p1[0] + p1[1])')
print("	Сумма: ", p1[0] + p1[1])
print()

#Кортеж с именованным параметром
print("#Кортеж с именованным параметром")
print("p2 = pos(x = 30, y = 40)")
p2 = pos(x = 30, y = 40)
print("print(p2)")
print(p2)
print('print("	Сумма: ", p2[0] + p2[1])')
print("	Сумма: ", p2[0] + p2[1])
print()

#Можно распоковать, как обычный кортеж
print("#Можно распоковать, как обычный кортеж")
print("x1, y1 = p1")
x1, y1 = p1
print("print(x1, y1)")
print(x1, y1)

#Поля также доступны по названию
print("#Поля также доступны по названию")
print("#PS: которое мы присвоили в самом начале, т.е")
print("#	pos = namedtuple('pos', ['x', 'y'])")
print("print(p1.x + p1.y)")
print(p1.x + p1.y)
print()

print("#Именованные кортежи поддерживают функцию getattr():")
print("print(getattr(p1, 'x'))")
print(getattr(p1, 'x'))
