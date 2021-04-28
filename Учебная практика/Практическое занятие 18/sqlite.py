import sqlite3 as sq

conn = sq.connect("St.db")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS students
                     (  Names text,
                        Age integer)
                        """)
conn.commit()

print("1. Add student\n2. Show students")
n = int(input())
if n == 1:
    print("insert name")
    name = input()
    print("insert age")
    age = int(input()) 
    cursor.execute('''INSERT INTO students (Names, Age) VALUES(?, ?)''', (name, age,))
    conn.commit()
elif n == 2:
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    for row in rows:
        print(*row)
else:
    print("Wrong number")
