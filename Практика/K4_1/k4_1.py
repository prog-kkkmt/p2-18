'''
#Выполнили: Сумин Константин
#Группа: П2-18

К4_1. Техника работы с линейными программами

Задание 1. Разработать программы по темам
- input
- print
- stdin, stdout, stderr
- форматная строка и метод формат
'''

import sys

def Integer(x):
    try:
        return int(x)
    except:
        return -1

std_out = sys.stdout
std_in = sys.stdin
std_err = sys.stderr

std_in=open('in.txt',"r")
std_out=open('out.txt',"w")

text_age = ''
text_line = ''

for i in std_in:
    if i == 'try yo text...':
        continue
    for j in range(len(i)):
        bol = False
        if i[j] == '-':
            std_err.write('Wrong age')
            bol = True
        if Integer(i[j]) != -1:
            text_age += i[j]
if bol == False:
    std_out.write('age: {} '.format(text_age))

std_in.close()
std_out.close()
exit(0)
 

