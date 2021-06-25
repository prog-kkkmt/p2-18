# Выполнил:Степаненко Кирилл Алексеевич
# Группа: П2-18

# Придумать пример(ы) на использование break / continue /else.


# Задача.Дан массив чисел ,напечатать этот массив с следующими условиями:

# если число нечетное его не печатать, если четное напечатать 2 раза


Arr = []

len_arr = int(input())

i = 0

while i < len_arr:
    x = int(input())

    Arr.append(x)

    i += 1

i = 0

while i < len_arr:

    if Arr[i] % 2 == 1:

        i += 1

        continue

    else:

        print(Arr[i], Arr[i])

        i += 1