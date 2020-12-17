# Выполнил:Степаненко Кирилл Алексеевич
# Группа: П2-18
# Задание 3. https://pythontutor.ru/lessons/dicts/problems/most_frequent_word/
# Задача «Самое частое слово»
# Условие. Дан текст: в первой строке задано число строк, далее идут сами строки.
# Выведите слово, которое в этом тексте встречается чаще всего. Если таких слов несколько,
# выведите то, которое меньше в лексикографическом порядке.

n=int(input())
d={}
for i in range(n):
    s=input()
    s=s.split()
    for x in s:
        d[x]=d.get(x, 0)+1
l=list(d.keys())
l.sort()
c=list(d.values())
c.sort()
max=c[len(c)-1]
for x in l:
    if d[x]==max:
        print(x)
        break