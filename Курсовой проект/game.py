from tkinter import *
from PIL import ImageTk, Image

money = 0
upgrade = 1

priceRAM = 50
moneyRAM = 5
KolVoRAM = 0

priceCPU = 5000
moneyCPU = 20
KolVoCPU = 0

priceCARD = 25000
moneyCARD = 60
KolVoCARD = 0

def main():

    def upgradeRAM():  
        global money
        global upgrade
        global priceRAM
        global moneyRAM
        global KolVoRAM
        if money >= priceRAM:
            money -= priceRAM
            upgrade += moneyRAM
            KolVoRAM += 1
            priceRAM = priceRAM*1.07**KolVoRAM
            moneyRAM += 1
        UpgradeText.set("{}$".format(int(upgrade)))
        MoneyText.set("{}$".format(int(money)))
        PriceRAMset.set("{}$".format(int(priceRAM)))
        MoneyRAMset.set("{}$".format(int(moneyRAM)))

    def upgradeCPU():  
        global money
        global upgrade
        global priceCPU
        global moneyCPU
        global KolVoCPU
        if money >= priceCPU:
            money -= priceCPU
            upgrade += moneyCPU
            KolVoCPU += 1
            priceCPU = priceCPU*1.07**KolVoCPU
            moneyCPU += 2
        UpgradeText.set("{}$".format(int(upgrade)))
        MoneyText.set("{}$".format(int(money)))
        PriceCPUset.set("{}$".format(int(priceCPU)))
        MoneyCPUset.set("{}$".format(int(moneyCPU)))

    def upgradeCARD():  
        global money
        global upgrade
        global priceCARD
        global moneyCARD
        global KolVoCARD
        if money >= priceCARD:
            money -= priceCARD
            upgrade += moneyCARD
            KolVoCARD += 1
            priceCARD = priceCARD*1.07**KolVoCARD
            moneyCARD += 5
        UpgradeText.set("{}$".format(int(upgrade)))
        MoneyText.set("{}$".format(int(money)))
        PriceCARDset.set("{}$".format(int(priceCARD)))
        MoneyCARDset.set("{}$".format(int(moneyCARD)))


    def click():  
        global money
        global upgrade
        money += upgrade
        MoneyText.set("{}$".format(int(money)))



    def code():

        def secret() :
            global money
            global upgrade
            if SecretCodeEN.get() == 'GE5GS':
                money = 9999999
                upgrade = 9999999
                UpgradeText.set("{}$".format(int(upgrade)))
                MoneyText.set("{}$".format(int(money)))
                lb21 = Label(code, text="Код активирован", background="gray22", foreground="#ccc")
                lb21.place(x=53, y=152)
            else:
                lb20 = Label(code, text="Код введен неверно", background="gray22", foreground="#ccc")
                lb20.place(x=43, y=152)

                
        code = Toplevel(mainwindow)
        code.title("Ввод кода")
        code.geometry("200x175+480+380")
        code["bg"] = "gray22"
        ico = Image.open('img\Icon.ico')
        photo = ImageTk.PhotoImage(ico)
        code.wm_iconphoto(False,photo)
        SecretCodeEN = StringVar()
        codebg = Label(code, background="gray22", image=img5)
        codebg.place(x=1,y=20)
        b18 = Button(code, text="Подтвердить", relief = 'flat', background="#555", font = ('Arial' , 13), foreground="#ccc", activebackground="#333333", width=15, height=1, command=secret)
        b18.place(x=30, y=110)
        en1 = Entry(code, width=15, textvariable=SecretCodeEN)
        en1.place(x=55, y=74)
        lb19 = Label(code, text="Введите код", background="#414141", font = ('Arial' , 20), foreground="#ccc")
        lb19.place(x=19, y=25)
    
    
    def save1():
        f = open('prof.txt', 'w')
        f.writelines("\n".join(box1.get(0, END)))
        f.close()

    # Создание объекта окна верхнего уровня (на нём будут распологаться все элементы)
    mainwindow = Tk()
    # Задание размера окна и его координат расположения
    mainwindow.geometry("580x360+700+300")
    mainwindow.title("Симулятор программиста")
    ico = Image.open('img\Icon.ico')
    photo = ImageTk.PhotoImage(ico)
    mainwindow.wm_iconphoto(False,photo)
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
    MoneyText.set("{}$".format(int(money)))
    UpgradeText = StringVar()
    UpgradeText.set("{}$".format(int(upgrade)))
    
    PriceRAMset = StringVar()
    PriceRAMset.set("{}$".format(int(priceRAM)))
    MoneyRAMset = StringVar()
    MoneyRAMset.set("{}$".format(int(moneyRAM)))

    PriceCPUset = StringVar()
    PriceCPUset.set("{}$".format(int(priceCPU)))
    MoneyCPUset = StringVar()
    MoneyCPUset.set("{}$".format(int(moneyCPU)))

    PriceCARDset = StringVar()
    PriceCARDset.set("{}$".format(int(priceCARD)))
    MoneyCARDset = StringVar()
    MoneyCARDset.set("{}$".format(int(moneyCARD)))
    
    
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

    b2 = Button(mainwindow, background="#414141", relief = 'flat', image=img8, activebackground="#333333", command=upgradeRAM)
    b2.place(x=37, y=130)
    lb7 = Label(mainwindow, text="RAM", background="#414141", foreground="#ccc")
    lb7.place(x=49, y=190)
    lb8 = Label(mainwindow, text="Цена:", background="#414141", foreground="#ccc")
    lb8.place(x=36, y=210)
    lb13 = Label(mainwindow, textvariable=PriceRAMset, background="#414141", foreground="#ccc")
    lb13.place(x=70, y=210)
    lb9 = Label(mainwindow, text="Заработок:", background="#414141", foreground="#ccc")
    lb9.place(x=26, y=230)
    lb14 = Label(mainwindow, textvariable=MoneyRAMset, background="#414141", foreground="#ccc")
    lb14.place(x=90, y=230)

    b5 = Button(mainwindow, background="#414141", relief = 'flat', image=img4, activebackground="#333333", command=upgradeCPU)
    b5.place(x=133, y=130)
    lb4 = Label(mainwindow, text="CPU", background="#414141", foreground="#ccc")
    lb4.place(x=146, y=190)
    lb5 = Label(mainwindow, text="Цена:", background="#414141", foreground="#ccc")
    lb5.place(x=126, y=210)
    lb15 = Label(mainwindow, textvariable=PriceCPUset, background="#414141", foreground="#ccc")
    lb15.place(x=160, y=210)
    lb6 = Label(mainwindow, text="Заработок:", background="#414141", foreground="#ccc")
    lb6.place(x=116, y=230)
    lb16 = Label(mainwindow, textvariable=MoneyCPUset, background="#414141", foreground="#ccc")
    lb16.place(x=180, y=230)

    b6 = Button(mainwindow, background="#414141", relief = 'flat', image=img7, activebackground="#333333", command=upgradeCARD)
    b6.place(x=227, y=139)
    lb10 = Label(mainwindow, text="Videocard", background="#414141", foreground="#ccc")
    lb10.place(x=226, y=190)
    lb11 = Label(mainwindow, text="Цена:", background="#414141", foreground="#ccc")
    lb11.place(x=218, y=210)
    lb17 = Label(mainwindow, textvariable=PriceCARDset, background="#414141", foreground="#ccc")
    lb17.place(x=251, y=210)
    lb12 = Label(mainwindow, text="Заработок:", background="#414141", foreground="#ccc")
    lb12.place(x=211, y=230)
    lb17 = Label(mainwindow, textvariable=MoneyCARDset, background="#414141", foreground="#ccc")
    lb17.place(x=275, y=230)


    b3 = Button(mainwindow, text="Сохранить", relief = 'flat', background="#555", foreground="#ccc", activebackground="#333333", width=15, height=1)
    b3.place(x=165, y=285)
    b3 = Button(mainwindow, text="Ввести код", relief = 'flat', background="#555", foreground="#ccc", activebackground="#333333", width=15, height=1, command=code)
    b3.place(x=45, y=285)
    clickbtn = Button(mainwindow, background="gray22", relief = 'flat', image=img, activebackground="#333333", command=click)
    clickbtn.place(x=320, y=100)

    # Запуск цикла обработки событий
    mainloop()


if __name__ == '__main__':
    main()
