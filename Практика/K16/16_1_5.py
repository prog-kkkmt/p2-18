#Выполнили: Щепкин М.В П2-18
#Задание 5. Параметр self

"""
Параметр self является ссылкой на сам класс и используется
для доступа к переменным принадлежащим классу.
Его не обязательно называть self, вы можете называть его как хотите,
но он должен быть первым параметром любой функции в классе
"""
#пример
class Table:
    def __init__(self, legs, color, height):
        self.legs = legs
        self.color = color
        self.height = height

p1 = Table(3, "black", 120)
print(p1.legs, p1.color, p1.height)
