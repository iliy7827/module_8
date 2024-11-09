'''Задача "Некорректность":
Создайте 3 класса (2 из которых будут исключениями):
-- Классы исключений IncorrectVinNumber и IncorrectCarNumbers,
 объекты которых обладают атрибутом message - сообщение,
 которое будет выводиться при выбрасывании исключения.'''

class IncorrectVinNumber (Exception): #Класс исключение
    def __init__(self, message):
        self.message = message

class IncorrectCarNumbers(Exception): #Класс исключение
    def __init__(self, message):
        self.message = message

class Car:
    def __init__(self, model: str,__vin: int, __nambers: str):
        self.model = model      #название автомобиля (строка).
        self.__vin = __vin      #vin номер автомобиля (целое число). Уровень доступа private.
        self.__nambers = __nambers  #номера автомобиля (строка)
        self.__is_valid_vin(self.__vin) #метод принимает vin_number и проверяет его на корректность.
                                        #Возвращает True, если корректный, в других случаях выбрасывает исключение.
        self.__is_valid_numbers(self.__nambers) #метод принимает numbers и проверяет его на корректность,
                                        #Возвращает True, если корректный, в других случаях выбрасывает исключение


    def __is_valid_vin(self, vin_number):
        '''принимает vin_number и проверяет его на корректность.
        Возвращает True, если корректный, в других случаях выбрасывает исключение.
         Уровень доступа private.'''
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        if not (1000000 <= vin_number <= 9999999):
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        return True

    def __is_valid_numbers(self, numbers):
        '''-Выбрасывает исключение IncorrectCarNumbers с сообщением 'Некорректный тип данных для номеров',
если передана не строка. (тип данных можно проверить функцией isinstance).
-Выбрасывает исключение IncorrectCarNumbers с сообщением 'Неверная длина номера',
переданная строка должна состоять ровно из 6 символов.
Возвращает True, если исключения не были выброшены.'''
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers ('Некорректный тип данных для номеров')
        elif not (len(numbers) == 6):
            raise IncorrectCarNumbers ('Неверная длина номера')
        return True

try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')