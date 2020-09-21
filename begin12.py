# Даны катеты прямоугольного треугольника a и b.
#Найти его гипотенузу c и периметр P:
#c = (a2 + b2)1/2,        P = a + b + c.

import math

a = int(input())
b = int(input())

print("Катет 1: ", a)
print("Катет 2: ", b)
c = math.sqrt(a**2 + b**2)
P = a + b + c
print("Гипотенуза: ", c)
print("Периметр: ", P)
