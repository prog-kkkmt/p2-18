#Выполнил: Зайцев Никита
#Группа: П2-18
'''
К5_2. Техника работы с циклическими программами _ цикл while;

Задание 3.
Разработать программу для нахождения наибольшего общего делителя
'''

def nod(a, b):
	 assert a >= 0 and b >= 0
	 
	 if a == 0 or b == 0:
	 	return max(a, b)
	 return nod(b % a, a)

if __name__ == "__main__":
	a,b = map(int, input().split())
	print( nod(a, b) )
