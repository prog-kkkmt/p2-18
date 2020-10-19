text = open('четнечет.txt', 'w')
a = list(map(int, input().split()))
for i in range(len(a)):
 if a[i] % 2 != 0:
  a[i] = -a[i]
print(a)
text.write(str(a))
text.close()