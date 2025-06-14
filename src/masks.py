from typing import Union


def get_mask_card_number(card_number: Union[int, str]) -> str:
    """Выводит маску карты из её номера"""

    FIRST_UNMASK_DIGITS_NUMBER = 6
    LAST_UNMASK_DIGITS_NUMBER = 4
    SPACE_PLACE_NUMBER = 4

    if not card_number:
        raise ValueError

    str_card_number = str(card_number)
    number_length = len(str_card_number)
    if number_length < 13:
        return '**' + str_card_number[-2:]
    result = []
    for i in range(number_length):
        if not i % SPACE_PLACE_NUMBER and i:
            result.append(" ")

        if i < FIRST_UNMASK_DIGITS_NUMBER or i >= len(str_card_number) - LAST_UNMASK_DIGITS_NUMBER:
            result.append(str_card_number[i])
        else:
            result.append("*")

    return "".join(result)


def get_mask_account(account_number: Union[int, str]) -> str:
    """Выводит маску счета из его номера"""

    LAST_UNMASK_DIGITS_NUMBER = 4
    HIDDEN_DIGITS = 2
    MIN_DIGITS = 6

    str_account_number = str(account_number)

    if len(str_account_number) < MIN_DIGITS:
        raise ValueError

    result = "*" * HIDDEN_DIGITS + str_account_number[(len(str_account_number) - LAST_UNMASK_DIGITS_NUMBER):]
    return result


if __name__ == "__main__":
    print(get_mask_card_number(7000792289606361))
    print(get_mask_account(73654108430135874305))
