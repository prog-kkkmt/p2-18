#Выполнил Кузнецов М. С. П2-18.
#Дано целое число N (> 0). Если оно является степенью числа 3,
#то вывести true, если не является — вывести false.
n = int(input("Введите целое число N( >0 ):"))
s = 3
r = 1
while (r * s <= n):
    r *= s
if r == n:
    print("True")
else:
    print("False")
