#Выполнил: Зайцев Никита
#Группа: П2-18
'''
К14_1. Техника работы с файлами
Задание 2. http://ptaskbook.com/ru/tasks/text.php
Text12. Дана строка S и текстовый файл. Заменить в файле все пустые строки на строку S.
'''

import os

fin = open("file.txt", "r")
list_ = fin.readlines()
fin.close()
os.remove("./file.txt")
s = input()
fout = open("file.txt","w")
for i in list_:
    for j in range(len(i)):
        if(i[j-1] == '\n' and i[j] == '\n'):
            fout.write(s+'\n')
        else:
            fout.write(i[j])

fout.close()
