#Text14. Дан непустой текстовый файл. Удалить из него последнюю строку.
f=open('file2.txt').readlines()
for i in [0]:
    f.pop()
with open('file2.txt','w') as F:
    F.writelines(f)
