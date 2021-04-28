l = []
a = input().split(".")
for n in a:
    l.append(int(n))
a = " ".join(a)
print(a, "\n", sum(l))
