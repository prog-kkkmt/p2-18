#Выполнил: Зайцев Никита
#Группа: П2-18
'''
К12_1. Техника работы с множествами


Задание 5. https://pythontutor.ru/lessons/sets/problems/polyglotes/
Задача «Полиглоты»
Условие. Каждый из некоторого множества школьников некоторой школы знает некоторое
количество языков. Нужно определить сколько языков знают все школьники, и сколько языков
знает хотя бы один из школьников.
В первой строке задано количество школьников. Для каждого из школьников сперва записано
количество языков, которое он знает, а затем - названия языков, по одному в строке.
В первой строке выведите количество языков, которые знают все школьники. Начиная со
второй строки - список таких языков. Затем - количество языков, которые знает хотя бы
один школьник, на следующих строках - список таких языков. Языки нужно выводить в
лексикографическом порядке, по одному на строке.
'''

n = int(input())

language = []

for i in range(n):
    k = int(input())
    buff = set()
    for j in range(k):
        buff.add(input())
    language.append(buff)

unic = set.union(*language)
intersec = set.intersection(*language)

print(len(intersec), '\n'.join(sorted(intersec)), len(unic), '\n'.join(sorted(unic)), sep='\n')

