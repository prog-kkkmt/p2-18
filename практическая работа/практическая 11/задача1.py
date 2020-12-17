a = {}
sch = 1
for i in input().split():
    if i not in a:
        a.update({i:sch})
    else:
        a.update({i:a[i] + 1})
print(a)
