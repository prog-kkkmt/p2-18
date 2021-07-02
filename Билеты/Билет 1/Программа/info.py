from bd import *

class main:
    def fun():
        # Вызов нужных таблиц
        *bus, = curs.execute('SELECT Код_станции FROM Рейсы')
        *bus2, = curs.execute('SELECT Вместимость FROM Автобусы')
        return bus, bus2

bus, bus2 = main.fun()

# Переменная для записи количества пассажиров
kolvo = 0

# Цикл для записи из таблицы общего числа пассажиров 
for i in bus2:
    kolvo += int(*i,)

# Вывод рейсов и количества пассажиров 
print('= Рейсов до станции =',
      '\nФрязино -', bus.count((1,)),
      '\nИвантеевка -', bus.count((2,)),
      '\nЗеленый Бор -', bus.count((3,)),
      '\nПодлипки дачные -', bus.count((4,)),
      '\nМытищи -', bus.count((5,)),
      '\nМосква -', bus.count((6,)),
      '\n======================',
      '\nОбщее количество пассажиров -', kolvo)


