#Дан непустой текстовый файл. Удалить из него последнюю строку.
text = open('text14.txt', 'r')
s = text.readlines()
text.close()
s.pop()#Удаление последней строчки
text = open('text14.txt', 'w')
text.writelines(s)
text.close()
