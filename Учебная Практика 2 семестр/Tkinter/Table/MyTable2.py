from tkinter import *

    # Создание объекта окна верхнего уровня (на нём будут распологаться все элементы
    root = Tk()
    # Задание размера окна и его координат расположения
    root.geometry("300x300+700+300")
    mainmenu = Menu(root)
    root.config(menu=mainmenu)
    # StringVar используется для легкого отслеживания изменений в переменных tkinter
    my_var = StringVar('')
    my_var2 = StringVar('')
    my_var3 = StringVar('')

    def file():
        print("1")

    b = Button(root, text="Добавить", width=25, height=2, command=file).grid(row=9, column=1, columnspan=2)

