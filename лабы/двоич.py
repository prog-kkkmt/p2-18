text = open('четнечет.txt', 'w')
a = list(map(int,input().split()))
x=0
while len(a)>x: #for i in range(len(a))
    if a[x] % 2 != 0:
        a[x] = -a[x]
    x+=1
text.write(str(a))
text.close()
