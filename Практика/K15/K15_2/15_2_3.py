#Выполнили: Щепкин М.В П2-18
# Задание 3. Изменение директории
changesName = input()
os.chdir(changesName)
print("Текущая директория изменилась на", "<", changesName, ">", ":", os.getcwd())
