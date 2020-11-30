# Выполнил: Пихтов Виталий Алексеевич
# Группа: П2-18
# Decimal- это вычисления с заданной точностью
from decimal import Decimal
print(2.4 + 3.8) # Ответом будет 6.199999999999999, в нашем же случае 6.2
a = Decimal('2.4') + Decimal('3.8')
print(a)
2.4 + 3.8 == 6.2 # должно быть True, но с числами типа Decimal все верно:
c = Decimal('2.4') + Decimal('3.8')
print(c)
# С помощью дополнительных знаков мы можем определить, сколько будет символов в дробной части числа:
num = Decimal("0.20")
num = 3 * num
print(num) # 0.60
# Однако нельзя смешивать в операциях дробные числа float и Decimal:
# number = Decimal("0.1")
# number = number + 0.1   # здесь возникнет ошибка
# Округление чисел
# Объекты Decimal имеют метод quantize(),который позволяет округлять числа.
# В этот метод в качестве первого аргумента передается также объект Decimal,
# который указывает формат округления числа:
number = Decimal("0.888")
number = number.quantize(Decimal("1.00"))
print(number)  # 0.89
number = Decimal("0.1112345")
print(number.quantize(Decimal("1.00")))  # 0.11
number = Decimal("0.999")
print(number.quantize(Decimal("1.00")))  # 1.00
# Как отделить целое от дроби в вещественных числах ?
# Decimal вместо float:
a = Decimal('580.140')
b = int(a)
c = int(100 * (a - b))
print(b, c)  # => 580 14
