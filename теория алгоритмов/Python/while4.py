"""
Дано целое число N (> 0). Если оно является степенью числа 3,
то вывести true, если не является — вывести false.
"""
a = int(input ())
b = 1
while b < a:
    b = b*3
if b == a:
    print("true")
else:
    print("false")
