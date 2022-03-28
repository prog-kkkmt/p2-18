from tkinter import *
from tkinter import ttk
import sqlite3

root = Tk()
root.title("calories")
conn = sqlite3.connect("products.db")

cur = conn.cursor()


root.geometry("600x200+400+400")
select_label = Label(root, text="Select product")
select_label.grid(row=0, column=0)

Cal_label = Label(root, text="Calories")
Cal_label.grid(row=0, column=1, padx=150)

lst = cur.execute("SELECT product FROM prods")

prod_box = ttk.Combobox(root, values=[*lst], state="readonly")
prod_box.current(0)
prod_box.grid(row=1, column=0)

cal_take = prod_box.get()

print(cal_take)

cal_info = Label(root, text="Cal info")
cal_info.grid(row=1, column=1, padx=150, pady=20)


def add_product():
    window = Toplevel()

    window.title("Add Prduct")

    window.geometry("400x100+400+400")

    name_label = Label(window, text="product name")
    name_label.grid(row=0, column=0)

    name_entry = Entry(window)
    name_entry.grid(row=0, column=1, padx=20)

    cal_label = Label(window, text="amount of calories")
    cal_label.grid(row=1, column=0)

    cal_entry = Entry(window)
    cal_entry.grid(row=1, column=1, padx=20)

    def add_all():

        name = name_entry.get()
        cals = cal_entry.get()

        print(name, cals)
        cur.execute("INSERT INTO prods (product, calories) VALUES (?, ?);", (name, cals))

        conn.commit()

        window.destroy()

        lst = cur.execute("SELECT product FROM prods")

        prod_box = ttk.Combobox(root, values=[*lst], state="readonly")
        prod_box.current(0)
        prod_box.grid(row=1, column=0)

        def start():
            item = prod_box.get()
            print(item)
            cl = cur.execute("SELECT calories FROM prods WHERE product = ?", [item])
            cl = cur.fetchone()
            cal_info.configure(text=cl)

        confirm_button = Button(root, text="confirm", command=start)
        confirm_button.grid(row=2, column=1)



    add_button = Button(window, text="add", command=add_all)
    add_button.grid(row=2, column=0)

    window.mainloop()


add_product_button = Button(root, text="add producrt", command=add_product)
add_product_button.grid(row=2, column=0)


def del_product():

    del_win = Toplevel()
    del_win.title("del Prduct")

    del_win.geometry("400x100+400+400")

    del_label = Label(del_win, text="Write product name")
    del_label.grid(row=0, column=0)

    del_entry = Entry(del_win)
    del_entry.grid(row=0, column=1)

    def delpr():
        pr_name = del_entry.get()

        cur.execute("DELETE FROM prods WHERE product = ?", [pr_name])
        conn.commit()

        del_win.destroy()

        lst = cur.execute("SELECT product FROM prods")

        prod_box = ttk.Combobox(root, values=[*lst], state="readonly")
        prod_box.current(0)
        prod_box.grid(row=1, column=0)

        def start():
            item = prod_box.get()
            print(item)
            cl = cur.execute("SELECT calories FROM prods WHERE product = ?", [item])
            cl = cur.fetchone()
            cal_info.configure(text=cl)

        confirm_button = Button(root, text="confirm", command=start)
        confirm_button.grid(row=2, column=1)



    del_button = Button(del_win, text="Delete", command=delpr)
    del_button.grid(row=1, column=0)


del_product_button = Button(root, text="del producrt", command=del_product)
del_product_button.grid(row=2, column=2)


def start():
    item = prod_box.get()
    print(item)
    cl = cur.execute("SELECT calories FROM prods WHERE product = ?", [item])
    cl = cur.fetchone()
    cal_info.configure(text=cl)

confirm_button = Button(root, text="confirm", command=start)
confirm_button.grid(row=2, column=1)


root.mainloop()