#Выполнил Зайцев Н. Е. П2-18.
#С клавиатуры вводятся строки, последовательность заканчивается точкой. 
#Выведите буквы введенных слов в верхнем регистре, разделяя их пробелами.
import re #Импорт регуляров
login = input();
login = re.sub(' ','_',login) #Если есть пробел в переменной, то меняем его на _
print(''.join(login))  #Выводим из масива
