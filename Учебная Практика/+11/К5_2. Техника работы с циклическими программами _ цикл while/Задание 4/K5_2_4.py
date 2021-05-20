#Выполнил: Зайцев Никита
#Группа: П2-18
'''
К5_2. Техника работы с циклическими программами _ цикл while;

Задание 4.
С использованием результата задания 2 разработать программу для нахождения наименьшего
общего кратного
'''

def bruh():
	n = -1
	sum_n = 0
	while n != 0:
		n = int(input())
		sum_n += n
	return sum_n

def gcd(a, b):
	 assert a >= 0 and b >= 0
	 
	 if a == 0 or b == 0:
	 	return max(a, b)
	 return gcd(b % a, a)

#least common multiple - lcm
def lcm(a, b):
	assert a >= 0 and b >= 0
	
	return a/gcd(a, b) * b

#	{--BASIC--}
def main():
	#Ввод чисел, пока не ноль
	print("Input numbers. To stop typint, enter 0")
	a = bruh();
	print("The sum of all entered numbers: ", a)
	
	#Нахождение наимньшего общего кратного
	print("\nInput number, to search \"least common multiple\": ")
	b = int(input())
	v_lcm = lcm(a, b)
	print("Least common multiple: ", v_lcm)

if __name__ == "__main__":
	main()
