#Выполнил: Безбородов Константин
#Группа: П2-18

'''
К15_1. Техника работы с модулями

Задание 1. Вывод текущей директории
Задание 2. Создание папки
Задание 3. Изменение директории
Задание 4. Создание вложенных папок
Задание 5. Создание файлов
Задание 6. Переименование файлов
Задание 7. Перемещение файлов
Задание 8. Список файлов и директорий
Задание 9. Удаление файлов
Задание 10. Удаление директорий
Задание 11. Получение информации о файлах
'''
import os

#Задание 1. Вывод текущей директории
print("Текущая деректория:", os.getcwd())
print()


#Задание 2. Создание папки
if not os.path.isdir("Балдеж"):  # Проверка на отсутсвие папки с таким названием
    os.mkdir("Балдеж")


#Задание 3. Изменение директории
os.chdir("./Балдеж")

if not os.path.isdir("Новая папка"):  # Проверка на отсутсвие папки с таким названием
    os.mkdir("Новая папка")

os.chdir("Новая папка")

print("Текущая директория изменилась на :", os.getcwd())
print()


#Задание 4. Создание вложенных папок
os.chdir("..")
path_dir = os.getcwd()

n = int(input("Введите количество вложенных папок, которые вы хотите создать: "))

for i in range(n):
    path = path_dir + "/Папка " + str(i)
    os.mkdir(path)
    path_dir += "/Папка " + str(i)
print()

#Задание 5. Создание файлов
file = open("file.txt", "w")
file.write("Уж тварь ли я дрожащая или право имею?")
file.close()


#Задание 6. Переименование файлов
file = open("newfile.txt", "w")
file.write("Ну, да, я файл. И что")
file.close()
Second_name = input("Как Вы хотите переименовать файл: ")
os.rename("newfile.txt", Second_name)
print()


#Задание 7. Перемещение файлов
file = open("First_name.txt", "w")
file.close()
os.replace("First_name.txt", "Новая папка/First_name.txt")


#Задание 8. Список файлов и директорий
# распечатать все файлы и папки
for dirpath, dirnames, filenames in os.walk("."):	#Перебирает все переданные составляющие.
	# перебрать каталоги
	for dirname in dirnames:
		print("Каталог:", os.path.join(dirpath, dirname))
	# перебрать файлы
	for filename in filenames:
		print("Файл:", os.path.join(dirpath, filename))
print()


#Задание 9. Удаление файлов
File_name = input("Введите имя файла: ")
f = open(File_name + ".txt", "w")
f.close()

os.remove(File_name + ".txt")


#Задание 10. Удаление директорий
os.mkdir('Bruh')
print("Текущая деректория:", os.getcwd())
print("Все папки и файлы: ", os.listdir())
del_name = input("Введите имя папки которую Вы хотите удалить: ")
os.rmdir(del_name)
print()

#Задание 11. Получение информации о файлах
f = open("text.txt", "w")
f.write('Hell, World')
f.close()
print(os.stat("text.txt"))
os.remove("text.txt")
print()










