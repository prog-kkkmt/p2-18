print('Введите порядковый номер числа Фибоначчи, который хотите вывести : ')
n = int(input())
a = 1
def fibonacci(n):
    global a
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a += 1
        return fibonacci(n - 1) + fibonacci(n - 2)

print('Количество чисел в сетке: ', a)
print('Само число: ', fibonacci(n))
