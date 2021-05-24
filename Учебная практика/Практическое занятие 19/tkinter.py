# Выполнили Воронцов Александр, Бурлаев Захар

"""
Данная программа выводит коды оператора в соответствии с выбраныным оператором
"""

from tkinter import *
from tkinter import ttk
# Создаём корневое окно
root = Tk()
# Меняем название окну
root.title("Phone checker")
# Добавляем коды операторов в массивы
ros_numbers = [901, 902, 912, 930, 939, 955, 958, 970, 971, 991, 992, 993]
matrix_numbers = [939, 958, 969, 980, 993, 999]
like_numbers = [901, 969, 977, 985, 989, 992, 995]

# Настраиваем размер окна
root.geometry('300x200')

# Добавляем текстовый лэйбл и пакуем
label_text = Label(root, text="Choose Operator")
label_text.grid(row=0, column=0, pady=10)

# Делаем функцию, чтобы в связи с выбранными значениями выводились коды определённого оператора
def swap(event):
    if box.current() == 0:
        numbers_label.configure(text=like_numbers, justify=LEFT, font='Times 10')
        box.get()

    elif box.current() == 1:
        numbers_label.configure(text=matrix_numbers, justify=LEFT, font='Times 10')
        box.get()
    elif box.current() == 2:
        numbers_label.configure(text=ros_numbers, justify=LEFT, font='Times 10')
        box.get()
# Добавляем и Настраиваем комбобокс для выдвигающего списка с выбором
box = ttk.Combobox(root)
box['values'] = ("Likemobile", "Matrix", "Rostelecom")
box.current(0)
box.grid(row=0, column=1, sticky=W, padx=0, pady=10)

#Создаём лейбл для вывода кодов
numbers_label = Label(root, height=10, width=45)
numbers_label.grid(row=3, column=0, sticky=W, columnspan=3, rowspan=3)
box.bind("<<ComboboxSelected>>", swap)

root.mainloop()
