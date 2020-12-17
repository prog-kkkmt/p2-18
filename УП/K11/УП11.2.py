# Выполнил:Степаненко Кирилл Алексеевич
# Группа: П2-18
# https://pythontutor.ru/lessons/dicts/problems/permissions/
# Условие. В файловую систему одного суперкомпьютера проник вирус, который сломал контроль
# за правами доступа к файлам. Для каждого файла известно, с какими действиями можно к
# нему обращаться:
def conv(s):
    if s == 'write':
        return 'w'
    elif s == 'read':
        return 'r'
    else:
        return 'x'

n = int(input())
data = {}
for i in range(n):
    a, *b = input().split()
    data[a] = ''.join(b).lower()
n = int(input())
for i in range(n):
    a, b = input().split()
    if conv(a) in data[b]:
        print('OK')
    else:
        print('Access denied')