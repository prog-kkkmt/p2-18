print("Ввелите 2 числа: ")
a=int(input())
b=int(input())
if a<b:
    a,b=b,a
for i in range (a,0,-1):
    if a%i==0 and b%i==0:
        break
print("Наибольший общий делитель: ",i)
