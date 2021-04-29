"""
2. Автосалон.
Менеджеры автосалона осуществляют продажу клиентам автомобилей различных марок.

Таблицы: Покупатели (Код покупателя, ФИО), Менеджеры (Код менеджера, ФИО),
Автомобили (код, марка),
Продажи (Код менеджера, код автомобиля, государственный номер,
код покупателя, дата, цена).

Определить:
- среднюю сумму сделки
- долю продаж автомобилей разных марок.
"""
from tkinter import *

def main():
    def save():
        str = get_codep() + ' '
        with open ("Autoservis.txt", 'a') as f:
            f.write (str + '\n')
    def delete():
        f = open ("Autoservis.txt",  'w+')
        f.seek(0)
        f.close()

    def get_codep():
        return my_var2.get()

    root = Tk()
    root.title ("Autosalon")
    root.geometry ("450x350")

    my_var = StringVar('')
    my_var2 = StringVar('')

    lbl_p = Label(root, text = "Покупатели").grid(column = 0, row = 0)
    lbl = Label(root, text = "Код покупателя").grid(column = 1, row = 0)
    en = Entry(width = 15, textvariable = my_var2).grid(column = 1, row = 2, columnspan = 1)

    #seve and delete
    s = Button (root, text = "Save", width = 10, height = 1, command = save).grid(column = 2, row = 9, columnspan = 2)
    d = Button (root, text = "Delete", width = 10, height = 1, command = delete).grid(column = 3, row = 10, columnspan = 2)
    
    root.mainloop()

if __name__ == '__main__':
    main()



        
