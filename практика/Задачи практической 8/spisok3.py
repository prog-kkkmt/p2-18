from random import randint
li=[]
mas=[]
jojo=[]
jostar=[]
bug=[]
n = int(input("Введите количество списков: "))
temp=0
for i in range (0,n,+1):
    for j in range(0,randint(2,5),+1):
        a=randint(0,5)
        mas.insert(j, a)
        if li.count(a)==0:
            li.append(a)
        if bug.count(a)==0:
            bug.append(a)
    temp+=1
    print("Список №",temp,": ",mas)
    jojo.extend(bug)
    bug.clear()
    mas.clear()
    for i in range(0,6,+1):
        if jojo.count(i)==n:
            jostar.append(i)
print("В каждом списке есть: ",jostar)
print("Хотя бы в одном списке есть: ",li)
