#Выполнил Щепкин Михаил П2-18
#Импортируем sqlite3
import sqlite3
#Создаём базу данных.
db = sqlite3.connect('TableBase.db')
sql = db.cursor()
#Создаём таблицу в базе данных.
sql.execute("""CREATE TABLE IF NOT EXISTS DataBase (Age INTEGER, Login REAL, Password REAL)""")
db.commit()
#Вводим: Возраст, Логин и Пароль.
DataBase_Age = input('Age: ')
DataBase_Login = input('Login: ')
DataBase_Password = input('Password: ')
#Проверяем логин который был введен.
sql.execute(f"SELECT Login FROM DataBase WHERE Login = '{DataBase_Login}'")
if sql.fetchone() is None:
	sql.execute(f"INSERT INTO DataBase VALUES('{DataBase_Age}','{DataBase_Login}','{DataBase_Password}')")
	db.commit()
#Если логин не используется выводим.
	print("Зарегестрировано!")
else:
#Если логин уже был использован выводим.
	print("Такой логин уже существует!")
	print("Список логинов которые уже были зарегистрированы: ")
	for value in sql.execute("SELECT * FROM DataBase"):
		print(value[1])
db.close()
