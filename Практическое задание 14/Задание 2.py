#Выполнил Зайцев Н. Е. П2-18.
#Дана строка S и текстовый файл. Заменить в файле все пустые строки на строку S.

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


txt = file_get_contents("text.txt")
s = ' строка S '
txt = re.sub(r'\s', s, txt)
file_put_contents("text.txt",txt)
