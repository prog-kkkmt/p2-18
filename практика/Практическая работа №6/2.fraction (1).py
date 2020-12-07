# Завадский Михаил Задание разбор модуля Fraction
# Модуль fractions

from fractions import Fraction
print (Fraction()) # по умолчанию(Fraction(0, 1))
print (Fraction(2, 4), Fraction(3, 9), Fraction(4, 16))  # если есть общий делитель то, числа будут сокращены
print (Fraction('1/3').__round__()) #округляет до ближайшего чётного числа
print (Fraction(1, 3) + Fraction(1, 4)) # также можно выполнять разные математические действия
print (Fraction(1, 3) - Fraction(1, 4))
print (Fraction(1, 3) ** Fraction(1, 4))
print (Fraction(1, 3) % Fraction(1, 4))
print (Fraction(1, 3) * Fraction(1, 4))


