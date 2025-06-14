def filter_by_state(operations: list[dict], state: str = 'executed') -> list[dict]:
    '''Функция выбирает из списка словарей operations только те, у которых параметр state соответствует заданому'''

    return list(filter(lambda x: ('state' in x) and (x['state'].lower() == state), operations))


def sort_by_date(operations: list[dict], reverse: bool = True) -> list[dict]:
    '''Функция сортирует операции из списка operations'''

    clean_date_operations = list(i for i in operations if 'T' in i['date'] and '-' in i['date'])
    return sorted(clean_date_operations, key=lambda x: x['date'], reverse=reverse)


if __name__ == '__main__':
    print(filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                           {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                           {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                           {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))
    print(sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))
