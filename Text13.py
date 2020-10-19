#Text13 Дан непустой текстовый файл. Удалить из него первую строку.
f=open('file.txt').readlines()
for i in [0]:
    f.pop(i)
with open('file.txt','w') as F:
    F.writelines(f)
