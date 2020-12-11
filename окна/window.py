
from tkinter import *

class Window:   #self оворит о том, что переменная принадлежит данномуц классу
    def __init__(self, width, height, title="MyProgram", resizable(False, False)):
        self.root = Tk() # корневая переменная хранит Tk
        self.root.title(title)
        self.root.geometry("{width}x{height}+700+500")
        self.root.rezistable(rezistable[0], rezistable[1])
        if icon is not none:
            self.root.iconbitmap(icon)
            

    def run(self):
        self.root.mainloop()
            

#window = Tk() #Иницилизация окна
#window.title("Программа!")
#window.geometry("400x360+700+500")
#window.resizable(True, True)
#window.iconbitmap("icon.ico")



#window.mainloop() # циклим окно
