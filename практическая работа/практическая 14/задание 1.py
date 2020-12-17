
f = open("text1.txt", "r")
a = f.read()
a += 'S'
f.close()
f = open("text1.txt", "w")
f.write(a)
f.close()
