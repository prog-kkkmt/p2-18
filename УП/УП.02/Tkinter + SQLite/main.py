#Импортируем библиотеки и подключаем второй файл
from tkinter import *
import backend


main_win = Tk() #Создание главного окна
main_win.title("Менеджер книжного магазина") #Меняем название
main_win["bg"] = "#555D50"

#При нажатии на строку в списке автоматически заполняем поля ввода данных(помогает если вы удалили что-то случайно из списка и хотите вернуть)
def get_selected_row(event):
    global selected_tuple
    index = list_box.curselection()[0]
    selected_tuple = list_box.get(index)
    e_title.delete(0, END)
    e_title.insert(END, selected_tuple[1])
    e_author.delete(0, END)
    e_author.insert(END, selected_tuple[2])
    e_year.delete(0, END)
    e_year.insert(END, selected_tuple[3])
    e_price.delete(0, END)
    e_price.insert(END, selected_tuple[4])

    
#Настройка кнопок
def view_command(): #Вывести строки из базы данных на экран
    list_box.delete(0, END)
    for row in backend.view():
        list_box.insert(END, row)

def search_command(): #Поиск по тегам
    list_box.delete(0, 100)
    for row in backend.search(title_text.get(), author_text.get(), year_text.get(), price_text.get()):
        list_box.insert(END, row)
    e_title.delete(0, END)
    e_author.delete(0, END)
    e_year.delete(0, END)
    e_price.delete(0, END)


def add_command(): #Добавить строку в базу данных
    backend.insert(title_text.get(), author_text.get(), year_text.get(), price_text.get())
    list_box.delete(0, END)
    list_box.insert(END,(title_text.get(), author_text.get(), year_text.get(), price_text.get()))
    e_title.delete(0, END)
    e_author.delete(0, END)
    e_year.delete(0, END)
    e_price.delete(0, END)

    
def update_command(): #Изменить строку в базе данных
    backend.update(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), price_text.get())
    view_command()

def delete_command(): #Удалить строку из базы данных
    backend.delete(selected_tuple[0])
    view_command()
    

#Названия и вводы данных
l_title = Label(main_win, text = "Название", bg = "#C2B280")
l_title.grid(row = 0, column =0)
title_text = StringVar()
e_title = Entry(main_win, textvariable = title_text)
e_title.grid(row = 0, column = 1)

l_author = Label(main_win, text = "Автор",bg = "#C2B280")
l_author.grid(row = 0, column = 2)
author_text = StringVar()
e_author = Entry(main_win, textvariable = author_text)
e_author.grid(row = 0, column = 3)

l_year = Label(main_win, text = "Год выпуска",bg = "#C2B280")
l_year.grid(row = 1, column = 0)
year_text = StringVar()
e_year = Entry(main_win, textvariable = year_text)
e_year.grid(row = 1, column = 1)

l_price = Label(main_win, text = "Цена",bg = "#C2B280")
l_price.grid(row = 1, column = 2)
price_text = StringVar()
e_price = Entry(main_win, textvariable = price_text)
e_price.grid(row = 1, column = 3)

list_box = Listbox(main_win, height = 8 , width = 55)
list_box.grid(row = 2, column = 0, rowspan = 6, columnspan = 2)
list_box.bind("<<ListboxSelect>>", get_selected_row)

#Кнопки
b_view = Button(main_win, text = "Список", width = 10, bg = "#EFDFBB",command = view_command)
b_view.grid(row = 2, column =3)

b_search = Button(main_win, text = "Найти", width = 10, bg = "#EFDFBB",command = search_command)
b_search.grid(row = 3, column = 3)

b_add = Button(main_win, text = "Добавить", width = 10, bg = "#EFDFBB",command = add_command)
b_add.grid(row = 4, column =3)

b_update = Button(main_win, text = "Обновить", width = 10, bg = "#EFDFBB",command = update_command)
b_update.grid(row = 5, column = 3)

b_delete = Button(main_win, text = "Удалить", width = 10, bg = "#EFDFBB",command = delete_command)
b_delete.grid(row = 6, column = 3)

b_exit = Button(main_win, text = "Выход", width = 10, bg = "#EFDFBB",command = main_win.destroy)
b_exit.grid(row = 7, column = 3)


main_win.mainloop()#Вывод приложения на экран
