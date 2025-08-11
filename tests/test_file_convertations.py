import os
from unittest.mock import Mock, patch

import pandas as pd

from src.file_convertations import read_csv_transactions, read_xlsx_transactions


@patch("csv.DictReader")
def test_read_csv_transactions(mock_reader: Mock) -> None:
    with open("test.csv", "w") as f:
        f.write("Test file")
    mock_reader.return_value = [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
        },
    ]
    assert read_csv_transactions("test.csv") == [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
        },
    ]
    os.remove("test.csv")


def test_read_xlsx_transactions() -> None:
    test_df = pd.DataFrame(
        {
            "id": [650703, 3598919],
            "state": [
                "EXECUTED",
                "EXECUTED",
            ],
            "date": ["2023-09-05T11:30:32Z", "2020-12-06T23:00:58Z"],
            "amount": [16210, 29740],
            "currency_name": ["Sol", "Peso"],
        }
    )
    mock_read_excel = Mock(return_value=test_df)
    pd.read_excel = mock_read_excel
    with open("test.xlsx", "w") as f:
        f.write("Test file")
    assert read_xlsx_transactions("test.xlsx") == [
        {"id": 650703, "state": "EXECUTED", "date": "2023-09-05T11:30:32Z", "amount": 16210, "currency_name": "Sol"},
        {"id": 3598919, "state": "EXECUTED", "date": "2020-12-06T23:00:58Z", "amount": 29740, "currency_name": "Peso"},
    ]
    mock_read_excel.assert_called_once_with("test.xlsx")
    os.remove("test.xlsx")
