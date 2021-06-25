# http://ptaskbook.com/ru/tasks/text.php
# Выполнил задание Яковлев Прокопий Максимович
'''
Дан текстовый файл. Заменить в нем все подряд идущие пробелы на один пробел.
'''
f = open("text3.txt", "r")
a = ''
sch = 0
for i in f.read():
    for j in i:
        if sch == 1 and j == ' ':
            j = ''
        elif j != ' ':
            sch = 0
        if j == ' ':
            sch = 1
        a += j
f.close()
f = open("text3.txt", "w")
f.write(a)
f.close()
