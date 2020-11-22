# Строки
# Задача «Переставить два слова»
a = input()
b = a.find(" ")
c1 = a[:int(b) + 1]
c2 = a[int(b):]
print(c2 +" "+ c1)
