#Выполнил Завадский Михаил П2-18.
#Необходимо вывести все четные числа на отрезке [a; a * 10].
a= int(input())
b=a
if b%2==1:
    b=b+1
print(tuple(range(b,a*10+1,2)))
