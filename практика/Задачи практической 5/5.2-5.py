a = int(input())
b = []
for n in range(a):
    j = 0
    while j < n + 1:
        b.append(n + 1)
        j += 1
    if len(b) > a: break
b = b[0:a]
for n in b:
    print(n, end=" ")
