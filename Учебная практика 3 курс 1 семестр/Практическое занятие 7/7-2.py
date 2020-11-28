# Выполнил: Короленко Иван Романович
# Группа: П2-18

# Задание 1. Подготовить сравнительную инструкцию по использованию
# форматирования строк

# 1 Форматирование строк “По старинке” (оператор %)
name = input()
print('1) Hello, %s' % name)

# 2 Форматирование строк “По новому” (str.format)
print('2) Hello, {}'.format(name))

# 3 Интерполяция строк / f-Строки (Python 3.6+)
print(f'3) Hello, {name}!')
 
def greet(name, question):
    return f"Hello, {name}! How's it {question}?"
print(greet(name, 'going'))

# 4 Шаблонные строки (Стандартная библиотека Template Strings)
from string import Template
t = Template('4) Hey, $name!')

print(t.substitute(name=name))

# Если для подстановки требуется только один аргумент,
# то значение - сам аргумент:
print('Hello, {}!'.format(name))
# А если несколько, то значениями будут
# являться все аргументы со строками подстановки (обычных или именованных):
print('{0}, {1}, {2}'.format('a', 'b', 'c'))
print('Coordinates: {latitude}, {longitude}'.format(latitude='37.24N', longitude='-115.81W'))
# В общем случае, аргументы могут быть как именованными, так и позиционными:
s = '{x}; {0}; {y}; {1}'
print(s.format('A', 'B', x = 1, y = 2))
# Здесь нужно обратить внимание на два нюанса: первый – позиционные аргументы, должны следовать перед именованными;
# второй – аргументами могут быть данные любого типа:
s = '{int}; {float}; {complex}'
print(s.format(int = 2, float = 2e-5, complex = 2+0.2j))
a = list(range(3))
b = dict([[1,'a'],[2,'b']])
c = set('aabbcc')
s = '{list}; {dict}; {set}'
print(s.format(list = a, dict = b, set = c))
# Мало того, что мы можем подставлять списки и словари, мы еще и можем обращаться к элементам, которые в них расположены.
