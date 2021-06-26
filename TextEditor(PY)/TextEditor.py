import tkinter as tk
from tkinter import *
from tkinter import font
import tkinter.font as tkFont
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter import messagebox as MessageBox
from tkinter.messagebox import showinfo
from tkinter.scrolledtext import ScrolledText
from tkinter.filedialog import asksaveasfile, askopenfile


root = Tk()
#Название окна
root.title("TextEditor")

#Окно блокнота
#Изначальный размер окна и его место положение
root.geometry('700x700+200+20')
text = tk.Text(root, width = 900, height = 900, undo = "True", wrap = "none")

root.iconbitmap('C:/TextEditor/phero.ico')

#Стандартный шрифт в блокноте
text.configure(font = ("Courier Now","12"))

frame = tk.Frame()
FileName = tk.NONE

#Global переменные
global selected
selected = False
global textFile
global OpenStatusName
OpenStatusName = False

#Функция новый файл
def NewFile(event = 'n'):
    text.delete('1.0', END)
    root.title('Новый Файл')
    statusBar.config(text = "Новый Файл  - TextEditor")
    global OpenStatusName
    OpenStatusName = False
    
#Функция сохранить файл
def SaveFile(event = 's'):
    global OpenStatusName
    if OpenStatusName:
        textFile = open(OpenStatusName, 'w')
        textFile.write(text.get(1.0, END)) 
        statusBar.config(text = f'Saved: {OpenStatusName}  ')
        showinfo(title = "TextEditor", message = "Ваш файл успешно сохранён" )
    else:
        SaveAs()
        textFile.close()

#Функция сохранить файл как
def SaveAs(event = 's'):
    textFile = filedialog.asksaveasfilename(defaultextension = ".*", title = "Сохранить файл как", filetypes = (("Text Files", "*.txt"),("HTML Files","*.html"),("Python Files", "*.py"),("All Files", "*.*")))
    if textFile:
        name = textFile
        statusBar.config(text = f'Saved: {name}  ')
        showinfo(title = "TextEditor", message = "Ваш файл успешно сохранён" )
        name = name.replace("C:/", "")
        root.title(f'   {name} ')
        textFile = open(textFile, 'w')
        textFile.write(text.get(1.0, END))
        textFile.close()
          
#Функция открыть файл
def OpenFile(event = 'q'):
    text.delete('1.0', END)
    textFile = filedialog.askopenfilename(title = "Открыть Файл", filetypes = (("Text Files", "*.txt"),("HTML Files","*.html"),("Python Files", "*.py"),("All Files", "*.*")))
    if textFile:
        global OpenStatusName
        OpenStatusName = textFile
    name = textFile
    statusBar.config(text = f'{name}        ')
    root.title('TextEditor')
    textFile = open(textFile, 'r')
    stuff = textFile.read()
    text.insert(END, stuff)
    textFile.close()
    
#Функция копировать
def copy(event = None):
    global selected
    if event:
        selected = root.clipboard_get()
    if text.selection_get():
        selected = text.selection_get()
        root.clipboard_append(selected)
        
#Функция вырезать
def cut(event = None):
    global selected
    if event:
        selected = root.clipboard_get()
    else:
        if text.selection_get():
            selected = text.selection_get()
            text.delete("sel.first", "sel.last")
            root.clipboard_clear()
            root.clipboard_append(selected)
            
#Функция вставить
def paste(event = None):
    global selected
    if event:
        selected = root.clipboard_get()
    else:
        if selected:
            position = text.index(INSERT)
            text.insert(position, selected)
            
#Функция отменить действие
def undo(event = None):
    text.edit_undo
    
#Функция возврата действия
def redo(event = None):
    text.edit_redo
    
#Функция выхода из приложения
def quit():
    root.destroy()

#Функция полужирного шрифта
def BoldFont(event = "b"):
    bold = font.Font(text, text.cget("font"))
    bold.configure(weight = "bold")
    text.tag_configure("bold", font = bold)
    current_tags = text.tag_names("sel.first")
    if "bold" in current_tags:
        text.tag_remove("bold", "sel.first", "sel.last")
    else:
        text.tag_add("bold", "sel.first", "sel.last")

#Функция курсивного шрифта
def ItalicsFont(event = "g"):
    italics = font.Font(text, text.cget("font"))
    italics.configure(slant = "italic")
    text.tag_configure("italic", font = italics)
    current_tags = text.tag_names("sel.first")
    if "italic" in current_tags:
        text.tag_remove("italic", "sel.first", "sel.last")
    else:
        text.tag_add("italic", "sel.first", "sel.last")

def reset_list():
    if s != entry_widget_name.get():
        print(entry_widget_name.get())
        search_list.clear()
        text_widget_name.tag_remove(SEL, 1.0,"end-1c")
        

        
#Прокрутка ползунка в блокноте
#По вертикали
ScrollMouse_1 = Scrollbar(root, orient = VERTICAL, command = text.yview)
text.configure(yscrollcommand = ScrollMouse_1.set, wrap = "none")
#По горезонтали
ScrollMouse_2 = Scrollbar(root, orient = HORIZONTAL, command  = text.xview)
text.configure(xscrollcommand = ScrollMouse_2.set, wrap = "none")


#Меню файла
menuBar = tk.Menu(root)
fileMenu = tk.Menu(menuBar)
fileMenu.add_command(label = "Новый файл", command = NewFile)
fileMenu.add_command(label = "Открыть", command = OpenFile)
fileMenu.add_command(label = "Сохранить", command = SaveFile)
fileMenu.add_command(label = "Сохранить как", command = SaveAs)

#Меню правки
editMenu = tk.Menu(menuBar)
editMenu.add_command(label = "Скопировать", command = lambda: copy (False))
editMenu.add_command(label = "Вставить", command = lambda: paste (False))
editMenu.add_command(label = "Вырезать", command = lambda: cut (False))
editMenu.add_separator()
editMenu.add_command(label = "Отменить действие", command = text.edit_undo)
editMenu.add_command(label = "Вернуть действие", command = text.edit_redo)

#Меню Шрифта
fontMenu = tk.Menu(menuBar)
fontMenu.add_separator()
fontMenu.add_command(label = "Полужирный шрифт", command = BoldFont)
fontMenu.add_command(label = "Курсивный шрифт", command = ItalicsFont)


#Меню помощи
helpMenu = tk.Menu(menuBar)
helpMenu.add_command(label = "Скопировать", accelerator = "(CTRL + C)")
helpMenu.add_command(label = "Вставить",  accelerator = "(CTRL + V)")
helpMenu.add_command(label = "Вырезать",  accelerator = "(CTRL + X)")
helpMenu.add_command(label = "Отменить действие",  accelerator = "(CTRL + Z)")
helpMenu.add_command(label = "Отменить действие",  accelerator = "(CTRL + SHIF + Z)")
helpMenu.add_separator()
helpMenu.add_command(label = "Новый файл",  accelerator = "(CTRL + N)")
helpMenu.add_command(label = "Сохранить ",  accelerator = "(CTRL + S)")
helpMenu.add_command(label = "Сохранить как",  accelerator = "(CTRL + SHIFT + S)")
helpMenu.add_command(label = "Открыть файл",  accelerator = "(CTRL + Q)")
helpMenu.add_separator()
helpMenu.add_command(label = "Полужирный шрифт",  accelerator = "(CTRL + B)")
helpMenu.add_command(label = "Курсивный шрифт",  accelerator = "(CTRL + G)")

#Подменю файла
menuBar.add_cascade(label = "Файл", menu = fileMenu)
#Подменю правки
menuBar.add_cascade(label = "Правка", menu = editMenu)
#Подменю шрифта
menuBar.add_cascade(label = "Шрифт", menu = fontMenu)
#Подменю помощи
menuBar.add_cascade(label = "Помощь", menu = helpMenu)
#Кнопка выхода
menuBar.add_cascade(label = "Выход", command = quit)

#menuBar.add_cascade(label = "Undo", command = text.edit_undo)

#Кнопки
toolBarFrame = Frame(root)

#Button(root, image = image, command = text.edit_undo, relief = 'flat').pack()
#Button(root, image = image, command = text.edit_redo, relief = 'flat').pack()


#Отмена действия
#undoImage = ImageTk.PhotoImage(file = "C:/Users/p2-18/Desktop/TextEditor/undo.png")
undoImage = ImageTk.PhotoImage(file = "C:/TextEditor/undo.png")
undoButton = Button(root, image = undoImage, command = text.edit_undo, relief = 'flat')
undoButton.pack(anchor = W)


#Возврат действия
#redoImage = ImageTk.PhotoImage(file = "C:/Users/p2-18/Desktop/TextEditor/redo.png")
redoImage = ImageTk.PhotoImage(file = "C:/TextEditor/redo.png")
redoButton = Button(root, image = redoImage, command = text.edit_redo, relief = 'flat')
redoButton.place(x = 20)


#Кнопка шрифт полужирный
#boldImage = ImageTk.PhotoImage(file = "C:/Users/p2-18/Desktop/TextEditor/bold.png")
boldImage = ImageTk.PhotoImage(file = "C:/TextEditor/bold.png")
boldButton = Button(root, image = boldImage, command = BoldFont, relief = 'flat')
boldButton.place(x = 40)


#Кнопка шрифт курсивный
#italicsImage = ImageTk.PhotoImage(file = "C:/Users/p2-18/Desktop/TextEditor/italic.png")
italicsImage = ImageTk.PhotoImage(file = "C:/TextEditor/italic.png")
italicsButton = Button(root, image = italicsImage, command = ItalicsFont, relief = 'flat')
italicsButton.place(x = 60)

#searchButton = Button(root, text = "Вызов строки поиска по тексту ", command = createNewWindowSearch, relief = 'flat')

root.config(menu = menuBar)
statusBar = Label(root, text = 'Новый Файл        ', anchor = W)

#Pack
statusBar.pack(side = "bottom", fill = 'x', ipady = 1)
#СкроллБар снизу
ScrollMouse_2.pack(side = "bottom", fill = 'x',expand = True)
#СкроллБар справа
ScrollMouse_1.pack(side = "right", fill = 'y',expand = True)

toolBarFrame.pack(fill = 'x')
text.pack()
frame.pack()

#Binds
root.bind('<Control - Key - n>', NewFile)
root.bind('<Control - Key - s>', SaveFile)
root.bind('<Control - Key - q>', OpenFile)
root.bind('<Control - Key - S>', SaveAs)
root.bind('<Control - Key - c>', copy)
root.bind('<Control - Key - v>', paste)
root.bind('<Control - Key - x>', cut)
root.bind('<Control - Key - z>', undo)
root.bind('<Control - Key - Z>', redo)
root.bind('<Control - Key - b>', BoldFont)
root.bind('<Control - Key - g>', ItalicsFont)



root.mainloop()

