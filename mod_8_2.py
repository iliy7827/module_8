def personal_sum(numbers):
    ''' функция возвращает кортеж из двух значений:
    result - сумма чисел,
    incorrect_data - кол-во некорректных данных'''
    result = 0 # задаем переменные - это будет сумма чисел
    incorrect_data = 0 # кол-во некорректных данных
    for i in numbers:
        try:
            result += i
        except TypeError:  #если i не число
            incorrect_data += 1
    return result, incorrect_data

def calculate_average(numbers):
    '''принимает коллекцию numbers и возвращает:
     среднее арифметическое всех чисел.'''
    try:
        count = 0 # кол-во чисел
        for i in numbers:
            if isinstance(i, (int, float)): # если i - число
                count += 1
            else:
                print(f'Некорректный тип данных подсчета суммы - {i}')
        try:
            sum_number = personal_sum(numbers)[0]
            return sum_number / count #среднее арифметическое всех чисел
        except ZeroDivisionError:
            return 0
    except TypeError:
        print('В numbers записан не корректный тип данных')


print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать