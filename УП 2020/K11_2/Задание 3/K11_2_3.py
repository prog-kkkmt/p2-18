#Выполнил: Безбородов Константин
#Группа: П2-18
'''
К11_2. Техника работы со словарями

Задание 3. https://stepik.org/lesson/243394/step/13?unit=215740
Телефонная книга. Этап 3. Коле очень понравилась Ваша программа, однако он стал 
замечать, что иногда в его телефонную книгу попадают номера в некорректном формате. 
Чтобы не сохранять недействительные номера, он попросил Вас обрабатывать только номера, 
соответствующие критериям:
- номер должен начинаться либо с +7, либо с 8 и состоять из 11 цифр.
- блоки цифр могут разделяться пробелами или дефисами.
- вторая, третья и четвертая цифры могут помещаться в скобки.
Если программа встречает некорректный номер, она должна его проигнорировать. В обратном 
случае она должна привести номер к виду +7 (900) 800-70-60 и запомнить. Остальной 
функционал программы остается без изменений.

Sample Input:
Ben 89001234050, +7 050 432 10-09
Alice 404-502, 894053212-65, 439-095
Nick +1(650)781 12-51
Ben
Alex +4(908)273-22-421, 8 (908) 273-22-42
Alice
Nick
Robert 51234047129, 89174043215
Alex
Robert
.

Sample Output:
+7 (900) 123-40-50, +7 (050) 432-10-09
+7 (940) 532-12-65
Не найдено
+7 (908) 273-22-42
+7 (917) 404-32-15
'''

#Фильтрует поступающие номера
def FilterNumbers(data, str):
    index = 0    #наша позиция в строке
    #data = []    #список данных
    
    #Узнем имя
    s = ''
    while str[index] != ' ':
        s += str[index]
        index += 1
    data.append(s)    #кладем имя в список
    
    s = ''
    for i in range(index, len(str)):
        #Filter
        if str[i] == ',':
            if (s[0] == '8' and len(s) == 11):
                s2 = '+7' + s[1:]
                data.append(s2)
            elif (s[0] == '+' and s[1] == '7' and len(s) == 12):
                data.append(s)
            s = ''
        #--Filter--
        else:
            if str[i].isdigit() or str[i] == '+':
                s += str[i]
    #Filter
    if (s[0] == '8' and len(s) == 11):
        s2 = '+7' + s[1:]
        data.append(s2)
    elif (s[0] == '+' and s[1] == '7' and len(s) == 12):
        data.append(s)
        s = ''
    #--Filter--

#Выводим в правильной форме
def TrueForm(list):
    #+7 (940) 532-12-65
    len_list = len(list)
    for str in list:
        if (list[len_list-1] != str):
            print(f"{str[:2]} ({str[2:5]}) {str[5:8]}-{str[8:10]}-{str[10:12]}", end = ', ')
        else:
            print(f"{str[:2]} ({str[2:5]}) {str[5:8]}-{str[8:10]}-{str[10:12]}")
    
d = dict()
for str in iter(input, '.'):
    if ( len(str.split()) == 1):
        ret = d.get(str, 0)
        TrueForm(ret) if ret else print('Не найдено')
    else:
        data = []
        FilterNumbers(data, str)
        key = data[0]
        d[key] = d.get(key, [])
        len_data = len(data)
        for i in range(1, len_data):
            d[key].append(data[i])
