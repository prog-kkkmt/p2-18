import sqlite3

# Массив для внесения данных в таблицы
bus = []

# Создание/Подключение к базе данных
conn = sqlite3.connect('Bus.db')
print('Создание/Подключение базы данных...\n')
curs = conn.cursor()

# Проверка удалена ли таблица в файле 'Bus.db'.
try:

    # Создание таблиц
    curs.execute("""CREATE TABLE Cтанции(Код_станции INTEGER,
                 Название_станции TEXT)""")

    curs.execute("""CREATE TABLE Автобусы(Код_автобуса INTEGER,
                 Марка_автобуса TEXT, Государственный_номер TEXT,
                 Вместимость INTEGER)""")

    curs.execute("""CREATE TABLE Рейсы(Код_рейса INTEGER,
                 Код_станции INTEGER, Код_автобуса INTEGER,
                 Время_отправления TEXT)""")

    # Внесение данных в таблицы
    bus = [('1','Фрязино'),
            ('2','Ивантеевка'),
            ('3','Зеленый Бор'),
            ('4','Подлипки дачные'),
            ('5','Мытищи'),
            ('6','Москва')]
    curs.executemany('INSERT INTO Cтанции VALUES (?, ?)' , bus)

    bus = [('1','ГАЗ', 'Е277УР','25'),
            ('2','ПАЗ', 'А083КН','35'),
            ('3','УАЗ', 'С121ВМ','17'),
            ('4','НефАЗ', 'Н722ВТ','50'),
            ('5','ЛиАЗ', 'Е155ЕА','22'),
            ('6','ЗИЛ', 'Е142СМ','43')]
    curs.executemany('INSERT INTO Автобусы VALUES (?, ?, ?, ?)' , bus)

    bus = [('1','3', '1','13:00'),
            ('2','5', '6','11:00'),
            ('3','6', '4','16:00'),
            ('4','2', '5','18:00'),
            ('5','4', '3','19:00'),
            ('6','1', '2','21:00'),
            ('7','1', '6','21:30'),
            ('8','6', '5','22:00'),
            ('9','1', '4','22:30'),
            ('10','4', '3','23:00'),]
    curs.executemany('INSERT INTO Рейсы VALUES (?, ?, ?, ?)' , bus)

    # Сохранение базы данных
    conn.commit()
    print('Таблицы успешно созданы\n')
    
# Если таблицы уже существуют в 'Bus.db',
# то программа продолжит работу, без вывода ошибок в консоль.
except sqlite3.OperationalError:
    None
