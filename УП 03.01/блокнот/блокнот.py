import tkinter
from tkinter import *
from tkinter.filedialog import asksaveasfile, askopenfile
from tkinter.messagebox import showerror
from tkinter import messagebox

FILE_NAME = tkinter.NONE

def new_file():
	global FILE_NAME
	FILE_NAME = "Без названия"
	text.delete('1.0', tkinter.END)

def save_file():
	data = text.get('1.0', tkinter.END)
	out = open(FILE_NAME, 'w')
	out.write(data)
	out.close()

def save_as():
	out = asksaveasfile(mode='w', defaultextension='txt')
	data = text.get('1.0', tkinter.END)
	try:
		out.write(data.rstrip())
	except Exception:
		showerror(title="Ошибка", message="Ошибка сохранения файла")

def open_file():
	global FILE_NAME
	inp = askopenfile(mode="r")
	if inp is None:
		return
	FILE_NAME = inp.name
	data = inp.read()
	text.delete('1.0', tkinter.END)
	text.insert('1.0', data)

def info():
	messagebox.showinfo("Информация", "П2-18 Пилипушко А.С., Васькевич Ю.А., Яковлев П.М.")


root = tkinter.Tk()
root.title("Блокнот")

root.minsize(width=500, height=500)
root.maxsize(width=500, height=500)

text = tkinter.Text(root, width=400, height=400, wrap="word")
scrollb = Scrollbar(root, orient=VERTICAL, command=text.yview)
scrollb.pack(side="right", fill="y")
text.configure(yscrollcommand=scrollb.set)

text.pack()
menuBar = tkinter.Menu(root)
fileMenu = tkinter.Menu(menuBar)
fileMenu.add_command(label="Новый файл", command=new_file)
fileMenu.add_command(label="Открыть файл", command=open_file)
fileMenu.add_command(label="Сохранить", command=save_file)
fileMenu.add_command(label="Сохранить как", command=save_as)

menuBar.add_cascade(label="Файл", menu=fileMenu)
menuBar.add_cascade(label="Информация", command=info)
menuBar.add_cascade(label="Выйти", command=root.quit)
root.config(menu=menuBar)
root.mainloop()
