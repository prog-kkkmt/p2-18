a = int(input())
b = int(input())
c = int(input())
k = 0
if a > 0:
    k += 1
if b > 0:
    k += 1
if c > 0:
    k += 1
else:
    print("Все числа отрицательные")
print(k)
