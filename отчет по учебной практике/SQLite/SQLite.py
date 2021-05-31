import sqlite3

# Функция для таблицы в базе данных
def Create():
    cursor.execute("""CREATE TABLE albums(Name text, Integer int)""")
    conn.commit()

# Ввод значений
def Input(text):
    cursor.executemany("INSERT INTO albums VALUES (?,?)", text)
    conn.commit()

# Удаление по названиям
def Delete(n):
    sql = "DELETE FROM albums WHERE Name = ?"
    cursor.execute(sql, (n, ))
    conn.commit()

# Создание базы данных
conn = sqlite3.connect('Base')
cursor = conn.cursor()

Create()

# Цикл выполнения запросов
while True:
    text_a = input().split()

    # Команда для остановки цикла
    if text_a == ['stop']:
        break
    elif len(text_a) == 1:
        # Проверка на нахождение имени в базе данных
        info = cursor.execute('SELECT * FROM albums WHERE Name = ?', (text_a[0], )).fetchall()
        if len(info):
            Delete(text_a[0])
            print(text_a[0] + ' deleted')
            continue
        else:
            print('Error')
            continue

    
    text_a = [tuple(text_a)]
    Input(text_a)
