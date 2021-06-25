# Выполнил:Степаненко Кирилл
# Группа: П2-18
# Наследование класса
# Вместо того, чтобы начинать с нуля, вы можете создать класс, на основе #уже
# существующего. Укажите родительский класс в круглых скобках после имени #нового
# класса.
# Класс наследник наследует атрибуты своего родительского класса. Вы можете
# использовать эти атрибуты так, как будто они определены в классе #наследнике.
# Он может переопределять элементы данных и методы родителя.

# Пример наследования класса в Python

class Parent:
    parent_attr = 100
    def __init__(self):
        print('Вызов родительского конструктора')
    def parent_method(self):
        print('Вызов родительского метода')
    def set_attr(self, attr):
        Parent.parent_attr = attr
    def get_attr(self):
        print('Атрибут родителя: {}'.format(Parent.parent_attr))
    def my_method(self):
        print('Вызов родительского метода')

class child(Parent):
    def __init__(self):
        print('Вызов конструктора класса наследника')
    def child_method(self):
        print('Вызов метода класса наследника')
    def my_method(self):
        print('Вызов метода наследника')

c = child()
c.child_method()
c.parent_method()
c.set_attr(300)
c.get_attr()
print()
# Вы можете использовать функции issubclass() или isinstance() для
# проверки отношений двух классов и экземпляров.

# Логическая функция issubclass(sub, sup) возвращает значение True,
# если данный подкласс sub действительно является подклассом sup.
# Логическая функция isinstance(obj, Class) возвращает True, если obj
# является экземпляром класса Class или является экземпляром подкласса #класса.

# Переопределение методов

# Вы всегда можете переопределить методы родительского класса. В вашем #подклассе
# могут понадобиться специальные функции. Это одна из причин переопределения
# родительских методов.

c.my_method()
print()

# Популярные базовые методы
# В данной таблице перечислены некоторые общие функции. Вы можете
# переопределить их в своих собственных классах.

# 1)__init__(self [, args...]) — конструктор (с любыми необязательными
# аргументами)
#   obj = className(args)
# 2)__del__(self) — деструктор, удаляет объект
# del obj
# 3)__repr__(self) — оценочное строковое представление
# repr(obj)
# 4)__str__(self) — печатное строковое представление
# str(obj)

# Пример

class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __str__(self):
        return 'Vector ({}, {})'.format(self.a, self.b)
    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)

v1 = Vector(2, 10)
v2 = Vector(5, -2)
print(v1 + v2)
print()

# Приватные методы и атрибуты класса
# Атрибуты класса могут быть не видимыми вне определения
# класса. Вам нужно указать атрибуты с __ вначале, и эти атрибуты не будут
# вызваны вне класса.

# Пример приватного атрибута

class JustCounter:
    __secret_count = 0
    def count(self):
        self.__secret_count += 1
        print(self.__secret_count)

counter = JustCounter()

counter.count()
counter.count()
# print(counter.__secret_count) выдаст ошибку

# Вы можете получить доступ к таким атрибутам, так object._className__attrName.
print(counter._JustCounter__secret_count)