f = open('propusk.txt', 'r')
a = []
b = 0
for i in f:
    a.append(i.split(" - "))
for i in range(len(a)):
    b += int(a[i][1])
f.close()
f = open('propusk1.txt', 'w')
f.write(str(b))
f.close()
