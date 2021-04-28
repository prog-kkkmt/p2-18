#Выполнил: Кузнецов Матвей
#Группа: П2-18
'''
К11_1. Техника работы со словарями

Задание 3. https://pythontutor.ru/lessons/dicts/problems/most_frequent_word/
Задача «Самое частое слово»
Условие. Дан текст: в первой строке задано число строк, далее идут сами строки. 
Выведите слово, которое в этом тексте встречается чаще всего. Если таких слов несколько, 
выведите то, которое меньше в лексикографическом порядке.
'''

text = list()
for i in range( int(input()) ):
    words = input().split()
    for word in words:
        text.append(word)

d = dict()
for key in text:
    d[key] = d.get(key, 0) + 1

maxx = max(d.values())
for key, value in sorted(d.items()):
    if (value == maxx):
        print(key)
        break

