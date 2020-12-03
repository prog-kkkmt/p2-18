import random
n = random.randrange(2, 10)
a = [random.randrange(1, 8) for i in range(n)]
print(n)
print(a)
for i in range(1, n):
    d = False
    b = a[i]
    c = i - 1
    while c >= 0 :
        if b >= a[c] :
            break
        else :
            a[c + 1] = a[c]
            d = True
        c -= 1
    if d and c >= -1:
        a[c + 1] = b
    print(i)
    print(a)
print(a)
