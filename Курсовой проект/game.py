from tkinter import *
from PIL import ImageTk, Image

money = 1
upgrade = 1


def main():

    def upgradeCPU():  
        global money
        global upgrade
        if money >= 50:
            money -= 50
            upgrade += 5
        UpgradeText.set("{}$".format(upgrade))
        MoneyText.set("{}$".format(money))


    def click():  
        global money
        global upgrade
        money += upgrade
        MoneyText.set("{}$".format(money))
    
    def save1():
        f = open('prof.txt', 'w')
        f.writelines("\n".join(box1.get(0, END)))
        f.close()

    # Создание объекта окна верхнего уровня (на нём будут распологаться все элементы
    mainwindow = Tk()
    # Задание размера окна и его координат расположения
    mainwindow.geometry("580x340+700+300")
    mainwindow.title("Симулятор программиста")
    mainwindow["bg"] = "gray22"
    mainmenu = Menu(mainwindow)
    mainwindow.config(menu=mainmenu)
    helpmenu = Menu(mainmenu, tearoff=0)
    helpmenu2 = Menu(helpmenu, tearoff=0)
    mainmenu.add_cascade(label="О игре",menu=helpmenu)
    helpmenu.add_cascade(label="Информация",menu=helpmenu2)
    helpmenu2.add_command(label="Версия v0.1",)
    helpmenu2.add_separator()
    helpmenu2.add_command(label="Секретный код - GE5GS",)
    helpmenu.add_separator()
    helpmenu.add_command(label="Выход",)

    MoneyText = StringVar()
    MoneyText.set("{}$".format(upgrade))
    UpgradeText = StringVar()
    UpgradeText.set("{}$".format(upgrade))
    
    img = ImageTk.PhotoImage(Image.open("img\comp.png"))
    img2 = ImageTk.PhotoImage(Image.open("img\cart.png"))
    img3 = ImageTk.PhotoImage(Image.open("img\money.png"))
    img4 = ImageTk.PhotoImage(Image.open("img\shop\cpu.png"))
    img5 = ImageTk.PhotoImage(Image.open("img\shop.png"))
    img6 = ImageTk.PhotoImage(Image.open("img\logo.png"))
    img7 = ImageTk.PhotoImage(Image.open("img\shop\card.png"))
    img8 = ImageTk.PhotoImage(Image.open("img\shop\oram.png"))
    img9 = ImageTk.PhotoImage(Image.open("img\logoshop.png"))

    Logo = Label(mainwindow, background="gray22", image=img6)
    Logo.place(x=28, y=0)
    LogoShop = Label(mainwindow, background="#414141", image=img9)
    LogoShop.place(x=10, y=85)

    lb3 = Label(mainwindow, text="Магазин", background="#414141", font = ('Arial' , 15), foreground="#ccc")
    lb3.place(x=53, y=89)
    b4 = Label(mainwindow, background="#414141", image=img2)
    b4.place(x=18, y=87)
    
    MoneyEntry = Label(mainwindow, image=img3, background="gray22")
    MoneyEntry.place(x=220, y=12)
    ShopEntry = Label(mainwindow, image=img5, background="#414141")
    ShopEntry.place(x=10, y=123)
    lb1 = Label(mainwindow, textvariable=MoneyText, font = ('Arial' , 40), background="#414141", foreground="#ccc")
    lb1.place(x=230, y=14)
    lb2 = Label(mainwindow, text="Заработок за нажатие:", background="#414141", foreground="#ccc")
    lb2.place(x=230, y=70)
    lb1 = Label(mainwindow, textvariable=UpgradeText, background="#414141", foreground="#ccc")
    lb1.place(x=359, y=70)

    b2 = Button(mainwindow, background="#414141", relief = 'flat', image=img4, activebackground="#333333", command=upgradeCPU)
    b2.place(x=36, y=130)
    lb7 = Label(mainwindow, text="CPU", background="#414141", foreground="#ccc")
    lb7.place(x=49, y=190)
    lb8 = Label(mainwindow, text="Цена: 50$", background="#414141", foreground="#ccc")
    lb8.place(x=36, y=210)
    lb9 = Label(mainwindow, text="Заработок: 5$", background="#414141", foreground="#ccc")
    lb9.place(x=26, y=230)

    b5 = Button(mainwindow, background="#414141", relief = 'flat', image=img7, activebackground="#333333", command=upgradeCPU)
    b5.place(x=134, y=138)
    lb4 = Label(mainwindow, text="Videocard", background="#414141", foreground="#ccc")
    lb4.place(x=131, y=190)
    lb5 = Label(mainwindow, text="Цена: 1000$", background="#414141", foreground="#ccc")
    lb5.place(x=126, y=210)
    lb6 = Label(mainwindow, text="Заработок: 25$", background="#414141", foreground="#ccc")
    lb6.place(x=116, y=230)

    b6 = Button(mainwindow, background="#414141", relief = 'flat', image=img8, activebackground="#333333", command=upgradeCPU)
    b6.place(x=226, y=133)
    lb10 = Label(mainwindow, text="Ram", background="#414141", foreground="#ccc")
    lb10.place(x=239, y=190)
    lb11 = Label(mainwindow, text="Цена: 10000$", background="#414141", foreground="#ccc")
    lb11.place(x=218, y=210)
    lb12 = Label(mainwindow, text="Заработок: 50$", background="#414141", foreground="#ccc")
    lb12.place(x=211, y=230)


    b3 = Button(mainwindow, text="Сохранить и выйти", relief = 'flat', background="#555", foreground="#ccc", activebackground="#333333", width=15, height=1)
    b3.place(x=165, y=280)
    b3 = Button(mainwindow, text="Ввести код", relief = 'flat', background="#555", foreground="#ccc", activebackground="#333333", width=15, height=1)
    b3.place(x=45, y=280)
    clickbtn = Button(mainwindow, background="gray22", relief = 'flat', image=img, activebackground="#333333", command=click)
    clickbtn.place(x=320, y=100)


    

    # Запуск цикла обработки событий
    mainloop()


if __name__ == '__main__':
    main()
