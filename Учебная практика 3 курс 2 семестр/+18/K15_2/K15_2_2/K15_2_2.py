#Выполнил: Кузнецов Матвей
#Группа: П2-18
'''
К15_2. Техника работы с модулями

Задание 2. Контейнерные типы данных модуля collections.
Класс OrderedDict() модуля collections в Python.
https://docs-python.ru/standart-library/modul-collections-python/klass-ordereddict-modulja-collections/
'''

from collections import *

c = Counter()

items = []
n = int(input())
for i in range(n):
	string = input()
	items.append(string)
	for i in items:
		c[i] += 1
print(c)
print()

defdict = defaultdict(list)
for i in range(n+1):
	for j in range(1, i+1):
		defdict[i].append(j)
print(defdict)
print()

d = OrderedDict.fromkeys('abcd')
d.move_to_end('b') # добавляет элемент из строки в конец
print(''.join(d.keys())) #print(d.keys())

d.move_to_end('a')
print(''.join(d.keys()))

d.popitem('a') # удаляем элемент
d.popitem('b')
print(''.join(d.keys()))

d.move_to_end('d', last=True) #переносим d вперёд
print(''.join(d.keys()))
d.move_to_end('d', last=False) #переносим d вперёд
print(''.join(d.keys()))
