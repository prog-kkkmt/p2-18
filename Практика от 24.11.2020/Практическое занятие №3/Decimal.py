#Выполнил: Короленко Иван Романович
#Группа: П2-18

#Decimal- вычисления с заданной точностью

3.3 + 4.1  # Ответом будет 7,33333, в нашем же случае 7.4
from decimal import Decimal
a = Decimal('3.3') + Decimal('4.1')
print(a)
3.3 + 4.1 == 7.4   #  должно быть True, но...

#Но с числами типа Decimal все верно:
c = Decimal('3.3') + Decimal('4.1') 
print(c)

#С помощью дополнительных знаков мы можем определить, сколько будет символов в дробной части числа:
number = Decimal("0.10")
number = 3 * number
print(number)       # 0.30

#Однако нельзя смешивать в операциях дробные числа float и Decimal:
#number = Decimal("0.1")
#number = number + 0.1   # здесь возникнет ошибка

#Округление чисел
#Объекты Decimal имеют метод quantize(),который позволяет округлять числа.
#В этот метод в качестве первого аргумента передается также объект Decimal,
#который указывает формат округления числа:
 
number = Decimal("0.444")
number = number.quantize(Decimal("1.00"))
print(number)       # 0.44
 
number = Decimal("0.555678")
print(number.quantize(Decimal("1.00")))       # 0.56
 
number = Decimal("0.999")
print(number.quantize(Decimal("1.00")))       # 1.00

#Как отделить рубли от копеек в вещественных числах?
#Используйте decimal.Decimal вместо float:

x = Decimal('40.80')
a = int(x)
b = int(100 * (x - a))
print(a, b)  # => 40 80
