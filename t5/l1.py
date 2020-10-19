"""Text5. Дана строка S и текстовый файл. Добавить строку S в конец файла."""
i = input()
f = open('bef.txt', 'a')
f.write(i)
f.close()
