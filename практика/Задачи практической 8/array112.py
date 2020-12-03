import random
n = random.randrange(2,10)
a = [random.randrange(0,10) for i in range(n)]
print("N = ", n)
print("Array:")
print(a)
for i in range(1, n) :
    for j in range(0,n - i) :
        if a[j] > a[j + 1] :
            a[j], a[j + 1] = a[j + 1], a[j]
print("Sort Array:")
print(a)
