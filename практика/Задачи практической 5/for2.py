#Посчитайте сумму всех чисел на полуинтервале [a; b) или [b; a),
#в зависимости от того, какое число больше.
a = int(input())
b = int(input())
sum = 0
if a < b:
    for c in range(a, b):
        sum += c
else:
    for c in range(b, a):
        sum += c
print(sum)
