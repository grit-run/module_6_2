class Vehicle:
    _COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, model, engine_power, color):
        self.owner = owner
        self.model = model
        self._engine_power = engine_power
        self._color = color

    def get_model(self):
        return "Модель: {}".format(self.model)

    def get_engine_power(self):
        return "Мощность двигателя: {}".format(self._engine_power)

    def get_color(self):
        return "Цвет: {}".format(self._color)

    def print_info(self):
        print(self.get_model())
        print(self.get_engine_power())
        print(self.get_color())
        print("Владелец: {}".format(self.owner))

    def set_color(self, new_color):
        if str(new_color).lower() in self._COLOR_VARIANTS:
            self._color = new_color
        else:
            print("Нельзя сменить цвет на {}".format(new_color))


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
