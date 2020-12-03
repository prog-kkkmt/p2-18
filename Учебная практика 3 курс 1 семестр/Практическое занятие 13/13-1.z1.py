# Выполнил Кузнецов М. С. П2-18.
# Вывести чётные
# Необходимо вывести все четные числа на отрезке [a; a * 10].
# Sample Input:
# 2
# Sample Output:
# (2, 4, 6, 8, 10, 12, 14, 16, 18, 20)

import random as r

a = r.randrange(1, 10)
b = []
for i in range(a, a * 10 + 1):
    if i % 2 == 0:
        b.append(i)
print(tuple(b))
