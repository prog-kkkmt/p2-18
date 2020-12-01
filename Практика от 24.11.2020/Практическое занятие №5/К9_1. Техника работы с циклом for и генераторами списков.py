#Выполнил: Короленко Иван Романович
#Студент: ККМТ П2-18

'''
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
'''
dict = {}

file = open('text.txt')
onstring = file.read().split("\n")[:-1]

for item in onstring:
    key = item.split(" ")[0]
    value = item.split(" ")[1:]
    dict[key] = value
    print(dict)
file.close()
 
while True:
    fio = input('Введите ФИО студента, который нужно изменить: ')
    student_num = None
    for student in students:
        if students[student][0] == fio:
            student_num = student
 
    if student_num is not None:
        new_fio = input('Введите новые ФИО: ')
        students[student_num][0] = new_fio
        student_num = None
    else:
        print('Студент с ФИО "{}" не найден'.format(fio))
 
    number = input('Введите номер группы, который нужно изменить:')
    student_num = None
    for student in students:
        if students[student][2] == number:
            student_num = student
 
    if student_num is not None:
        new_number = input('Введите номер группы:')
        students[student_num][2] = new_number
        student_num = None
    else:
        print('Такой номер группы "{}" не найден'.format(number))
 
    print(students)



