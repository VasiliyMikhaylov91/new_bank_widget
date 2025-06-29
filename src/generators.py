from typing import Generator, Union


def filter_by_currency(transactions_list: list[dict], currency: str) -> Generator[Union[dict, None]]:
    """Функция отсеивает все транзакции из списка transactions_list кроме тех operationAmount[code] == currency"""

    filter_transactions = list(
        filter(lambda x: x["operationAmount"]["currency"]["code"] == currency, transactions_list)
    )
    if not filter_transactions:
        yield None
    else:
        for transaction in filter_transactions:
            yield transaction


def transaction_descriptions(transactions_list: list[dict]) -> Generator[Union[str, None]]:
    """Генератор описания транзакций из списка transactions_list"""

    if not transactions_list:
        yield None
    else:
        for transaction in transactions_list:
            yield transaction["description"]


def card_number_generator(start_number: int, end_number: int) -> Generator[str]:
    """Генератор номеров карт от start_number до end_number включительно"""

    MAX_LENGTH_CARD_NUMBER = 16

    for i in range(start_number, end_number + 1):
        i_str = str(i)
        while len(i_str) < MAX_LENGTH_CARD_NUMBER:
            i_str = "0" + i_str
        yield i_str[:4] + " " + i_str[4:8] + " " + i_str[8:12] + " " + i_str[12:]
