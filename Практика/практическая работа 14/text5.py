# http://ptaskbook.com/ru/tasks/text.php
# Выполнил задание Яковлев Прокопий Максимович
'''
Дан текстовый файл. Создать символьный файл, содержащий все знаки препинания, 
встретившиеся в текстовом файле (в том же порядке).
'''
f = open("text5.txt", "r")
a = [[j for j in i if j.islower() == 0 and j.isdigit() == 0 and j.isalpha() == 0 and j.isupper() == 0 and j != ' ' and j != '\n'] for i in f.read()]
[print(*i) for i in a if i]
f.close()
