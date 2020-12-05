matrix = [[1, 3, 5, 0], [3, 1, 8, 7], [9, 0, 6, 7]]


def swap(m: list):
    size = int(len(m[0]) / 2)
    left_half = []
    right_half = []

    for s in m:
        left_half.append(list(s[i] for i in range(size)))
        right_half.append(list(s[i] for i in range(size, len(s))))

    res = []
    for i in range(len(m)):
        res.append(right_half[i] + left_half[i])
    return res


for string in matrix:
    for item in string:
        print(item, end=' ')
    print()

print()
result = swap(matrix)

for string in result:
    for item in string:
        print(item, end=' ')
    print()
