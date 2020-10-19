#Text16. Дан текстовый файл. Удалить из него все пустые строки.
string = open('het.txt').readlines()
 
for i in string:
    if not i.isspace():
        print(i.replace('\n', ''))
