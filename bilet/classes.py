import sqlite3 as sq


# Базовый класс дескриптор
class Vokzal:
    def __init__(self, database='vokzal.db'):
        self.database = database.capitalize()
        with sq.connect(f'{self.database}') as con:
            cur = con.cursor()
            cur.execute("")

    def clear_table(self, table_name):
        with sq.connect(f'{self.database}') as con:
            cur = con.cursor()
            cur.execute(f"DELETE FROM {table_name}")

    def remove_from_table(self, table_name, rel=''):
        with sq.connect(self.database) as con:
            cur = con.cursor()
            cur.execute(f"DELETE FROM {table_name} WHERE {rel}")


# Класс Станции
class Stantion(Vokzal):
    def __init__(self, name='unnamed', table_name='stantions'):
        super().__init__()
        self.data = [name.capitalize()]
        self.table_name = table_name

    # Создание таблицы
    def add_in_table(self):
        with sq.connect(self.database) as con:
            cur = con.cursor()
            cur.execute(
                f"""PRAGMA foreign_keys=on;
            CREATE TABLE IF NOT EXISTS '{self.table_name}'(
            stantion_id  INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT 
            )""")
            cur.execute(f"INSERT INTO {self.table_name} VALUES(Null,?)", self.data)


# Класс Автобуса
class Bus(Vokzal):
    def __init__(self, model='NotFound', number=None, peoples=0, table_name='buses'):
        super().__init__()
        self.data = [model.capitalize(), number, peoples],
        self.table_name = table_name

    # Создание таблицы
    def add_in_table(self):
        with sq.connect(self.database) as con:
            cur = con.cursor()
            cur.execute(f"""
            CREATE TABLE IF NOT EXISTS {self.table_name}(
            bus_id  INTEGER PRIMARY KEY ,
            model TEXT ,
            number INTEGER ,
            peoples INTEGER 
            )""")
            cur.execute(f"INSERT INTO {self.table_name} VALUES(Null,?,?,?)", self.data[0])

    # Задание 2 Поиск всех людей
    def find_all_peoples(self):
        with sq.connect(self.database) as con:
            cur = con.cursor()
            a = str(cur.execute(f"SELECT sum(peoples) FROM {self.table_name}").fetchall()[0][0]) + ' Чел.'
            return a


# Класс поездки
class Tour(Stantion, Bus):
    def __init__(self, time='00:00', station_id=10 ** 7, bus_id=10 ** 7):
        super().__init__()
        self.table_name = 'tours'
        self.data = [time, station_id, bus_id]

    def add_in_table(self):
        with sq.connect(self.database) as con:
            cur = con.cursor()
            cur.executescript(f"""PRAGMA foreign_keys = 1;
            CREATE TABLE IF NOT EXISTS {self.table_name}(
            tour_id INTEGER PRIMARY KEY ,
            time TEXT,
            stantion_id INTEGER,
            bus_id INTEGER,
            FOREIGN KEY (stantion_id) REFERENCES '{Stantion(self.table_name)}'
            FOREIGN KEY (bus_id) REFERENCES '{Bus(self.table_name)}'
            )""")
            try:
                cur.execute(f"INSERT INTO {self.table_name} VALUES(Null,?,?,?)", self.data)
            except sq.IntegrityError:
                cur.execute("")

    # Задание 1 Найти сколько поездок к каждой станции
    def find_many_to_many(self):
        with sq.connect(self.database) as con:
            cur = con.cursor()
            a = cur.execute("SELECT stantion_id, count(bus_id) FROM tours GROUP BY stantion_id").fetchall()
            for i in range(len(a)):
                e = 'Станция номер: ' + ' '.join(str(a[i][0])) + \
                    ' Кол-во поездок: ' + ' '.join(str(a[i][1]))
                print(e)


