#Выполнил Кузнецов М. С. П2-18.
#Дано целое число. Если оно является положительным, то прибавить к нему 1;
#в противном случае не изменять его. Вывести полученное число.
x = int(input("Введите число: "))
if x > 0:
    x = x + 1
    print("Число положительное.", x)
else:
    print("Число отрицательное или ноль.", x)
