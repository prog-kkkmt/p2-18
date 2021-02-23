from tkinter import *
import sqlite3 as sq
from tkinter.filedialog import *
from tkinter.messagebox import *

db = sq.connect('Marks.db')
cur = db.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS Things (

            name TEXT NOT NULL

)""")

db.commit()

def show_mark_list():
    pass


def add_mark(event):

    def insert_name(event):
        text = mark_name_entry.get()
        cur.execute(f"SELECT name FROM Things WHERE name = '{text}'")
        if cur.fetchone() is None:
            cur.execute(f"INSERT INTO Things VALUES (?)", (text,))
            db.commit()

            new_db = sq.connect(text + ".db")
            new_cur = new_db.cursor()
            new_cur.execute("""CREATE TABLE IF NOT EXISTS Elements (

                        name TEXT NOT NULL

            )""")
            new_db.commit()
        else:
            pass
        db.commit()

        mark_enter_button = Button(text=text, width=100)
        mark_enter_button.pack(anchor=NW)



        mark_name_window.withdraw()

    mark_name_window = Toplevel(root, width=200, height=100)
    mark_name_window

    mark_name_label = Label(mark_name_window, text="Insert mark name")
    mark_name_label.pack()

    mark_name_entry = Entry(mark_name_window)
    mark_name_entry.pack()

    mark_name_button = Button(mark_name_window, text="OK")
    mark_name_button.bind("<Button-1>", insert_name)
    mark_name_button.pack()


root = Tk()

root.geometry('600x400')

btn_add = Button(root, text="Add mark",)
btn_add.bind("<Button-1>", add_mark)
btn_add.pack(side=BOTTOM)


root.mainloop()
db.close()