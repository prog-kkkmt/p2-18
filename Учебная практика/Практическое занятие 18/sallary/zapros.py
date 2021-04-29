import sqlite3

db = sqlite3.connect('sal.db')

cur = db.cursor()

db.commit()


names = cur.execute(" SELECT Surname, sallary FROM Sal JOIN Workers On Workers.id = Sal.id WHERE sallary > 6000 ")

for i in names:
    print(i)
