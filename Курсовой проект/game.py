from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import sqlite3
from settings import *

'''Функция для покупки оперативной памяти'''
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

    # Обновление переменных в интерфейсе игры
    UpgradeText.set("{}".format(int(upgrade)))
    MoneyText.set("{}".format(int(money)))
    PriceRAMset.set("{}".format(int(priceRAM)))
    MoneyRAMset.set("{}".format(int(moneyRAM)))
    KolVoRAMset.set("{}".format(int(KolVoRAM)))

'''Функция для покупки процессора'''
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

    # Обновление переменных в интерфейсе игры
    UpgradeText.set("{}".format(int(upgrade)))
    MoneyText.set("{}".format(int(money)))
    PriceCPUset.set("{}".format(int(priceCPU)))
    MoneyCPUset.set("{}".format(int(moneyCPU)))
    KolVoCPUset.set("{}".format(int(KolVoCPU)))

'''Функция для покупки видеокарты'''
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

    # Обновление переменных в интерфейсе игры
    UpgradeText.set("{}".format(int(upgrade)))
    MoneyText.set("{}".format(int(money)))
    PriceCARDset.set("{}".format(int(priceCARD)))
    MoneyCARDset.set("{}".format(int(moneyCARD)))
    KolVoCARDset.set("{}".format(int(KolVoCARD)))

'''Функция для считывания нажатия по кнопке'''
def click():  
    global money
    global upgrade
    money += upgrade

    # Обновление переменных в интерфейсе игры
    MoneyText.set("{}".format(int(money)))

'''Функция для создания дочернего окна, в который пользователь будет вводить секретный код'''
def code():
    
    '''Функция для проверки секретного кода и получение бонусов за правильный ввод'''
    def secret() :
        global money
        global upgrade
        global SecretCodeActive

        # Проверка введеного кода
        if SecretCodeEN.get() == 'P2-18_ZN':

            # Проверка не введен ли код дважды
            if SecretCodeActive == 0:
                SecretCodeActive = 1
                
                # Получение бонусов
                money = 10000
                upgrade += 10

                # Обновление переменных в интерфейсе игры
                UpgradeText.set("{}".format(int(upgrade)))
                MoneyText.set("{}".format(int(money)))

                # Уведомление о активации кода
                codebg2 = Label(code, background="gray22", image=img10)
                codebg2.place(x=1,y=155)
                lb21 = Label(code, text="Код активирован", background="gray22", foreground="#ccc")
                lb21.place(x=53, y=155)
            else:
                # Уведомление о повторной активации кода
                codebg2 = Label(code, background="gray22", image=img10)
                codebg2.place(x=1,y=155)
                lb21 = Label(code, text="Код уже был активирован", background="gray22", foreground="#ccc")
                lb21.place(x=28, y=155)
        else:
            # Уведомление о ошибки активации кода
            codebg2 = Label(code, background="gray22", image=img10)
            codebg2.place(x=1,y=155)
            lb21 = Label(code, text="Ошибка активации кода", background="gray22", foreground="#ccc")
            lb21.place(x=33, y=155)

    # Создание дочернего окна       
    code = Toplevel(mainwindow)
    code.title("Ввод кода")
    code.geometry("200x175+480+380")
    code["bg"] = "gray22"
    ico = Image.open('img\Icon.ico')
    photo = ImageTk.PhotoImage(ico)
    code.wm_iconphoto(False,photo)

    # Переменная для ввода кода
    SecretCodeEN = StringVar()

    # Интерфейс дочернего окна
    codebg = Label(code, background="#414141", image=img11)
    codebg.place(x=1,y=20)
    b18 = Button(code, text="Подтвердить", relief = 'flat', background="#555", font = ('Arial' , 13), foreground="#ccc", activebackground="#333333", width=15, height=1, command=secret)
    b18.place(x=30, y=110)
    en1 = Entry(code, width=15, textvariable=SecretCodeEN, background="gray22", relief = 'flat', font = ('Arial' , 13), foreground="#ccc")
    en1.place(x=33, y=74)
    lb19 = Label(code, text="Введите код", background="#414141", font = ('Arial' , 20), foreground="#ccc")
    lb19.place(x=19, y=25)

'''Функция для сохранение при выходе из игры'''
def save():
    global money
    global upgrade 
    global priceRAM 
    global moneyRAM 
    global KolVoRAM 
    global priceCPU 
    global moneyCPU 
    global KolVoCPU 
    global priceCARD 
    global moneyCARD 
    global KolVoCARD

    # Создание списка для записи в базу данных
    save = [('1','money', money),
            ('2','upgrade ', upgrade),
            ('3','priceRAM', priceRAM),
            ('4','moneyRAM', moneyRAM),
            ('5','KolVoRAM', KolVoRAM),
            ('6','priceCPU', priceCPU),
            ('7','moneyCPU', moneyCPU),
            ('8','KolVoCPU',  KolVoCPU),
            ('9','priceCARD', priceCARD),
            ('10','moneyCARD', moneyCARD),
            ('11','KolVoCARD', KolVoCARD),
            ('12', 'SecretCodeActive', SecretCodeActive)]

    # Удаление старой таблицы
    curs.execute('DELETE FROM Save')

    # Запись списка в таблицу
    curs.executemany('INSERT INTO Save VALUES (?, ?, ?)' , save)

    # Сохранение базы данных
    conn.commit()

    # Создание окна предупреждения перед выходом из игры
    if messagebox.askokcancel('Выход', '                 Прогресс сохранен\nВы действительно хотите закрыть игру?'):
        mainwindow.destroy()

# Создание главного окна игры
mainwindow = Tk()
mainwindow.geometry("580x360+700+300")
mainwindow.title("Симулятор программиста")
ico = Image.open('img\Icon.ico')
photo = ImageTk.PhotoImage(ico)
mainwindow.wm_iconphoto(False,photo)
mainwindow["bg"] = "gray22"
mainwindow.protocol('WM_DELETE_WINDOW', save)
mainmenu = Menu(mainwindow)
mainwindow.config(menu=mainmenu)

# Создание меню с информацией
helpmenu = Menu(mainmenu, tearoff=0)
helpmenu2 = Menu(helpmenu, tearoff=0)
mainmenu.add_cascade(label="О игре",menu=helpmenu)
helpmenu.add_cascade(label="Информация",menu=helpmenu2)
helpmenu2.add_command(label="Версия v1.1",)
helpmenu2.add_separator()
helpmenu2.add_command(label="Секретный код - P2-18_ZN",)
helpmenu.add_separator()
helpmenu.add_command(label="Выход",)

# Переменные для обновления интерфейса игры
MoneyText = StringVar()
MoneyText.set("{}".format(int(money)))
UpgradeText = StringVar()
UpgradeText.set("{}".format(int(upgrade)))

PriceRAMset = StringVar()
PriceRAMset.set("{}".format(int(priceRAM)))
MoneyRAMset = StringVar()
MoneyRAMset.set("{}".format(int(moneyRAM)))
KolVoRAMset = StringVar()
KolVoRAMset.set("{}".format(int(KolVoRAM)))

PriceCPUset = StringVar()
PriceCPUset.set("{}".format(int(priceCPU)))
MoneyCPUset = StringVar()
MoneyCPUset.set("{}".format(int(moneyCPU)))
KolVoCPUset = StringVar()
KolVoCPUset.set("{}".format(int(KolVoCPU)))

PriceCARDset = StringVar()
PriceCARDset.set("{}".format(int(priceCARD)))
MoneyCARDset = StringVar()
MoneyCARDset.set("{}".format(int(moneyCARD)))

PriceCARDset = StringVar()
PriceCARDset.set("{}".format(int(priceCARD)))
MoneyCARDset = StringVar()
MoneyCARDset.set("{}".format(int(moneyCARD)))
KolVoCARDset = StringVar()
KolVoCARDset.set("{}".format(int(KolVoCARD)))

# Переменные с изображениями
img = ImageTk.PhotoImage(Image.open("img\comp.png"))
img2 = ImageTk.PhotoImage(Image.open("img\cart.png"))
img3 = ImageTk.PhotoImage(Image.open("img\money.png"))
img4 = ImageTk.PhotoImage(Image.open("img\shop\cpu.png"))
img5 = ImageTk.PhotoImage(Image.open("img\shop.png"))
img6 = ImageTk.PhotoImage(Image.open("img\logo.png"))
img7 = ImageTk.PhotoImage(Image.open("img\shop\card.png"))
img8 = ImageTk.PhotoImage(Image.open("img\shop\oram.png"))
img9 = ImageTk.PhotoImage(Image.open("img\logoshop.png"))
img10 = ImageTk.PhotoImage(Image.open("img\error.png"))
img11 = ImageTk.PhotoImage(Image.open("img\codebg.png"))

# Показ лого и создание фонового оформления игры
Logo = Label(mainwindow, background="gray22", image=img6)
Logo.place(x=28, y=0)
LogoShop = Label(mainwindow, background="#414141", image=img9)
LogoShop.place(x=10, y=85)

# Вкладка 'Магазин'
lb3 = Label(mainwindow, text="Магазин", background="#414141", font = ('Arial' , 15), foreground="#ccc")
lb3.place(x=53, y=89)
b4 = Label(mainwindow, background="#414141", image=img2)
b4.place(x=18, y=87)

# Создание окна с информацией о счете в игре
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

# Создание товара для покупки в магазине
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
lb25 = Label(mainwindow, text="Уровень:", background="#414141", foreground="#ccc")
lb25.place(x=33, y=250)
lb26 = Label(mainwindow, textvariable=KolVoRAMset, background="#414141", foreground="#ccc")
lb26.place(x=87, y=250)

# Создание окна с информацией о счете в игре
b5 = Button(mainwindow, background="#414141", relief = 'flat', image=img4, activebackground="#333333", command=upgradeCPU)
b5.place(x=130, y=130)
lb4 = Label(mainwindow, text="CPU", background="#414141", foreground="#ccc")
lb4.place(x=143, y=190)
lb5 = Label(mainwindow, text="Цена:", background="#414141", foreground="#ccc")
lb5.place(x=126, y=210)
lb15 = Label(mainwindow, textvariable=PriceCPUset, background="#414141", foreground="#ccc")
lb15.place(x=160, y=210)
lb6 = Label(mainwindow, text="Заработок:", background="#414141", foreground="#ccc")
lb6.place(x=116, y=230)
lb16 = Label(mainwindow, textvariable=MoneyCPUset, background="#414141", foreground="#ccc")
lb16.place(x=180, y=230)
lb23 = Label(mainwindow, text="Уровень:", background="#414141", foreground="#ccc")
lb23.place(x=126, y=250)
lb24 = Label(mainwindow, textvariable=KolVoCPUset, background="#414141", foreground="#ccc")
lb24.place(x=180, y=250)

# Создание окна с информацией о счете в игре
b6 = Button(mainwindow, background="#414141", relief = 'flat', image=img7, activebackground="#333333", command=upgradeCARD)
b6.place(x=223, y=139)
lb10 = Label(mainwindow, text="Videocard", background="#414141", foreground="#ccc")
lb10.place(x=222, y=190)
lb11 = Label(mainwindow, text="Цена:", background="#414141", foreground="#ccc")
lb11.place(x=218, y=210)
lb17 = Label(mainwindow, textvariable=PriceCARDset, background="#414141", foreground="#ccc")
lb17.place(x=251, y=210)
lb12 = Label(mainwindow, text="Заработок:", background="#414141", foreground="#ccc")
lb12.place(x=211, y=230)
lb17 = Label(mainwindow, textvariable=MoneyCARDset, background="#414141", foreground="#ccc")
lb17.place(x=275, y=230)
lb22 = Label(mainwindow, text="Уровень:", background="#414141", foreground="#ccc")
lb22.place(x=221, y=250)
lb25 = Label(mainwindow, textvariable=KolVoCARDset, background="#414141", foreground="#ccc")
lb25.place(x=275, y=250)

# Кнопка для открытия дочернего окна
b3 = Button(mainwindow, text="Ввести код", relief = 'flat', background="#555", foreground="#ccc", activebackground="#333333", width=15, height=1, command=code)
b3.place(x=103, y=290)

# Кнопка для запуска функции которая считывает нажатия
clickbtn = Button(mainwindow, background="gray22", relief = 'flat', image=img, activebackground="#333333", command=click)
clickbtn.place(x=320, y=100)

# Запуск цикла обработки событий
mainloop()
