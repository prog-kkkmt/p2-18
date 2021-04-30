#Выполнил: Сумин Константин
#Группа: П2-18
'''
К5_1. Техника работы с циклическими программами _ цикл while

Задание 1. На плоскости нарисован квадрат заданного размера с левой нижней
вершиной в начале координат. В квадрат вписывается окружность.
Случайным образом в квадрате выбирается 1000 точек.
а) нужно определить, сколько точек попало внутрь круга
б) считая количество точек пропорциональным площади, найти отношение площадей
круга и квадрата
в) по этому отношению определить приближённое значение числа пи
г) определить, насколько найденное значение отличается от "библиотечного".
'''
import math
import random

left_corn=[0,0]
right_corn=random.randint(1000,5000)
sqwer_q=[left_corn,right_corn]

rad=right_corn/2
i=0
temp=0

while i!= 1000:
    unit=[random.randint(0,right_corn),random.randint(0,right_corn)]
    i+=1

    #x^2+y^2=r^2
    if unit[0]**2+unit[1]**2<=rad**2:
        temp+=1
print('кол-во точек: ',temp)
print('соотношение площадей:', "%.2f" %((right_corn**2)/(math.pi*rad**2)))
print('пи: ', "%.5f" %(((right_corn**2)/((right_corn**2)/(math.pi*rad**2)))/(rad**2)))
print('разница: ',math.pi-(((right_corn**2)/((right_corn**2)/(math.pi*rad**2)))/(rad**2)))