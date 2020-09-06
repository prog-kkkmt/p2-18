"""
Описать функцию TriangleP(a, h),
находящую периметр равнобедренного треугольника по его основанию a и высоте h,
проведенной к основанию (a и h — вещественные).
С помощью этой функции найти периметры трех треугольников,
для которых даны основания и высоты. Для нахождения боковой стороны b
треугольника использовать теорему Пифагора:

b^2 = (a/2)^2 + h^2.
"""
import math
def TrinagleP(a, h):
    b = math.sqrt((a/2)**2 + h**2)
    P = b*2+a
    print(P)
a_1 = float(input("a1 = "))
h_1 = float(input("h1 = "))
TrinagleP(a_1, h_1)
print(" ")
a_2 = float(input("a2 = "))
h_2 = float(input("h2 = "))
TrinagleP(a_2, h_2)
print(" ")
a_3 = float(input("a3 = "))
h_3 = float(input("h3 = "))
TrinagleP(a_3, h_3)
