#Pythontutor
#https://pythontutor.ru/lessons/lists/problems/num_equal_pairs/
#Выполнили: Щепкин М.В П2-18

"""
Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
"""

cnt = 0
a = [int(num) for num in input().split()]
for i in range(len(a)-1):
    for j in range(i+1, len(a)):
        if a[i] == a[j]:
            cnt += 1

print(cnt)
