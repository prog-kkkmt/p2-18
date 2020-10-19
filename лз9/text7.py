#Дана строка S и текстовый файл. Добавить строку S в начало файла.
text = open('text7.txt', 'r')
s = input()#Введите текст, который будет в конце строки
s += text.read()#Вводим текст в переменную
text.close()
text = open('text7.txt', 'w')
text.write(s)
text.close()
