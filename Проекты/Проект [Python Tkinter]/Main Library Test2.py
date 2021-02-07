from tkinter import *
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename 
from tkinter import Frame, Tk, BOTH, Text, Menu, END
from tkinter import filedialog
from tkinter import messagebox
 
class Example(Frame):
 
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def info(self): 
        messagebox.showinfo('Информация', 'Создатель: ivauuka99\nВерсия: 2.0', )
 
    def initUI(self):
        self.master.title("Library")
        self.pack(fill=BOTH, expand=1)
         
        mainTray = Menu(self.master)
        self.master.config(menu=mainTray)
        
        fileTray = Menu(mainTray, tearoff=0)
        fileTray.add_command(label = "Новый")
        fileTray.add_command(label = "Открыть", command=self.onOpen)
        fileTray.add_command(label = "Сохранить как...", command = self.save_file)
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
 
    def onOpen(self):
        """Открываем файл для редактирования"""
        filepath = askopenfilename(
            filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")]
        )
        if not filepath:
            return
        with open(filepath, "r") as input_file:
            text = input_file.read()
            txt_edit.insert(tk.END, text)
        window.title(f"Простой текстовый редактор - {filepath}") 
 
    def readFile(self, askopenfilename):
        with open(askopenfilename, "r") as f:
            text = f.read()
 
        return text
    
    def save_file(self):
        filepath = asksaveasfilename(
            defaultextension="txt",
            filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")],
        )
        if not filepath:
            return
        with open(filepath, "w") as output_file:
            text = txt_edit.get("1.0", tk.END)
            output_file.write(text)
        window.title(f"Простой текстовый редактор - {filepath}")
               
    def onExit(self):
        self.quit()
 
def main():
    root = Tk()
    root.resizable(False, False)
    ex = Example()
    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    w = w//2                                                                # середина экрана
    h = h//2 
    w = w - 200                                                             # смещение от середины
    h = h - 200
    root.geometry('500x500+{}+{}'.format(w, h))    
    root.mainloop()
 
if __name__ == '__main__':
    main()
