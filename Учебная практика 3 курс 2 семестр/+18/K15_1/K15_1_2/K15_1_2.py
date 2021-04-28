#Выполнил: Кузнецов Матвей
#Группа: П2-18
'''
К15_1. Техника работы с модулями

Задание 2. Контейнерные типы данных модуля collections.
Класс Counter() модуля collections в Python.
https://docs-python.ru/standart-library/modul-collections-python/klass-counter-modulja-collections/
'''

import collections
import re
cnt = collections.Counter(a=4, b=2, c=0, d=-2)
print(cnt)
print(*cnt.elements())

ct = collections.Counter("abbbaaaccacccascd")
s = set(ct)
print(ct.most_common(len(s)))

cnt1 = collections.Counter(a=3, b=6, c=6, d=5)
cnt1.subtract(cnt) # вычитает элементы текущего счетчика
print(cnt1)

cnt1.update(cnt) # складывает элементы текущего счетчика
print(cnt1)
print()

print("#print(cnt + cnt1)")
print(cnt + cnt1) #Сложить два счетчика
print("#print(cnt - cnt1)")
print(cnt - cnt1) #Вычитание счетчиков
print("#print(cnt & cnt1)")
print(cnt & cnt1) #Пересечение счетчиков
print("#print(cnt | cnt1)")
print(cnt | cnt1) #Объединение счётчиков
print()

print(cnt.items())
print(cnt.values())
cnt.clear()

string = ""
c = collections.Counter()
with open("text1.txt", "r") as file:
    for i in file:
        string += i

c = collections.Counter(string).most_common(len(string))
print(c)

cn = collections.Counter()
with open("text1.txt", "r") as file:
    for i in file:
        words = re.findall(r'\w+', file.read())   #findall используется для поиска всех непересекающихся совпадений в шаблоне

cn = collections.Counter(words).most_common(len(words))
print(cn)
