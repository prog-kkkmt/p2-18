from math import *         #Найти расстояние между двумя точками с заданными координатами (x1, y1) и (x2, y2) на плоскости. Расстояние вычисляется по формуле  ((x2 − x1)2 + (y2 − y1)2)1/2.
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

def distance(x1, y1,x2,y2):
    c=sqrt((x2-x1)**2+(y2-y1)**2)
c= distance(x1,y1,x2,y2)
print(c)
