a = [int(n) for n in input().split()]
summa = 0
b = 0
while b != len(a) - 1:
    for n in range(b + 1, len(a)):
        if a[b] == a[n]:
            summa += 1
    b += 1
print(summa)
