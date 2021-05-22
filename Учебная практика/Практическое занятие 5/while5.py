# Выполнил: Бурлаев З. С.
# https://pythontutor.ru/lessons/while/problems/kth_fibonacci/
# Последовательность Фибоначчи определяется так:
# φ0 = 0,  φ1 = 1,  φn = φn−1 + φn−2.
# По данному числу n определите n-е число Фибоначчи φn.

n = int(input())
if n == 0:
    print(0)
else:
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    print(b)
