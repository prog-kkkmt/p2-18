# Выполнил:Степаненко Кирилл Алексеевич
# Группа: П2-18
# Задание 3. https://pythontutor.ru/lessons/sets/problems/sets_intersection/
# Задача «Пересечение множеств»
# Условие. Даны два списка чисел. Найдите все числа, которые входят как в первый,
# так и во второй список и выведите их в порядке возрастания.
a = set(input().split())
b = set(input().split())
c = list(a & b)
for i in range (len(c)):
    c[i] = int(c[i])
c.sort()
print(' '.join([str(i) for i in c]))
