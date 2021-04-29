from tkinter import *



def save():
    str =get_name() + ' ' +  delo_get()
    with open("egednevnik.txt", "a") as f:
        f.write(str + '\n')
def delo_get():
    return my_var.get()
def get_name():
    return my_var2.get()




root = Tk()

root.title('Ежедневник')
root.geometry('300x250+940+300')

my_var = StringVar('')
my_var2 = StringVar('')

root.resizable(width=False, height=False)

canvas = Canvas(root, height=300, width=250)
canvas.pack()

frame = Frame(root)
frame.place(relwidth=1, relheight=1)

title = Label(frame, text='вид события', font=40).grid(row=0, column=0)

dela = ('дело', 'встреча', 'звонок')


vidInput = Spinbox(frame, width=12, values=dela, font=40, command=delo_get, textvariable=my_var).grid(row=1, column=0)

title1 = Label(frame, text='названия события', font=40).grid(row=2, column=0)

vidInput = Entry(frame, bg='white', textvariable=my_var2).grid(row=3, column=0)

title2 = Label(frame, text='приоритет', font=40)
title2.grid(row=4, column=0)
pr1 = Radiobutton(frame, text='1', value=1).grid(row=4, column=1)
pr2 = Radiobutton(frame, text='2', value=2).grid(row=4, column=2)
pr3 = Radiobutton(frame, text='3', value=3).grid(row=4, column=3)

btn = Button(frame, text='сохранить в текстовик', command=save).grid(row=5, column=0)




root.mainloop()


