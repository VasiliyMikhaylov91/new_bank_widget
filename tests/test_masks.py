import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number(card_numbers):

    for i in card_numbers:
        if not i[0]:
            with pytest.raises(ValueError) as exc_info:
                get_mask_card_number(i[0])
        else:
            assert get_mask_card_number(i[0]) == i[1]


def test_get_mask_account(account_numbers):
    for i in account_numbers:
        if len(str(i[0])) < 6:
            with pytest.raises(ValueError) as exc_info:
                get_mask_account(i[0])
        else:
            assert get_mask_account(i[0]) == i[1]
