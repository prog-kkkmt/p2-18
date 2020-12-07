#Pythontutor
#https://pythontutor.ru/lessons/lists/problems/more_than_neighbours/
#Выполнили: Воронцов А.А. Бурлаев З.С Щепкин М.В П2-18

"""
Дан список чисел. Определите, сколько в этом списке элементов, которые больше двух своих соседей, и выведите количество таких элементов.
Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
"""

cnt = 0
a = [int(num) for num in input().split()]
counter = 0
for i in range(1, len(a) - 1):
    if a[i] > a[i+1] and a[i] > a[i-1]:
        cnt += 1
print(cnt)
