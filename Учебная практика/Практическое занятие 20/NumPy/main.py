# Выполнил: Бурлаев З. С.

"""
Программа складывает, вычитает, умножает, делит и обьединяет матрицу.
"""

import numpy as np
def main():
    while(True):
        menu()
        print("Введите цифру меню: ")
        num = int(input())
        if(num == 1):
            print("Введите функцию: -, +, *, /  ")
            s = input()
            fun_1(s)
            print("\n")
        elif(num == 2):
            fun_2()
            print("\n")
        elif(num == 0):
            exit(0)
        else:
            print("Вы ввели некорректный номер функции. Попробуйте ещё раз\n")
def menu():
    print("1. Сложение/вычитание/умножение/деление матриц")
    print("2. Объединение массивов")
    print("0. Выход")
def fun_1(s):
    a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    b = a.copy()[::-1, ::-1]
    if(s == "+"):
        print("a\n", a)
        print("b\n", b)
        print("a + b\n", a + b)
    elif(s == "-"):
        print("a\n", a)
        print("b\n", b)
        print("a - b\n", a - b)
    elif(s == "*"):
        print("a\n", a)
        print("b\n", b)
        print("a * b\n", a * b)
    elif(s == "/"):
        print("a\n", a)
        print("b\n", b)
        print("a / b\n", a // b)
def fun_2():
    a = np.array([[1, 2, 3], [4, 5, 6]])
    b = a[::-1]
    c = a[:, ::-1]
    print("a\n", a)
    print("\nb\n", b)
    print("\nc\n", c)
    print("\nstack(a, b, c)\n", np.stack((a, b, c)))
if __name__ == '__main__':
    main()
