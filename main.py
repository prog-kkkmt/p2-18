from tkinter import *

def save():
    str = get_marsh() + ' ' + gru_get()
    with open("tur_club.txt", "a") as f:
        f.write(str + '\n')
def gru_get():
    return my_var.get()
def get_marsh():
    return my_var2.get()

root = Tk()

root.title('Туристский клуб')
root.geometry('300x200+740+300')

root.resizable(width=False, height=False)

my_var = StringVar('')
my_var2 = StringVar('')

canvas = Canvas(root, width=300, height=250)
canvas.pack()

frame = Frame(root)
frame.place(relwidth=1, relheight=1)

title = Label(frame, text='код маршрута').grid(row=0, column=0)
marshInput = Entry(frame, bg='white', textvariable=my_var2).grid(row=1, column=0)

title = Label(frame, text='название группы').grid(row=2, column=0)
gruInput = Entry(frame, bg='white', textvariable=my_var).grid(row=3, column=0)

btn = Button(frame, text='сохранить в txt', command=save).grid(row=4, column=0)



root.mainloop()