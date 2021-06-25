# Выполнил:Степаненко Кирилл Алексеевич
# Группа: П2-18
# https://stepik.org/lesson/201702/step/9?unit=175778

# Уберите точки из введенного IP-адреса.
# Выведите сначала четыре числа через пробел, а затем сумму получившихся чисел.

lst = []
summ = 0
a = input()
a = a.split(".")
for i in a:
    lst.append(int(i))
a = " ".join(a)
print(a)
print(sum(lst))