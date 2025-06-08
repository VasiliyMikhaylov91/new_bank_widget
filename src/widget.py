from masks import get_mask_card_number, get_mask_account


def mask_account_card(type_account_card_number: str) -> str:
    res_list = type_account_card_number.split()
    number = res_list[-1]

    if res_list[0] != 'Счет':
        res_list[-1] = get_mask_card_number(number)
    else:
        res_list[-1] = get_mask_account(number)

    return ' '.join(res_list)


def get_date(date_and_time: str) -> str:
    date = date_and_time.split('T')[0].split('-')
    date.reverse()
    return '.'.join(date)


if __name__ == '__main__':
    print(mask_account_card('Visa Platinum 7000792289606361'))
    print(mask_account_card('Счет 73654108430135874305'))
    print(get_date("2024-03-11T02:26:18.671407"))
