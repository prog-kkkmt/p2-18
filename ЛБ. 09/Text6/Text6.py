# Даны два текстовых файла. Добавить в конец первого файла
#содержимое второго файла.
txt2 = open('text66x2.txt', 'r')
a = txt2.read()
txt2.close()
txt1 = open('text66.txt', 'a')
txt1.write(a)
txt1.close()
print("Готово!")
