'''
Дана строка S и текстовый файл. Добавить строку S в конец файла
'''

'''f = open("text1.txt", "r")
a = f.read()
a += 'S'
f.close()
f = open("text1.txt", "w")
f.write(a)
f.close()
'''
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
