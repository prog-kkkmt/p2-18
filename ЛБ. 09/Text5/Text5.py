#Дана строка S и текстовый файл. Добавить строку S в конец файла.
txt = open('text55.txt', 'a')
print("Введите текст, который должен быть записан в конец файла.")
a = input()
txt.write(a)
print("Готово!")
txt.close()
