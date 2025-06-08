from masks import get_mask_account, get_mask_card_number


def mask_account_card(type_account_card_number: str) -> str:
    """Функция принимает тип карты с номером или счет и маскирует их номера"""

    res_list = type_account_card_number.split()
    number = res_list[-1]

    if res_list[0] != "Счет":
        res_list[-1] = get_mask_card_number(number)
    else:
        res_list[-1] = get_mask_account(number)

    return " ".join(res_list)


def get_date(date_and_time: str) -> str:
    """Извлечение даты в формате "ДД.ММ.ГГГГ" из времени"""

    date = date_and_time.split("T")[0].split("-")
    date.reverse()
    return ".".join(date)


if __name__ == "__main__":
    print(mask_account_card("Maestro 1596837868705199"))
    print(mask_account_card("Счет 64686473678894779589"))
    print(mask_account_card("MasterCard 7158300734726758"))
    print(mask_account_card("Счет 35383033474447895560"))
    print(mask_account_card("Visa Classic 6831982476737658"))
    print(mask_account_card("Visa Platinum 8990922113665229"))
    print(mask_account_card("Visa Gold 5999414228426353"))
    print(mask_account_card("Счет 73654108430135874305"))
    print(get_date("2024-03-11T02:26:18.671407"))
