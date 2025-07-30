import logging
from typing import Union

masks_logger = logging.getLogger(__name__)
with open("../logs/masks.log", "w") as file:
    file.write("")
file_handler = logging.FileHandler("../logs/masks.log", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(funcName)s %(message)s")
file_handler.setFormatter(file_formatter)
file_handler.setLevel(logging.DEBUG)
masks_logger.addHandler(file_handler)
masks_logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: Union[int, str]) -> str:
    """Выводит маску карты из её номера"""

    FIRST_UNMASK_DIGITS_NUMBER = 6
    LAST_UNMASK_DIGITS_NUMBER = 4
    SPACE_PLACE_NUMBER = 4

    if not card_number:
        logging.error("Не задан номер карты")
        raise ValueError

    str_card_number = str(card_number)
    number_length = len(str_card_number)
    if number_length < 13:
        mask = "**" + str_card_number[-2:]
        masks_logger.debug(f"Карта с длинной номера меньше 13 символов, выведена короткая маска {mask}")
        return mask
    result = []
    for i in range(number_length):
        if not i % SPACE_PLACE_NUMBER and i:
            result.append(" ")

        if i < FIRST_UNMASK_DIGITS_NUMBER or i >= len(str_card_number) - LAST_UNMASK_DIGITS_NUMBER:
            result.append(str_card_number[i])
        else:
            result.append("*")

    mask = "".join(result)
    masks_logger.debug(f"Маска карты {mask}")
    return mask


def get_mask_account(account_number: Union[int, str]) -> str:
    """Выводит маску счета из его номера"""

    LAST_UNMASK_DIGITS_NUMBER = 4
    HIDDEN_DIGITS = 2
    MIN_DIGITS = 6

    str_account_number = str(account_number)

    if len(str_account_number) < MIN_DIGITS:
        logging.error(f"Длинна номера аккаунта меньше {MIN_DIGITS}")
        raise ValueError

    result = "*" * HIDDEN_DIGITS + str_account_number[(len(str_account_number) - LAST_UNMASK_DIGITS_NUMBER):]
    masks_logger.debug(f"Маска аккаунта {result}")
    return result


if __name__ == "__main__":
    print(get_mask_card_number(7000792289606361))
    print(get_mask_account(73654108430135874305))
