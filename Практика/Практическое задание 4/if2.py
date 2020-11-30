A = int(input())
B = int(input())
if A == B:
    A += B
    B = A
elif A != B:
    A = 0
    B = 0
else:
    print("Ошибка")
print("A =", A,"B =", B)
