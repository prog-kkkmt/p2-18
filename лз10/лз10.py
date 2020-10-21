text = open('лз10.txt', 'w')
a = list(map(int, input().split()))
for i in range(len(a)):
    if a[i] % 2 != 0:
        a[i] = -a[i]
text.write(str(a))
text.close()
