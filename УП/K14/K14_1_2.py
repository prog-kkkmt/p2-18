# Выполнил:Степаненко Кирилл
# Группа: П2-18
# Дана строка S и текстовый файл. Заменить в файле все пустые строки на #строку S.

file = open('text2.txt', 'r')
file1 = open('text3.txt', 'a')
s = input()
for line in file:
    if line == '\n':
        file1.write(s + '\n')
    else:
        file1.write(line)
    print(line)
file.close()
file1.close()