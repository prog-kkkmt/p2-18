# Слесарев А.М. П2-18.

from collections import defaultdict

a = [('Леша', 1), ('Ваня', 2), ('Мотя', 3), ('Леша', 4), ('Мотя', 1)]
b = {}
for k, v in a:
    b.setdefault(k, []).append(v)

sorted(b.items())
print(a)
print(b)


##############


def constant_factory(value):
    return lambda: value


d = defaultdict(constant_factory('<missing>'))
d.update(name='John', action='ran')
print(d)


####################


s = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4), ('red', 1), ('blue', 4)]
d = defaultdict(set)
for k, v in s:
    d[k].add(v)

sorted(d.items())
print(d)
