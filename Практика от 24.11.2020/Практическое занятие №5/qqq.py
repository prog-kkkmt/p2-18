student = {}
for line in open('text.txt'):
    line = line.split('\n')
    line = line[0]
    line = line.split(' ')
    student[line[0]] = line[1:]
#print(sorted(student))
print(student)
