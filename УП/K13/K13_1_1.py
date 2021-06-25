#Выполнил:Степаненко Кирилл
#Группа: П2-18
#Вывести чётные
#Необходимо вывести все четные числа на отрезке [a; a * 10].

n = int(input())
k = n * 10

if n % 2 == 0:
    s1 = tuple(n for n in range(k+1))
    s2 = s1[0:len(s1):2]
    print(s2)
else:
    s1 = tuple(n for n in range(k+1))
    s2 = s1[2:len(s1):2]
    print(s2)