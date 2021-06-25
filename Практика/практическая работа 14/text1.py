# http://ptaskbook.com/ru/tasks/text.php
# Выполнил задание Яковлев Прокопий Максимович
'''
Дана строка S и текстовый файл. Добавить строку S в конец файла
'''

f = open("text1.txt", "r")
a = f.read()
a += 'S'
f.close()
f = open("text1.txt", "w")
f.write(a)
f.close()
