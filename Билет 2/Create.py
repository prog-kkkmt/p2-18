import sqlite3

#----------------------------------
text = [(123, 'Стрыгин Иван Павлович'),
        (234, 'Ковалев Степан Павлович'),
        (558, 'Зиновьева Софья Демидовна'),
        (789, 'Назарова Мария Тиграновна')]

conn = sqlite3.connect('Table')
curs = conn.cursor()
curs.execute("""CREATE TABLE Покупатели(
                Код_покупателя INTEGER,
                ФИО TEXT)""")
curs.executemany("INSERT INTO Покупатели VALUES (?, ?)", text)
conn.commit()
#----------------------------------
text = [(1, 'Вилов Анатолий Никитович'),
        (2, 'Спиридонова Виктория Николаевна'),
        (3, 'Ефимова Василиса Ильинична'),
        (4, 'Федотов Илья Маркович')]

conn = sqlite3.connect('Table')
curs = conn.cursor()
curs.execute("""CREATE TABLE Менеджеры(
                Код_менеджера INTEGER,
                ФИО TEXT)""")
curs.executemany("INSERT INTO Менеджеры VALUES (?, ?)", text)
conn.commit()
#----------------------------------
text = [(2281337, 'Sequoia'),
        (4547896, 'ВАЗ'),
        (7873241, 'AUDI'),
        (1161178, 'Hyundai')]

conn = sqlite3.connect('Table')
curs = conn.cursor()
curs.execute("""CREATE TABLE Автомобили(
                Код_автомобиля INTEGER,
                Марка TEXT)""")
curs.executemany("INSERT INTO Автомобили VALUES (?, ?)", text)
conn.commit()
#----------------------------------
text = [(1, 2281337, 'в666ад', 123, '13.08.2021', 3500000),
        (2, 7873241, 'к457мр', 558, '21.02.2020', 3000000),
        (4, 4547896, 'а228ну', 789, '02.11.2021', 200000),
        (2, 7873241, 'в747тр', 234, '09.09.2019', 2800000)]

conn = sqlite3.connect('Table')
curs = conn.cursor()
curs.execute("""CREATE TABLE Продажи(
                Код_менеджера INTEGER,
                Код_автомобиля INTEGER,
                Гос_номер TEXT,
                Код_покупателя INTEGER,
                Дата TEXT,
                Цена INTEGER)""")
curs.executemany("INSERT INTO Продажи VALUES (?, ?, ?, ?, ?, ?)", text)
conn.commit()
#----------------------------------
