import pytest


@pytest.fixture
def card_numbers() -> list[tuple]:
    """Фикстура для теста функции get_mask_card_number"""

    return [
        (7000792289606361, "7000 79** **** 6361"),
        ("92289", "**89"),
        ("7000792289606361653", "7000 79** **** ***1 653"),
        (None, None),
    ]


@pytest.fixture
def account_numbers() -> list[tuple]:
    """Фикстура для теста функции get_mask_account"""

    return [
        (73654108430135874305, "**4305"),
        ("73654108430135874305654221", "**4221"),
        ("736541084301358", "**1358"),
        (7365, None),
    ]
