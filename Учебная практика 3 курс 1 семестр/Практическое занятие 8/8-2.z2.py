#Выполнил: Короленко Иван Романович
#Студент: ККМТ П2-18

'''Задание 2. Array113. Дан массив A размера N.
Упорядочить его по возрастанию методом сортировки простым
выбором: найти максимальный элемент массива и поменять его
местами с последним (N-1 м) элементом; выполнить описанные
действия N  1 раз, каждый раз уменьшая на 1 количество
анализируемых элементов и выводя содержимое массива'''

from random import randint

arr = []
N = int(input())
for i in range(N):
    arr.append(randint(1, 99))
print('Начальный массив\n',arr)

for i in range(0,N):
    print(arr)
    max_val = max(arr[:N-i])
    MaxI = arr.index(max_val)
    arr[MaxI], arr[N-i-1] = arr[N-i-1], arr[MaxI]
print('\nКонечный массив\n',arr)


'''
i = 0
while i < N - 1:
    m = i
    j = i + 1
    print(arr)
    while j < N:
        if arr[j] < arr[m]:
            m = j
        j += 1
    arr[i], arr[m] = arr[m], arr[i]
    i += 1
print(arr)'''
