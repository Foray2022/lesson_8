# Задание
# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки
# формата «день-месяц-год». В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип
# к типу «Число». Второй, с декоратором @staticmethod,
# должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

# Решение

class Date(object):
    def __init__(self, day=10, month=10, year=2000):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, string_date):
        try:
            day, month, year = map(int, string_date.split('-'))
            my_date = cls(day, month, year)
            return my_date
        except ValueError:
            return 'the date is incorrect'

    @staticmethod
    def valid_date(date_string):
        try:
            day, month, year = map(int, date_string.split('-'))
            return day <= 31 and month <= 12 and year <= 3000
        except ValueError:
            return 'the date is incorrect'


dateObj = Date.from_string('26-09-2022')
valid_date = Date.valid_date('26-09-2022')
print(valid_date)
