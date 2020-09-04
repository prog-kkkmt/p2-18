#If4. Даны три целых числа.
#Найти количество положительных чисел в исходном наборе.
a = int(input())
b = int(input())
c = int(input())
flag = 0 
for i in a, b, c:
    if i > 0:
        flag += 1
print(flag)
