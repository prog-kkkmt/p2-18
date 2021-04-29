from tkinter import *

def main():

    def get_name1():
        return 2
    
    def input1():
        global my_var
        my_var = 1
        menu()
    def input2():
        global my_var
        my_var = 2
        menu()
    def input3():
        global my_var
        my_var = 3
        menu()

    def menu():
        global text
        
        def kill():
            tk1.destroy()
            return main()
#----------------------------------------------------
        tk.destroy()
        tk1 = Tk()
        tk1.title('')
        tk1.geometry("300x300+900+400")

        tk1_but1 = Button(tk1, text='Добавить').grid(row=0, column=0)
        e_tk1_but1 = Entry(width=20, textvariable=text).grid(row=0, column=1)

        tk1_but2 = Button(tk1, text='Изменить').grid(row=1, column=0)
        s_tk1_but2 = Spinbox(width = 7, values = mas).grid(row=1, column=2)
        e_tk1_but2 = Entry(width=20, textvariable=text).grid(row=1, column=1)

        tk1_but3 = Button(tk1, text='  Удалить  ').grid(row=2, column=0)
        s_tk1_but3 = Spinbox(width = 7, values = mas).grid(row=2, column=1)
        
        tk1_but1 = Button(tk1, text='Back', command=kill).grid(row=10, column=0)
#----------------------------------------------------
    

    print(my_var)
    tk = Tk()
    tk.title('')
    tk.geometry("300x300+900+400")

    tk_but1 = Button(tk, text='Предметы', command=input1).grid(row=0, column=0)
    tk_but2 = Button(tk, text='Предметы', command=input2).grid(row=1, column=0)
    tk_but3 = Button(tk, text='Предметы', command=input3).grid(row=2, column=0)

    mainloop()
    
'''tk = Tk()

my_var = StringVar('')
tk.title('')
tk.geometry("300x300+500+300")

tk_but1 = Button(tk, text='Предметы', command=input).grid(row=0, column=0)

#Кнопки с соответствующеми строками ввода
inbut = Button(tk, text='Добавить', command=input).grid(row=0, column=0)
s_inbut = Entry(width=30, textvariable=my_var).grid(row=0, column=1)

but = Button(tk, text='Изменить').grid(row=1, column=0)
s_but = Entry(width=30, textvariable=my_var).grid(row=1, column=1)

delbut = Button(tk, text='Удалить все').grid(row=2, column=0)

outbut = Button(tk, text='Показать').grid(row=3, column=0)'''

my_var = 0
text = ''
mas = [1, 2, 3]
if __name__=='__main__':
    main()
