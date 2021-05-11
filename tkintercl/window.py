# Подготовлено Завадским Михаил Андреевичем П2-18
from tkinter import *
# импортируем библиотеку для работы с окнами
class Window:   
# self говорит о том, что переменная принадлежит данному классу
    def __init__(self, width, height, title="MyProblem", resizable=(False, False), icon=None):
# отвечает какими параметрами изначально владеет наше окно 
        self.root = Tk() 
# корневая переменная хранит Tk 
        self.root.title(title)
# название нашего окна
        self.root.geometry(f"{450}x{450}+740+300")
# геометрия нашего окна(начальное расположение и рзарешение)
        self.root.resizable(resizable[0], resizable[1])
# возможность изменения окна по координатам (x, y)
        canvas = Canvas(self.root, width=300, height=250)
        canvas.pack()

        frame = Frame(self.root)
        frame.place(relwidth=1, relheight=1)
        if icon:
            self.root.iconbitmap(icon)
# иконка
        self.label = Label(self.root, text="Интересный текст")    
# виджет label. Нужен для работы с текстом в окне
    def run(self):
        self.draw_wigets()
        self.root.mainloop()       

    def draw_wigets(self):
        self.label.pack()
# настройка виджетов
