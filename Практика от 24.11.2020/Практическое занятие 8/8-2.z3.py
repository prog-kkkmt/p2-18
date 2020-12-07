#Выполнил: Короленко Иван Романович
#Студент: ККМТ П2-18

'''
Задание 3. Array114. Дан массив A размера N. Упорядочить
его по возрастанию методом сортировки простыми вставками:
сравнить элементы A0 и A1 и, при необходимости меняя их
местами, добиться того, чтобы они оказались упорядоченными
по возрастанию; затем обратиться к элементу A2 и
переместить его в левую (уже упорядоченную) часть массива,
сохранив ее упорядоченность; повторить этот процесс для
остальных элементов, выводя содержимое массива после
обработки каждого элемента (от 1-го до N-1 го).
'''

from random import randint

arr = []
N = int(input())
for i in range(N):
    arr.append(randint(1, 99))
print('Начальный массив\n',arr)

for i in range(1,N) :
    flag = False
    x = arr[i]
    k = i - 1
    while k >= 0 :
        if x >= arr[k] :
            break
        else :
            arr[k+1] = arr[k]
            flag = True
        k -= 1
    if flag and k >= -1:
        arr[k+1] = x
    print(arr)
print('\nКонечный массив\n',arr)

'''
for i in range(N):
        m = arr[i]
        j = i
        while (arr[j-1] > m) and (j > 0):
            arr[j] = arr[j-1]
            j = j - 1
        arr[j] = m
        if m != arr[i]:
            print(' '.join([str(c) for c in arr]))
if m == arr[i]:
            print(' '.join(arr))
'''
