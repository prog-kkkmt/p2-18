"""
https://stepik.org/lesson/538/step/8?unit=861
"""

"""
Напишите рекурсивную функцию вычисления наибольшего общего делителя двух положительных целых чисел (Greatest Common Divisor, GCD).
Для этого воспользуйтесь следующими свойствами:

GCD(a, b) = GCD(b, a \bmod b)GCD(a,b)=GCD(b,amodb)
GCD(0, a) = aGCD(0,a)=a
GCD(a, b) = GCD(b, a)GCD(a,b)=GCD(b,a)
Требования к реализации: в данном задании запрещено пользоваться циклами.
Вы можете заводить любые вспомогательные функции, если они вам нужны. Функцию main определять не нужно.
Напишите программу. Тестируется через stdin → stdout
"""

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

#пример работы в программе

a, b = map(int, input().split())
a, b = abs(a), abs(b)
print(gcd(a, b))
