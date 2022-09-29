# Задание
# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию
# и не завершиться с ошибкой.

# Решение
class MyError(Exception):
    def __init__(self, str_text):
        self.str_text = str_text


def dividing_numbers():
    try:
        num_1 = int(input('enter the divisible:'))
        num_2 = int(input('enter the divisor:'))
        if num_2 == 0:
            raise MyError("You can't divide by zero")
        else:
            number = num_1 / num_2
            return number
    except ValueError:
        return "It's not a number"
    except MyError as err:
        return err


print(dividing_numbers())
