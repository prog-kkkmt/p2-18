# Выполнил Кузнецов М. С. П2-18.
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

# Синтаксис:
# import collections
# dq = collections.deque([iterable[, maxlen]])

# Параметры:
# iterable - итерируемая последовательность,
# maxlen   - int, максимальное кол-во хранимых записей.


# Примеры работы с ним:
from collections import deque
# Создаем
D = deque(["Mon", "Tue", "Wed"])
print(D)

# Добавим вправо
D.append("Thu")
print(D)

# Добавим влево
D.appendleft("Sun")
print(D)

# Убираем справа
D.pop()
print(D)

# Убираем слева
D.popleft()
print(D)

# Переворачиваем
D.reverse()
print(D)

# Можно ограничить его размер:
D = deque([], maxlen=3)
D.append(5)
print(D)
D.append(55)
print(D)
D.append(555)
print(D)
D.append(5555)
print(D)
# Когда будет превышен лимит, D[0] исчезнет.
