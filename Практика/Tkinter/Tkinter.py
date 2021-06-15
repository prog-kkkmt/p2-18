from tkinter import *


def main():

    def mainwindow1():

        def add1():
            box1.insert(END, en1.get() + ' ' + en2.get())
            en1.delete(0, END)
            en2.delete(0, END)

        def change1():
            select = list(box1.curselection())
            select.reverse()
            for i in select:
                box1.delete(i)
                box1.insert(i, en1.get() + ' ' + en2.get())
            en1.delete(0, END)
            en2.delete(0, END)

        def remove1():
            select = list(box1.curselection())
            select.reverse()
            for i in select:
                box1.delete(i)

        def save1():
            f = open('prof.txt', 'w')
            f.writelines("\n".join(box1.get(0, END)))
            f.close()




        # Создание объекта окна верхнего уровня (на нём будут распологаться все элементы
        root = Tk()
        # Задание размера окна и его координат расположения
        root.geometry("300x230+700+300")
        root["bg"] = "gray22"


        # Задаём местоположение текстовой метке и полю для ввода
        lb1 = Label(root,text="Код должности:", background="gray22", foreground="#ccc")
        lb1.place(x=2, y=16)
        en1 = Entry(root, width=15)
        en1.pack()
        en1.place(x=100, y=18)

        # Задаём местоположение текстовой метке и полю для ввода
        lb2 = Label(root,text="Название:", background="gray22", foreground="#ccc")
        lb2.place(x=15, y=48)
        en2 = Entry(root, width=15)
        en2.pack()
        en2.place(x=100, y=50)

        lb3 = Label(root,text="База данных:", background="gray22", foreground="#ccc")
        lb3.place(x=15, y=130)
        box1 = Listbox(root, selectmode=EXTENDED, width=15, height=8)
        box1.place(x=100, y=80)
        scroll1 = Scrollbar(root, command=box1.yview)
        scroll1.pack(side=RIGHT, fill=Y)
        box1.config(yscrollcommand=scroll1.set)

        b1 = Button(root, text="Добавить",background="#555", foreground="#ccc", width=10, height=1, command=add1)
        b1.place(x=200, y=87)
        b2 = Button(root, text="Изменить",background="#555", foreground="#ccc", width=10, height=1, command=change1)
        b2.place(x=200, y=117)
        b3 = Button(root, text="Удалить",background="#555", foreground="#ccc", width=10, height=1, command=remove1)
        b3.place(x=200, y=147)
        b4 = Button(root, text="Сохранить",background="#555", foreground="#ccc", width=10, height=1, command=save1)
        b4.place(x=200, y=177)

        with open('prof.txt', 'r') as f:
            lst = f.readlines()
 
        for item in lst:
            box1.insert(END, item)

    # Создание объекта окна верхнего уровня (на нём будут распологаться все элементы
    mainwindow = Tk()
    # Задание размера окна и его координат расположения
    mainwindow.geometry("300x230+700+300")
    mainwindow["bg"] = "gray22"
    mainmenu = Menu(mainwindow)
    mainwindow.config(menu=mainmenu)
    helpmenu = Menu(mainmenu, tearoff=0)
    helpmenu2 = Menu(helpmenu, tearoff=0)
    mainmenu.add_cascade(label="О программе",menu=helpmenu)
    helpmenu.add_cascade(label="Справка",menu=helpmenu2)
    helpmenu2.add_command(label="Открыть сайт",)
    helpmenu.add_separator()
    helpmenu.add_command(label="Выход",)

    lb1 = Label(mainwindow, text="Таблицы", background="gray22", foreground="#ccc")
    lb1.place(x=128, y=10)
    b1 = Button(mainwindow, text="Должности", background="#555", foreground="#ccc", width=15, height=1, command=mainwindow1)
    b1.place(x=100, y=50)
    

    # Запуск цикла обработки событий
    mainloop()



if __name__ == '__main__':
    main()
