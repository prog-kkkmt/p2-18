from tkinter import *

books = []

vids=[]
def convert_for_tk(v):
    l = v
    for i in range(len(l)):
        l[i] = ' '.join(l[i])
    return l


def add_book():
    a = bmm.get()
    e = a.split(' ')
    e.append('\n')
    books.append(e)


def add_reader():
    a = rmm.get()
    e = a.split(' ')
    e.append('\n')
    reds.append(e)


def remove_book():
    try:
        n = ind.get()
        for i in range(len(books)):
            if books[i][0] == n:
                books.pop(i)
                break
    except:
        pass


def remove_reds():
    try:
        n = ind1.get()
        for i in range(len(reds)):
            if reds[i][0] == n:
                reds.pop(i)
                break
    except:
        pass


def show_books():
    bk.delete(1.0, END)
    for i in range(len(books)):
        bk.insert(END, ' '.join(books[i]))


def show_readers():
    red.delete(1.0, END)
    for i in range(len(reds)):
        red.insert(END, ' '.join(reds[i]))


def exporter_b():
    with open('books.txt', 'w') as fl:
        for ls in books:
            ls = ' '.join(ls)
            fl.write('%s\n' % ls)


def exporter_r():
    with open('readers.txt', 'w') as ff:
        for ll in reds:
            ll = ' '.join(ll)
            ff.write('%s\n' % ll)


def replace_b():
    try:
        n = ind2.get()
        print('hi')
        print(n)
        for i in range(len(books)):
            if books[i][0] == n:
                print('fsdfd')
                a = bmm.get()
                e = a.split(' ')
                e.append('\n')
                print(e)
                books[i] = e
    except:
        pass


def replace_r():
    try:
        n = ind3.get()
        for i in range(len(reds)):
            if reds[i][0] == n:
                a = rmm.get()
                e = a.split(' ')
                e.append('\n')
                reds[i] = e
    except:
        pass


def sort_by_data():
    aed.delete(1.0, END)
    def Sort(a):
        a.sort(key=lambda x: x[2])
    Sort(vids)
    for i in range(len(vids)):
        aed.insert(END, ' '.join(vids[i]))


def add_vkid():
    a = smm.get()
    e = a.split(' ')
    e.append('\n')
    vids.append(e)
root = Tk()
root.title("Умные бумажки>")
root.geometry("1100x400")

render = Button(text="EXP К", background="#555", foreground="#ccc",
                padx="10", pady="0", font="16", command=exporter_b)
render.pack()
render.place(x=995, y=30)

renderr = Button(text="EXP Ч", background="#555", foreground="#ccc",
                 padx="10", pady="0", font="16", command=exporter_r)
renderr.pack()
renderr.place(x=800, y=30)

sors = Button(text="SORT", background="#555", foreground="#ccc",
              padx="10", pady="0", font="16", command=sort_by_data)
sors.pack()
sors.place(x=890, y=350)

btn1 = Button(text="Add К", background="#555", foreground="#ccc",
              padx="10", pady="0", font="16", command=add_book)
btn2 = Button(text="Remove К", background="#555", foreground="#ccc",
              padx="10", pady="0", font="16", command=remove_book)
btn3 = Button(text="Show К", background="#555", foreground="#ccc",
              padx="10", pady="0", font="16", command=show_books)
btn1.pack()
btn2.pack()
btn3.pack()

btn1.place(x=44, y=20)
btn2.place(x=44, y=90)
btn3.place(x=44, y=160)
btn4 = Button(text="Add Ч", background="#555", foreground="#ccc",
              padx="10", pady="0", font="16", command=add_reader)
btn5 = Button(text="Remove Ч", background="#555", foreground="#ccc",
              padx="10", pady="0", font="16", command=remove_reds)
btn6 = Button(text="Show Ч", background="#555", foreground="#ccc",
              padx="10", pady="0", font="16", command=show_readers)
btn4.pack()
btn5.pack()
btn6.pack()
btn4.place(x=184, y=20)
btn5.place(x=184, y=90)
btn6.place(x=184, y=160)

add = Button(text="Выдача", background="#555", foreground="#ccc",
              padx="10", pady="0", font="16", command=add_vkid)
add.pack()
add.place(x=320, y=348)

repb = Button(text="Изм К", background="#555", foreground="#ccc",
              padx="10", pady="0", font="16", command=replace_b)
repr = Button(text="Изм Ч", background="#555", foreground="#ccc",
              padx="10", pady="0", font="16", command=replace_r)
repb.place(x=44, y=230)
repr.place(x=184, y=230)

bmm = StringVar()
bm = Entry(textvariable=bmm, width='30', background='#06C')
bm.place(x=150, y=320, anchor="c")

rmm = StringVar()
rm = Entry(textvariable=rmm, width='30', background='#06C')
rm.place(x=150, y=360, anchor="c")

smm = StringVar()
sm = Entry(textvariable=smm, width='30', background='#06C')
sm.place(x=520, y=362, anchor="c")

ind = StringVar()
indexs = Entry(textvariable=ind, width='3', background='#C06')
indexs.place(x=20, y=105, anchor="c")
ind1 = StringVar()
indexs1 = Entry(textvariable=ind1, width='3', background='#C06')
indexs1.place(x=165, y=105, anchor="c")

ind2 = StringVar()
indexs2 = Entry(textvariable=ind2, width='3', background='#C06')
indexs2.place(x=20, y=245, anchor="c")
ind3 = StringVar()
indexs3 = Entry(textvariable=ind3, width='3', background='#C06')
indexs3.place(x=165, y=245, anchor="c")

bk = Text(width=50, height=8, background='#06C')
bk.pack()
bk.place(x=300, y=20)

red = Text(width=50, height=8, background='#06C')
red.pack()
red.place(x=300, y=200)

aed = Text(width=30, height=12, background='#06C')
aed.pack()
aed.place(x=800, y=100)

root.mainloop()
