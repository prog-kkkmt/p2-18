#Выполнил: Короленко Иван Романович
#Студент: ККМТ П2-18

#Задание 5.
#Text53. Дан текстовый файл. Создать символьный файл, содержащий все знаки препинания, 
#встретившиеся в текстовом файле (в том же порядке).

with open('text53.txt') as inp, open('text53_2.txt','w') as out:
    res = []
    for line in inp.readlines():
        res += ''.join(list(line.rstrip()))
    out.write(''.join(sorted(set(res),key = ord)))
print(res)
print(line)
