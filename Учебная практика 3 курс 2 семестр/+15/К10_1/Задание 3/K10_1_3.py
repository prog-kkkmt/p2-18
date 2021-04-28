#Выполнил: Кузнецов Матвей
#Группа: П2-18
'''
К10_1. Техника работы с функциями

Задание 3. Func10. Описать функцию IsSquare(K) логического типа, возвращающую True, 
если целый параметр K (> 0) является квадратом некоторого целого числа, и False 
в противном случае. С ее помощью найти количество квадратов в наборе из 10 целых 
положительных чисел.
'''

import math

def IsSquare(k):
	if (k < 1):
		return False
	else:
		sqrt_k = math.sqrt(k)
		if (sqrt_k == int(sqrt_k)):
			return True
		else:
			return False

a = [int(x) for x in input().split()]
len_a = len(a)
count = 0
for i in a:
	count += IsSquare(i)
print(count)
