"""
Задание 2. (Гусятинер Л.Б., МГОТУ ККМТ, 23.04.2020)
"""

"""
Разработать программу с меню для работы с массивом целых чисел из 10 элементов.
Пункты меню: Заполнение, Нахождение максимального, Нахождение суммы, Печать, Выход.
Для каждого действия (кроме выхода) разработать функцию, принимающую в качестве параметров
адрес первого элемента массива и количество элементов.
"""

import filling as fil
import findmax as fmax
import findsum as fsum
import printing as pr

print("menu")
print("1. filling \n2. find max\n3. find sum\n4. print\n5. exit\n")
print("select option\n")

mas = []

opt = int(input())
while opt != 5:
    if opt == 1:
        fil.filling(mas)
    if opt == 2:
        fmax.findmax(mas)
    if opt == 3:
        fsum.findsum(mas)
    if opt == 4:
        pr.printing(mas)
    if opt == 5:
        exit
    print("\nselect option\n")
    opt = int(input())
