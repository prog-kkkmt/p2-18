from tkinter import *
from tkinter import ttk
import sqlite3

#----------------------------------------------------------
# Функци для кнопок "Показать"
def main():
    
    def getk():
        global rowtext, mainlist, Yearbox1, Yearbox2
        conn = sqlite3.connect('LibTable')
        curs = conn.cursor()
        *gridAuto, = curs.execute("""SELECT *
                                        FROM Lib
                                        WHERE Year BETWEEN ? AND ?
                                        ORDER BY Year DESC""",\
                                        (Yearbox1.get(), Yearbox2.get()))
        mainlist.delete(0, END)
        for i in gridAuto:
            *i, = i
            rowtext.set(str(i[0]) + ' ' + str(i[1]) + '' + \
                        str(i[2]) + '   ' + str(i[3]))
            mainlist.insert(END, rowtext.get())

    def geth():
        global rowtext, mainlist, Pricebox1, Pricebox2
        conn = sqlite3.connect('LibTable')
        curs = conn.cursor()
        *gridAuto, = curs.execute("""SELECT *
                                        FROM Lib
                                        WHERE Price BETWEEN ? AND ?
                                        ORDER BY Price DESC""",\
                                        (Pricebox1.get(), Pricebox2.get()))
        mainlist.delete(0, END)
        for i in gridAuto:
            *i, = i
            rowtext.set(str(i[0]) + ' ' + str(i[1]) + '' + \
                        str(i[2]) + '   ' + str(i[3]))
            mainlist.insert(END, rowtext.get())

    def getplayer():
        global rowtext, mainlist, namebox
        conn = sqlite3.connect('LibTable')
        curs = conn.cursor()
        *gridAuto, = curs.execute("""SELECT *
                                        FROM Lib
                                        WHERE Name LIKE ?
                                        ORDER BY Name""",\
                                        ('%' + namebox.get() + '%',))
        mainlist.delete(0, END)
        for i in gridAuto:
            *i, = i
            rowtext.set(str(i[0]) + ' ' + str(i[1]) + '' + \
                        str(i[2]) + '   ' + str(i[3]))
            mainlist.insert(END, rowtext.get())

    def getAuthor():
        global rowtext, mainlist, HPbox1
        conn = sqlite3.connect('LibTable')
        curs = conn.cursor()
        *gridAuto, = curs.execute("""SELECT *
                                        FROM Lib
                                        WHERE HP LIKE ?
                                        ORDER BY HP""",\
                                        ('%' + HPbox1.get() + '%',))
        mainlist.delete(0, END)
        for i in gridAuto:
            *i, = i
            rowtext.set(str(i[0]) + ' ' + str(i[1]) + '' + \
                        str(i[2]) + '   ' + str(i[3]))
            mainlist.insert(END, rowtext.get())




    def savedBD():
        conn = sqlite3.connect('LibTable')
        curs = conn.cursor()
        curs.execute("DELETE FROM Lib")
        a = []
        for l, i in enumerate(mainlist.get(0, END)):
            a.append([])
            for j in i.split('  '):
                a[l].append(j)
        curs.executemany("INSERT INTO Lib VALUES (?, ?, ?, ?)", a)
        conn.commit()

    def update():
        conn = sqlite3.connect('LibTable')
        curs = conn.cursor()
        *grid, = curs.execute("""SELECT *
                                FROM Lib""")
        mainlist.delete(0, END)
        for i in grid:
            mainlist.insert(END, str(i[0]) + '  ' + str(i[1]) + '  ' + \
                                str(i[2]) + '  ' + str(i[3]))
        
    def add():
        mainlist.insert(END, NameVar1.get() + '  ' \
                        + AuthorVar2.get() + '  ' \
                        + YearVar3.get() + '  ' \
                        + PriceVar4.get())
        NameVar1.set('')
        AuthorVar2.set('')
        YearVar3.set('')
        PriceVar4.set('')
        savedBD()

    def remove(self):
        select = list(mainlist.curselection())
        mainlist.delete(select)
        savedBD()

    def change():
        select = list(mainlist.curselection())
        mainlist.delete(select)
        mainlist.insert(select, NameVar1.get() + '  ' \
                        + AuthorVar2.get() + '  ' \
                        + YearVar3.get() + '  ' \
                        + PriceVar4.get())
        NameVar1.set('')
        AuthorVar2.set('')
        YearVar3.set('')
        PriceVar4.set('')
        savedBD()



    #----------------------------------------------------------
    # Создание окна, иконки и переменных
    tk = Tk()
    tk.title('Рабочее место библиотекаря')
    tk.geometry('1025x300+700+300')
    tk["bg"] = "gray22"

    tk.call('wm', 'iconphoto', tk._w, PhotoImage(file='lib-logo.png'))
    #logo = Label(tk, text='LIBRARY', font='Arial 45', background="gray22", foreground="#ccc").place(x=10, y=50)

    rowtext = StringVar()
    nameplayer = StringVar()
    NameVar1 = StringVar()
    AuthorVar2 = StringVar()
    YearVar3 = StringVar()
    PriceVar4 = StringVar()
    grid = ['', '', '', '', '', '', '']

    #----------------------------------------------------------
    # Создание названий разделов и кнопок
    nametext = Label(tk, text='Название', background="gray22", foreground="#ccc").place(x=20, y=35)
    HPtext = Label(tk, text='Автор', background="gray22", foreground="#ccc").place(x=20, y=95)
    Yeartext = Label(tk, text='Год', background="gray22", foreground="#ccc").place(x=20, y=160)
    Pricetext = Label(tk, text='Год выпуска', background="gray22", foreground="#ccc").place(x=20, y=220)
    searchtext = Label(tk, text='Поиск', background="gray22", foreground="#ccc").place(x=140, y=5)
    searchtext = Label(tk, text='Редактирование', background="gray22", foreground="#ccc").place(x=850, y=5)

    #----------------------------------------------------------
    # Создание окн ввода и кнопок "Показать"
    namebox = Entry(tk, width=15, textvariable=nameplayer)
    namebox.place(x=20, y=60)

    HPbox1 = Entry(tk, width=15)
    HPbox1.place(x=20, y=120)

    Yearbox1 = Entry(tk, width=15)
    Yearbox1.place(x=20, y=185)
    Yeartext = Label(tk, text='-', background="gray22", foreground="#ccc").place(x=120, y=183)
    Yearbox2 = Entry(tk, width=15)
    Yearbox2.place(x=135, y=185)

    Pricebox1 = Entry(tk, width=15)
    Pricebox1.place(x=20, y=245)
    Pricetext = Label(tk, text='-', background="gray22", foreground="#ccc").place(x=120, y=243)
    Pricebox2 = Entry(tk, width=15)
    Pricebox2.place(x=135, y=245)

    namebutton = Button(tk, text='Показать', relief = 'flat', background="#555", foreground="#ccc", activebackground="#333333", command=getplayer).place(x=125, y=57)
    HPbutton = Button(tk, text='Показать', relief = 'flat', background="#555", foreground="#ccc", activebackground="#333333", command=getAuthor).place(x=125, y=117)
    Yearbutton = Button(tk, text='Показать', relief = 'flat', background="#555", foreground="#ccc", activebackground="#333333", command=getk).place(x=240, y=182)
    Pricebutton = Button(tk, text='Показать', relief = 'flat', background="#555", foreground="#ccc", activebackground="#333333", command=geth).place(x=240, y=242)

    Namebox3 = Entry(tk, width=15, textvariable=NameVar1).place(x=780, y=60)
    Authorbox3 = Entry(tk, width=15, textvariable=AuthorVar2).place(x=780, y=120)
    Yearbox3 = Entry(tk, width=15, textvariable=YearVar3).place(x=780, y=185)
    Pricebox3 = Entry(tk, width=15, textvariable=PriceVar4).place(x=780, y=245)
    nametext = Label(tk, text='Название', background="gray22", foreground="#ccc").place(x=780, y=35)
    HPtext = Label(tk, text='Автор', background="gray22", foreground="#ccc").place(x=780, y=95)
    Yeartext = Label(tk, text='Год', background="gray22", foreground="#ccc").place(x=780, y=160)
    Pricetext = Label(tk, text='Год выпуска', background="gray22", foreground="#ccc").place(x=780, y=220)
    addbutton = Button(tk, text='Добавить', relief = 'flat', font='Arial 15', background="#555", foreground="#ccc", activebackground="#333333", command=add).place(x=900, y=115)
    delbutton = Button(tk, text='Изменить', relief = 'flat', font='Arial 15', background="#555", foreground="#ccc", activebackground="#333333", command=change).place(x=900, y=165)


    #----------------------------------------------------------
    # Создание окна для показа таблици
    maintext = Label(tk, text = 'Книги', background="gray22", foreground="#ccc").place(x=528, y=5)

    mainlist = Listbox(tk, width=55, height=17, font='Courier 8')
    mainlist.place(x=350, y=30)

    mainlist.bind('<Delete>', remove)

    update()
    mainloop()

if __name__ == '__main__':
    main()
