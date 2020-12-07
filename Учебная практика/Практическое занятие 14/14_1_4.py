#http://ptaskbook.com/ru/tasks/text.php
#Text44
# Выполнили: Воронцов А.А. Бурлаев З.С. Щепкин М.В. П2-18

"""
Дан текстовый файл, каждая строка которого изображает целое число, дополненное слева и справа 
несколькими пробелами. Вывести количество этих чисел и их сумму.
"""
a = []
with open("zad 4.txt", "r") as f:
    lines = f.readlines()
for i in range(0, len(lines)):
    a.append(int(lines[i].strip()))
    
print(len(a), sum(a))

