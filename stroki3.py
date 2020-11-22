# Строки
# Задача «Две половинки»
a = input()
b = len(a) // 2 + len(a) % 2
print(a[b:] + a[:b])
