# Выполнил: Бурлаев З.С.
# Задача:
# С клавиатуры вводятся целые числа a > b.
# Выведите убывающую последовательность чисел по одному числу в строке.

a = int(input())
b = int(input())
for i in range(a, b, -1):
    print(i)
