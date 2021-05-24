# Выполнили Бурлаев Захар, Воронцов Александр
"""Данная программа добавляет в базу данных, имена учеников и их возраст, и выводит их из БД """

import sqlite3 as sq

# Подключаемся(создаём) к базе данных
conn = sq.connect("St.db")

# Подключаем курсор
cursor = conn.cursor()

#Создаём таблицу с именами и возрастом
cursor.execute("""CREATE TABLE IF NOT EXISTS students
                     (  Names text,
                        Age integer)
                        """)
# Подтверждаем изменения
conn.commit()

#Выводим в консоли меню с выбором доавить студента или показать список
print("1. Add student\n2. Show students")
n = int(input())
if n == 1:
    # Добавляем имя студента
    print("insert name")
    name = input()
    
    #Добавляем возраст студента
    print("insert age")
    age = int(input()) 
    
    # Добавляем значения в таблицу и сохраняем
    cursor.execute('''INSERT INTO students (Names, Age) VALUES(?, ?)''', (name, age,))
    conn.commit()

# При выборе второго пункта меню выводим посторчно значения из таблицы 
elif n == 2:
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    for row in rows:
        print(*row)
#Если число выбрано непраивльно, выводим оповещение        
else:
    print("Wrong number")
