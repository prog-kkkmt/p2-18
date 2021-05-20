#Выполнил: Зайцев Никита
#Группа: П2-18
'''
К16_4. Техника работы с классами.

Задание 1. Придумать собственный класс
Задание 2. Неформально описать функционал класса
Задание 3. Реализовать класс в модуле
Задание 4. Разработать скрипт для демонстрации работы с классом (импортировать модуль,
создать экземпляры, вызвать методы)
'''

class SubjectsHero:
	"""Предметы героя"""
	
	def __init__(self):
		self.num_subj = 0
		self.damage = 0
		self.helthy = 0
		self.subjects = list()
	
	def numSubj(self):
		return self.num_subj
		
	def sword(self):
		self.damage += 5
		self.num_subj += 1
		self.subjects.append('sword')
		
	def shield(self):
		self.helthy += 10
		self.num_subj += 1
		self.subjects.append('shield')
	
	def printSubjectsHero(self):
		print("Damage:", self.damage)
		print("Helthy:", self.helthy)
		print("Subjects hero:", end=' ')
		for i in range(self.num_subj):
			print(self.subjects[i], end = ' ')
		print()
	
	def SubjectsHero(self):
		return [self.damage, self.helthy, self.subjects]
	
	def __del__(self):
		class_name = self.__class__.__name__
		print(f"Класс \"{class_name}\" удален")
