'''
    Туристский клуб
 Туристский клуб организует одно – и многодневные пешеходные туры в группах с
руководителем по разным маршрутам и разной категории сложности.
 Таблицы: Маршруты (Код маршрута, название, продолжительность, категория сложности),
Руководители (Код руководителя, ФИО, телефон), Группы (Код группы, название группы,
код маршрута, код руководителя, количество туристов, дата отправления).
Требуется:
- определить перечень групп на маршруте;
- построить сравнительную диаграмму количества туристов по уровню сложности маршрутов.
'''
from tkinter import *
# Функция save сохраняет введённые данные в строку и записывает строчку в файл
def save():
    str = get_marsh() + ' ' + naz_get() + ' ' + get_tim() + ' ' + get_dif() +'\n'+ get_ruk() + ' ' + get_fio() + ' ' + get_tel() +'\n'+gru_get() + ' ' + get_nazgru() + ' ' + get_kodmarch() + ' ' + get_kodruk() + ' ' + get_koltur() + ' ' + get_data()
    with open("marshrut.txt", "a") as f:
        f.write(str + '\n')
# Функция get_name возвращает имя введённое пользователем
def naz_get():
    return my_var.get()
def get_marsh():
    return my_var2.get()
def get_tim():
    return my_var3.get()
def get_dif():
    return my_var4.get()
def get_ruk():
    return my_var5.get()
def get_fio():
    return my_var6.get()
def get_tel():
    return my_var7.get()
def gru_get():
    return my_var8.get()
def get_nazgru():
    return my_var9.get()
def get_kodmarch():
    return my_var10.get()
def get_kodruk():
    return my_var11.get()
def get_koltur():
    return my_var12.get()
def get_data():
    return my_var13.get()

root = Tk()

root.title('Туристский клуб')
root.geometry('450x450+740+300')

root.resizable(width=False, height=False)

my_var = StringVar('')
my_var2 = StringVar('')
my_var3 = StringVar('')
my_var4 = StringVar('')
my_var5 = StringVar('')
my_var6 = StringVar('')
my_var7 = StringVar('')
my_var8 = StringVar('')
my_var9 = StringVar('')
my_var10 = StringVar('')
my_var11 = StringVar('')
my_var12 = StringVar('')
my_var13 = StringVar('')

canvas = Canvas(root, width=300, height=250)
canvas.pack()

frame = Frame(root)
frame.place(relwidth=1, relheight=1)

lable1 = Label(frame, text='заполните поля и сохраните', fg='white', bg='black').place(relx=.2, rely=.81)
lable2 = Label(frame, text='Маршрут', fg='white', bg='black').grid(row=0, column=1)
lable3 = Label(frame, text='Руководители', fg='white', bg='black').grid(row=5, column=1)
lable4 = Label(frame, text='Группы', fg='white', bg='black').grid(row=9, column=1)
# Первые данные
title = Label(frame, text='код маршрута').grid(row=1, column=0)
marshInput = Entry(frame, bg='white', textvariable=my_var2).grid(row=1, column=1)
title = Label(frame, text='название маршрута').grid(row=2, column=0)
nazInput = Entry(frame, bg='white', textvariable=my_var).grid(row=2, column=1)
title = Label(frame, text='продолжительность').grid(row=3, column=0)
timInput = Entry(frame, bg='white', textvariable=my_var3).grid(row=3, column=1)
title = Label(frame, text='категория сложности').grid(row=4, column=0)
difInput = Entry(frame, bg='white', textvariable=my_var4).grid(row=4, column=1)
# Вторые данные
title = Label(frame, text='код руководителя').grid(row=6, column=0)
rukInput = Entry(frame, bg='white', textvariable=my_var5).grid(row=6, column=1)
title = Label(frame, text='ФИО').grid(row=7, column=0)
fioInput = Entry(frame, bg='white', textvariable=my_var6).grid(row=7, column=1)
title = Label(frame, text='телефон').grid(row=8, column=0)
telInput = Entry(frame, bg='white', textvariable=my_var7).grid(row=8, column=1)
# Третие данные
title = Label(frame, text='Код группы').grid(row=10, column=0)
gruInput = Entry(frame, bg='white', textvariable=my_var8).grid(row=10, column=1)
title = Label(frame, text='Название группы').grid(row=11, column=0)
nazgruInput = Entry(frame, bg='white', textvariable=my_var9).grid(row=11, column=1)
title = Label(frame, text='Код маршрута').grid(row=12, column=0)
kodmarchInput = Entry(frame, bg='white', textvariable=my_var10).grid(row=12, column=1)
title = Label(frame, text='Код руководителя').grid(row=13, column=0)
kodrukInput = Entry(frame, bg='white', textvariable=my_var11).grid(row=13, column=1)
title = Label(frame, text='Количество туристов').grid(row=14, column=0)
kolturInput = Entry(frame, bg='white', textvariable=my_var12).grid(row=14, column=1)
title = Label(frame, text='Дата отправления').grid(row=15, column=0)
dataInput = Entry(frame, bg='white', textvariable=my_var13).grid(row=15, column=1)


btn = Button(frame, text='сохранить в txt', command=save).place(relx=.29, rely=.75)

root.mainloop()