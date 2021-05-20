#Выполнил: Зайцев Никита
#Группа: П2-18
'''
К15_3. Техника работы с модулями

Модуль sys в Python.
https://docs-python.ru/standart-library/modul-sys-python/

Задание 2. Имя используемой OS.
https://docs-python.ru/standart-library/modul-sys-python/imja-ispolzuemoj-os/
'''

import sys
import os

if sys.platform.startswith('linux'):
    print(f"This is linux {os.name}")
else:
    print(f"This is not linux. This is {os.name}")
    print(sys.getwindowsversion())

