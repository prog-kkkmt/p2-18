#Выполнили: Щепкин М.В П2-18

"""
Контейнерные типы данных модуля collections.
Класс Counter() модуля collections в Python.
https://docs-python.ru/standart-library/modul-collections-python/klass-counter-modulja-collections/

Подсчет количества повторений элементов в последовательности.
класс collections.Counter() предназначен для удобных и быстрых подсчетов количества появлений неизменяемых
элементов в последовательностях.

>>> from collections import Counter
>>> cnt = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])
>>> dict(cnt)
{'blue': 3, 'red': 2, 'green': 1}

Синтаксис:
import collections
cnt = collections.Counter([iterable-or-mapping])

Параметры:
iterable-or-mapping - итерируемая последовательность или словарь.
"""

# Примеры работы с ним:

import collections

c = (['a', 'b', 'c', 'd', 'e', 'f', 'f', 'f', 'a', 'c', 'd'])
print('Оно помогает выводить количество неизменяемых элементов.\nПоследовательность: ', c)
print('А сколько в ней элементов:')
print(collections.Counter(c))
print('\n')
print('Так же с помощью ')
