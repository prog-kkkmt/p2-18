#http://ptaskbook.com/ru/tasks/text.php
#Text44
# Выполнили: Воронцов А.А. Бурлаев З.С. Щепкин М.В. П2-18

"""
Дан текстовый файл. Создать символьный файл, содержащий все знаки препинания, 
встретившиеся в текстовом файле (в том же порядке).
"""
a =  []
punctuation=['(', ')', '?', ':', ';', ',', '.', '!', '/', '"', "'"]
with open("zad 5 in.txt", "r") as f:
    lines = f.readlines()
    
for i in range(0, len(lines)):
    for j in range(0, len(lines[i])):
       if lines[i][j] in punctuation:
           a.append(lines[i][j])

with open("zad 5 out.txt", "w") as f_o:
    f_o.writelines(a)
