#Выполнил: Безбородов Константин
#Группа: П2-18
'''
К16_4. Техника работы с классами.

Задание 1. Придумать собственный класс
Задание 2. Неформально описать функционал класса
Задание 3. Реализовать класс в модуле
Задание 4. Разработать скрипт для демонстрации работы с классом (импортировать модуль,
создать экземпляры, вызвать методы)
'''

class Hero:
	"""Данные героя"""
	obj_count = 0
	damage = 5
	helthy = 10
	
	def __init__(self, name):
		self.name = name
		Hero.obj_count += 1
	
	def count(self):
		return Hero.obj_count
		
	def InputHero(self, damage, helthy):
		self.damage = damage
		self.helthy = helthy
	
	def printDataHero(self):
		print("Name:", self.name)
		print("Damage:", self.damage)
		print("Helthy:", self.helthy)
	
	def DataHero(self):
		return [self.name, self.damage, self.helthy]
	
	def __del__(self):
		class_name = self.__class__.__name__
		print(f"Герой \"{self.name}\" удален. Класс \"{class_name}\"")
		Hero.obj_count -= 1

qwe = Hero("Qwe")
print(qwe.DataHero())
print(f"Heroes: {qwe.count()}")
print()

fire = Hero("Fire")
fire.InputHero(15, 30)
print(fire.DataHero())
print(f"Heroes: {fire.count()}")
print()

import modul

predmets = modul.SubjectsHero()
predmets.sword()
predmets.shield()
predmets.printSubjectsHero()
print()
