#Выполнил: Безбородов Константин
#Группа: П2-18
'''
К12_2. Техника работы с множествами

Задание 2. (Л.Б.) Сессия
В файле disc.txt хранится перечень дисциплин, выносимых на сессию, например,
Теория алгоритмов
МДК.01.01
Основы экономики
...

В файле session.txt хранятся сведения о результатах сессии, например,
Грушников; П2-18; Теория алгоритмов; 5
Константинович; П2-18; Теория алгоритмов; 5
...

Студент считается сдавшим сессию, если у него сданы все предметы и нет оценки "2".
Студент считается "отличником", если у него все пятерки

Требуется сформировать множества:
- студентов, сдавших сессию
- студентов-отличников
- дисциплин, по которым нет задолженностей
Результат вывести в файл output.txt
'''

file1 = open("session.txt", "r")
file2 = open("disc.txt", "r")

list_ = file1.readlines()
session = [i.strip().split('; ') for i in list_]
list_ = file2.readlines()
disc = [i.strip() for i in list_]
file1.close()
file2.close()
names = []

for str in session:
    if str[0] not in names:
        names.append(str[0])

otli4nik = set()
sdali = set()
predmet = {*disc}

for i in range(len(names)):
    count_5 = 0
    count_2 = 0
    for j in range(len(session)):
        if(session[j][0] == names[i]):
            if(session[j][3] == '5'):
                count_5 += 1
            elif(session[j][3] == '2'):
                count_2 += 1
                predmet.discard(session[j][2])
    if(count_5 == len(disc)):
        otli4nik.add(names[i])
    if(count_2 == 0):
        sdali.add(names[i])


file3 = open("out.txt","w")
file3.write('Сдали:\n'+'\n'.join(names))
file3.write('\n-----------------------------------------------------------------------------\n')
file3.write('Отличники:\n'+'\n'.join(otli4nik))
file3.write('\n-----------------------------------------------------------------------------\n')
file3.write('Предметы по которым нет задолжности:\n'+'\n'.join(predmet))
file3.close()
