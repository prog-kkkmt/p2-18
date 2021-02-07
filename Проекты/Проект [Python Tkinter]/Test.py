import tkinter as tk
from subprocess import call
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext 

def info():  
    messagebox.showinfo('Информация', 'Создатель: ivauuka99\nВерсия: 2.0', )
    
def quit(root):
    root.destroy()
    root.quit()

def fileOpen():
    try:
        print(open("BD.txt").read())
    except IOError:
        print ("No file")    
    
root = tk.Tk()
root.resizable(False, False)
root.title("Library")

Button(root, text="Quit", command = lambda root=root:quit(root)).pack()

w = root.winfo_screenwidth()
h = root.winfo_screenheight()
w = w//2                                                                # середина экрана
h = h//2 
w = w - 200                                                             # смещение от середины
h = h - 200
root.geometry('500x500+{}+{}'.format(w, h))                             # размеры окна

root["bg"] = "steelblue"

mainTray = Menu(root)                                                   # основное меню
root.config(menu = mainTray)                                            # присвоение основному меню

# подменю основного меню файл
fileTray = Menu(mainTray, tearoff=0)
fileTray.add_command(label = "Новый")
fileTray.add_command(label = "Открыть", command = fileOpen)
fileTray.add_command(label = "Сохранить")
fileTray.add_separator()
fileTray.add_command(label = "Выход")
# подменю основного меню действия
actTray = Menu(mainTray, tearoff=0)
actTray.add_command(label = "1")
actTray.add_command(label = "2")
actTray.add_command(label = "3")
# подменю основного меню помощь
helpTray2 = Menu(mainTray, tearoff=0)
helpTray2.add_command(label = "Справка")
helpTray2.add_command(label = "Сайт")
# подменю основного меню помощь
helpTray = Menu(mainTray, tearoff = 0)
helpTray.add_cascade(label = "Помощь",menu = helpTray2)
helpTray.add_separator()
helpTray.add_command(label = "О программе", command = info)
# первые функции трея
mainTray.add_cascade(label = "Файл", menu = fileTray)
mainTray.add_cascade(label = "Действия", menu = actTray)
mainTray.add_cascade(label = "Помощь", menu = helpTray)

root.config(menu = mainTray)                                            # конфиги меню
root.mainloop()




