matrix = [[1, 3, 5, 0], [3, 1, 8, 7], [9, 0, 6, 7], [0, 1, 7, 3]]


def m_z(m: list):
    for i in range(len(m)):
        for j in range(i):
            m[i][j] = 0


for string in matrix:
    for item in string:
        print(item, end=' ')
    print()

print()

m_z(matrix)

for string in matrix:
    for item in string:
        print(item, end=' ')
    print()

print()
