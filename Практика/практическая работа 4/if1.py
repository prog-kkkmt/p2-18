#Выполнил работу Михайлов Данила Алексеевич
#Оформил задачу Пилипушко Андрей Сергеевич
#Задача:
#Необходимо написать программу, выводящую кортеж, содержащий числа в полуинтервале [a; b), если a < b, и [b; a), если b < a. Числа a и b вводятся с клавиатуры.
a = int(input())
b = int(input())
c = ()
if(a>b):
    a,b = b,a
c = tuple(range(a,b))
print(c)
