# Сделал Толоконников Алексей Михайлович П2-18

# Decimal- вычисления с заданной точностью
from decimal import Decimal
# Округление чисел
# Объекты Decimal имеют метод quantize(),который позволяет округлять числа.
# В этот метод в качестве первого аргумента передается также объект Decimal,
# который указывает формат округления числа:

number = Decimal("0.444")
number = number.quantize(Decimal("1.00"))
print(number)  

number = Decimal("0.555678")
print(number.quantize(Decimal("1.00")))  

number = Decimal("0.999")
print(number.quantize(Decimal("1.00")))  

# Как отделить рубли от копеек в вещественных числах?
# Decimal вместо float:

x = Decimal('100.25')
a = int(x)
b = int(100 * (x - a))
print(a, b)  
