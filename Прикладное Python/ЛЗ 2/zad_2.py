"""
https://stepik.org/lesson/13377/step/7?unit=3571
"""

"""
Предположим, что в программе определён макрос sqr.

#define sqr(x) x * x


Какое значение будет иметь следующее выражение?

sqr(3 + 0)

"""
# в с++ данная фунция вывела бы 3, но так как мы будем использовать lambda фунцкию то результат будет равен 9


#реализация

func =  lambda x: x*x

print(func(3 + 0))
