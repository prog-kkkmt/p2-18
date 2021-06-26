#выполнил Завадский М.А, Джабраилов Т.А
import numpy


def main():
    # Бесконечно выводим меню в консоль, пока пользователь не введёт 0
    while(True):
        menu()
        print("Введите цифру меню: ")
        num = int(input())
        if(num == 1):
            print("Введите функцию(-, +, *, /):")
            s = input()
            function_1(s)
            print("\n")
        elif(num == 2):
            function_2()
            print("\n")
        elif(num == 3):
            function_3()
            print("\n")
        elif(num == 4):
            function_4()
            print("\n")
        elif(num == 0):
            # Выход из программы
            exit(0)
        else:
            print("Вы ввели не корректный номер функции. Попробуйте ещё раз\n")


# Функция menu обеспечивает вывод меню в консоль
def menu():
    print("Доброго времени суток, представляю вам небольшой\
 инструментарий от NumPy. Выберите необходимый номер и посмотрите что выведет.")
    print("1. Сложение/вычитание/умножение/деление матриц")
    print("2. Объединение массивов")
    print("3. Транспонирование")
    print("4. Разбиваем одномерный массив на многомерный")
    print("0. Выход")

# Функция function_1 выводит в консоль пример сложения/вычитания/деления/умножения матриц
def function_1(s):
    A = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    B = A.copy()[::-1, ::-1]
    if(s == "+"):
        print("A\n", A)
        print("B\n", B)
        print("A + B\n", A + B)
    elif(s == "-"):
        print("A\n", A)
        print("B\n", B)
        print("A - B\n", A - B)
    elif(s == "*"):
        print("A\n", A)
        print("B\n", B)
        print("A * B\n", A * B)
    elif(s == "/"):
        print("A\n", A)
        print("B\n", B)
        print("A / B\n", A // B)

# Функция function_2 выводит в консоль пример объединения двух матриц в одну
def function_2():
    A = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    B = A[::-1]
    C = A[:, ::-1]
    print("A\n", A)
    print("\nB\n", B)
    print("\nC\n", C)
    print("\nstack(A, B, C)\n", numpy.stack((A, B, C)))

# Функция function_3 выводит в консоль пример транспонирования матрицы
def function_3():
    A = numpy.array([[1, 2, 3], [4, 5, 6]])
    print('A\n', A)

    B = A.T
    print('\nА транспонированный\n', B)

# Функция function_4 выводит в консоль пример разбиения одномерного массива на многомерный
def function_4():
    A = numpy.arange(24)
    B = A.reshape(4, 6)
    C = A.reshape(4, 3, 2)
    print("Массив размером 1х1\n", A)
    print('\nМассив размером 4х6\n', B)
    print('\nМассив размером 4х3х2\n', C)


if __name__ == '__main__':
    main()
