# Выполнил:Степаненко Кирилл
# Группа: П2-18
# Задание 1. Придумать собственный класс
# Задание 2. Неформально описать функционал класса
# Задание 3. Реализовать класс в модуле
# Задание 4. Разработать скрипт для демонстрации работы с классом #(импортировать
# модуль, создать экземпляры, вызвать методы)

class Machine:
    '''
    Общая характеристика машин
    '''
    # кол-во машин
    __all_types = 0
    def __init__(self, doors, wheels, atype, body):
        self.doors = doors
        self.wheels = wheels
        self.atype = atype
        self.body = body
        Machine.__all_types += 1
        # Общие сведения
    def machine_info(self):
        print('Тип: {}'.format(self.atype))
        print('Кузов: {}'.format(self.body))
        print('Кол-во дверей: {}'.format(self.doors))
        print('Кол-во: {}'.format(self.wheels))
        print()
    def what_is_this(self):
        print('Machine')
        print()
    # Экземпляр №1

machine1 = Machine(4, 4, 'w2001', 'car')
machine1.machine_info()
print(machine1._Machine__all_types)
# Экземпляр #2
machine2 = Machine(2, 3, 'w21001', 'car')
machine2.machine_info()
print(machine1._Machine__all_types)

class Motorcycle(Machine):
    '''
    Общая характеристика мотоциклов
    '''

    def __init__(self, doors, wheels, atype, body, engine, gas_tank_volume, engine_power, max_speed, acceliration,
                 fuel_consuption):
        self.doors = doors
        self.wheels = wheels
        self.atype = atype
        self.body = body
        self.engine = engine
        self.gas_tank_volume = gas_tank_volume
        self.engine_power = engine_power
        self.max_speed = max_speed
        self.acceliration = acceliration
        self.fuel_consuption = fuel_consuption
        # подробное описание

    def motorcycle_info(self):
        print('Тип: {}'.format(self.atype))
        print('Кузов: {}'.format(self.body))
        print('Кол-во дверей: {}'.format(self.doors))
        print('Кол-во: {}'.format(self.wheels))
        print('Двигатель: {}'.format(self.engine))
        print('Объем бензобака: {}'.format(self.gas_tank_volume))
        print('Мощность двигателя: {}'.format(self.engine_power))
        print('Макс. скорость: {}'.format(self.max_speed))
        print('Разгон до 100: {}'.format(self.acceliration))
        print('Расход топлива: {}'.format(self.fuel_consuption))
        print()
    def what_is_this(self):
        print('Motorcycle')
        print()
    # Экземпляр №3

motorcycle1 = Motorcycle('None', 2, 'w21002', 'motorcycle', 'v6', '20', '120 hp', '180 km/h', '3.01 s', 3.5)
motorcycle1.machine_info()
motorcycle1.motorcycle_info()

class Cars(Machine):
    '''
    Общая характеристика автомобилей
    '''
    def __init__(self, doors, wheels, atype, body, engine, gas_tank_volume, engine_power, max_speed, acceliration,
                 fuel_consuption):
        self.doors = doors
        self.wheels = wheels
        self.atype = atype
        self.body = body
        self.engine = engine
        self.gas_tank_volume = gas_tank_volume
        self.engine_power = engine_power
        self.max_speed = max_speed
        self.acceliration = acceliration
        self.fuel_consuption = fuel_consuption
        # подробное описание
    def car_info(self):
        print('Тип: {}'.format(self.atype))
        print('Кузов: {}'.format(self.body))
        print('Кол-во дверей: {}'.format(self.doors))
        print('Кол-во: {}'.format(self.wheels))
        print('Двигатель: {}'.format(self.engine))
        print('Объем бензобака: {}'.format(self.gas_tank_volume))
        print('Мощность двигателя: {}'.format(self.engine_power))
        print('Макс. скорость: {}'.format(self.max_speed))
        print('Разгон до 100: {}'.format(self.acceliration))
        print('Расход топлива: {}'.format(self.fuel_consuption))
        print()
    def what_is_this(self):
        print('car')
        print()
    # Экземпляр №4

car1 = Cars(5, 6, 'w2002', 'SUV', 'v8', '40', '160 hp', '195 km/h', '4.23 s', 4.5)
car1.machine_info()
car1.car_info()
# Нам больше не нужна харатеристика "объём бака" у car1

del car1.gas_tank_volume
# Теперь при обращение и при печати будет выдавать ошибку
# print(car1.gas_tank_volume) ошибка

# В подклассах можно изменять методы классов
machine1.what_is_this()
car1.what_is_this()
# Мы можем увидеть, что представляет собой тот или иной класс и его названия
# с помощью встроенных атрибутов класса

print('Machine documentation:', Machine.__doc__)
print('Machine name:', Machine.__name__)

