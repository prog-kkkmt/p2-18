#http://ptaskbook.com/ru/tasks/text.php
#Text12
# Выполнили: Воронцов А.А. Бурлаев З.С. Щепкин М.В. П2-18

"""
Дана строка S и текстовый файл. Заменить в файле все пустые строки на строку S.
"""

s = input()
with open("zad 2.txt", "r") as f:
   lines = f.readlines()
   for i in range(0, len(lines)):
       if lines[i] == "\n":
            lines[i] = s+"\n"
with open("zad 2.txt", "w") as f:
    f.writelines(lines)
