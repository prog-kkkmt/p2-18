import sqlite3

def start():
    conn = sqlite3.connect('EmployeeBD')
    curs = conn.cursor()

    try:
        curs.execute("""CREATE TABLE Employee(
            newNameBD TEXT,
            newSecNameBD TEXT,
            newPostBD TEXT)""")
    except sqlite3.OperationalError:
        None

    curs.execute("DELETE FROM Employee")
    curs.executemany("INSERT INTO Employee VALUES (?, ?, ?)", text)

    conn.commit()


text = [('Ли', 'Цвинишвили', 'Кассир'),
        ('Син', 'Цзиньпин', 'Фасовщик'),
        ('Мухаммед', 'Али', 'Консультант')]

start()
