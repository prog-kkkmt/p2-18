#Выполнил Кузнецов М. С. П2-18.
#Напишите программу, которая считывает целое число и выводит текст,
#аналогичный приведенному в примере (пробелы важны!).
a = int(input("Write the number: "))
print('The next number for the number', a, 'is', a + 1, sep = ' ')
print('The previous number for the number', a, 'is', a - 1, sep = ' ')