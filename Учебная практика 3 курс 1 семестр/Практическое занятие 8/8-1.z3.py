# Выполнил Кузнецов М. С. П2-18.
# В списке все элементы различны. Поменяйте местами минимальный и максимальный элемент этого списка.

x = [int(i) for i in input().split()]
minn = 0
maxx = 0
for i in range(1, len(x)):
    if x[i] < x[minn]:
        minn = i
    if x[i] > x[maxx]:
        maxx = i
x[minn], x[maxx] = x[maxx], x[minn]
print(' '.join([str(i) for i in x]))
