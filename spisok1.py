# Списки Задача «Четные индексы»
# Выведите все элементы списка с четными индексами
spisok = input().split()
for index in range(0, len(spisok), 2):
    print(spisok[index])
