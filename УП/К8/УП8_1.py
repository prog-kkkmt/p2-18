# Выполнил:Степаненко Кирилл Алексеевич
# Группа: П2-18
# https://pythontutor.ru/lessons/lists/problems/more_than_neighbours/

# Дан список чисел.
# Определите, сколько в этом списке элементов, которые больше двух своих соседей, и выведите количество таких элементов.
# Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.

a = [int(i) for i in input().split()]
counter = 0
for i in range(1, len(a) - 1):
    if a[i - 1] < a[i] > a[i + 1]:
        counter += 1
print(counter)
