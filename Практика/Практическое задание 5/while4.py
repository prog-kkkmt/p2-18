#Выполнил Зайцев Н. Е. П2-18.
#Дано целое число N (> 1). Найти наименьшее целое число K, при
#котором выполняется неравенство 3K > N.

N = int(input())
K = 0
a = 1
while a < N:
    a *= 3
    K += 1
K -= 1
print('K =', K, '3^K =', 3**K, '3^(K+1) =', 3**(K+1))
									
