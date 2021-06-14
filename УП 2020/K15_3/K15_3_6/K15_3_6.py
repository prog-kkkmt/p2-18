#Выполнил: Безбородов Константин
#Группа: П2-18
'''
К15_3. Техника работы с модулями

Модуль sys в Python.
https://docs-python.ru/standart-library/modul-sys-python/

Задание 6. Функция exit() модуля sys в Python.
https://docs-python.ru/standart-library/modul-sys-python/funktsija-exit-modulja-sys/
'''

import sys

if len(sys.argv) > 1:
	if ("-exit" in sys.argv) or ("-e" in sys.argv):
		print("Ну вы вышли")
		sys.exit(0)
