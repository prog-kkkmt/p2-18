# Выполнил студент: Бурлаев З. С.
# https://stepik.org/lesson/189133/step/8?auth=login&unit=163636
# stepik.Вася приводит примеры возрастающих последовательностей из трех чисел,
# однако кое-где он допустил ошибки: в некоторых примерах
# второе и/или третье число не больше предыдущего. Он попросил вас написать
# программу, которая выводит "2 <= 1", если второе число не больше первого,
# "3 <= 2", если третье число не больше второго,
# и "Все в порядке" в остальных случаях. Все числа целые.

a = int(input())
b = int(input())
c = int(input())
if a >= b:
    print("2 <= 1")
if b >= c:
    print("3 <= 2")
if a < b < c:
    print("Все в порядке")
