"""
ЛЗ 9. Разработка программ со строками
Составитель: Гусятинер Л.Б., 25.04.2020, МГОТУ ККМТ, П1-17, П2-17
"""

"""
Изменить программу упражнения 3.10. так, чтобы входные данные поступали из файла input.txt,
а результат записывался в файл output.txt
"""

import re

f_i = open('in.txt', 'r')
f_o = open('out.txt', 'w')
for line in f_i:
    s = line
    s_n = re.sub(r'[^\w\s]','',s)
    f_o.write(s_n + '\n')
print("done")
f_i.close()
f_o.close()
#re.sub(r'[^\w\s]','',s)

