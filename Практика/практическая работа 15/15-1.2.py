# Выполнил задание Яковлев Прокопий Максимович
# Контейнерные типы данных модуля collections.
# Класс Counter() модуля collections в Python.
# https://docs-python.ru/standart-library/modul-collections-python/klass-counter-modulja-collections/

# Подсчет количества повторений элементов в последовательности.
# класс collections.Counter() предназначен для удобных и быстрых подсчетов количества появлений неизменяемых
# элементов в последовательностях.
# 
# from collections import Counter
# c = Counter(['a', 'b', 'a', 'c', 'b', 'a'])
# print(dict(c))
# Вывод => {'a': 3, 'b': 2, 'c': 1}

import collections

c = (['a', 'b', 'a', 'c', 'c', 'b', 'a', 'c', 'a', 'a', 'b'])
print(c)# Вывод списка
print(collections.Counter(c))# Вывод кол-ва каждых элементов в списке
