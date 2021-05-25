import random
from tkinter import *

result = 0

class Dice_4d:
    "4d dice"

    def __init__(self, d=4):
        self.d = d

    def show_result(self):
        global result
        result = random.randint(1, self.d)


class Dice_6d:
    "6d dice"

    def __init__(self, d=6):
        self.d = d

    def show_result(self):
        global result
        result = random.randint(1, self.d)


class Dice_8d:
    "8d dice"

    def __init__(self, d=8):
        self.d = d

    def show_result(self):
        global result
        result = random.randint(1, self.d)


class Dice_12d:
    "12d dice"

    def __init__(self, d=12):
        self.d = d

    def show_result(self):
        global result
        result = random.randint(1, self.d)


class Dice_20d:
    "20d dice"

    def __init__(self, d=20):
        self.d = d

    def show_result(self):
        global result
        result = random.randint(1, self.d)


root = Tk()

root.geometry('600x400')


# Type buttons
def type_select():

    if t_var.get() == 4:
        dice = Dice_4d()
        dice.show_result()

    elif t_var.get() == 6:
        dice = Dice_6d()
        dice.show_result()

    elif t_var.get() == 8:
        dice = Dice_8d()
        dice.show_result()

    elif t_var.get() == 12:
        dice = Dice_12d()
        dice.show_result()

    elif t_var.get() == 20:
        dice = Dice_20d()
        dice.show_result()

type_label = Label(text="Choose type of dice")
type_label.pack()

t_var = IntVar()
t_var.set(0)

t_frame = Frame(root)

type_1 = Radiobutton(t_frame, text="d4", variable=t_var, value=4,
                     command=type_select)
type_1.pack(side=LEFT)

type_2 = Radiobutton(t_frame, text="d6", variable=t_var, value=6,
                     command=type_select)
type_2.pack(side=LEFT)

type_3 = Radiobutton(t_frame, text="d8", variable=t_var, value=8,
                     command=type_select)
type_3.pack(side=LEFT)

type_4 = Radiobutton(t_frame, text="d12", variable=t_var, value=12,
                     command=type_select)
type_4.pack(side=LEFT)

type_5 = Radiobutton(t_frame, text="d20", variable=t_var, value=20,
                     command=type_select)
type_5.pack(side=LEFT)

t_frame.pack()


# Amount buttons

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

"""
# dices frame
dices_frame = Frame(root)
dice_1_label = Label(width=20, height=10, bg='yellow')
dice_1_label.place(relx=0.25, rely=0.25)
dice_2_label = Label(width=20, height=10, bg='red')
dice_2_label.place(relx=0.55, rely=0.25)
dices_frame.pack(side=TOP)
"""
# result frame
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

# roll button

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
