#Дан непустой текстовый файл. Удалить из него первую строку.

with open('text13.txt', 'r') as fin:
    data = fin.read().splitlines(True)
with open('text13.txt', 'w') as fout:
    fout.writelines(data[1:])
