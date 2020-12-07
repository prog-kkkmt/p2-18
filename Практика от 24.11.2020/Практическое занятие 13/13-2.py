#Выполнил: Короленко Иван Романович
#Студент: ККМТ П2-18

#Задание 1. Класс namedtuple() модуля collections в Python.

'''
Класс namedtuple() модуля collections возвращает новый подкласс кортежа с именем typename.
Новый подкласс используется для создания объектов, похожих на кортежи, которые имеют индексируемые и итерируемые поля, доступные для поиска по атрибутам.
Экземпляры подкласса также имеют полезную строку документации с typename и field_names, а так же метод __repr__(), который перечисляет содержимое кортежа в формате name=value.
Имена полей field_names представляют собой последовательность строк, таких как ['x', 'y'].
В качестве альтернативы, field_names может быть одной строкой, в которой каждое имя поля разделено пробелами и/или запятыми, например, 'x y' или 'x, y'.
Для имен полей (элементов кортежа) может использоваться любой действительный идентификатор Python, за исключением имен, начинающихся с подчеркивания.
Допустимые идентификаторы состоят из букв, цифр и символов подчеркивания, но не начинаются с цифры или символа подчеркивания и не могут быть ключевыми словами, такими как class, for, return, global, pass и т. д.
Если аргумент rename=True, то недопустимые имена полей автоматически заменяются позиционными именами.
Например ['abc', 'def', 'ghi', 'abc'] преобразуется в ['abc', '_1', 'ghi', '_3'], исключая ключевое слово def и повторяющееся имя поля abc.
Значения аргумента defaults могут быть None или итерируемой последовательностью.
Поскольку аргумента со значением по умолчанию должны идти после любых обязательных аргументов, то значения по умолчанию будут применяются к самым правым параметрам. Например, если имена полей именованного кортежа это ['x', 'y', 'z'], а значения по умолчанию (1, 2), то тогда x будет обязательным аргументом, y по умолчанию будет 1, а z будет 2.
Если аргумент module определен, то атрибуту именованного кортежа __module__ присваивается значение module.
Экземпляры именованных кортежей не имеют словарей, поэтому они легковесны и требуют не больше памяти, чем обычные кортежи.
'''

# Параметры:
# typename - строка, имя именованного кортежа,
# field_names - последовательность строк, имена элементов кортежа,
# rename - bool, авто-переименование повторяющихся имен элементов,
# defaults = None - итерируемая последовательность, значения по умолчанию имен кортежа,
# module = None - атрибут __module__ именованного кортежа.

# Простой пример
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(11, y=22)
# можно обращаться по индексу
# как к обычному кортежу
p[0] + p[1]
# 33

# распаковать как обычный кортеж
x, y = p
x, y
# (11, 22)

# поля также доступны по названию
p.x + p.y
# 33

# человеко-читаемый __repr__
print(p)
# Point(x=11, y=22)

# Именованные кортежи особенно полезны для присвоения имен полей в результате кортежей, возвращаемых модулями csv или sqlite3:

from collections import namedtuple

EmployeeRecord = namedtuple('EmployeeRecord', 'name, age, \title, department, paygrade')

import csv
for emp in map(EmployeeRecord._make, csv.reader(open("employees.csv", "rb"))):
    print(emp.name, emp.title)

import sqlite3
conn = sqlite3.connect('/companydata')
cursor = conn.cursor()
cursor.execute('SELECT name, age, title, department, paygrade FROM employees')
for emp in map(EmployeeRecord._make, cursor.fetchall()):
    print(emp.name, emp.title)

# Поскольку именованный кортеж является обычным классом Python, его легко добавить или изменить с помощью подкласса.
#Вот как добавить вычисляемое поле и формат печати фиксированной ширины:

from collections import namedtuple

class Point(namedtuple('Point', ['x', 'y'])):
    __slots__ = ()

    @property
    def hypot(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __str__(self):
        return 'Point: x=%6.3f  y=%6.3f  hypot=%6.3f' % (self.x, self.y, self.hypot)

for p in Point(3, 4), Point(14, 5/7):
    print(p)

# Point: x=3.000  y=4.000  hypot=5.000
# Point: x=14.000  y=0.714  hypot=14.018

'''
Примеры
'''

from collections import Counter

counter_one = Counter('superfluous')

# Counter({'u': 3, 's': 2, 'e': 1, 'l': 1, 'f': 1, 'o': 1, 'r': 1, 'p': 1})
print(counter_one)

counter_two = Counter('super')
counter_one.subtract(counter_two)

print(counter_one)
# Counter({'u': 2, 'l': 1, 'f': 1, 'o': 1, 's': 1, 'e': 0, 'r': 0, 'p': 0})

sentence = "The red for jumped over the fence and ran to the zoo for food"
words = sentence.split(' ')

reg_dict = {}
for word in words:
    if word in reg_dict:
        reg_dict[word] += 1
    else:
        reg_dict[word] = 1

print(reg_dict)
