# https://pythontutor.ru/lessons/sets/problems/number_of_words/
# Выполнил задание Яковлев Прокопий Максимович
'''
Условие. Дан текст: в первой строке задано число строк, далее идут сами строки.
Выведите слово, которое в этом тексте встречается чаще всего. Если таких слов несколько,
выведите все.
'''
a = {}
for i in range(int(input())):
    st = input()
    if st not in a:
        a.update({st:1})
    else:
        a.update({st:a[st] + 1})
sch = max(a.values())
for k, v in a.items():
    if v == sch:
        print(k + ':', v)
