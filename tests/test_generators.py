import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(transactions: list[dict]) -> None:
    usd_filter = filter_by_currency(transactions, "USD")
    for _ in range(2):
        transaction = next(usd_filter)
        assert transaction["operationAmount"]["currency"]["code"] == "USD"
    rub_filter = filter_by_currency(transactions, "RUB")
    for _ in range(2):
        transaction = next(rub_filter)
        assert transaction["operationAmount"]["currency"]["code"] == "RUB"
    chf_filter = filter_by_currency(transactions, "CHF")
    assert not next(chf_filter)


def test_transaction_descriptions(transactions: list[dict], trans_descriptions: list[str]) -> None:
    description_from_transaction = transaction_descriptions(transactions)
    for description in trans_descriptions:
        assert next(description_from_transaction) == description
    description_from_transaction = transaction_descriptions([])
    assert not next(description_from_transaction)


@pytest.mark.parametrize(
    "start_number, end_number, result",
    [
        (
            9999,
            10010,
            [
                "0000 0000 0000 9999",
                "0000 0000 0001 0000",
                "0000 0000 0001 0001",
                "0000 0000 0001 0002",
                "0000 0000 0001 0003",
                "0000 0000 0001 0004",
                "0000 0000 0001 0005",
                "0000 0000 0001 0006",
                "0000 0000 0001 0007",
                "0000 0000 0001 0008",
                "0000 0000 0001 0009",
                "0000 0000 0001 0010",
            ],
        ),
        (0, 0, ["0000 0000 0000 0000"]),
        (9999999999999999, 9999999999999999, ["9999 9999 9999 9999"]),
    ],
)
def test_card_number_generator(start_number: int, end_number: int, result: list[str]) -> None:
    number = card_number_generator(start_number, end_number)
    for i in range(start_number, end_number + 1):
        assert result[i - start_number] == next(number)
