#Вы уже знакомы с термином "факториал",
#однако предыдущее наше решение не идеально – оно считает
#факториал только одного числа. Модифицируйте вашу программу из
#задачи "18!" таким образом, чтобы она принимала на вход натуральное
#число n и печатала значение выражения n!
a = int(input())
factorial = 1
for n in range(2, a+1):
    factorial *= n
print(factorial)
