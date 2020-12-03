import random
n = random.randrange(2, 24)
a = [i for i in range(n)]
b = a[1::2]
print(n)
print(a)
print(len(b))
print(b)
