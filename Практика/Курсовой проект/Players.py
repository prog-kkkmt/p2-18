import sqlite3

# Создание списка таблици
'''       nick           team       Country      rat          kpr         hs   '''  
text = [('Hobbit    ','Gambit   ','Kaz',      '1.22',     '0.77',     '47.2'),
        ('s1mple    ','NaVi     ','Ukr',      '1.34',     '0.88',     '36.1'),
        ('cadiaN    ','Heroic   ','Dnk',      '1.15',     '0.71',     '24.5'),
        ('Xyp9x     ','Astralis ','Dnk',      '0.97',     '0.59',     '43.9'),
        ('sh1ro     ','Gambit   ','Rus',      '1.26',     '0.77',     '26.2'),
        ('JaCkz     ','G2       ','Fra',      '0.98',     '0.63',     '64.3'),
        ('nexa      ','G2       ','Srb',      '0.97',     '0.60',     '53.0'),
        ('electronic','NaVi     ','Rus',      '1.08',     '0.68',     '49.5'),
        ('AmaNEk    ','G2       ','Fra',      '0.98',     '0.59',     '42.3'),
        ('B1T       ','NaVi     ','Ukr',      '1.02',     '0.66',     '66.3'),
        ('NiKo      ','G2       ','Bih',      '1.15',     '0.75',     '46.6'),
        ('sjuush    ','Heroic   ','Dnk',      '1.11',     '0.69',     '47.7'),
        ('Interz    ','Gambit   ','Rus',      '0.98',     '0.56',     '48.8'),
        ('Bubzkji   ','Astralis ','Dnk',      '1.04',     '0.70',     '43.2'),
        ('refrezh   ','Heroic   ','Dnk',      '1.10',     '0.68',     '51.4'),
        ('dupreeh   ','Astralis ','Dnk',      '1.02',     '0.66',     '51.7'),
        ('Boombl4   ','NaVi     ','Rus',      '0.98',     '0.60',     '44.2'),
        ('stavn     ','Heroic   ','Dnk',      '1.10',     '0.68',     '40.1'),
        ('Magisk    ','Astralis ','Dnk',      '1.03',     '0.63',     '52.0'),
        ('nafany    ','Gambit   ','Rus',      '1.07',     '0.69',     '48.9'),
        ('huNter-   ','G2       ','Bih',      '1.14',     '0.77',     '52.6'),
        ('gla1ve    ','Astralis ','Dnk',      '0.96',     '0.59',     '48.1'),
        ('Perfecto  ','NaVi     ','Rus',      '1.01',     '0.61',     '44.7'),
        ('TeSeS     ','Heroic   ','Dnk',      '1.13',     '0.72',     '58.7'),
        ('Ax1le     ','Gambit   ','Rus',      '1.21',     '0.77',     '48.1')]

# Создание и запись списка в таблицу
conn = sqlite3.connect('PlayersTable')
curs = conn.cursor()

curs.execute("""CREATE TABLE Players(
    Name TEXT,
    Team TEXT,
    Country TEXT,
    Rating TEXT,
    Kill_per_round TEXT,
    Headshot REAL)""")

curs.executemany("INSERT INTO Players VALUES (?, ?, ?, ?, ?, ?)", text)
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
