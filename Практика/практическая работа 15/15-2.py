# Выполнил задание Яковлев Прокопий Максимович
# Варианты использования defaultdict
from collections import defaultdict

a = [('a', 1),
     ('b', 2),
     ('c', 3),
     ('a', 4),
     ('c', 5)]

b = {}
for k, v in a:
    b.setdefault(k, []).append(v)

sorted(b.items())
print(a)
print(b)


print()###


s = [('a', 1),
     ('b', 2),
     ('b', 3),
     ('a', 4),
     ('a', 5),
     ('b', 6)]

d = defaultdict(set)
for k, v in s:
    d[k].add(v)

sorted(d.items())
print(d)


print()###


def c(a):
    return lambda: a

d = defaultdict(c('<missing>'))
d.update(name='Micke', action='kick')
print(d)
