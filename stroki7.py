# Строки
# Задача «Удаление фрагмента»
a = input()
Str1 = a[:int(a.find("h"))]
Str2 = a[int(a.rfind("h") + 1):]
print(Str1 + Str2)
