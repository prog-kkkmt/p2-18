#Выполнил: Безбородов Константин
#Группа: П2-18
'''
К14_1. Техника работы с файлами
Задание 3. http://ptaskbook.com/ru/tasks/text.php
Text20. Дан текстовый файл. Заменить в нем все подряд идущие пробелы на один пробел.
'''

fout = open("file2.txt","w")

with open("file.txt","r") as fin:
    fout.write('\n'.join(' '.join(line.split()) for line in fin))
fout.close()