#Выполнил:Степаненко Кирилл Алексеевич
#Группа: П2-18

#Text5. Дана строка S и текстовый файл. Добавить строку S в конец файла.

a = open('text.txt', 'a')
a.write(input()+'\n')
a.close()