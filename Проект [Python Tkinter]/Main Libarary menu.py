from tkinter import *
import tkinter as tk
from tkinter import Frame, Tk, BOTH, Text, Menu, END
from tkinter import filedialog
from tkinter import messagebox
 
class Example(Frame):
#Основная функция 
    def __init__(self):
        super().__init__()
        self.initUI()
#Функция информации        
    def info(self): 
        messagebox.showinfo('Информация', 'Создатель: ivauuka99\nВерсия: 1.4b', )
#Функция основного трея  
    def initUI(self):
        self.master.title("Library")
        self.pack(fill=BOTH, expand=1)
         
        mainTray = Menu(self.master)
        self.master.config(menu=mainTray)
        # подменю освновного меню Файл
        fileTray = Menu(mainTray, tearoff=0)
        fileTray.add_command(label = "Новый")
        fileTray.add_command(label = "Открыть", command=self.onOpen)
        fileTray.add_command(label = "Сохранить как...")
        fileTray.add_separator()
        fileTray.add_command(label = "Выход", command = self.onExit)
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
        helpTray.add_command(label = "О программе", command = self.info)
        # первые функции трея
        mainTray.add_cascade(label = "Файл", menu = fileTray)
        mainTray.add_cascade(label = "Действия", menu = actTray)
        mainTray.add_cascade(label = "Помощь", menu = helpTray)
 
        self.txt = Text(self)
        self.txt.pack(fill=BOTH, expand=1)
        
    #Функция открытия файла
    def onOpen(self):
        ftypes = [('Python файлы', '*.py'), ('Текстовые файлы', '.txt'), ('Все файлы', '*')]
        dlg = filedialog.Open(self, filetypes = ftypes)
        fl = dlg.show()
 
        if fl != '':
            text = self.readFile(fl)
            self.txt.insert(END, text)
            
    #Функция чтения и вывода информации
    def readFile(self, filename):
        with open(filename, "r") as f:
            text = f.read()
 
        return text
    
    #Функция выхода/закрытия приложения           
    def onExit(self):
        self.quit()
 
def main():
    root = Tk()
    root.resizable(False, False)
    ex = Example()
    
    #Автоматическое определения окна в центр
    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    w = w//2                                                                # середина экрана
    h = h//2 
    w = w - 200                                                             # смещение от середины
    h = h - 200
    root.geometry('500x500+{}+{}'.format(w, h))                             # размеры окна
    
    root.mainloop()
 
if __name__ == '__main__':
    main()
