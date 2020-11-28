#Дан список чисел. Выведите все элементы списка,
#которые больше предыдущего элемента.
spisok = [int(n) for n in input().split()]
for n in range(1, len(spisok)):
    if spisok[n] > spisok[n - 1]:
        print(spisok[n])
