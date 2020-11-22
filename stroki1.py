# Строки
# Задача «Делаем срезы»
a, b, c, d, e, f, g, h, i = (str(input()) for n in range(9))
print(a[2], b[-1], c[0:5], d[:-2], e[::2], f[1::2], g[::-1], h[::-2], len(i))
