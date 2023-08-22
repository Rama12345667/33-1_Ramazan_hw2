class Transport:
    def __init__(self, the_model, the_year, the_color):
        self.model = the_model
        self.year = the_year
        self.color = the_color

    def change_color(self, new_color):
        self.color = new_color


class Plane(Transport):
    def __init__(self, the_model, the_year, the_color):
        super().__init__(the_model, the_year, the_color)


# Класс / шаблон / сложный тип данный
class Car(Transport):
    # Классовые атрибуты
    counter = 0
    number_of_wheels_by_standart = 4

    # Конструктор
    def __init__(self, the_model, the_year, the_color, penalties=0):
        super().__init__(the_model, the_year, the_color)
        # Атрибуты / поля
        self.penalties = penalties
        Car.counter += 1

    # Методы
    def drive(self, city):
        print(f'Car {self.model} is driving to {city}')

    def change_color(self, new_color):
        self.color = new_color


class Truck(Car):
    number_of_wheels_by_standart = 12
    def __init__(self, the_model, the_year, the_color,
                 penalties=0, load_capacity=0):
        super().__init__(the_model, the_year, the_color, penalties)
        self.load_capacity = load_capacity

    def load_cargo(self, type, weight):
        if weight > self.load_capacity:
            print(f'You can not load more than {self.load_capacity} kg.')
        else:
            print(f'Cargo of {type} ({weight} kg.) '
                  f'was successfully loaded on {self.model}')


print(f'Cars fabric produced: {Car.counter}')
bmw_car = Car('BMW X7', 2020, 'Black')
print(bmw_car)
print(f'MODEL: {bmw_car.model} YEAR: {bmw_car.year} COLOR: {bmw_car.color} '
      f'PENALTIES: {bmw_car.penalties}')
# bmw_car.color = 'Red'
bmw_car.change_color('Red')
print(f'MODEL: {bmw_car.model} YEAR: {bmw_car.year} '
      f'NEW COLOR: {bmw_car.color} PENALTIES: {bmw_car.penalties}')

honda_car = Car('Honda CR-V', 2009,
                'White', 900)
print(f'MODEL: {honda_car.model} YEAR: {honda_car.year} COLOR: {honda_car.color} '
      f'PENALTIES: {honda_car.penalties}')

honda_car.drive('Osh')
bmw_car.drive('Tokmok')

print(f'Cars fabric produced: {Car.counter}')
price_of_one_winter_lastic = 5000
print(f'We need '
      f'{Car.number_of_wheels_by_standart * Car.counter * price_of_one_winter_lastic} '
      f'soms to buy winter lastics.')

boeing_plane = Plane('Boeing 747', 2023, 'Blue')
print(f'MODEL: {boeing_plane.model} YEAR: {boeing_plane.year} '
      f'COLOR: {boeing_plane.color}')

mersedes_truck = Truck('Mersedes GT 45', 2021,
                       'Red', 800, 30000)
print(f'MODEL: {mersedes_truck.model} YEAR: {mersedes_truck.year} '
      f'COLOR: {mersedes_truck.color} PENALTIES: {mersedes_truck.penalties} '
      f'LOAD CAPACITY: {mersedes_truck.load_capacity} kg.')
mersedes_truck.load_cargo('apples', 35000)
mersedes_truck.load_cargo('potatoes', 25000)
mersedes_truck.drive('Kant')

print(f'Standart quantity of wheel on truck: {Truck.number_of_wheels_by_standart}')