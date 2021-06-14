#Выполнил: Безбородов Константин
#Группа: П2-18
'''
К7_2. Техника работы со строками;

Задание 1. 
Задание 1. Подготовить сравнительную инструкцию по использованию
форматирования строк
'''

print("1 Форматирование строк “По старинке” (оператор %)")
print("name = \"PYH\"")
name = "PYH"
print("print('Hello, %s' %name)")
print("Output: Hello, %s" %name)
print()

print("Вывод в шестнадцатиричного числа")
print("errno = 50159747054")
errno = 50159747054
print("print('%x' % errno)")
print("Output: %x" % errno)
print("------------------------------------")
print()


print("2 Форматирование строк “По новому” (str.format)")
print("name = \"PYH\"")
name = "PYH"
print("print('Hello, {}'.format(name))")
print("Output:", 'Hello, {}'.format(name))
print()

print("Или")
print("errno = 50159747054")
errno = 50159747054
print("print(")
print("\t'Hey {name}, there is a 0x{errno:x} error!'.format("")")
print("\t\tname=name, errno=errno")
print("\t)")
print(")")
print(
    'Output: Hey {name}, there is a 0x{errno:x} error!'.format(
        name=name, errno=errno
    )
)
print("------------------------------------")
print()


print("3 Интерполяция строк / f-Строки (Python 3.6+)")
print("name = \"PYH\"")
name = "PYH"
print("print(f'Hello, {name}!')")
print(f'Output: Hello, {name}!')
print()

print("a = 5")
a = 5
print("b = 10")
b = 10
print("print(f'Five plus ten is {a + b} and not {2 * (a + b)}.')")
print(f'Five plus ten is {a + b} and not {2 * (a + b)}.')
print("------------------------------------")
print()


print("4 Шаблонные строки (Стандартная библиотека Template Strings)")
print("from string import Template")
from string import Template
print("name = \"PYH\"")
name = "PYH"
print("t = Template('Hey, $name!')")
t = Template('Hey, $name!')
print("print(t.substitute(name=name))")
print(t.substitute(name=name))
print()

print("templ_string = 'Hey $name, there is a $error error!'")
templ_string = 'Hey $name, there is a $error error!'
 
print("print(")
print("	Template(templ_string).substitute(")
print("		name=name, error=hex(errno)")
print("	)")
print(")")
print(
    Template(templ_string).substitute(
        name=name, error=hex(errno)
    )
)
print("------------------------------------")
print()
