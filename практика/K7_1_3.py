'''
Задание 3. https://stepik.org/lesson/201702/step/9?unit=175778
Уберите точки из введенного IP-адреса. Выведите сначала четыре числа через пробел,
а затем сумму получившихся чисел.
Sample Input: 192.168.0.1
Sample Output:
192 168 0 1
361
'''
l = []
a = input().split(".")
for n in a:
    l.append(int(n))
a = " ".join(a)
print(a, "\n", sum(l))
