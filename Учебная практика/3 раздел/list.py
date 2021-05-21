from tkinter import *
import sqlite3


db = sqlite3.connect("base.db")
cur = db.cursor()

db.commit()


root = Tk()
root.title("form")

root.geometry('700x400')




name_label = Label(root, text="Name")
name_label.grid(row=0, column=0)

name_entry = Entry(width=30)
name_entry.grid(row=0, column=1, columnspan=3)

surname_label = Label(root, text="Surname")
surname_label.grid(row=1, column=0)

surname_entry = Entry(width=30)
surname_entry.grid(row=1, column=1, columnspan=3)

country_label = Label(root, text="Country")
country_label.grid(row=2, column=0)

country_entry = Entry(width=30)
country_entry.grid(row=2, column=1, columnspan=3)

index_label = Label(root, text="Index")
index_label.grid(row=3, column=0)

index_entry = Entry(width=30)
index_entry.grid(row=3, column=1, columnspan=3)

def update():
    text.delete("1.0", "end")  # if you want to remove the old data
    raws = cur.execute("SELECT * FROM people")
    for i in raws:
        line = str(i) + "\n"
        text.insert(INSERT, line)

    text.after(1000, update)

def take_all():
    name = name_entry.get()
    surname = surname_entry.get()
    country = country_entry.get()
    index = int(index_entry.get())
    print(name, surname, country, index)


    cur.execute('''INSERT INTO people (Name, Surname, Country, Ind) VALUES(?, ?, ?, ?)''',
                   (name, surname, country, index))

    db.commit()
    update()


def clear():
    cur.execute('''DELETE from people''')
    db.commit()
    text.insert(INSERT, "Successful Cleared")


add_button = Button(text="Add", width=10, command=take_all)
add_button.grid(row=4, column=1)

clear_button = Button(text="Clear all", width=10, command=clear)
clear_button.grid(row=4, column=2)

text = Text(width=50, height=20, wrap=WORD)
text.grid(row=0, column=6, sticky=W, padx=30, pady=10, rowspan=5, columnspan=2)

raws = cur.execute("SELECT * FROM people")

for i in raws:
    line = str(i) + "\n"
    text.insert(INSERT, line)

root.mainloop()