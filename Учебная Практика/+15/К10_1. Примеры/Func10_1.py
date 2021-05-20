''' Описать процедуру plus2(a), увеличивающую значение каждого чётного
элемента списка на 2.

 '''
# Решение. Гусятинер Л.Б., 30.11.2020

def plus2(a):
     for i in range(len(a)):
          a[i] += 2

a = [int(x) for x in input().split()]
print(*a)
plus2(a)
print(*a)
