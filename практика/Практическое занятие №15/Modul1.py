# Выполнил Толоконников Алексей Михайлович П2-18.
# Контейнерные типы данных модуля collections.
# Класс Counter() модуля collections в Python.

# Подсчет количества повторений элементов в последовательности.
# класс collections.Counter() предназначен для удобных и быстрых подсчетов количества появлений неизменяемых
# элементов в последовательностях.

# >>> from collections import Counter
# >>> cnt = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])
# >>> dict(cnt)
# # {'blue': 3, 'red': 2, 'green': 1}

# Синтаксис:
# import collections
# cnt = collections.Counter([iterable-or-mapping])

# Параметры:
# iterable-or-mapping - итерируемая последовательность или словарь.

# Пример работы с ним:

import collections

c = (['g', 'b', 'c', 'd', 'g', 'f', 'f', 'f', 'g', 'c', 'd'])
print('Оно помогает выводить количество неизменяемых элементов.\nПоследовательность: ', c)
print('Сколько в ней элементов:')
print(collections.Counter(c))

