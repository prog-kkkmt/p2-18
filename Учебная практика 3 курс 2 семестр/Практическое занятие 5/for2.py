#Выполнил Кузнецов М. С. П2-18.
#Дано вещественное число A и целое число N (> 0).
#Найти A в степени N:
A = int(input("Введите A: "))
N = int(input("Введите степень, в которую должно быть возведено число A: "))
n = int(1)
for i in range(1, N + 1):
    x = A ** n
    print(A, "в степени", n, "будет", x)
    n += 1
