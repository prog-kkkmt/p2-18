import sqlite3 as sq
import random
def insert_stancus(name_stancus = 'Северок'):
    with sq.connect("database.db") as con:
        cursor = con.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS stancus(
        stancus_id integer PRIMARY KEY,
        name_stancus text)""")
        if name_stancus !='Северок':
            cursor.execute(f"INSERT into stancus VALUES(null,'{name_stancus}')")
        a = cursor.execute("SELECT * FROM stancus").fetchall()
        print(a)
def insert_bus(model='mercebeb', number='оа000о',):
    with sq.connect("database.db") as con:
        cursor = con.cursor()
        cursor.execute("""
                CREATE TABLE IF NOT EXISTS busus(
                busus_id integer PRIMARY KEY,
                model_busus text,
                nomer_busus text,
                pipis_busus integer)""")
        if number != 'оа000о':
            cursor.execute(f"INSERT into busus VALUES(null,'{model}','{number}', {random.randint(30, 55)})")
        b = cursor.execute("SELECT * FROM busus").fetchall()
        print(b)
def insert_tour(stancus_id,busus_id,time):
    with sq.connect("database.db") as con:
        cursor = con.cursor()
        cursor.executescript(f"""PRAGMA foreign_keys = 1;
                    CREATE TABLE IF NOT EXISTS tours(
                    tour_id INTEGER PRIMARY KEY ,
                    stantion_id INTEGER,
                    bus_id INTEGER,
                    time TEXT,
                    FOREIGN KEY (stantion_id) REFERENCES 'stancus(stancus_id)'
                    FOREIGN KEY (bus_id) REFERENCES 'busus(busus_id)'
                    )""")
        try:
            cursor.execute(f"INSERT INTO tours VALUES(Null,{stancus_id},{busus_id},'{time}')")
        except sq.IntegrityError:
            cursor.execute("")
        c = cursor.execute("SELECT * from tours").fetchall()
        print(c)
insert_bus()
insert_tour(1,1,'19:30')
def count_all_pipis():
    with sq.connect("database.db") as con:
        cursor = con.cursor()
        print(cursor.execute("SELECT sum(pipis_busus) from busus").fetchall())
count_all_pipis()
def escape_from_stancus():
    with sq.connect("database.db") as con:
        cursor = con.cursor()
        d = cursor.execute("SELECT stantion_id, count(bus_id) FROM tours GROUP BY stantion_id").fetchall()
        print(d)
escape_from_stancus()