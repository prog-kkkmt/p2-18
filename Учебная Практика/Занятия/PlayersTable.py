from tkinter import *
import sqlite3

# Создание классов для кнопок "Команды" и "Страны"
class ButtonsTeam:
    def __init__(self, var, px, py):

        self.var = var
        self.teambuttons = Button(text=self.var, width=7,
                                  command=self.teambutton).place(x=px, y=py)

    def teambutton(self):
        conn = sqlite3.connect('PlayersTable')
        curs = conn.cursor()
        *gridplayers, = curs.execute("""SELECT *
                                        FROM Players
                                        WHERE Team LIKE ?""", (self.var + '%',))
        mainlist.delete(0, END)
        for i in gridplayers:
            *i, = i
            rowtext.set(str(i[0]) + ' ' + str(i[1]) + '' + \
                        str(i[2]) + '   ' + str(i[3]) + '   ' + \
                        str(i[4]) + '   ' + str(i[5]))
            mainlist.insert(END, rowtext.get())

class ButtonsCountry:
    def __init__(self, var, px, py):

        self.i = 0
        self.var = var
        self.turn = IntVar()
        self.teambuttons = Checkbutton(text=self.var, command=self.teambutton,
                                       variable=self.turn).place(x=px, y=py)

    def teambutton(self):
        global grid
        conn = sqlite3.connect('PlayersTable')
        curs = conn.cursor()
        if self.turn.get() == 1:
            self.i = grid.index('')
            grid[self.i] = self.var
        else:
            grid[self.i] = ''
        *gridplayers, = curs.execute("""SELECT *
                                        FROM Players
                                        WHERE Country IN (?, ?, ?, ?, ?, ?, ?)
                                        ORDER BY Country""", grid)
        mainlist.delete(0, END)
        for i in gridplayers:
            *i, = i
            rowtext.set(str(i[0]) + ' ' + str(i[1]) + '' + \
                        str(i[2]) + '   ' + str(i[3]) + '   ' + \
                        str(i[4]) + '   ' + str(i[5]))
            mainlist.insert(END, rowtext.get())

#----------------------------------------------------------
# Функци для кнопок "Показать"
def getr():
    global rowtext, mainlist, ratingbox1, ratingbox2
    conn = sqlite3.connect('PlayersTable')
    curs = conn.cursor()
    *gridplayers, = curs.execute("""SELECT *
                                    FROM Players
                                    WHERE Rating BETWEEN ? AND ?
                                    ORDER BY Rating DESC""",\
                                    (float(ratingbox1.get()), float(ratingbox2.get())))
    mainlist.delete(0, END)
    for i in gridplayers:
        *i, = i
        rowtext.set(str(i[0]) + ' ' + str(i[1]) + ' ' + \
                    str(i[2]) + '   ' + str(i[3]) + '   ' + \
                    str(i[4]) + '   ' + str(i[5]))
        mainlist.insert(END, rowtext.get())

def getk():
    global rowtext, mainlist, killbox1, killbox2
    conn = sqlite3.connect('PlayersTable')
    curs = conn.cursor()
    *gridplayers, = curs.execute("""SELECT *
                                    FROM Players
                                    WHERE Kill_per_round BETWEEN ? AND ?
                                    ORDER BY Kill_per_round DESC""",\
                                    (float(killbox1.get()), float(killbox2.get())))
    mainlist.delete(0, END)
    for i in gridplayers:
        *i, = i
        rowtext.set(str(i[0]) + ' ' + str(i[1]) + '' + \
                    str(i[2]) + '   ' + str(i[3]) + '   ' + \
                    str(i[4]) + '   ' + str(i[5]))
        mainlist.insert(END, rowtext.get())

def geth():
    global rowtext, mainlist, hsbox1, hsbox2
    conn = sqlite3.connect('PlayersTable')
    curs = conn.cursor()
    *gridplayers, = curs.execute("""SELECT *
                                    FROM Players
                                    WHERE Headshot BETWEEN ? AND ?
                                    ORDER BY Headshot DESC""",\
                                    (hsbox1.get(), hsbox2.get()))
    mainlist.delete(0, END)
    for i in gridplayers:
        *i, = i
        rowtext.set(str(i[0]) + ' ' + str(i[1]) + '' + \
                    str(i[2]) + '   ' + str(i[3]) + '   ' + \
                    str(i[4]) + '   ' + str(i[5]))
        mainlist.insert(END, rowtext.get())

def getplayer():
    global rowtext, mainlist, namebox
    conn = sqlite3.connect('PlayersTable')
    curs = conn.cursor()
    *gridplayers, = curs.execute("""SELECT *
                                    FROM Players
                                    WHERE Name LIKE ?
                                    ORDER BY Name""",\
                                    ('%' + namebox.get() + '%',))
    mainlist.delete(0, END)
    for i in gridplayers:
        *i, = i
        rowtext.set(str(i[0]) + ' ' + str(i[1]) + '' + \
                    str(i[2]) + '   ' + str(i[3]) + '   ' + \
                    str(i[4]) + '   ' + str(i[5]))
        mainlist.insert(END, rowtext.get())

#----------------------------------------------------------
# Создание окна, иконки и переменных
tk = Tk()
tk.title('HLTV')
tk.geometry('680x370+700+300')
tk.call('wm', 'iconphoto', tk._w, PhotoImage(file='HLTV-logo.png'))

rowtext = StringVar()
grid = ['', '', '', '', '', '', '']

logo = Label(tk, text='HLTV', font='Arial 45').place(x=20, y=50)

nameplayer = StringVar()

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
nametext = Label(tk, text='Никнейм').place(x=20, y=155)
teamtext = Label(tk, text='Команды').place(x=200, y=5)
countrytext = Label(tk, text='Страны').place(x=280, y=5)
reatingtext = Label(tk, text='Рейтинг').place(x=20, y=215)
KDtext = Label(tk, text='K/D').place(x=130, y=220)
HStext = Label(tk, text='HS').place(x=240, y=220)

ButtonsTeam('NaVi', 200, 40)
ButtonsTeam('Gambit', 200, 73)
ButtonsTeam('Astralis', 200, 106)
ButtonsTeam('G2', 200, 139)
ButtonsTeam('Heroic', 200, 172)

ButtonsCountry('Rus', 280, 30)
ButtonsCountry('Ukr', 280, 55)
ButtonsCountry('Fra', 280, 80)
ButtonsCountry('Srb', 280, 105)
ButtonsCountry('Kaz', 280, 130)
ButtonsCountry('Bih', 280, 155)
ButtonsCountry('Dnk', 280, 180)

#----------------------------------------------------------
# Создание окон ввода и кнопок "Показать"
namebox = Entry(tk, width=13, textvariable=nameplayer)
namebox.place(x=20, y=180)

ratingbox1 = Entry(tk, width=15)
ratingbox1.place(x=20, y=245)
ratingtext = Label(tk, text='-').place(x=20, y=265)
ratingbox2 = Entry(tk, width=15)
ratingbox2.place(x=20, y=290)

killbox1 = Entry(tk, width=15)
killbox1.place(x=130, y=245)
killtext = Label(tk, text='-').place(x=130, y=265)
killbox2 = Entry(tk, width=15)
killbox2.place(x=130, y=290)

hsbox1 = Entry(tk, width=15)
hsbox1.place(x=240, y=245)
hstext = Label(tk, text='-').place(x=240, y=265)
hsbox2 = Entry(tk, width=15)
hsbox2.place(x=240, y=290)

namebutton = Button(tk, text='Показать', command=getplayer).place(x=110, y=173)
ratingbutton = Button(tk, text='Показать', command=getr).place(x=20, y=320)
killbutton = Button(tk, text='Показать', command=getk).place(x=130, y=320)
hsbutton = Button(tk, text='Показать', command=geth).place(x=240, y=320)
#----------------------------------------------------------
# Создание окна для показа таблици
maintext = Label(tk, text = 'Игроки').place(x=470, y=5)

mainlist = Listbox(tk, width=45, height=21, font='Courier 8')
mainlist.place(x=350, y=30)

mainloop()
