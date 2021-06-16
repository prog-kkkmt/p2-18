# Выполнил Кузнецов М. С. П2-18.
# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.

x = [int(a) for a in input().split()]  # Сканим все числа и загоняем в список.
o = 0
for i in range(len(x)):  # цикл в пределах количества чисел в списке.
    t = 0
    while t + i + 1 < len(x):  # Счет значений.
        if x[i] == x[t + i + 1]:  # Проверка элементов.
            o += 1
        t += 1
print(o)
