#Выполнили: Воронцов А.А. Бурлаев З.С Щепкин М.В П2-18
#Задание 7. Удалить свойства объекта
#Выполнили: Воронцов А.А. Бурлаев З.С Щепкин М.В П2-18
# Задание 1. Создание класса
class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    def  myfunc(self):
        print("Знакомьтесь, это "  + self.name + ",", "он " + self.color)
        
p1 = Cat("Барсик", "рыжий")
p1.myfunc()
#удаляем свойства объекта
del p1.color
