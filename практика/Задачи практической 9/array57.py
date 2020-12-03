import random
n = random.randrange(2, 22)
a = [i for i in range(n)]
b = a[0::2] + a[1::2]
print(n)
print(a)
print(len(b))
print(b)
