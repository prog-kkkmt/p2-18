#https://pythontutor.ru/lessons/lists/problems/even_elements/
#Выполнил задание Яковлев Прокопий Максимович
#Выведите все четные элементы списка.
#При этом используйте цикл for, перебирающий элементы списка, а не их индексы!
for num in input().split(' '):
    if int(num) % 2 == 0:
        print(int(num), end=' ')
