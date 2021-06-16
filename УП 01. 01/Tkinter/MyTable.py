#Выполнил: Кузнецов Матвей
#Группа: П2-18
'''
from tkinter import *

def main():
    #Функция save сохраняет введённые данные в строку и записывает строчку в файл
    def save():
        str = get_name() + ' ' + group_get() + ' ' + show_parametrs() + m_g()
        with open("test.txt", "a") as f:
            f.write(str + '\n')

    # Функция group_get возвращает выбранную группу пользователем
    def group_get():
        return my_var.get()

    # Функция show_parametrs возвращает все языки, которые выбрал пользователь
    def show_parametrs():
        str = ""
        for name, var in parametrs:
            if var.get():
                str += name + ' '
        return str

    # Функция get_name возвращает имя введённое пользователем
    def get_name():
        return my_var2.get()

    # Функция delete очищает текстовоый файл полностью
    def delete():
        f = open('test.txt', 'w+')
        f.seek(0)
        f.close()

    # Функция m_g возвращает выбранный пол пользователем
    def m_g():
        if v.get() == 1:
            return "Мужской"
        else:
            return "Женский"

    # Создание объекта окна верхнего уровня (на нём будут распологаться все элементы
    root = Tk()
    # Задание размера окна и его координат расположения
    root.geometry("300x300+700+300")
    # StringVar используется для легкого отслеживания изменений в переменных tkinter
    my_var = StringVar('')
    my_var2 = StringVar('')
    parametrs = (("Java", IntVar()), ("C#", IntVar()), ("C++", IntVar()),\
                 ("Python", IntVar()), ("Pascal", IntVar()))

    # Заполнение и задание расположения CheckBox'ов
    x, y = 2, 0
    for name, var in parametrs:
        Checkbutton(root, text=f"{name}", variable=var).grid(row=x, column=y)
        x += 1

    # Задаём местоположение текстовой метке и полю для ввода
    lb1 = Label(text="Имя:").grid(row=0, column=0)
    en = Entry(width=30, textvariable=my_var2).grid(row=0, column=1, columnspan=3)

    # Задаём местоположение текстовой метке и SpinBox'у(в котором находится список групп)
    lb2 = Label(text="Группа:").grid(row=1, column=0, columnspan=1)
    mas = ('П1-18', 'П2-18', 'П1-19', 'П2-19', 'П3-19')
    sb = Spinbox(width=7, values=mas, textvariable=my_var,\
                 command=group_get).grid(row=1, column=1)

    # Задаём местоположение кнопкам Save и Delete
    b = Button(root, text="Save", width=25, height=2, command=save).grid(row=9, column=1, columnspan=2)
    b1 = Button(root, text="Delete", width=25, height=2,\
                command=delete).grid(row=10, column=1, columnspan=2)

    # Создаём и задаём местоположение текстовой метке и RadioButton'ам
    v = IntVar()
    lb3 = Label(text="Пол:").grid(row=8, column=0)
    rb1= Radiobutton(root, text="Мужской", value=1,\
                     variable=v).grid(row=8, column=1, columnspan=1)
    rb2 = Radiobutton(root, text="Женский", value=2,\
                      variable=v).grid(row=8, column=2, columnspan=1)

    # Запуск цикла обработки событий
    mainloop()



if __name__ == '__main__':
    main()