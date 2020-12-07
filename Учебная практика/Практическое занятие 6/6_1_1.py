# Fractions1
# Выполнили: Воронцов А.А. Бурлаев З.С. Щепкин М.В. П2-18

"""
 На вход подаются две строки с числами, содержашие пару числитель-знаменатель через пробел. Вывести сумму этих чисел
"""
from fractions import Fraction
s = input().split()
s_1 = input().split()
print(Fraction(int(s[0]), int(s[1])) + Fraction(int(s_1[0]), int(s_1[1])))
