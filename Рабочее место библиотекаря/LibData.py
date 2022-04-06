import sqlite3

# Создание списка таблици
'''      Название                 Автор               Год      Год выпуска   '''  
text = [('Мастер и Маргарита  ', 'Михаил Булгаков  ','1929  ','2003  '),
        ('Ася                 ', 'Иван Тургенев    ','1858  ','2006  '),
        ('Мертвые души        ', 'Николай Гоголь   ','1842  ','2005  '),
        ('Хождение по мукам   ', 'Алексей Толстой  ','1922  ','2004  '),
        ('Записки охотника    ', 'Иван Тургенев    ','1852  ','2001  '),
        ('Война и Мир         ', 'Лев Толстой      ','1865  ','2012  '),
        ('Левша               ', 'Николай Лесков   ','1881  ','2007  '),
        ('Двенадцать стульев  ', 'Илья Ильф        ','1928  ','2021  '),
        ('Белая гвардия       ', 'Михаил Булгаков  ','1924  ','2015  '),
        ('Палата N6           ', 'Антон Чехов      ','1892  ','2013  '),
        ('Собачье сердце      ', 'Михаил Булгаков  ','1925  ','1950  '),
        ('Мор                 ', 'Ice-Pick         ','2005  ','2019  '),
        ('Тарас Бульба        ', 'Николай Гоголь   ','1835  ','1930  '),]

# Создание и запись списка в таблицу
conn = sqlite3.connect('LibTable')
curs = conn.cursor()

curs.execute("""CREATE TABLE Lib(
    Name TEXT,
    HP INTEGER,
    Year INTEGER,
    Price INTEGER)""")

curs.executemany("INSERT INTO Lib VALUES (?, ?, ?, ?)", text)

conn.commit()
