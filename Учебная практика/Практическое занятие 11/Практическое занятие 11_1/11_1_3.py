# https://pythontutor.ru/lessons/dicts/problems/most_frequent_word/
# Задача «Самое частое слово»
# Выполнили: Воронцов А.А. Бурлаев З.С. Щепкин М.В. П2-18

"""
Дан текст: в первой строке задано число строк, далее идут сами строки. 
Выведите слово, которое в этом тексте встречается чаще всего. Если таких слов несколько, 
выведите то, которое меньше в лексикографическом порядке.

"""

d = {}
for i in range(int(input())):
    line = input().split()
    for word in line:
        d[word] = d.get(word, 0) + 1
         
maxi = max(d.values())
sl = [j for j, v in d.items() if maxi == v]
print(min(sl))
