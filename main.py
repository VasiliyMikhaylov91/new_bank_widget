from typing import Union
import logging, os
from src import (data_from_json, read_csv_transactions, read_xlsx_transactions, filter_by_state,
                 sort_by_date, process_bank_search, mask_account_card)


main_logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("./logs/main.log", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(funcName)s %(message)s")
file_handler.setFormatter(file_formatter)
file_handler.setLevel(logging.DEBUG)
main_logger.addHandler(file_handler)
main_logger.setLevel(logging.DEBUG)

settings_data = [
    {"question": "Отсортировать операции по дате? Да/Нет", "answers": ["да", "нет"]},
    {"question": "Отсортировать по возрастанию или по убыванию?", "answers": ["по убыванию", "по возрастанию"]},
    {"question": "Выводить только рублевые транзакции? Да/Нет", "answers":  ["да", "нет"]},
    {"question": "Отфильтровать список транзакций по определенному слову в описании?", "answers":  ["да", "нет"]},
]


def print_transaction(transaction: dict, json_transaction: bool = False) -> None:
    print(transaction["date"].split("T")[0], " ", transaction["description"])
    from_to_row = f"{mask_account_card(transaction["from"])} -> {mask_account_card(transaction["to"])}" \
        if "from" in transaction and transaction["from"] \
        else f"{mask_account_card(transaction["to"])}"
    print(from_to_row)
    amount_row = "Сумма: " + (f"{transaction["operationAmount"]["amount"]} "
                              f"{transaction["operationAmount"]["currency"]["name"]}" if json_transaction else
                              f"{transaction["amount"]} {transaction["currency_name"]}")
    print(amount_row)


def get_answer(question: str, answer_variants: list[str]) -> bool:
    is_answer = False
    result = False
    while not is_answer:
        print(question)
        answer = input(">> ").lower()
        if answer == answer_variants[0] or answer == answer_variants[1]:
            is_answer =True
            if answer == answer_variants[0]:
                result = True
        else:
            print("Неверный ввод")
            main_logger.info(f'Отвечая на вопрос "{question}" пользователь ввел "{answer}"')
    return result


def state_filter(data_for_filter: list[dict]) -> list[dict]:
    answer_variants = ["executed", "canceled", "pending"]
    is_answer = False
    answer = ""
    while not is_answer:
        print("""
        Программа: Введите статус, по которому необходимо выполнить фильтрацию. 
        Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
        """)
        answer = input(">> ").lower()
        if not answer in answer_variants:
            print(f"Статус операции '{answer}' недоступен.")
            main_logger.info(f"Пользователь запросил операции со статусом {answer}")
        else:
            is_answer = True
    return filter_by_state(data_for_filter, answer)


def data_choice() -> (Union[list[dict], None], bool):
    cur_path = os.getcwd()

    print("""
        Привет! Добро пожаловать в программу работы 
        с банковскими транзакциями. 
        Выберите необходимый пункт меню:
        1. Получить информацию о транзакциях из JSON-файла
        2. Получить информацию о транзакциях из CSV-файла
        3. Получить информацию о транзакциях из XLSX-файла
    """)

    file_is_chosen = False
    msg = ""
    while not  file_is_chosen:
        try:
            file_select = int(input(">>> "))
            if file_select == 1:
                msg = "Для обработки выбран JSON-файл."
                path = os.path.join(cur_path, "data", "operations.json")
                cur_data = data_from_json(path)
                cur_data = filter(lambda x: "date" in x, cur_data)
                cur_data = filter(lambda x: "description" in x, cur_data)
                cur_data = filter(lambda x: "to" in x, cur_data)
                cur_data = filter(lambda x: "operationAmount" in x, cur_data)
                return cur_data, True
            elif file_select == 2:
                path = os.path.join(cur_path, "data", "transactions.csv")
                msg = "Для обработки выбран CSV-файл."
                return read_csv_transactions(path), False
            elif file_select == 3:
                path = os.path.join(cur_path, "data", "transactions_excel.xlsx")
                msg ="Для обработки выбран XLSX-файл."
                return read_xlsx_transactions(path), False
            else:
                raise ValueError
        except ValueError as e:
            print('Неверный ввод')
            main_logger.error(e)
        finally:
            if msg:
                file_is_chosen = True
                main_logger.info(msg)
                print(msg)
            print()
    return None


if __name__ == '__main__':
    data, data_json = data_choice()
    data = state_filter(data)
    if get_answer(settings_data[0]["question"], settings_data[0]["answers"]):
        print()
        data = sort_by_date(data, get_answer(settings_data[1]["question"], settings_data[1]["answers"]))
    print()
    if get_answer(settings_data[2]["question"], settings_data[2]["answers"]):
        if data_json:
            data = filter(lambda x: x["operationAmount"]["currency"]["code"] == "RUB", data)
        else:
            data = filter(lambda x: x["currency_code"] == "RUB", data)
    print()
    if get_answer(settings_data[3]["question"], settings_data[3]["answers"]):
        print()
        word = input("Введите слово для фильтрации >> ")
        data = process_bank_search(data, word)
    print()
    print("Распечатываю итоговый список транзакций...")
    print()
    if data:
        for item in data:
            print_transaction(item, data_json)
            print()
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
