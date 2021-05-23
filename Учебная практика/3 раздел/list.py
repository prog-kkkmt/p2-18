# Выполниили Бурлаев Захар, Воронцов Александр

"""Данная программа Добавляет значения с именами, фамилиями, странами и индексами в базу данных,
 динамически выводит их в текстовом виджете и может полностью удавлить все значения из БД
"""

from tkinter import *
import sqlite3

#Подключаемся к базе данных
db = sqlite3.connect("base.db")
#Создаём курсор
cur = db.cursor()

db.commit()

#Создаём корневое окно и задаём размеры
root = Tk()
root.title("form")

root.geometry('700x400')



# Создаём лейбл с именем. пакуем и размещаем его упаковщиком грид
name_label = Label(root, text="Name")
name_label.grid(row=0, column=0)

# Создаём поле для зполнения имени, пакуем и размещаем
name_entry = Entry(width=30)
name_entry.grid(row=0, column=1, columnspan=3)

# Создаём лейбл с фамилией. пакуем и размещаем
surname_label = Label(root, text="Surname")
surname_label.grid(row=1, column=0)

# Создаём поле для зполнения фамилии, пакуем и размещаем
surname_entry = Entry(width=30)
surname_entry.grid(row=1, column=1, columnspan=3)

# Создаём лейбл со страной. пакуем и размещаем
country_label = Label(root, text="Country")
country_label.grid(row=2, column=0)

# Создаём поле для зполнения страны, пакуем и размещаем
country_entry = Entry(width=30)
country_entry.grid(row=2, column=1, columnspan=3)

# Создаём лейбл с индексом. пакуем и размещаем
index_label = Label(root, text="Index")
index_label.grid(row=3, column=0)

# Создаём поле для зполнения индекса, пакуем и размещаем
index_entry = Entry(width=30)
index_entry.grid(row=3, column=1, columnspan=3)

# Создаём функцию динамического обновления виджета с текстом при добавлении значений
def update():
    text.delete("1.0", "end")  # if you want to remove the old data
    raws = cur.execute("SELECT * FROM people")
    for i in raws:
        line = str(i) + "\n"
        text.insert(INSERT, line)

    text.after(1000, update)

# Создаём функцию для добавления значений в БД
def take_all():

    # Присваеваем временным переменным значения с полей ввода
    name = name_entry.get()
    surname = surname_entry.get()
    country = country_entry.get()
    index = int(index_entry.get())
    print(name, surname, country, index)

    # Добавляем в БД значения в соотвествии со значениями переменных
    cur.execute('''INSERT INTO people (Name, Surname, Country, Ind) VALUES(?, ?, ?, ?)''',
                   (name, surname, country, index))

    # Сохраняем изменения в БД
    db.commit()
    # Оновляем значения в текстовом виджете
    update()

# Создаём фунцкию для очистки БД
def clear():
    cur.execute('''DELETE from people''')
    db.commit()
    text.insert(INSERT, "Successful Cleared")

# Добавляем кнопку для добавления данных и отсылаем её к функции добавления
add_button = Button(text="Add", width=10, command=take_all)
add_button.grid(row=4, column=1)

# Добавляем кнопку для очищения базы, и отсылаем её к фунцкии очитски
clear_button = Button(text="Clear all", width=10, command=clear)
clear_button.grid(row=4, column=2)

# Добавляем виджет для отображения текста со значениями из базы данных
text = Text(width=50, height=20, wrap=WORD)
text.grid(row=0, column=6, sticky=W, padx=30, pady=10, rowspan=5, columnspan=2)

# Отображаем построчно текст из БД в виджете
raws = cur.execute("SELECT * FROM people")

for i in raws:
    line = str(i) + "\n"
    text.insert(INSERT, line)

# Зацикливаем корневое окно
root.mainloop()
