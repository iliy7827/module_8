'''Домашнее задание по уроку "Try и Except".'''

def add_everything_up(a, b):
    """add_everything_up(a, b) принимает a и b, которые могут быть как числами(int, float),
    так и строками(str). TypeError - когда a и b окажутся разными типами (числом и строкой),
    то возвращать строковое представление этих двух данных вместе (в том же порядке).
    Во всех остальных случаях выполнять стандартные действия."""
    try: # пишем код с возможной ошибкой
        #проверяем является ли первый объект экземпляром или подклассом второго аргумента
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return a + b
        elif isinstance(a, str) and isinstance(b, str):
            return a + b
        elif isinstance(a, str) and isinstance(b, (int, float)):
            return a + str(b)
        elif isinstance(a, (int, float)) and isinstance(b, str):
            return str(a) + b
    except TypeError: # когда a и b окажутся разными типами (числом и строкой)
        return f'{str(a)}{str(b)}' #возвращать строковое представление этих двух данных вместе


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
