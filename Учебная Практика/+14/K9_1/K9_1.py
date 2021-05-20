#Выполнил: Зайцев Никита
#Группа: П2-18
'''
К9_1. Техника работы с циклом for и генераторами списков

Задание 1. (Л.Б.) Для проведения конкурса проектов в ККМТ формируются группы
из 4х участников: coder, writer, tester, designer, программирующих
на одном и том же языке.
Каждый студент может программировать только на одном языке
и занимать только одну позицию.
Дан текстовый файл, содержащий перечень студентов с указанием языка и позиции
(каждый студент с новой строки)
Требуется
1. Получить список студентов с указанием языка и позиции
2. Сформировать список всевозможных команд
3. Вывести список команд с указанием состава и названия команды:
Команда 1
coder: ...
designer: ...
tester: ...
writer: ...

Команда 2
...
Пункты 1 и 2 выполнить с использованием генераторов списка
'''


file = open("file.txt", "r")

def prof(mtrx,mas):             # Проверка на "подходит ли чел в команду"
    if (len(mtrx) == 0):
        return True
    count = 0
    for i in range(len(mtrx)):
        if(mtrx[i][1] != mas[1]):
            count += 1
        if(mtrx[i][2] == mas[2]):
            count += 1
    if(count == len(mtrx)*2):
        return True
    return False

#---------1--------------------
list_ = file.readlines()

out = [i.strip().split() for i in list_]
for i in range(len(out)):
    print(f'{out[i][1]}: {out[i][0]} | {out[i][2]}')
print()
print(out)
print('Всего участников - ', len(out), '\n')
#---------1--------------------
#[
# [
# ['Dima', 'coder', 'C++'],
# ['Roma', 'designer', 'C++'],
# ['Ivan', 'tester', 'C++'],
# ['Stiv', 'writer', 'C++']
# ]
#]
#---------2--------------------
teams = [[]]    #[[['Dima', 'coder', 'C++'], ['Roma', 'designer', 'C++'],['Ivan', 'tester', 'C++'],['Stiv', 'writer', 'C++']]]

k = 0
count = 0
i = 0
while(i != len(out)):
    if(prof(teams[k],out[i])):
        if(len(teams[k]) < 4):
            teams[k].append(out[i])
            out.pop(i)
            i -= 1
            if(len(teams[k]) == 4):
                teams.append([])
                k += 1
                i = 0
                continue
    i += 1
    if(i == len(out)):
        teams.append([])
        k += 1
        i = 0
teams.pop(-1)

#---------2--------------------
'''3. Вывести список команд с указанием состава и названия команды:
Команда 1
coder: ...
designer: ...
tester: ...
writer: ...

Команда 2
...'''

#---------3--------------------
l = 0
for i in range(len(teams)):
    if(len(teams[i]) < 4):
        print("Неполная команда")
    else:
        l += 1
        print("Команда", l)
    for j in range(len(teams[i])):
        print(f'{teams[i][j][1]}: {teams[i][j][0]} | {teams[i][j][2]}')
    print()

#---------3--------------------

