''' Func9. Описать функцию Even(K) логического типа, возвращающую True, 
если целый параметр K является четным, и False в противном случае. 
С ее помощью найти количество четных чисел в наборе из 10 целых чисел. '''

# вариант 1
def even(k):
     return k % 2 == 0

a = [int(input()) for i in range(10)]
s = sum(1 for x in a if even(x))
print(s)

# вариант 2
s = len(list(filter(even, a)))
print(s)

# вариант 3
s = len(list(filter(lambda x: x % 2 == 0, a)))
print(s)

