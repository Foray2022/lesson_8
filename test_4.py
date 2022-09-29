# Задание
# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов.
# В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.
# Разработайте методы, которые отвечают за приём оргтехники на склад и передачу в определённое подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру (например, словарь).
# Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

# Решение
class NumbersOnly(ValueError):
    pass


class Warehouse:
    def __init__(self):
        self.dict = {}  # для хранения данных

    def add_to(self, equipment):
        """ добавляем в словарь обьект по его названию, в значении
        будет список экземпляров этого оборудования"""
        self.dict.setdefault(equipment.group_name(), []).append(equipment)

    def extract(self, name):
        # извлекаем из значения обьект по названию группы
        if self.dict[name]:
            self.dict.setdefault(name).pop(0)


class Equipment:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.my_store_full = []
        self.my_store = []
        self.group = self.__class__.__name__
        self.my_unit = {'Device Model': self.name, 'Price per unit': self.price, 'Quantity': self.quantity}

    def group_name(self):
        return f'{self.group}'

    def __repr__(self):
        return f'{self.name} {self.price} {self.quantity}'

    def enter_date(self):
        unit = input(f'Enter the name {self.group}:')
        unit_p = int(input(f'Price per unit: '))
        try:
            unit_q = input(f'Enter the quantity:')
            if not unit_q.isdigit():
                raise NumbersOnly(unit_q)
        except NumbersOnly as ex:
            print('Not number!', ex)
        unique = {'Device Model': unit, 'Price per unit': unit_p, 'Quantity': unit_q}
        self.my_unit.update(unique)
        self.my_store.append(self.my_unit)
        print(f'Current list -\n {self.my_store}')


class Printer(Equipment):
    def __init__(self, series, name, price, quantity):
        super().__init__(name, price, quantity)
        self.series = series

    def __repr__(self):
        return f'{self.name} {self.series} {self.price} {self.quantity}'

    @staticmethod
    def action():
        return 'Prints'


class Scaner(Equipment):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)

    @staticmethod
    def action():
        return 'Scans'


class Xerox(Equipment):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)

    @staticmethod
    def action():
        return 'Copies'


# создаем объект и добавляем
sklad = Warehouse()
scaner = Scaner('hp', '321', 90)
scaner.enter_date()
sklad.add_to(scaner)
printer = Printer('e-320', 'sony', 126, 2018)
printer.enter_date()
sklad.add_to(printer)
xerox = Xerox('lg', 1230, 50)
xerox.enter_date()
# выводим склад
print(sklad.dict)
# забираем с склада и выводим склад
name_tip = input(f'Enter the name of the product to be removed from the warehouse:')
sklad.extract(name_tip)
print()
print(sklad.dict)
