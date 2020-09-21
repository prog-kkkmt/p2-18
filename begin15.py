#Дана площадь S круга. Найти его диаметр D и длину L окружности,
#ограничивающей этот круг, учитывая, что L = π·D,    S = π·D2/4.
#В качестве значения π использовать 3.14.

import math

print(math.pi)
S = int(input())
R = math.sqrt(S / math.pi)
L = 2 * math.pi * R
print(R)
print(S)
print(L)
