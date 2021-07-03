import random


result = 0
#Создаём класс для 4х гранного кубика и рандомом записываем число в результат
class Dice_4d:
    "4d dice"

    def __init__(self, d=4):
        self.d = d

    def show_result(self):
        global result
        result = random.randint(1, self.d)

#Создаём класс для 6х гранного кубика и рандомом записываем число в результат
class Dice_6d:
    "6d dice"

    def __init__(self, d=6):
        self.d = d

    def show_result(self):
        global result
        result = random.randint(1, self.d)

#Создаём класс для 8х гранного кубика и рандомом записываем число в результат
class Dice_8d:
    "8d dice"

    def __init__(self, d=8):
        self.d = d

    def show_result(self):
        global result
        result = random.randint(1, self.d)

#Создаём класс для 12х гранного кубика и рандомом записываем число в результат
class Dice_12d:
    "12d dice"

    def __init__(self, d=12):
        self.d = d

    def show_result(self):
        global result
        result = random.randint(1, self.d)

#Создаём класс для 20х гранного кубика и рандомом записываем число в результат
class Dice_20d:
    "20d dice"

    def __init__(self, d=20):
        self.d = d

    def show_result(self):
        global result
        result = random.randint(1, self.d)

#Создаём главное окно и настраиваем геометрию окна
root = Tk()

root.geometry('600x400')


# делаем виджет ждя выбора типа кубика
def type_select():
    # Делаем выбор на кубик 4x и выбираем его
    if t_var.get() == 4:
        dice = Dice_4d()
        dice.show_result()
    # Делаем выбор на кубик 6x и выбираем его
    elif t_var.get() == 6:
        dice = Dice_6d()
        dice.show_result()
    # Делаем выбор на кубик 8x и выбираем его
    elif t_var.get() == 8:
        dice = Dice_8d()
        dice.show_result()
    # Делаем выбор на кубик 12x и выбираем его
    elif t_var.get() == 12:
        dice = Dice_12d()
        dice.show_result()
    # Делаем выбор на кубик 20x и выбираем его
    elif t_var.get() == 20:
        dice = Dice_20d()
        dice.show_result()
#Делаем лейбл для выбора типа кубика и пакуем его
type_label = Label(text="Choose type of dice")
type_label.pack()

t_var = IntVar()
t_var.set(0)
# Делаем фрейм под выбор кубика
t_frame = Frame(root)
# Делаем выбор на кубик 4x и выбираем его
type_1 = Radiobutton(t_frame, text="d4", variable=t_var, value=4,
                     command=type_select)
type_1.pack(side=LEFT)
# Делаем выбор на кубик 6x и выбираем его
type_2 = Radiobutton(t_frame, text="d6", variable=t_var, value=6,
                     command=type_select)
type_2.pack(side=LEFT)
# Делаем выбор на кубик 8x и выбираем его
type_3 = Radiobutton(t_frame, text="d8", variable=t_var, value=8,
                     command=type_select)
type_3.pack(side=LEFT)
# Делаем выбор на кубик 12x и выбираем его
type_4 = Radiobutton(t_frame, text="d12", variable=t_var, value=12,
                     command=type_select)
type_4.pack(side=LEFT)
# Делаем выбор на кубик 20x и выбирем его
type_5 = Radiobutton(t_frame, text="d20", variable=t_var, value=20,
                     command=type_select)
type_5.pack(side=LEFT)

t_frame.pack()


# Ствим лейбл на выбор количества кубиуков

a_var = IntVar()
a_var.set(0)

am_label = Label(text="Choose amount of dices")
am_label.pack()

a_frame = Frame(root)

amount_1 = Radiobutton(a_frame, text="1", variable=a_var, value=1)
amount_1.pack(side=LEFT)

amount_2 = Radiobutton(a_frame, text="2", variable=a_var, value=2)
amount_2.pack(side=LEFT)

a_frame.pack()



# делаем вывод в лейбл с результатом выбранных типов и количеств кубиков
result_frame = Frame(root)

dice_1_frame = Label(width=10, height=2, text="Dice 1 result:")
dice_1_frame.place(relx=0.25, rely=0.3)
dice_2_frame = Label(width=10, height=2, text="Dice 2 result:")
dice_2_frame.place(relx=0.6, rely=0.3)

result_frame.pack()
# score frame

score_frame = Frame(root)

dice_1_label = Label(width=10, height=1, text="0")
dice_1_label.place(relx=0.25, rely=0.4)
dice_2_label = Label(width=10, height=1, text="0")
dice_2_label.place(relx=0.6, rely=0.4)

score_frame.pack()

# Делаем кнопку реролла кубиков

def roll():
    if a_var.get() == 1:
        dice_1_label.configure(text=result)
        type_select()
        dice_2_label.configure(text="0")
    elif a_var.get() == 2:
        dice_1_label.configure(text=result)
        type_select()
        dice_2_label.configure(text=result)
        type_select()

roll_button = Button(text="Roll",
                     width=15, height=1, command=roll)
roll_button.place(relx=0.4, rely=0.8)

root.mainloop()
