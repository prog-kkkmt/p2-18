#Выполнил Щепкин Михаил П2-18
#Импортирование библиотеки.
from tkinter import *
from tkinter import messagebox
#Настройки окна
root = Tk()
root.geometry ('300x300')
root.title('window')
root ['bg'] = '#ccc'
#Создание параметра функции check, проверки ввода Логина и Пароля
def check( all ):
	Lg = login.get()
	Pg = password.get()
	if Lg and Pg:
		messagebox.showinfo('Success','Вы успешно вошли!')
	if not Lg and Pg:
		messagebox.showerror('Error 0x1', 'Введите логин!')
	elif not Pg and Lg:
		messagebox.showerror('Error 0x2', 'Введите пароль!')
	if not Lg and not Pg:
		messagebox.showerror('Error 0x0', 'Введите данные!')
#Создание текста логин
text_login = Label(text = 'Login', font = ("Times New Roman", 14), 
	fg = '#000000', 
	bg = '#ccc')
#Создание логина
login = Entry(root, font = ("Times New Roman", 16), fg = '#eff5c9', 
	bg = '#48494f', 
	relief = 'solid', 
	justify = 'center')
#Создание текста пароль
text_password = Label(text = 'Password', font = ("Times New Roman", 14), 
	fg = '#000000',
	bg = '#ccc')
#Создание пароля
password = Entry(root, font = ("Times New Roman", 16),
	fg = '#eff5c9',
	bg = '#48494f',
	relief = 'solid',
	justify = 'center',
	show = '*')
#Создание флажка, Оставаться в системе!
check_status = Checkbutton(text = 'Оставаться в системе!',
	font = ("Times New Roman", 14),
	bg = '#ccc',
	fg = '#3d3d42',
	activebackground = '#ccc',
	activeforeground = '#3d3d42')
#Создание кнопки, Войти 
enter = Button(text = 'Войти', font = ("Times New Roman", 16), 
	bg = '#48494f',
	fg = '#000000',
	relief = 'solid',
	activeforeground = '#eff5c9',
	activebackground = '#6e6f73',
	width = '20')
#Packer
text_login.pack()
login.pack()

text_password.pack()
password.pack()

check_status.pack()

enter.pack()
#Bind 
enter.bind('<Button - 1>', check )

root.mainloop()



