from tkinter import *
from tkinter import ttk
import sqlite3

def main():

    def savedBD(namebd, nametb):
        conn = sqlite3.connect(namebd)
        curs = conn.cursor()
        curs.execute("DELETE FROM " + nametb)
        a = []
        for l, i in enumerate(mainlist.get(0, END)):
            a.append([])
            for j in i.split('  '):
                a[l].append(j)
        curs.executemany("INSERT INTO " + nametb + " VALUES (?, ?, ?)", a)
        conn.commit()

    def update(self):
        if str(tab.select()) == str(tab3):
            conn = sqlite3.connect('EmployeeBD')
            curs = conn.cursor()
            *grid, = curs.execute("""SELECT *
                                    FROM Employee""")
            mainlist.delete(0, END)
            for i in grid:
                mainlist.insert(END, str(i[0]) + '  ' + str(i[1]) + '  ' + \
                                    str(i[2]))

        else:
            conn = sqlite3.connect('TeaShopBD')
            curs = conn.cursor()
            *grid, = curs.execute("""SELECT *
                                    FROM TeaShop""")
            mainlist.delete(0, END)
            for i in grid:
                mainlist.insert(END, str(i[0]) + '  ' + str(i[1]) + '  ' + \
                                    str(i[2]))
    
    def add():
        if ProductText.get() and AmountProductText.get() and PriceText.get():
            mainlist.insert(END, ProductText.get() + '  ' \
                            + AmountProductText.get() + '  ' + PriceText.get())
            ProductText.set('')
            AmountProductText.set('')
            PriceText.set('')
            savedBD("TeaShopBD", "TeaShop")
    
    def add2():
        if NewNameText.get() and NewSecNameText.get() and NewPostText.get():
            mainlist.insert(END, NewNameText.get() + '  ' \
                            + NewSecNameText.get() + '  ' + NewPostText.get())
            NewNameText.set('')
            NewSecNameText.set('')
            NewPostText.set('')
            savedBD("EmployeeBD", "Employee")

    def remove(self):
        select = list(mainlist.curselection())
        mainlist.delete(select)
        if str(tab.select()) == str(tab3):
            savedBD("EmployeeBD", "Employee")
        else:
            savedBD("TeaShopBD", "TeaShop")

    def changee():
        select = list(mainlist.curselection())
        if ProductText.get() and \
            AmountProductText.get() and PriceText.get() and select:
            mainlist.delete(select)
            mainlist.insert(select, ProductText.get() + '  ' \
                            + AmountProductText.get() + '  ' + PriceText.get())
            ProductText.set('')
            AmountProductText.set('')
            PriceText.set('')
            savedBD("TeaShopBD", "TeaShop")


    tk = Tk()
    tk.title('TeaShop')
    tk.geometry('580x290+700+300')
    '570'

    tab = ttk.Notebook(tk)
    tab1 = ttk.Frame(tab)
    tab2 = ttk.Frame(tab)
    tab3 = ttk.Frame(tab)
    tab.add(tab1, text='Создание заявки')
    tab.add(tab2, text='Изменение заявки')
    tab.add(tab3, text='Сотрудники')
    
    #--------------------------------------------------------
    ProductText = StringVar()
    AmountProductText = StringVar()
    PriceText = StringVar()
    NewNameText = StringVar()
    NewSecNameText = StringVar()
    NewPostText = StringVar()
    

    #--------------------------------------------------------
    newProduct = Label(tab1, text = 'Новый товар').place(x=20, y=10)
    changeProduct = Label(tab2, text = 'Изменить название товар').place(x=20, y=10)
    newName = Label(tab3, text = 'Добавить имя').place(x=20, y=10)

    newAmountProduct = Label(tab1, text = 'Количество товара.').place(x=20, y=50) 
    changeAmountProduct = Label(tab2, text = 'Изменить кол-во товара').place(x=20, y=50)
    'y=130'
    newSecName = Label(tab3, text = 'Добавить фамилию').place(x=20, y=50)


    newPrice = Label(tab1, text = 'Цена за шт.').place(x=20, y=90)
    changePrice = Label(tab2, text = 'Изменить цену').place(x=20, y=90)
    'y=170'
    newPost = Label(tab3, text = 'Добавить должность').place(x=20, y=90)

    #--------------------------------------------------------
    newProductIn = Entry(tab1, width=20, textvariable=ProductText).place(x=20, y=30)
    newAmountProductIn = Entry(tab1, width=20, textvariable=AmountProductText).place(x=20, y=70)
    'y=175'
    newPriceIn = Entry(tab1, width=20, textvariable=PriceText).place(x=20, y=110)
    'y=215'

    changeProductIn = Entry(tab2, width=20, textvariable=ProductText).place(x=20, y=30)
    changeAmountProductIn = Entry(tab2, width=20, textvariable=AmountProductText).place(x=20, y=70)
    'y=150'
    changePriceIn = Entry(tab2, width=20, textvariable=PriceText).place(x=20, y=110)
    'y=190'

    newNameIn = Entry(tab3, width=20, textvariable=NewNameText).place(x=20, y= 30)
    newSecNameIn = Entry(tab3, width=20, textvariable=NewSecNameText).place(x=20, y= 70)
    newPostIn = Entry(tab3, width=20, textvariable=NewPostText).place(x=20, y= 110)

    #--------------------------------------------------------
    button = Button(tab1, text ='Добавить', width=17, command=add).place(x=20, y=220)
    button = Button(tab2, text ='Изменить', width=17, command=changee).place(x=20, y=220)
    button = Button(tab3, text ='Добавить', width=17, command=add2).place(x=20, y=220)

    mainlist = Listbox(tk, width=53, height=14, font='Courier 8')
    mainlist.place(x=170, y=40)


    mainlist.bind('<Delete>', remove)
    tab.bind('<<NotebookTabChanged>>', update)

    tab.pack(expand=1, fill='both')

    #update()
    mainloop()


if __name__ == '__main__':
    main()