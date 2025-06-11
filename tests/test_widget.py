import pytest

from src.widget import mask_account_card, get_date


@pytest.mark.parametrize('type_account_card_number, result',
                         [('Maestro 1596837868705199', 'Maestro 1596 83** **** 5199'),
                          ('Счет 64686473678894779589', 'Счет **9589'),
                          ('wfegsg', None)])
def test_mask_account_card(type_account_card_number, result):
    assert mask_account_card(type_account_card_number) == result


@pytest.mark.parametrize('date_time, date',
                         [('2024-03-11T02:26:18.671407', '11.03.2024'),
                          ('Нет даты', 'Введите дату и время в формате 2024-03-11T02:26:18.671407'),
                          ('2024.03.11T02:26:18.671407', 'Введите дату и время в формате 2024-03-11T02:26:18.671407'),
                          ('2024.03.11 02:26:18.671407', 'Введите дату и время в формате 2024-03-11T02:26:18.671407')])
def test_get_date(date_time, date):
    assert get_date(date_time) == date
