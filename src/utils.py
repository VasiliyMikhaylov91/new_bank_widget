import json, os

from dotenv import load_dotenv
import requests

from src.decorators import log


@log()
def data_from_json(path_to_file: str = '../data/operations.json') -> list[dict]:
    """
    Преобразование файла в формате *.json в список словарей
    """

    with open(path_to_file, 'r') as f:
        data = json.load(f)

    return data


@log()
def transaction_amount_rub(transaction: dict) -> float:
    """
    Из полученного словаря transaction возвращается сумма транзакции в рублях в float
    """

    transaction_currency_code = transaction["operationAmount"]["currency"]["code"]
    amount = transaction["operationAmount"]["amount"]
    if transaction_currency_code == "RUB":
        return amount

    load_dotenv()
    api_key = os.getenv('API_KEY')
    api_url = (f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&"
           f"from={transaction_currency_code}&"
           f"amount={amount}&"
           f"date={transaction["date"].split('T')[0]}")

    payload = {}
    headers = {
        "apikey": api_key
    }

    response_api = requests.request("GET", api_url, headers=headers, data=payload)
    result = json.loads(response_api)["result"]

    return float(result)


if __name__ == '__main__':
    url = 'https://drive.usercontent.google.com/u/0/uc?id=1C0bUdTxUhck-7BoqXSR1wIEp33BH5YXy&export=download'
    file_path = '../data/operations.json'

    response = requests.get(url)
    if response.status_code == 200:
        with open(file_path, 'w', encoding='utf-8') as file:
            for line in response.text:
                file.write(line)
        print('Downloading successful')
    else:
        print('Something went wrong')
