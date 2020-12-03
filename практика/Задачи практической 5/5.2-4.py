mas=[-1]
print("Введите числа: ")
while(mas.count(0)!=1):
    mas.insert(1,int(input()))
    mas[0]=mas[0]+mas[1]
    #print(mas) #если нужно посмотреть лист
print("Сумма: ",mas[0]+1)
c=1
for i in range (2,len(mas)-1,+1):
    a=abs(mas[i])
    b=abs(mas[i+1])
    if a<b:
        a,b=b,a
    if a%b==0:
        mas[i+1]=a
        c=a
    else:
        c=a
        mas[1]=0
        while(mas[1]==0):
            if c%b==0 and c%a==0:
                mas[i+1]=c
                mas[1]=1
            else:
                c+=1
print("НОК: ",c)
