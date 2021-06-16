# Слесарев А.М.

class Vehicle:

    def __init__(self, color, doors, tires):
        # __init__ это методе который применяется единожды

        self.color = color
        self.doors = doors
        self.tires = tires


def brake(self):
    # self это способ описания любого объекта, буквально

    return "Braking"


def drive(self):
    # методы объектов это функции принадлежащие объектам

    return "I'm driving!"


if __name__ == "__main__":
    car = Vehicle("blue", 5, 4, "car")
    print(car.brake())
    print(car.drive())

    truck = Vehicle("red", 3, 6, "truck")
    print(truck.drive())
    print(truck.brake())
# Создание двух классов грузового и легкового

# методы обычно для этого и предназначены – для изменения свойств конкретных объектов
