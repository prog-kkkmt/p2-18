#Выполнил задание Васькевич Юрий Андреевич
#Нахождение корней квадратного уравнения
import math
a, b, c = int(input('A*x + B*x + C = 0\nВведите А ')), int(input('В ')), int(input('С '))
d = b**2 - 4*a*c
if d > 0:
    x = []
    x.append((-b - math.sqrt(d)) / 2*a)
    x.append((-b + math.sqrt(d)) / 2*a)
    print('%.1f' % x[0], end = ' ')
    print('%.1f' % x[1])
if d == 0:
    x = -b / 2*a
    print(x)
if d < 0:
    print('Корней нет')