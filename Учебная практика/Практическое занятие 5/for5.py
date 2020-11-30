#https://pythontutor.ru/lessons/for_loop/problems/sum_of_ten_numbers/
#Дано 10 целых чисел. Вычислите их сумму.
#Напишите программу, использующую наименьшее число переменных.
sum = 0
for i in range(10):
    number = int(input())
    sum += number
print(sum)
