import sqlite3

# Создание базы данных и курсора.
conn = sqlite3.connect('save\SaveFile.db')
curs = conn.cursor()

# Проверка удалена ли таблица в файле 'SaveFile.db'.
try:
    save = [('1','money', 0),
            ('2','upgrade ', 1),
            ('3','priceRAM', 50),
            ('4','moneyRAM', 5),
            ('5','KolVoRAM', 0),
            ('6','priceCPU', 5000),
            ('7','moneyCPU', 20),
            ('8','KolVoCPU',  0),
            ('9','priceCARD', 25000),
            ('10','moneyCARD', 60),
            ('11','KolVoCARD', 0),
            ('12', 'SecretCodeActive', 0)]
    curs.execute("""CREATE TABLE Save(id TEXT,
                 Name TEXT,
                 Save INTENGER)""")
    curs.executemany('INSERT INTO Save VALUES (?, ?, ?)' , save)
    conn.commit()
except sqlite3.OperationalError:
    None

# Загрузка переменных из базы данных в игру.
*save, = curs.execute('SELECT * FROM Save')

# Переменные денег, цены, улучшения.
money = save[0][2]
upgrade = save[1][2]

priceRAM = save[2][2]
moneyRAM = save[3][2]
KolVoRAM = save[4][2]

priceCPU = save[5][2]
moneyCPU = save[6][2]
KolVoCPU = save[7][2]

priceCARD = save[8][2]
moneyCARD = save[9][2]
KolVoCARD = save[10][2]
SecretCodeActive = save[11][2]
