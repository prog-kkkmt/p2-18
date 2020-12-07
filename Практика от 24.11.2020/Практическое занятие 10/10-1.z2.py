# Выполнил Кузнецов М. С. П2-18.
# Описать функцию IsSquare(K) логического типа, возвращающую True,
# если целый параметр K (> 0) является квадратом некоторого целого числа, и False
# в противном случае. С ее помощью найти количество квадратов в наборе из 10 целых
# положительных чисел.

import math
import random as rnd


def IsSquare(k):
    a = int(math.sqrt(k))
    if k == a * a:
        return True
    else:
        return False


x = 0
for i in range(0, 10):
    a = rnd.randrange(1, 100)
    print(a, end=" ")
    x += int(IsSquare(a))
print('\nКоличество квадратов чисел:', x)
