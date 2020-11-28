#Выведите все элементы списка с четными индексами (то есть A[0], A[2], A[4], ...).
spisok = input().split()
for index in range(0, len(spisok), 2):
    print(spisok[index])
