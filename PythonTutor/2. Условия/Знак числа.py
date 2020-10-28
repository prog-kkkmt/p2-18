#Выполнил Кузнецов М. С. П2-18.
#Для данного числа x выведите значение sign(x).
x = int(input("Введите x: "))
if x < 0:
    print(-1)
elif x > 0:
    print(1)
else:
    print(0)