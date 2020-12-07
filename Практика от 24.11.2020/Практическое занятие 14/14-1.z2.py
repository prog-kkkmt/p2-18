# Выполнил Слесарев А. М. П2-18.
# Дана строка S и текстовый файл. Заменить в файле все пустые строки на строку S.

import os
import shutil
from os import path
s = input()
f1 = open('Text.txt', 'r')
f2 = open ('out.txt', 'w')
for line in f1:
    if line == '\n':
        f2.write(s + '\n')
    else:
        f2.write(line)
f2.close ()
f1.close ()
os.remove('Text.txt')
os.rename('out.txt','Text.txt')
