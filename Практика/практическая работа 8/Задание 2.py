#Выполнил задание Яковлев Прокопий Максимович
#pythontutor.ru
#https://pythontutor.ru/lessons/lists/problems/more_than_neighbours/
#Дан список чисел. Определите, сколько в этом списке элементов,
#которые больше двух своих соседей, и выведите количество таких элементов.
#Крайние элементы списка никогда не учитываются, поскольку у них
#недостаточно соседей.
a = [int(n) for n in input().split(' ')]
sch = 0
for i in range(len(a)):
    try:
        if a[i] > a[i-1] and a[i] > a[i+1] and i != 0 and i != len(a):
            sch += 1
    except IndexError:
        None
print(sch)
