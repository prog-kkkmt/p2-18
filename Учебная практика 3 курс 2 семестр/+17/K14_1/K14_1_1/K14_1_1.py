#Выполнил: Кузнецов Матвей
#Группа: П2-18
'''
К14_1. Техника работы с файлами
Задание 1. http://ptaskbook.com/ru/tasks/text.php
Text5. Дана строка S и текстовый файл. Добавить строку S в конец файла.
'''

fin = open("file.txt","a")
print("Enter your string:")
fin.write(input())
fin.close()
print("Pasted!")