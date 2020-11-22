# Строки
# Задача «Первое и последнее вхождения»
a = input()
StrF=a.count("f")
if StrF == 1:
    print(a.find("f"))
elif StrF >= 2:
    print(a.find("f"))
    print(a.rfind("f"))
