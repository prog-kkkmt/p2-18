a = input().split()
	n = 0
	for i in range(len(a)):
	    a[i]=int(a[i])
	for i in range(1,len(a)-1):
	    if a[i]>a[i-1] and a[i]>a[i+1]:
	        n+=1
	print(n)
