a = [int(n) for n in input().split()]
b = 0
for n in range(1, len(a) - 1):
    if a[n - 1] < a[n] > a[n + 1]:
        b += 1
print(b)
