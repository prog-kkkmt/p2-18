#Text14. Дан непустой текстовый файл. Удалить из него последнюю строку.
readf = open ('rew.txt')
lines = readf.readlines()
readf.close()
w = open ('rew.txt', 'w')
w.writelines([item for item in lines[:-1]])
w.close()
