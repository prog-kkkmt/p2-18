#Выполнил Кузнецов М. С. П2-18.
#Даны два целых числа A и B (A < B).
#Найти сумму всех целых чисел от A до B включительно.
A = int(input("Введите A: "))
B = int(input("Введите B: "))
if A < B:
    for i in range(A, B):
        x = A + A[1]
    print("Сумма всех целых чисел от", A, "до", B, "будет", x)
else:
    print("A !< B. Exit program...")
