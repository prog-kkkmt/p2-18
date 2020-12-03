mas=[-1]
print("Введите числа: ")
while(mas.count(0)!=1):
    mas.insert(1,int(input()))
    mas[0]=mas[0]+mas[1]
    #print(mas) если нужно посмотреть лист
print("Сумма: ",mas[0]+1)
