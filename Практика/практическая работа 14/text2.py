# http://ptaskbook.com/ru/tasks/text.php
# Выполнил задание Яковлев Прокопий Максимович
'''
Дана строка S и текстовый файл. Заменить в файле все пустые строки на строку S.
'''

f = open("text2.txt", "r")
a = ''
for i in f.read():
    for j in i:
        if j == ' ':
            j = 'S'
        a += j
f.close()
f = open("text2.txt", "w")
f.write(a)
f.close()
