# Выполнил: Кузнецов Матвей
# Группа: П2-18
# 11. Кинотеатр
#
# Таблицы:
# Зал (Код зала, вместимость);
# Фильм (Код фильма, Название, Жанр);
# Продажа (Код продажи, Код фильм   а, Код зала, Время, Номер места).
#
# Определить:
# - Процент наполнения зала по сеансам;
# - Самый популярный жанр.

from tkinter import *
import os

CWD = os.getcwd()


def main():
    def hall_doc():
        def killer():
            root1.destroy()
            return main()
        root.destroy()
        root1 = Tk()
        root1.title('Окно редактирования файла Hall')
        root1.geometry('800x600+400+400')

        def add_to():
            with open('Hall.txt') as f:
                HallList = [line.split() for line in f]

        def view():
            os.startfile(CWD + '\\Hall.txt')

        add_to_Button = Button(root1, text='Добавить', command=add_to).grid(row=0, column=0)
        editButton = Button(root1, text='Изменить').grid(row=1, column=0)
        deleteButton = Button(root1, text='Удалить').grid(row=2, column=0)
        viewButton = Button(root1, text='Просмотреть', command=view).grid(row=3, column=0)
        back_button = Button(root1, text='Назад', command=killer).grid(row=4, column=0)

    def film_doc():
        def killer():
            root1.destroy()
            return main()
        root.destroy()
        root1 = Tk()
        root1.title('Окно редактирования файла Film')
        root1.geometry('800x600+400+400')

        def view():
            os.startfile(CWD + '\\Film.txt')

        add_to_Button = Button(root1, text='Добавить').grid(row=0, column=0)
        editButton = Button(root1, text='Изменить').grid(row=1, column=0)
        deleteButton = Button(root1, text='Удалить').grid(row=2, column=0)
        viewButton = Button(root1, text='Просмотреть', command=view).grid(row=3, column=0)
        back_button = Button(root1, text='Назад', command=killer).grid(row=4, column=0)

    def sale_doc():
        def killer():
            root1.destroy()
            return main()
        root.destroy()
        root1 = Tk()
        root1.title('Окно редактирования файла Sale')
        root1.geometry('800x600+400+400')

        def view():
            os.startfile(CWD + '\\Sale.txt')

        add_to_Button = Button(root1, text='Добавить').grid(row=0, column=0)
        editButton = Button(root1, text='Изменить').grid(row=1, column=0)
        deleteButton = Button(root1, text='Удалить').grid(row=2, column=0)
        viewButton = Button(root1, text='Просмотреть', command=view).grid(row=3, column=0)
        back_button = Button(root1, text='Назад', command=killer).grid(row=4, column=0)


    root = Tk()
    root.title('Основное окно')
    root.geometry('800x600+400+400')
    hall_file_button = Button(root, text='Изменение информации по залам      ', command=hall_doc).grid(row=0, column=0)
    film_file_button = Button(root, text='Изменение информации по фильмам', command=film_doc).grid(row=1, column=0)
    sale_file_button = Button(root, text='Изменение информации по ценам      ', command=sale_doc).grid(row=2, column=0)

    mainloop()


# HallFileButton = Button(root, text='Добавить', command=Add_to).grid(row=0, column=0)
# add_to_Button = Button(root, text = 'Добавить', command = Add_to).grid(row = 0, column = 0)
# editButton = Button(root, text = 'Изменить', command = Edit).grid(row = 1, column = 0)
# deleteButton = Button(root, text = 'Удалить', command = Delete).grid(row = 2, column = 0)
# viewButton = Button(root, text = 'Просмотреть', command = View).grid(row = 3, column = 0)


if __name__ == '__main__':
    main()


'''with open('Hall.txt') as f:
    HallList = [line.split() for line in f]

with open('Film.txt') as f:
    FilmList = [line.split() for line in f]

with open('Sale.txt') as f:
    SaleList = [line.split() for line in f]'''