import sqlite3

def start():
    conn = sqlite3.connect('TeaShopBD')
    curs = conn.cursor()

    try:
        curs.execute("""CREATE TABLE TeaShop(
            newProduct TEXT,
            AmountProduct INTEGER,
            Price REAL)""")
    except sqlite3.OperationalError:
        None

    curs.execute("DELETE FROM TeaShop")
    curs.executemany("INSERT INTO TeaShop VALUES (?, ?, ?)", text)

    conn.commit()


text = [('Черный чай Цейлонский', '500', '249.50'),
        ('Черный кофе Люберцы', '1245', '54.99'),
        ('Зеленый чай МостВантед', '77', '1500')]

start()
