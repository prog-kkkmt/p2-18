def SumRange(x, y):
    s = 0
    if x < y:
        for i in range(x, y+1):
            s += i
        return s
    elif x > y:
        return 0

a, b, c = int(input()), int(input()), int(input())
print(SumRange(a, b))
print(SumRange(b, c))
