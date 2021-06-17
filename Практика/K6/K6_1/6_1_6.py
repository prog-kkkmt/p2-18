# Decimal 3
# Выполнили: Щепкин М.В. П2-18

"""
На вход подаются два числа с новой строки, вычесть из большего числа меньшее
и вывести результат
"""
from decimal import Decimal

num = Decimal(input())
num_2 = Decimal(input())
if num > num_2:
    print(num - num_2)
else:
    print(num_2 - num)
