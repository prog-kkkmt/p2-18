# Выполнил задание Михайлов Данила
# Контейнерные типы данных модуля collections.
# https://docs-python.ru/standart-library/modul-collections-python/
# Класс deque() модуля collections в Python.
# https://docs-python.ru/standart-library/modul-collections-python/klass-deque-modulja-collections/

# Двусторонняя очередь в Python.
# Класс collections.deque() это обобщение стеков и очередей и представляет собой двустороннюю очередь.
# Двусторонняя очередь deque() поддерживает поточно-ориентированные, эффективные по памяти операции добавления
# и извлечения элементов последовательности с любой стороны с примерно одинаковой производительностью O(1)
# в любом направлении.
#
# Списки поддерживают аналогичные операции, но они оптимизирован только для быстрых операций с последовательностями
# фиксированной длины и требуют затрат O(n) на перемещение памяти для операций pop(0) и insert(0, v), которые изменяют
# как размер, так и положение базового представления данных.

from collections import deque


d = deque(["One", "Two", "Three"])
print(d)

d.append("Four")# Добавим вправо
print(d)

d.appendleft("Zero")# Добавим влево
print(d)

d.pop()# Убираем справа
print(d)

d.popleft()# Убираем слева
print(d)

d.reverse()# Разворот
print(d)


d = deque([], maxlen=3)# Ограничение размера
d.append(1)
print(d)

d.append(12)
print(d)

d.append(123)
print(d)

d.append(1234)
print(d)
