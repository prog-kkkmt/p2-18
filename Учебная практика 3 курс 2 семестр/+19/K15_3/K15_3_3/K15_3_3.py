#Выполнил: Кузнецов Матвей
#Группа: П2-18
'''
К15_3. Техника работы с модулями

Модуль sys в Python.
https://docs-python.ru/standart-library/modul-sys-python/

Задание 3. Различные сведения о версии Python.
https://docs-python.ru/standart-library/modul-sys-python/razlichnye-svedenija-versii/
'''

import sys

string = sys.version_info
print(string)
print(sys.copyright)
print("API C languages: ", sys.api_version)
print(sys.version)
print("Hex version: ", sys.hexversion)

