# Выполнил:Степаненко Кирилл
# Группа: П2-18

# Задача «Количество совпадающих чисел»
# Условие. Даны два списка чисел. Посчитайте, сколько чисел содержится одновременно как
# в первом списке, так и во втором.

s1 = set(input().split())

s2 = set(input().split())

print(set.intersection(s1,s2))