# Строки
# Задача «Второе вхождение»
a = input()
StrF = a.count("f")
if StrF == 1:
    print(-1)
elif StrF >= 2:
    f = a.find("f")
    buf = s[int(f)+1:]
    f += buf.find("f") + 1
    print(f)
else:
    print(-2)
