import json
import logging
import os

import requests
from dotenv import load_dotenv
from requests import RequestException

utils_logger = logging.getLogger(__name__)
with open("../logs/utils.log", "w") as file:
    file.write("")
file_handler = logging.FileHandler("../logs/utils.log", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(funcName)s %(message)s")
file_handler.setFormatter(file_formatter)
file_handler.setLevel(logging.DEBUG)
utils_logger.addHandler(file_handler)
utils_logger.setLevel(logging.DEBUG)


def data_from_json(path_to_file: str = "../data/operations.json") -> list[dict]:
    """
    Преобразование файла в формате *.json в список словарей
    """

    try:
        with open(path_to_file, "r") as f:
            data = json.load(f)
        utils_logger.debug("Успешное считывание файла")
    except Exception as e:
        utils_logger.error(e)
        data = None

    if not data or type(data) is not list:
        data = []
    return list(data)


def transaction_amount_rub(transaction: dict) -> float:
    """
    Из полученного словаря transaction возвращается сумма транзакции в рублях в float
    """

    api_key = None
    transaction_currency_code = transaction["operationAmount"]["currency"]["code"]
    amount = transaction["operationAmount"]["amount"]
    if transaction_currency_code == "RUB":
        utils_logger.debug("Выведена сумма без конвертации")
        return float(amount)

    load_dotenv()
    try:
        api_key = os.getenv("API_KEY")
        utils_logger.debug("Успешно получен API_KEY из .env")
    except Exception as e:
        utils_logger.error(e)
        return 0.0

    api_url = (
        f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&"
        f"from={transaction_currency_code}&"
        f"amount={amount}&"
        f"date={transaction["date"].split('T')[0]}"
    )

    headers = {"apikey": api_key}

    try:
        response_api = str(requests.request("GET", api_url, headers=headers))
        utils_logger.debug("Получен ответ API")
    except RequestException as e:
        utils_logger.error(e)
        return 0.0

    result = json.loads(response_api)["result"]

    return float(result)


if __name__ == "__main__":
    url = "https://drive.usercontent.google.com/u/0/uc?id=1C0bUdTxUhck-7BoqXSR1wIEp33BH5YXy&export=download"
    file_path = "../data/operations.json"

    response = requests.get(url)
    if response.status_code == 200:
        with open(file_path, "w", encoding="utf-8") as file:
            for line in response.text:
                file.write(line)
        print("Downloading successful")
    else:
        print("Something went wrong")
