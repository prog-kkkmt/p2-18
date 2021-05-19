from tkinter import *
import sqlite3

# Создание классов для кнопок "Марки" и "Страны"
class ButtonsMarka:
    def __init__(self, var, px, py):

        self.var = var
        self.markabuttons = Button(text=self.var, width=7,
                                  command=self.markabutton).place(x=px, y=py)

    def markabutton(self):
        conn = sqlite3.connect('MarkaTable')
        curs = conn.cursor()
        *gridmarka, = curs.execute("""SELECT *
                                      FROM Model
                                      WHERE Proiz LIKE ?""", (self.var + '%',))
        mainlist.delete(0, END)
        for i in gridmarka:
            *i, = i
            rowtext.set(str(i[0]) + ' ' + str(i[1]) + ' ' + str(i[2]))
            mainlist.insert(END, rowtext.get())

class ButtonsCountry:
    def __init__(self, var, px, py):

        self.i = 0
        self.var = var
        self.turn = IntVar()
        self.markabuttons = Checkbutton(text=self.var, command=self.markabutton,
                                       variable=self.turn).place(x=px, y=py)

    def markabutton(self):
        global grid
        conn = sqlite3.connect('MarkaTable')
        curs = conn.cursor()
        if self.turn.get() == 1:
            self.i = grid.index('')
            grid[self.i] = self.var
        else:
            grid[self.i] = ''
        *gridmarka, = curs.execute("""SELECT *
                                        FROM Model
                                        WHERE Country IN (?, ?, ?, ?, ?)
                                        ORDER BY Country, Proiz""", grid)
        mainlist.delete(0, END)
        for i in gridmarka:
            *i, = i
            rowtext.set(str(i[0]) + ' ' + str(i[1]) + '' + \
                        str(i[2]))
            mainlist.insert(END, rowtext.get())

#----------------------------------------------------------
# Функци для кнопок "Показать"
def getmarka():
    global rowtext, mainlist, namebox
    conn = sqlite3.connect('MarkaTable')
    curs = conn.cursor()
    *gridmarka, = curs.execute("""SELECT *
                                    FROM Model
                                    WHERE Model LIKE ?
                                    ORDER BY Model""",\
                                    ('%' + namebox.get() + '%',))
    mainlist.delete(0, END)
    for i in gridmarka:
        *i, = i
        rowtext.set(str(i[0]) + ' ' + str(i[1]) + '' + \
                    str(i[2]))
        mainlist.insert(END, rowtext.get())

#----------------------------------------------------------
# Создание окна и переменных
tk = Tk()
tk.title('Autodoc')
tk.geometry('540x380+700+300')

rowtext = StringVar()
grid = ['', '', '', '', '']


namemodel = StringVar()

#----------------------------------------------------------
'''
minr = DoubleVar()
maxr = DoubleVar()
mink = DoubleVar()
maxk = DoubleVar()
minh = DoubleVar()
maxh = DoubleVar()
'''
#----------------------------------------------------------
# Создание названий разделов и кнопок
nametext = Label(tk, text='Модель').place(x=180, y=340)
teamtext = Label(tk, text='Производитель').place(x=75, y=5)
countrytext = Label(tk, text='Страны').place(x=20, y=5)

ButtonsMarka('BMW', 89, 40)
ButtonsMarka('Mercedes', 89, 73)
ButtonsMarka('Hyndai', 89, 106)
ButtonsMarka('Kia', 89, 139)
ButtonsMarka('Toyota', 89, 172)
ButtonsMarka('Nissan', 89, 205)
ButtonsMarka('Fiat', 89, 238)
ButtonsMarka('Ferrari', 89, 271)
ButtonsMarka('Ford', 89, 304)
ButtonsMarka('Pontiac', 89, 337)

ButtonsCountry('De', 20, 30)
ButtonsCountry('Kr', 20, 55)
ButtonsCountry('Jp', 20, 80)
ButtonsCountry('It', 20, 105)
ButtonsCountry('Us', 20, 130)

#----------------------------------------------------------
# Создание окон ввода и кнопок "Показать"
namebox = Entry(tk, width=20, textvariable=namemodel)
namebox.place(x=240, y=343)

namebutton = Button(tk, text='Показать', command=getmarka).place(x=390, y=343)
#----------------------------------------------------------
# Создание окна для показа таблици
maintext = Label(tk, text = 'Список авто').place(x=310, y=5)

mainlist = Listbox(tk, width=45, height=20, font='Courier 8')
mainlist.place(x=180, y=30)

mainloop()