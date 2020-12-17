#Выполнили: Воронцов А.А. Бурлаев З.С Щепкин М.В П2-18
#Задание 4. Методы объектов

"""
Объекты также содержат методы.
Методы в объектах — это функции, принадлежащие объекту.

"""
class Cat:
    def __init__(self, name, color, character):
        self.name = name
        self.color = color
        self.character = character
    #Метод
    def  myfunc(self):
        print("Знакомьтесь, это "  + self.name + ",", "он " + self.color + ",", "характер у него " + self.character)
        
p1 = Cat("Барсик", "рыжий", "ласковый")
p1.myfunc()
