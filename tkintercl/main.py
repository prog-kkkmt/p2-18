from tkinter import *
from tkinter import messagebox

# Функция save сохраняет введённые данные в строку и записывает строчку в файл

def on_closing():
    if messagebox.askokcancel("Выход из приложения", "Хотите выйти из приложения?"):
        root.destroy()
def save():
    str = get_marsh() + ' ' + naz_get() + ' ' + get_tim() + ' ' + get_dif() + '\n' + get_ruk() + ' ' + get_fio() + ' ' + get_tel() + '\n' + gru_get() + ' ' + get_nazgru() + ' ' + get_kodmarch() + ' ' + get_kodruk() + ' ' + get_koltur() + ' ' + get_data()
    with open("marshrut.txt", "a") as f:
        f.write(str + '\n')
# Функция delete очищает текстовоый файл полностью
def delete():
    f = open('marshrut.txt', 'w+')
    f.seek(0)
    f.close()
# Функция naz_get возвращает имя введённое пользователем
def naz_get():
    return my_var.get()
# Функция get_marsh возвращает имя введённое пользователем
def get_marsh():
    return my_var2.get()
# Функция get_tim возвращает имя введённое пользователем
def get_tim():
    return my_var3.get()
# Функция get_dif возвращает имя введённое пользователем
def get_dif():
    return my_var4.get()
# Функция get_ruk возвращает имя введённое пользователем
def get_ruk():
    return my_var5.get()
# Функция get_fio возвращает имя введённое пользователем
def get_fio():
    return my_var6.get()
# Функция get_tel возвращает имя введённое пользователем
def get_tel():
    return my_var7.get()
# Функция gru_get возвращает имя введённое пользователем
def gru_get():
    return my_var8.get()
# Функция get_nazgru возвращает имя введённое пользователем
def get_nazgru():
    return my_var9.get()
# Функция get_kodmarch возвращает имя введённое пользователем
def get_kodmarch():
    return my_var10.get()
# Функция get_kodruk возвращает имя введённое пользователем
def get_kodruk():
    return my_var11.get()
# Функция get_koltur возвращает имя введённое пользователем
def get_koltur():
    return my_var12.get()
# Функция get_data возвращает имя введённое пользователем
def get_data():
    return my_var13.get()


def windowopen():
    def on_closing_1():
            if messagebox.askokcancel("Выход из приложения", "Хотите выйти из приложения?"):
                new_window_1.destroy()

 
                
    new_window_1 = Toplevel(frame)
    new_window_1.title("Диограмма")
    new_window_1.resizable(0, 0)
    new_window_1.protocol("WM_DELETE_WINDOW", on_closing_1)
    canvas_1 = Canvas(new_window_1, width=300, height=250)
    canvas_1.pack()

root = Tk()
root.protocol("WM_DELETE_WINDOW", on_closing)
root.geometry(f"{450}x{450}+740+300")

# StringVar используется для легкого отслеживания изменений в переменных tkinter
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

canvas = Canvas(width=300, height=250)
canvas.pack()

frame = Frame()
frame.place(relwidth=1, relheight=1)


lable1 = Label(frame, text='заполните поля и сохраните', fg='white', bg='black').place(relx=.2, rely=.81)
lable2 = Label(frame, text='Маршрут', fg='white', bg='black').grid(row=0, column=1)
lable3 = Label(frame, text='Руководители', fg='white', bg='black').grid(row=5, column=1)
lable4 = Label(frame, text='Группы', fg='white', bg='black').grid(row=9, column=1)
# Первые данные
title = Label(frame, text='код маршрута').grid(row=1, column=0)
marshInput = Entry(frame, bg='white', textvariable=my_var2).grid(row=1, column=1)
title1 = Label(frame, text='название маршрута').grid(row=2, column=0)
nazInput = Entry(frame, bg='white', textvariable=my_var).grid(row=2, column=1)
title2 = Label(frame, text='продолжительность').grid(row=3, column=0)
timInput = Entry(frame, bg='white', textvariable=my_var3).grid(row=3, column=1)
title3 = Label(frame, text='категория сложности').grid(row=4, column=0)
difInput = Entry(frame, bg='white', textvariable=my_var4).grid(row=4, column=1)
# Вторые данные
title4 = Label(frame, text='код руководителя').grid(row=6, column=0)
rukInput = Entry(frame, bg='white', textvariable=my_var5).grid(row=6, column=1)
title5 = Label(frame, text='ФИО').grid(row=7, column=0)
fioInput = Entry(frame, bg='white', textvariable=my_var6).grid(row=7, column=1)
title6 = Label(frame, text='телефон').grid(row=8, column=0)
telInput = Entry(frame, bg='white', textvariable=my_var7).grid(row=8, column=1)
# Третие данные
title7 = Label(frame, text='Код группы').grid(row=10, column=0)
gruInput = Entry(frame, bg='white', textvariable=my_var8).grid(row=10, column=1)
title8 = Label(frame, text='Название группы').grid(row=11, column=0)
nazgruInput = Entry(frame, bg='white', textvariable=my_var9).grid(row=11, column=1)
title9 = Label(frame, text='Код маршрута').grid(row=12, column=0)
kodmarchInput = Entry(frame, bg='white', textvariable=my_var10).grid(row=12, column=1)
title10 = Label(frame, text='Код руководителя').grid(row=13, column=0)
kodrukInput = Entry(frame, bg='white', textvariable=my_var11).grid(row=13, column=1)
title11 = Label(frame, text='Количество туристов').grid(row=14, column=0)
kolturInput = Entry(frame, bg='white', textvariable=my_var12).grid(row=14, column=1)
title12 = Label(frame, text='Дата отправления').grid(row=15, column=0)
dataInput = Entry(frame, bg='white', textvariable=my_var13).grid(row=15, column=1)
# Кнопки

btn = Button(frame, text='сохранить в txt', command=save).place(relx=.29, rely=.75)
btn2 = Button(frame, text='очищение txt', command=delete).place(relx=.8, rely=.938)
btn3 = Button(frame, text='Диограмма', command=windowopen).place(relx=.6, rely=.938)
# Запуск цикла обработки событий
mainloop()

