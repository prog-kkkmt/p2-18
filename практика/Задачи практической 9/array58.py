import random
n = random.randrange(2,22)
a = [i for i in range(n)]
b = []
b.append(a[0])
print(n)
print(a)
for i in range(1, n) :
    b.append(a[i] + b[i - 1])
print(len(b))
print(b)
