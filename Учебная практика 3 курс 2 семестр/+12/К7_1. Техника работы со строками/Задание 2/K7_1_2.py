#Выполнил: Кузнецов Матвей
#Группа: П2-18
'''
К7_1. Техника работы со строками;

Задание 2. 
https://stepik.org/lesson/201702/step/8?unit=175778
?Известно, что для логина часто не разрешается использовать строки содержащие пробелы. 
Но пользователю нашего сервиса особенно понравилась какая-то строка. 
Замените пробелы в строке на символы нижнего подчеркивания, чтобы строка 
могла сгодиться для логина. Если строка состоит из одного слова, менять ничего не нужно.
Sample Input: python sila
Sample Output: python_sila
'''

print(*[_ for _ in input().split()], sep='_')
