#Выполнил: Зайцев Никита
#Группа: П2-18
'''
К10_1. Техника работы с функциями

Задание 2. Func6. Описать функцию SumRange(A, B) целого типа, находящую сумму всех целых 
чисел от A до B включительно (A и B — целые). Если A > B, то функция возвращает 0. 
С помощью этой функции найти суммы чисел от A до B и от B до C, если даны числа A, B, C.
'''

def SumRange(a, b):
	summ = 0
	for i in range(a, b+1):
		summ += i
	return summ

print("Введите числа:")
a = [int(x) for x in input().split()]
len_a = len(a)

summ = 0
for i in range(1, len_a):
	summ += SumRange(a[i-1], a[i])
print(summ)

