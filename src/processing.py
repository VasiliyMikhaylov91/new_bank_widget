def filter_by_state(operations: list[dict], state: str='EXECUTED') -> list[dict]:
    '''Функция выбирает из списка словарей operations только те, у которых параметр state соответствует заданому'''

    return list(filter(lambda x: x['state'] == state, operations))



def sort_by_date(operations: list[dict], reverse: bool=True):
    '''Фунция сортирует операции из спика operations'''

    return sorted(operations, key=lambda x: x['date'], reverse=reverse)


if __name__ == '__main__':
    print(filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                           {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                           {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                           {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))
    print(sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                           {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                           {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                           {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))
