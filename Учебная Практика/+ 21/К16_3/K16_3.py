#Выполнил: Зайцев Никита
#Группа: П2-18
'''
К16_3. Техника работы с классами.

Задание 1. Наследование класса
Задание 2. Переопределение методов
Задание 3. Популярные базовые методы
Задание 4. Приватные методы и атрибуты класса
'''

#1. Наследование класса
print("#Задание 1")
class Parent:
	"""Родительский класс"""
	parent_attr = 18
	def __init__(self):
		print("Вызов родительского класса")
	
	def parent_method(self):
		print('Вызов родительского метода')
	
	def set_attr(self, attr):
		Parent.parent_attr = attr

	def get_attr(self):
		print(f"Вызов родителя: {Parent.parent_attr}")
	
	#для задания 2
	def my_method(self):
		print('Вызов родительского метода')

#Ссылается на класс Parent
class Child(Parent):
	"""Класс наследник"""
	
	def __init__(self):
		print("Вызов класса наследника")
	
	def child_method(self):
		print("Вызов метода класса наследника")
		
	def set_attr_c(self, attr):
		Parent.parent_attr = attr
	
	#для задания 2
	def my_method(self):
		print('Вызов метода наследника')
#----------------------------------


c = Child()  # экземпляр класса Child  
c.child_method()  # вызов метода child_method  
c.parent_method()  # вызов родительского метода parent_method  

c.set_attr(200)  # еще раз вызов родительского метода  
c.get_attr()  # снова вызов родительского метода

c.set_attr_c(300)  # еще раз вызов родительского метода  
c.get_attr()  # снова вызов родительского метода

#Возвращает True, если 1ый аргумент подкласс 2го
print(issubclass(Child, Parent))
print(issubclass(Parent, Child))

#Возвращает True, если 1ый аргумент является экземпляром подкласса класса
print(isinstance(c, Parent))
print(isinstance(c, Child))

del c
print()

#Задание 2. Переопределение методов
print("#Задание 2")
v1 = Child()
v1.my_method()
print()

v2 = Parent()
v2.my_method()

del v1, v2
print()
# Т.е если у классов метод совпадает, то вызывается идет обращение к классу,
#к которому принадлежит наш объект


#Задание 3. Популярные базовые методы
class Vector:
	def __init__(self, a, b):
		self.a = a
		self.b = b
	
	def __str__(self):
		return f"Vector({self.a}, {self.b})"
	
	def __repr__(self):
		return f"Vector('{self.a}', '{self.b}')"
		
	def __add__(self, other):
		#return f"Vector({self.a + other.a}, {self.b + other.b})"
		return Vector(self.a + other.a, self.b + other.b)

v1 = Vector(2, 10)
v2 = Vector(10, -2)

print(str(v1))		#__str__
print(repr(v1))	#__repr__
print(v1 + v2)		#__add__

del v1, v2


#Задание 4. Приватные методы и атрибуты класса

class Class:
	__secret_count = 0
	
	def count(self):
		self.__secret_count += 1
		print(self.__secret_count)

counter = Class()
counter.count()
counter.count()
print(counter._Class__secret_count)	#Обращаемся к приватному атрибуту












