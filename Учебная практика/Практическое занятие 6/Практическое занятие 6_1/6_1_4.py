# Decimal 1
# Выполнили: Воронцов А.А. Бурлаев З.С. Щепкин М.В. П2-18

"""
На вход подаётся число, окуглить его до двух знаков после запятой и вывести рельзутат
"""
from decimal import Decimal

num = Decimal(input())
print(num.quantize(Decimal("1.00")))
