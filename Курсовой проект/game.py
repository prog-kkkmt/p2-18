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
    mainwindow.geometry("530x340+700+300")
    mainwindow.title("Симулятор программиста - Дом")
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

    MoneyEntry = Label(mainwindow, image=img3, background="gray22")
    MoneyEntry.place(x=190, y=12)
    ShopEntry = Label(mainwindow, image=img5, background="gray22")
    ShopEntry.place(x=10, y=123)
    lb1 = Label(mainwindow, textvariable=MoneyText, font = ('Arial' , 40), background="#414141", foreground="#ccc")
    lb1.place(x=200, y=14)
    lb2 = Label(mainwindow, text="Заработок за нажатие:", background="#414141", foreground="#ccc")
    lb2.place(x=200, y=70)
    lb1 = Label(mainwindow, textvariable=UpgradeText, background="#414141", foreground="#ccc")
    lb1.place(x=329, y=70)
    lb3 = Label(mainwindow, text="Магазин", background="gray22", foreground="#ccc")
    lb3.place(x=85, y=89)
    b2 = Button(mainwindow, background="#414141", relief = 'flat', image=img4, command=upgradeCPU)
    b2.place(x=30, y=130)
    lb3 = Label(mainwindow, text="CPU", background="#414141", foreground="#ccc")
    lb3.place(x=43, y=190)
    lb3 = Label(mainwindow, text="Цена: 50$", background="#414141", foreground="#ccc")
    lb3.place(x=30, y=210)
    lb3 = Label(mainwindow, text="Заработок: 5$", background="#414141", foreground="#ccc")
    lb3.place(x=20, y=230)
    b4 = Label(mainwindow, background="gray22", image=img2)
    b4.place(x=54, y=83)
    b3 = Button(mainwindow, text="Сохранить и выйти", relief = 'flat', background="#555", foreground="#ccc", width=15, height=1)
    b3.place(x=148, y=280)
    b3 = Button(mainwindow, text="Ввести код", relief = 'flat', background="#555", foreground="#ccc", width=15, height=1)
    b3.place(x=28, y=280)
    clickbtn = Button(mainwindow, background="gray22", relief = 'flat', image=img, command=click)
    clickbtn.place(x=280, y=100)


    

    # Запуск цикла обработки событий
    mainloop()


if __name__ == '__main__':
    main()
