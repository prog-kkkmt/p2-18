# https://stepik.org/lesson/193753/step/4?unit=168148
# Выполнил задание Михайлов Данила
'''
Вывести чётные
Необходимо вывести все четные числа на отрезке [a; a * 10].
'''
a = int(input())
[print(i) for i in range(a, a*10+1) if i % 2 == 0]
