#Подготовлено Завадским Михаил Андреевичем П2-18
from tkinter import *

class Window:   #self оворит о том, что переменная принадлежит данномуц классу
    def __init__(self, width, height, title="MyProblem", resizable=(False, False), icon=None):
        self.root = Tk() # корневая переменная хранит Tk 
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+700+500")
        self.root.resizable(resizable[0], resizable[1])
        if icon:
            self.root.iconbitmap(icon)
        
        self.label = Label(self.root, text="Интересный текст")    

    def run(self):
        self.draw_wigets()
        self.root.mainloop()
            

    def draw_wigets(self):
        self.label.pack()




















#window = Tk() #Иницилизация окна
#window.title("Программа?")
#window.geometry("400x360+700+500")
#window.resizable(True, True)
#window.iconbitmap("icon.ico")



#window.mainloop() # циклим окно
