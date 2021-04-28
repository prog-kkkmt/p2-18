#Выполнил: Кузнецов Матвей
#Группа: П2-18
'''
К4_2. Техника работы с разветвляющимися программами

Задание 2. Разработать программу с меню для демонстрации работы с типами данных:
список(list), словарь(dict), множество(set)
Меню -> выбор типа данных -> выбор метода -> краткая справка
'''




import sys

stdin_f = sys.stdin

print('Добро пожаловать в меню:')

print('{| 1. Узнать про сипсок    |}')
print('{| 2. Узнать про множество |}')
print('{| 3. Узнать про словарь   |}')
print('{| 0. Выйти из программы   |}')
print('Выберите пункт меню: ')
a = int(input())
if(a == 1):
    print('1. Пояснение (что такое список)')
    print('2. Некоторые методы списка')
    print('Выберите пункт:')
    b = int(input())
    if(b == 1):
        stdin_f = open('list.txt', "r")
        print(*stdin_f)
        stdin_f.close()

    elif(b == 2):
        stdin_f = open('list_m.txt', "r")
        print(*stdin_f)
        stdin_f.close()

elif(a == 2):
    print('1. Пояснение (что такое множество)')
    print('2. Некоторые методы множества')
    print('Выберите пункт:')
    c = int(input())
    if(c == 1):
        stdin_f = open('set.txt', "r")
        print(*stdin_f)
        stdin_f.close()

    elif(c == 2):
        stdin_f = open('set_m.txt', "r")
        print(*stdin_f)
        stdin_f.close()

elif(a == 3):
        print('1. Пояснение (что такое словарь)')
        print('2. Некоторые методы словаря')
        print('Выберите пункт:')
        d = int(input())
        if(d == 1):
            stdin_f = open('dict.txt', "r")
            print(*stdin_f)
            stdin_f.close()

        elif(d == 2):
            stdin_f = open('dict_m.txt', "r")
            print(*stdin_f)
            stdin_f.close()
elif(a == 0):
    print('Goodbye!')
    exit(0)
else:
    while(a < 0 or a > 3):
        print("Попробуйте ввести корректный пункт меню:")
        a = int(input())