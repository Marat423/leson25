class Vehicle():

    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, model, color, engine_power):
        self.owner = str(owner)
        self.__model = str(model)
        self.__color = str(color)
        self.__engine_power = int(engine_power)



    def get_model(self):
        return self.__model


    def get_horsepower(self):
        return self.__engine_power


    def get_color(self):
        return  self.__color

    def set_color(self, new_color):
        new_color = new_color.lower()
        if new_color in [color.lower() for color in self.__COLOR_VARIANTS]:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')

    def print_info(self):
        print(f'Модель: {self.get_model()}')
        print(f'Мощность двигателя: {self.get_horsepower()}')
        print(f'Цвет: {self.get_color()}')
        print(f'Владелец: {self.owner}')






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