#Выполнил: Зайцев Никита
#Группа: П2-18
'''
К16_2. Техника работы с классами.

Задание 1. Создание классов
Задание 2. Создание экземпляров класса
Задание 3. Доступ к атрибутам
Задание 4. Встроенные атрибуты класса
Задание 5. Уничтожение объектов (сбор мусора)
'''

#1. Создание классов
class DataHero:
	"""Функции героя, статистика и другое о нем"""
	obj_count = 0
	def __init__(self, name, age):
		self.name = name
		self.age = age
		DataHero.obj_count += 1
	
	#Методы класса
	#Количество объектов класса
	def ActCount(self):
		print(f"Количество объектов класса: {DataHero.obj_count}")
	
	#Приветствие
	def Welcome(self):
		print(f"Добро пожаловать, в долину силы, мой юный друг {self.name}")
	
	#Данные героя
	def DataHero(bruh):
		print(f"-------------------")
		print(f"Имя: {bruh.name}")
		print(f"Возраст: {bruh.age}")
		print(f"-------------------")
		print()
#----------------------------------


#2. Создание экземпляров класса
hero1 = DataHero("Владимир", 20)	#1ый объект класса DataHero
hero2 = DataHero("icefanik", 33)	#2ой объект класса DataHero

#Документация класса
print(hero1.__doc__)
print(DataHero.__doc__)
#----------------------------------


#3. Доступ к атрибутам
hero1.Welcome()
hero1.DataHero()

print(f"Количество героев: {DataHero.obj_count}")

#Свойство объекта можно менять
hero1.age = 9999
hero1.DataHero()

#Свойства объектов можно удалять
del hero2.age

#Также можно удалять сам объект
del hero2

print(hasattr(hero1, 'age'))	#Возвращает True, если атрибут 'age' существует
print(getattr(hero1, 'age'))	#Возвращает значение атрибута 'age'
delattr(hero1, 'age')	#Удаляет атрибут 'age'
setattr(hero1, 'age', 8)	#Устанавливает атрибут 'age' на 8
print()
#----------------------------------


#4. Встроенные атрибуты класса
#По объекту класса
print("#По объекту класса")
print(f"hero1.__doc__: {hero1.__doc__}")	#Документация класса
print(f"hero1.__dict__: {hero1.__dict__}")	#Словарь, содержащий пространство имен класса.
print()

#По классу
print("#По классу")
print(f"DataHero.__doc__: {DataHero.__doc__}")	#Документация класса
print(f"DataHero.__name__: {DataHero.__name__}")	#Наименование класса
print(f"DataHero.__module__: {DataHero.__module__}")	#Имя модуля, в котором определяется класс. Этот атрибут __main__ в интерактивном режиме.
print(f"hero1.__bases__: {DataHero.__bases__}")	#Могут быть пустые tuple, содержащие базовые классы, в порядке их появления в списке базового класса.
print(f"hero1.__dict__: {DataHero.__dict__}")	#Словарь, содержащий пространство имен класса.
print()
#----------------------------------


#5. Уничтожение объектов (сбор мусора)
class Point:
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y
	def __del__(self):
		class_name = self.__class__.__name__
		print(f"Класс {class_name} уничтожен")

ptr1 = Point()
print(f"id_ptr1 = {id(ptr1)}, ptr1 = {ptr1.x} {ptr1.y}")
ptr1 = Point(1, 2)
print(f"id_ptr1 = {id(ptr1)}, ptr1 = {ptr1.x} {ptr1.y}")

ptr2 = ptr1
ptr3 = ptr1
print(id(ptr1), id(ptr2), id(ptr3))
del ptr1
del ptr2
del ptr3

