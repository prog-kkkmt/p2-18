#Выполнил Кузнецов М. С. П2-18.
#Даны положительные числа A и B (A > B).
#На отрезке длины A размещено максимально возможное количество отрезков длины B (без наложений).
#Не используя операции умножения и деления, найти количество отрезков B, размещенных на отрезке A.
a = int(input("Введите А: "))
b = int(input("Введите B: "))
i = 1
while (a > b):
    a -= b
    i += 1
print("Количество возможных размещенных отрезков B -", i)
