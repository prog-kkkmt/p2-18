#Выполнил Зайцев Н. Е. П2-18.
#Дана строка S и текстовый файл. Добавить строку S в конец файла.

def file_get_contents(path,encoding="utf-8"):
     with open(path, "r",encoding=encoding) as f:
         out = f.read()
         f.close() 
         return out

f = open('text.txt', 'a+')
s = str(input())
f.write(s)
f.close()
print(file_get_contents("text.txt"))
