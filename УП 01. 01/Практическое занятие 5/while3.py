#Выполнил Кузнецов М. С. П2-18.
#По данному натуральному числу N найдите наибольшую целую степень двойки, не превосходящую N.
#Выведите показатель степени и саму степень.
#Операцией возведения в степень пользоваться нельзя!
n = int(input("Введите натуральное число N:"))
x = 2
y = 1
while x <= n:
    x *= 2
    y += 1
print(y - 1, x // 2)
