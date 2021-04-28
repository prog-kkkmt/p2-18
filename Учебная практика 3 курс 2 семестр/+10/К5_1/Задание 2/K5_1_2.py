#Выполнил: Кузнецов Матвей
#Группа: П2-18
'''
К5_1. Техника работы с циклическими программами _ цикл while

Задание 2.Придумать пример(ы) на использование break / continue /else.
'''

summ = 0
count = 0
while True:
    count += 1
    num = int(input("Введите число: "))
    if num < 10:
        continue
    if num > 100:
        summ += num
        break
    else:
    	summ += num
    	print(f"{count}| num: {num}, summ: {summ}")
print(f"{count}| num: {num}, summ: {summ}")
print()


print("Вводится строка и искомая буква. Надо найти номер буквы в строке и вывести её номер")
string = input()
find_letter = input()
n = 0
for i in range(len(string)):
    if (string[i] == find_letter):
        n = i+1
        break
print(n) if n else print("Буква в строке не найдена")
    

