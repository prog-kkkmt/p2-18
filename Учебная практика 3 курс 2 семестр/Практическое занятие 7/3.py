# Выполнил: Короленко И.Р.
# Группы: П2-18

s = input()
s = s.replace(".", " ")
s1 = s.split()
s1 = [int(x) for x in s1]
print(s)
print(sum(s1))
