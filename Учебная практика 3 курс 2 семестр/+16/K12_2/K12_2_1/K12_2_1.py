#Выполнил: Кузнецов Матвей
#Группа: П2-18
'''
К12_2. Техника работы с множествами

Задание 1. https://stepik.org/lesson/3380/step/3?unit=963
Простейшая система проверки орфографии может быть основана на использовании списка известных слов.
Если введённое слово не найдено в этом списке, оно помечается как "ошибка".
Попробуем написать подобную систему.
На вход программе первой строкой передаётся количество d известных нам слов, после чего
на d строках указываются эти слова.
Затем передаётся количество l строк текста для проверки, после чего l строк текста.
Выведите уникальные "ошибки" в произвольном порядке. Работу производите без учёта регистра.
'''

count = int(input())
words = set()
for i in range(count):
    s = input().lower()
    words.add(s)

errors = set()
l = int(input())
for i in range(l):
    str = input().lower().split()
    for j in s:
        if(j not in words and j not in errors):
            errors.add(j)
print('\n'.join(errors))

