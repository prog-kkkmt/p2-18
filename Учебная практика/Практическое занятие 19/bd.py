"""
2. Автосалон.
Менеджеры автосалона осуществляют продажу клиентам автомобилей различных марок.

Таблицы: Покупатели (Код покупателя, ФИО), Менеджеры (Код менеджера, ФИО),
Автомобили (код, марка),
Продажи (Код менеджера, код автомобиля, государственный номер, код покупателя, дата, цена).

Данные сохраняются в txt файл "Autoservis.txt".
"""

from tkinter import *

def main():
    def save():
        str = get_code2()+' '+get_code1()+'\n'+get_code3()+' '+get_code4()+'\n'+get_code5()+' '+get_code6()+'\n'+get_code7()+' '+get_code8()+' '+get_code9()+' '+get_code10()+ ' '+get_code11()+' '+get_code12()
        with open ("Autoservis.txt", 'a') as f:
            f.write (str + '\n')

    def delete():
        f = open ("Autoservis.txt",  'w+')
        f.seek(0)
        f.close()
        
    def get_code1():
        return my_var1.get()

    def get_code2():
        return my_var2.get()

    def get_code3():
        return my_var3.get()

    def get_code4():
        return my_var4.get()

    def get_code5():
        return my_var5.get()

    def get_code6():
        return my_var6.get()

    def get_code7():
        return my_var7.get()

    def get_code8():
        return my_var8.get()

    def get_code9():
        return my_var9.get()

    def get_code10():
        return my_var10.get()

    def get_code11():
        return my_var11.get()

    def get_code12():
        return my_var12.get()

    root = Tk()
    root.title ("Autosalon")
    root.geometry ('500x400+800+250')

    my_var1 = StringVar('')
    my_var2 = StringVar('')
    my_var3 = StringVar('')
    my_var4 = StringVar('')
    my_var5 = StringVar('')
    my_var6 = StringVar('')
    my_var7 = StringVar('')
    my_var8 = StringVar('')
    my_var9 = StringVar('')
    my_var10 = StringVar('')
    my_var11 = StringVar('')
    my_var12 = StringVar('')
    
    #Покупатели
    lbl_p = Label (root, text = "Покупатели").grid(column = 0, row = 0)
    lbl_kp = Label (root, text = "Код покупателя").grid(column = 1, row = 0, columnspan = 1)
    en1 = Entry (width = 15, textvariable = my_var2).grid(column = 1, row = 2, columnspan = 1)
    lbl_f = Label (root, text = "ФИО").grid(column = 3, row = 0)
    en2 = Entry (width = 25, textvariable = my_var1).grid(column = 2, row = 2, columnspan = 5)

    #Менеджеры
    lbl_mj = Label (root, text = "Менеджеры").grid(column = 0, row = 3)
    lbl_kmj = Label (root, text = "Код менеджера").grid(column = 1, row = 3)
    en3 = Entry (width = 15, textvariable = my_var3).grid(column = 1, row = 4, columnspan = 1)
    lbl_fmj = Label (root, text = "ФИО").grid(column = 3, row = 3)
    en4 = Entry (width = 25, textvariable = my_var4).grid(column = 2, row = 4, columnspan = 5)

    #Автомобили
    lbl_aut = Label (root, text = "Автомобили").grid(column = 0, row = 5)
    lbl_k = Label(root, text = "Код").grid(column = 1, row = 5)
    en5 = Entry (width = 15, textvariable = my_var5).grid(column = 1, row = 6, columnspan = 1)
    lbl_mr = Label(root, text = "Марка").grid(column = 2, row = 5)
    en6 = Entry (width = 15, textvariable = my_var6).grid(column = 2, row = 6, columnspan = 1)

    #Продажи
    lbl_pr = Label (root, text = "Продажи").grid(column = 0, row = 7)
    
    lbl_kmj1 = Label (root, text = "Код менеджера").grid(column = 1, row = 7)
    en7 = Entry (width = 15, textvariable = my_var7).grid(column = 1, row = 8, columnspan = 1)
    
    lbl_aut1 = Label (root, text = "Код автомобиля").grid(column = 2, row = 7)
    en8 = Entry (width = 15, textvariable = my_var8).grid(column = 2, row = 8, columnspan = 1)
    
    lbl_gos = Label (root, text = "Государственный номер").grid(column = 3, row = 7)
    en9 = Entry (width = 20, textvariable = my_var9).grid(column = 3, row = 8, columnspan = 1)
    
    lbl_kp1 = Label (root, text = "Код покупателя").grid(column = 1, row = 9)
    en10 = Entry (width = 15, textvariable = my_var10).grid(column = 1, row = 10, columnspan = 1)
    
    lbl_dat = Label (root, text = "Дата").grid(column = 2, row = 9)
    en11 = Entry (width = 15, textvariable = my_var11).grid(column = 2, row = 10, columnspan = 1)
    
    lbl_cen = Label (root, text = "Цена").grid(column = 3, row = 9)
    en12 = Entry (width = 15, textvariable = my_var12).grid(column = 3, row = 10, columnspan = 1)
    
    #seve and delete
    s = Button (root, text = "Save", width = 10, height = 1, command = save).place(x = 200, y = 250)
    d = Button (root, text = "Delete", width = 10, height = 1, command = delete).place(x = 200, y = 280)
    
    root.mainloop()

if __name__ == '__main__':
    main()



        
