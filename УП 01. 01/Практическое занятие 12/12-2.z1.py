# Выполнил Слесарев А. М. П2-18.
# Простейшая система проверки орфографии может быть основана на использовании списка известных слов.
# Если введённое слово не найдено в этом списке, оно помечается как "ошибка".
# Попробуем написать подобную систему.
# На вход программе первой строкой передаётся количество d известных нам слов, после чего
# на d строках указываются эти слова.
# Затем передаётся количество l строк текста для проверки, после чего l строк текста.
# Выведите уникальные "ошибки" в произвольном порядке. Работу производите без учёта регистра.


a = int(input())
b = []
for i in range(a):
    x = input().lower()
    if x not in b:
        b.append(x)

d = int(input())
e = []
for j in range(d):
    x = input().lower().split()
    for i in x:
        if i not in b and i not in e:
            e.append(i)

print('\n'.join(e))
