"""
 Дана строка S и текстовый файл. Добавить строку S в конец файла.
"""
f = open('text for text5.txt', 'a')
stroka = input()
f.write(stroka)
f.close()
