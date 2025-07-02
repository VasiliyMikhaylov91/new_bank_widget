from functools import wraps
from typing import Any


def log(filename:str = '') -> Any:
    '''
    Декоратор указывает имя выполненной функции и результат выполнения
    В случае выполнения функции с ошибкой указывается текст ошибки и входные параметры функции
    При указании параметра filename записи будут вестись в указанный файл.
    '''

    def wrapper(function: Any) -> Any:
        @wraps(function)
        def inner(*args: Any, **kwargs: Any) -> Any:
            result = f'{function.__name__} '
            try:
                function(*args, **kwargs)
                result += 'ok\n'
            except Exception as e:
                result += f'error: {e}. Inputs:{args}, {kwargs}\n'
            if filename:
                with open(filename, 'a') as file:
                    file.write(result)
            else:
                print(result)
        return inner
    return wrapper
