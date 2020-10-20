//////12
# Даны катеты прямоугольного треугольника a и b.
Найти его гипотенузу c и периметр P:
c = (a2 + b2)1/2,        P = a + b + c.


a=float(input())
b=float(input())
c=(a**2+b**2)**0.5
p=a+b+c
print(c)
print(p)

#Даны два ненулевых числа. Найти сумму, разность, произведение и частное их модулей.
////////11
a=float(input())
b=float(input())
print(abs(a)+abs(b))
print(abs(a)-abs(b))
print(abs(a)*abs(b))
print(abs(a)/abs(b))
