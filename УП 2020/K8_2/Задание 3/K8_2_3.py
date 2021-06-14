#Выполнил: Безбородов Константин
#Группа: П2-18
'''
К8_2. Техника работы со списками

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

def insertion(mas):
    for i in range(len(mas)):
        j = i - 1
        key = mas[i]
        while mas[j] > key and j >= 0:
            mas[j + 1] = mas[j]
            j -= 1
        mas[j + 1] = key
        print(mas)
    return mas

n = int(input())
mas = []
for i in range(n):
    mas.append(randint(1,100))
print(mas)
insertion(mas)
print(mas)