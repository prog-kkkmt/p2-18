import sqlite3

# Создание списка таблици
'''       Model     Proiz   Country'''
text = [('M5 F90     ','BMW      ','De'),
        ('E63        ','Mercedes ','De'),
        ('Solaris    ','Hyndai   ','Kr'),
        ('Sportage   ','Kia      ','Kr'),
        ('S63        ','Mercedes ','De'),
        ('Crown s220 ','Toyota   ','Jp'),
        ('M3 E46     ','BMW      ','De'),
        ('Sonata     ','Hyndai   ','Kr'),
        ('R32        ','Nissan   ','Jp'),
        ('Explorer   ','Ford     ','Us'),
        ('500        ','Fiat     ','It'),
        ('S220       ','Mercedes ','De'),
        ('SF90       ','Ferrari  ','It'),
        ('Cerato     ','Kia      ','Kr'),
        ('Supra A90  ','Toyota   ','Jp'),
        ('GTO        ','Pontiac  ','Us'),
        ('200        ','Fiat     ','It'),
        ('i20        ','Hyndai   ','Kr'),
        ('Juke       ','Nissan   ','Jp'),
        ('Punto      ','Fiat     ','It'),
        ('Vivant     ','Pontiac  ','Us'),
        ('488        ','Ferrari  ','It'),
        ('Rio        ','Kia      ','Kr'),
        ('G310GS     ','BMW      ','De'),
        ('Aristo     ','Toyota   ','Jp'),
        ('f40        ','Ferrari  ','It'),
        ('Focus      ','Ford     ','Us'),
        ('Qashqai    ','Nissan   ','Jp'),
        ('Mustang    ','Ford     ','Us'),
        ('Firebird   ','Pontiac  ','Us')]

# Создание и запись списка в таблицу
conn = sqlite3.connect('MarkaTable')
curs = conn.cursor()

curs.execute("""CREATE TABLE Model(
    Model TEXT,
    Proiz TEXT,
    Country TEXT)""")

curs.executemany("INSERT INTO Model VALUES (?, ?, ?)", text)

conn.commit()
'''
a = ['Rus', '', '', '']
print(*a)
g = curs.execute("""SELECT *
                    FROM Players
                    WHERE Country IN (?, ?, ?, ?)""", a)
print(*g, '----------------------------------------------')
a[1] = 'Ukr'
g = curs.execute("""SELECT *
                    FROM Players
                    WHERE Country IN (?, ?, ?, ?)""", a)
print(*g)
conn.commit()
'''

'''
SELECT *
FROM Players
WHERE Team = "G2";

SELECT *
FROM Players
WHERE Country IN ("Rus", "Ukr");

SELECT *
FROM Players
WHERE Rating >= 1
ORDER BY Rating DESC;

SELECT *
FROM Players
WHERE Name LIKE "S%";
'''
