#https://pythontutor.ru/lessons/while/problems/seq_sum/
#Определите сумму всех элементов последовательности,
#завершающейся числом 0. В этой и во всех следующих задачах числа,
#следующие за первым нулем, учитывать не нужно.
el = int(input())
sum = 0
while el != 0:
    sum += el
    el = int(input())
print (sum)
