#Выполнили: Щепкин М.В П2-18
#Задание 8. Удаление объектов

class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    def  myfunc(self):
        print("Знакомьтесь, это "  + self.name + ",", "он " + self.color)
        
p1 = Cat("Барсик", "рыжий")
p1.myfunc()

#добавляем новый объект
p2 = Cat("Чёрныш", "чёрный")
#выполняем функцию для второго объекта
p2.myfunc()
#удаляем первый объект
del p1
