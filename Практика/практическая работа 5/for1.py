#Выполнил работу Михайлов Данила Алексеевич
#Оформил задачу Пилипушко Андрей Сергеевич
#Задача:
#Дано несколько чисел. Вычислите их сумму.
#Сначала вводите количество чисел N, затем вводится ровно N целых чисел.
#Какое наименьшее число переменных нужно для решения этой задачи?
a = [0, int(input())]
for x in range(a[1]):
    a[0] += int(input())
print(a[0])
