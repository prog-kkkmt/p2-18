#Выполнили: Сумин Константин
#Группа: П2-18
'''
К5_2. Техника работы с циклическими программами _ цикл while;

Задание 3.
Разработать программу для нахождения наибольшего общего делителя
'''

import sys

def nod(x,y):
    if x==0 or y==0:
        return max(x,y)
    return nod((y%x),x)

def Integer(x):
    try:
        return int(x)
    except:
        std_err = sys.stderr
        return std_err.write('введено не число, ответ выше ложный')

print('НОД ',nod(Integer(input("первое число ")),Integer(input("второе число "))))