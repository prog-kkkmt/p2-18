#http://ptaskbook.com/ru/tasks/text.php
#Text5
# Выполнили: Воронцов А.А. Бурлаев З.С. Щепкин М.В. П2-18

"""
Дана строка S и текстовый файл. Добавить строку S в конец файла.
"""
f = open("zad 1.txt", "a")
s = input()
f.write(s)
f.close()
