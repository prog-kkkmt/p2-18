#Выполнил: Зайцев Никита
#Группа: П2-18

'''
К15_2. Техника работы с модулями

Задание 1. Контейнерные типы данных модуля collections.
https://docs-python.ru/standart-library/modul-collections-python/
Класс defaultdict() модуля collections в Python.
https://docs-python.ru/standart-library/modul-collections-python/klass-defaultdict-modulja-collections/
'''

from collections import defaultdict
import random

print("1.--------------")
lst = [("Ben", 89001234050), ("Alice", 210-220), ("Ben", 70504321009), ("Alice", 404-502), ("Nick", 16507811251),
       ("Robert", 51234047129), ("Alice", 894-455), ("Alice", 439-495)]
d = defaultdict(list)
for i, elem in lst:
    d[i].append(elem)

print(d.items())
print()


print("2.--------------")
lst_number = [('a', 1), ('b', 2), ('c', 3), ('d', 4) , ('e', 5) , ('f', 6), ('a', 2), ('a', 3)]
d_slov = {}
for i, elem in lst_number:
    d_slov.setdefault(i, []).append(elem**2)

print(sorted(d_slov.items()))
print()


print("3.--------------")
l = {}
for i, elem in lst:
    n = random.randint(1, 100)
    l.setdefault(i, []).append(n)

print(l)
print()


print("4.--------------")
string = "Hello world"
d = defaultdict(int)
for k in string:
    d[k] -= 1

print(d)
print()


print("5.--------------")
lst = ["qwertyui", "asdfghjkl", "zxcvbnm", "q"]
d = defaultdict(int)
for i in lst:
    d[i] += len(i)
print(d.items())
print()


print("6.--------------")
lst = [("Ben", 89001234050), ("Alice", 210-220), ("Ben", 70504321009), ("Alice", 404-502), ("Nick", 16507811251),
       ("Robert", 51234047129), ("Alice", 894-455), ("Alice", 439-495)]
d = defaultdict(set)
index = 0
for i, elem in lst:
    if (index % 2 == 0):
        d[i].add(elem)
    index += 1
print(d.items())
print()


print("7.--------------")
for elem in lst:
    print(elem)
print()


print("8.--------------")
for i, elem in lst:
	print(i, elem)
print()


