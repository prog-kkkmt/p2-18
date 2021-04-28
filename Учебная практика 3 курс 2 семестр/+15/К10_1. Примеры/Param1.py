''' Param1. Описать функцию MinElem(A, N) целого типа, находящую минимальный
элемент целочисленного списка a. С помощью этой функции найти
минимальные элементы списков a, b, c. '''
# Решение. Гусятинер Л.Б., 30.11.2020

def MinElem(a):
     if a == []:
          return None
     else:
          mn = a[0]
          for x in a[1:]:
               if mn > x:
                    mn = x
          return mn

for c in 'abc':
     lst = [int(x) for x in input().split()]
     print('list_', c, *lst, 'min =', MinElem(lst))
