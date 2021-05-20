#Выполнил: Зайцев Никита
#Группа: П2-18
'''
К10_2. Техника работы с функциями

Задание 4. Использовать lambda, map.
https://stepik.org/lesson/239422/step/2?unit=211833
Быстрая инициализация. Программа получает на вход три числа через пробел — начало и конец 
диапазона, а также степень, в которую нужно возвести каждое число из диапазона. Выведите 
числа получившегося списка через пробел.
Sample Input:
5 12 3
Sample Output:
125 216 343 512 729 1000 1331 1728
'''

a = int(input("Начало: "))
b = int(input("Конец: "))
power = int(input("Степень: "))

#arr = [x**power for x in range(a, b+1)]
#	ИЛИ

arr = list(map(lambda x: x**power, range(a, b+1)))

print(*arr)
