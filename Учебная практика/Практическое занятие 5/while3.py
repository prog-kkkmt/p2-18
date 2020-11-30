#https://pythontutor.ru/lessons/while/problems/minimal_divisor/
#Дано целое число, не меньшее 2.
#Выведите его наименьший натуральный делитель,
#отличный от 1.
n = int(input())
i = 2
while n % i != 0:
    i += 1
print(i)
