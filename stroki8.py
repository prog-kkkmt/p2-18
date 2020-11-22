# Строки
# Задача «Обращение фрагмента»
a = input()
Str1 = a[:int(a.find("h"))]
Str2 = a[int(a.rfind("h") + 1):]
Str3 = a[int(a.find("h")):int(a.rfind("h") + 1)]
a = (Str1 + Str3[::-1] + Str2)
print(a)
