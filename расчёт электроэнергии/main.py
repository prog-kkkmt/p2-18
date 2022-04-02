#Программа для расчёта электроэнергии

from tkinter import *

root = Tk()

root.geometry('800x500+500+250')

cost_t = 3.91
cost_v = 2.87
temp = 0

def tcost():
    costlabel.configure(text=str(cost_t)+"руб квт/ч")

    global temp

    temp = cost_t

    print (temp)

def vcost():
    costlabel.configure(text=str(cost_v)+"руб квт/ч")
    global temp
    temp = cost_v
    print(temp)



town = Button(text="Город", height=10, width=15, bd=4, command=tcost)
town.grid(row=0, column=0, rowspan=3)

village = Button(text="Деревня", height=10, width=15, bd=4, command=vcost)
village.grid(row=0, column=1, rowspan=3)

cost_name_label = Label(text="текущий курс")
cost_name_label.grid(row=0, column=3)

costlabel = Label()
costlabel.grid(row=0, column=4)

inf_label = Label(text="введите количество киловат" )
inf_label.grid(row=1, column=3)

text_en = Entry()
text_en.grid(row=1, column=5)


st_label = Label(text="Стоимость")
st_label.grid(row=2, column=3)

res_label = Label(text="here")
res_label.grid(row=2, column=4)


def count():

    textr = float(text_en.get())
    print(textr)

    if temp == cost_t:
         res_label.configure(text=textr * cost_t)
    elif temp == cost_v:
        res_label.configure(text=textr * cost_v)
    else:
        res_label.configure(text="error")

fin = Button(text="расчитать", command=count)
fin.grid(row=2, column=3)

root.mainloop()