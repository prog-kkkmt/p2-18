# Выполнил Кузнецов М. С. П2-18.
# Дана матрица размера M x N (N — четное число). Поменять местами
# левую и правую половины матрицы.

import random as rnd

m = rnd.randrange(2, 10, 2)
n = rnd.randrange(2, 10, 2)
a = [rnd.randrange(0, 100) for i in range(m)]
print('m =', m, 'n =', n)
half = len(a) // 2
b = [a[half:] + a[:half]] * n
print(a)
print(*b, sep='\n')