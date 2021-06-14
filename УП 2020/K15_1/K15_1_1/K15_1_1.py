#Выполнил: Безбородов Константин
#Группа: П2-18

'''
К15_1. Техника работы с модулями

Задание 1. Контейнерные типы данных модуля collections.
https://docs-python.ru/standart-library/modul-collections-python/
Класс deque() модуля collections в Python.
https://docs-python.ru/standart-library/modul-collections-python/klass-deque-modulja-collections/
'''

import collections

string = input()
string2 = "234523"
dq = collections.deque(string)

dq.append(string2)
print(dq)

dq.extend('ehwr')
print(dq)

dq.extendleft('ab')
print(dq)
print()


print("dq.index('a', 1) =>", dq.index('a', 1))

print("dq.pop() =>", dq.pop())
print(dq)

print("dq.popleft() =>", dq.popleft())
print(dq)
print()


dq.reverse()
print(dq)

dq.rotate(1)
print(dq)

dq.rotate(2)
print(dq)

dq.rotate(-2)
print(dq)

dq.rotate(-1)
print(dq)
