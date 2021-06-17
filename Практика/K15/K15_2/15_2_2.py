#Выполнили: Щепкин М.В П2-18
# Задание 2. Создание папки
fileName = input('Введите имя файла: ')
if not os.path.isdir(fileName):
    os.mkdir(fileName) 
