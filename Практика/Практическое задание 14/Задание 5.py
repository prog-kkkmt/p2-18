#Выполнил Зайцев Н. Е. П2-18.
#Дан текстовый файл. Создать символьный файл, содержащий все знаки препинания, 
#встретившиеся в текстовом файле (в том же порядке).

import re

def file_get_contents(path,encoding="utf-8"):
     with open(path, "r",encoding=encoding) as f:
         out = f.read()
         f.close() 
         return out


def file_put_contents(path,value,encoding="utf-8"):
    with open(path, "w",encoding=encoding) as f:
        out = f.write(value)
        f.close() 
        return True


txt = file_get_contents('text1.txt')
sri = re.findall(r"[\n']+?",txt)
num = re.findall(r"\d+",txt)

txt = file_get_contents('text2.txt')
sri = re.findall(r"[^\w\s\d]",txt)
sri = '\n'.join(sri)
file_put_contents('test2.txt',sri)
print(sri)
