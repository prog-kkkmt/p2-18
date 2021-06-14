#Выполнил: Безбородов Константин
#Группа: П2-18
'''
К15_3. Техника работы с модулями

Модуль sys в Python.
https://docs-python.ru/standart-library/modul-sys-python/

Задание 5. Объекты stdin, stdout, stderr модуля sys в Python.
https://docs-python.ru/standart-library/modul-sys-python/obekty-stdin-stdout-stderr-modulja-sys/
'''

import sys
stderr_age = stderr_value = sys.stderr
stdout_f = stdout_age = stdout_value = sys.stdout
stdin_f = sys.stdin

stdin_f = open('text.txt',"r")
stdout_f = open('data.txt', "w")

text_list = []
i = 0           # Операнд строки(используется в виде индекса list'a), изначально равен 0

text_list = stdin_f.readlines()     # Упаковываем каждую строчку из тиикстишника в элемент list'a

print("%s" % (text_list[i]), end = "")       # Узнаём имя товарища
name = str(input())
stdout_f.write("Name: {} \n".format(name))

i += 1          # 1
print("%s" % (text_list[i]), end = "")

i += 1          # 2
while True:                         # Узнаём сколько товарищу лет
    print("%s" % (text_list[i]), end="")
    age = int(input())
    if age < 1:
        i += 1  # 3
        stderr_age.write(text_list[i])
        i -= 1  # 2
    else:
        stdout_f.write("Age: {} \n".format(str(age)))
        i += 2  # 4
        stdout_age.write(text_list[i])
        break

i += 1          # 5
while True:                         # Узнаём как товарищ оценивает данную программу
    print("%s" % (text_list[i]), end = "")
    value = str(input())
    if value == 'like':
        stdout_f.write("Review: {} \n".format(value))
        i += 1  # 6
        stdout_value.write(text_list[i])
        stdin_f.close()             # Закрывает stdin
        stdout_f.close()            # Закрывает stdout
        exit(0)
    elif value == 'dis':
        i += 2  # 7
        stderr_value.write(text_list[i]+'\n')
        i -= 2
    else:
        i += 3
        stderr_value.write(text_list[i]+'\n')
        i -= 3
