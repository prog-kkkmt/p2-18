# Выполнил:Степаненко Кирилл Алексеевич
# Группа: П2-18
# Задание 1. На плоскости нарисован квадрат заданного размера с левой нижней
# вершиной в начале координат. В квадрат вписывается окружность.
# Случайным образом в квадрате выбирается 1000 точек.
# а) нужно определить, сколько точек попало внутрь круга
# б) считая количество точек пропорциональным площади, найти отношение площадей
# круга и квадрата
# в) по этому отношению определить приближённое значение числа пи
# г) определить, насколько найденное значение отличается от "библиотечного".


import random
import math
count = 100
len_1 = float(input())

points_inside_the_ring = []
points_out_of_ring = []

r = len_1 / 2
counter = 0

Pi = 0.0
k = 0.0
i = 0
j = 0
while i < count:
    x = random.uniform(0, len_1)
    y = random.uniform(0, len_1)
    points_koor = (x, y)
    point_with_num = [i+1, points_koor]
    i += 1
    if x >= r and y >= r:
        if r**2 >= (x-r)**2 + (y-r)**2:
            counter += 1 
            points_inside_the_ring.append(point_with_num)
            k+=(x**2 + y**2 < len_1**2 *1.0)
            j+=1
        else:
            points_out_of_ring.append(point_with_num)
    elif x >= r and y <= r:
        if r**2 >= (x-r)**2 + (r-y)**2:
            counter += 1 
            points_inside_the_ring.append(point_with_num)
            k+=(x**2 + y**2 < len_1**2 *1.0)
            j+=1
        else:
            points_out_of_ring.append(point_with_num)
    elif x <= r and y >= r:
        if r**2 >= (r-x)**2 + (y-r)**2:
            counter += 1 
            points_inside_the_ring.append(point_with_num)
            k+=(x**2 + y**2 < len_1**2 *1.0)
            j+=1
        else:
            points_out_of_ring.append(point_with_num)
    elif x <= r and y <= r:
        if r**2 >= (r-x)**2 + (r-y)**2:
            counter += 1 
            points_inside_the_ring.append(point_with_num)
            k+=(x**2 + y**2 < len_1**2 *1.0)
            j+=1
        else:
            points_out_of_ring.append(point_with_num)
attitude = len_1**2/(math.pi*r**2)
Pi = 4*k/j
print('attitude:', attitude)
print('points inlisde the ring:', counter)
print('Approximate number of pi:', Pi)
print('difference:', math.pi - 4*k/j)
# print('Inlisde the ring', points_inside_the_ring)
# print('Our of ring', points_out_of_ring)
