# http://ptaskbook.com/ru/tasks/text.php
# Text20
# Выполнили: Воронцов А.А. Бурлаев З.С. Щепкин М.В. П2-18
"""
Дан текстовый файл. Заменить в нем все подряд идущие пробелы на один пробел.
"""

a = input()
with open('text.txt','a') as b:
    b.write(' '.join(a.split()))
