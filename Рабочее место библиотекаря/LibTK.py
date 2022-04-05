from tkinter import *
import sqlite3

# Создание классов для кнопоки "Страны"
class ButtonsCountry:
    def __init__(self, var, px, py):

        self.i = 0
        self.var = var
        self.turn = IntVar()
        self.Manufacturerbuttons = Checkbutton(text=self.var, command=self.Manufacturerbutton,
                                               background="gray22", foreground="#ccc", activebackground="#333333",
                                       variable=self.turn).place(x=px, y=py)

    # Сортировка и отображение
    def Manufacturerbutton(self):
        global grid
        conn = sqlite3.connect('LibTable')
        curs = conn.cursor()
        if self.turn.get() == 1:
            self.i = grid.index('')
            grid[self.i] = self.var
        else:
            grid[self.i] = ''
        *gridAuto, = curs.execute("""SELECT *
                                        FROM Lib
                                        WHERE Country IN (?, ?, ?, ?, ?, ?)
                                        ORDER BY Country""", grid)
        mainlist.delete(0, END)
        for i in gridAuto:
            *i, = i
            rowtext.set(str(i[0]) + ' ' + str(i[1]) + '' + \
                        str(i[2]) + '   ' + str(i[3]) + '   ' + \
                        str(i[4]) + '   ' + str(i[5]))
            mainlist.insert(END, rowtext.get())

#----------------------------------------------------------
# Функци для кнопок "Показать"
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
                    str(i[2]) + '   ' + str(i[3]) + '   ' + \
                    str(i[3]) + '   ' + str(i[4]))
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
                    str(i[2]) + '   ' + str(i[3]) + '   ' + \
                    str(i[3]) + '   ' + str(i[4]))
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
                    str(i[2]) + '   ' + str(i[3]) + '   ' + \
                    str(i[3]) + '   ' + str(i[4]))
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
                    str(i[2]) + '   ' + str(i[3]) + '   ' + \
                    str(i[3]) + '   ' + str(i[4]))
        mainlist.insert(END, rowtext.get())

#----------------------------------------------------------
# Создание окна, иконки и переменных
tk = Tk()
tk.title('Рабочее место библиотекаря')
tk.geometry('750x370+700+300')
tk["bg"] = "gray22"

tk.call('wm', 'iconphoto', tk._w, PhotoImage(file='lib-logo.png'))
logo = Label(tk, text='LIBRARY', font='Arial 45', background="gray22", foreground="#ccc").place(x=10, y=50)

rowtext = StringVar()
nameplayer = StringVar()
grid = ['', '', '', '', '', '', '']

#----------------------------------------------------------
# Создание названий разделов и кнопок
nametext = Label(tk, text='Название', background="gray22", foreground="#ccc").place(x=20, y=155)
countrytext = Label(tk, text='Страны', background="gray22", foreground="#ccc").place(x=280, y=5)
HPtext = Label(tk, text='Автор', background="gray22", foreground="#ccc").place(x=20, y=215)
Yeartext = Label(tk, text='Год', background="gray22", foreground="#ccc").place(x=130, y=220)
Pricetext = Label(tk, text='Цена', background="gray22", foreground="#ccc").place(x=240, y=220)

ButtonsCountry('Ger', 280, 30)
ButtonsCountry('Jap', 280, 55)
ButtonsCountry('Cze', 280, 80)
ButtonsCountry('Usa', 280, 105)
ButtonsCountry('Rus', 280, 130)
#ButtonsCountry('Bih', 280, 155)
#ButtonsCountry('Dnk', 280, 180)

#----------------------------------------------------------
# Создание окн ввода и кнопок "Показать"
namebox = Entry(tk, width=13, textvariable=nameplayer)
namebox.place(x=20, y=180)

HPbox1 = Entry(tk, width=15)
HPbox1.place(x=20, y=245)

Yearbox1 = Entry(tk, width=15)
Yearbox1.place(x=130, y=245)
Yeartext = Label(tk, text='-', background="gray22", foreground="#ccc").place(x=130, y=265)
Yearbox2 = Entry(tk, width=15)
Yearbox2.place(x=130, y=290)

Pricebox1 = Entry(tk, width=15)
Pricebox1.place(x=240, y=245)
Pricetext = Label(tk, text='-', background="gray22", foreground="#ccc").place(x=240, y=265)
Pricebox2 = Entry(tk, width=15)
Pricebox2.place(x=240, y=290)

namebutton = Button(tk, text='Показать', relief = 'flat', background="#555", foreground="#ccc", activebackground="#333333", command=getplayer).place(x=110, y=176)
HPbutton = Button(tk, text='Показать', relief = 'flat', background="#555", foreground="#ccc", activebackground="#333333", command=getAuthor).place(x=20, y=320)
Yearbutton = Button(tk, text='Показать', relief = 'flat', background="#555", foreground="#ccc", activebackground="#333333", command=getk).place(x=130, y=320)
Pricebutton = Button(tk, text='Показать', relief = 'flat', background="#555", foreground="#ccc", activebackground="#333333", command=geth).place(x=240, y=320)
#----------------------------------------------------------
# Создание окна для показа таблици
maintext = Label(tk, text = 'Книги', background="gray22", foreground="#ccc").place(x=538, y=5)

mainlist = Listbox(tk, width=55, height=21, font='Courier 8')
mainlist.place(x=350, y=30)

mainloop()
