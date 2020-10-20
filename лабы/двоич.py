a=list()
b=int(input('Укажите количество поступающих чисел: '))
c=0
while c<b:
    e=input()
    a.append(e)
    c+=1
f = ' '.join(a)
with open("четнечет1.txt", "w") as file:
    file.write(f)
with open("четнечет1.txt", "r") as file:
    ref = file.read()
ref=ref.split(' ')
for i in range(len(ref)):
    if int(ref[i]) % 2 == 1:
        ref[i]=int(ref[i])*-1
        ref[i]=str(ref[i])
f = ' '.join(ref)
with open("четнечет2.txt", "w") as file:
    file.write(f)

