#Выполнил Зайцев Н. Е. П2-18.
#Дан текстовый файл, каждая строка которого изображает целое число, дополненное слева и справа 
#несколькими пробелами. Вывести количество этих чисел и их сумму.

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

out = 0
for n in num:
    out += int(n)
print('Количество строчек - ', len(sri)+1)
print('Сумма - ', out)
