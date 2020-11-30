# Пихтов Виталий Алексеевич
# Модуль fractions
from fractions import Fraction
from decimal import Decimal
import math
#Fraction.limit_denominator(max_denominator=1000000)- ближайшее
#рациональное число со знаменателем не больше данного.
a = Fraction(3.1415) # Целое и вещественное число, так же можно преобразовать в обыкновенную дробь
print(a) # 7074029114692207/2251799813685248
print(a.limit_denominator()) # 6283/2000
#  по умолчанию numerator = 0, denominator = 1
print(Fraction())
#  равносильно Fraction(1, 2)
print(Fraction(numerator=1, denominator=2))
#Если указанные числитель и знаменатель имеют общие делители,
#то перед созданием рационального числа они будут сокращены
print(Fraction(8, 16), Fraction(15, 30))
#Если указанные числитель и знаменатель имеют общие делители,
#то перед созданием рационального числа они будут сокращены
print(Fraction(3, Fraction(1, 2)))
#Округляет до ближайшего четного числа.
print(Fraction('1/2').__round__())
#создает обыкновенную дробь, которая является точным 
представлением
#десятичной дроби указанной в dec, где dec – это экземпляр класса decimal.Decimal
print(Fraction.from_decimal(Decimal('0.7')))
#принимает flt – число типа float и возвращает обыкновенную дробь отношение числителя
#к знаменателю которой максимально приближается к значению flt.
print(Fraction.from_float(0.5))
#fractions.gcd(a, b) - наибольший общий делитель чисел a и b.
print(math.gcd(1000, 3))
print(math.gcd(4, 6))
