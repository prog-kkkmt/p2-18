#Выполнил Кузнецов М. С. П2-18.
#По данному целому числу N распечатайте все квадраты натуральных чисел,
#не превосходящие N, в порядке возрастания.
n = int(input("Введите N:"))
i = 1
while i ** 2 <= n:
    print(i ** 2)
    i += 1
