#Выполнил Короленко Иван Романович
#Группа П2-18

''''Модуль fractions предоставляет поддержку рациональных чисел.
class fractions.Fraction(numerator=0, denominator=1)
class fractions.Fraction(other_fraction)
class fractions.Fraction(float)
class fractions.Fraction(decimal)
class fractions.Fraction(string)'''

from fractions import Fraction
import math
A = Fraction(1, 3)
print (A)

B = Fraction()    #  по умолчанию numerator=0, denominator=1
print(B)

C = Fraction(numerator=1, denominator=2)    #  равносильно Fraction(1, 2)
print(C)

#В качестве числителя и (или) знаменателя могут быть указаны другие дроби:
AC = Fraction(3, Fraction(1, 2))
print(AC)

#Математические операции над рациональными числами
   #Все арифметические операторы поддерживают вычисления с рациональными числами:
x = Fraction(2, 5)
y = Fraction(3, 7)
print(x + y, y - x)
print(x*y, x/y)

#Функции модуля math способны принимать рациональные числа в качестве аргументов,
#так как последние, по сути, могут быть просто преобразованы к вещественным числам:
Z = Fraction(4, 11)
math.exp(Z), math.exp(4/11)
print(Z)
