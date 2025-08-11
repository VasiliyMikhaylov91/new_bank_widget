import csv, requests

import pandas as pd


def read_csv_transactions(file_csv_path: str) -> list[dict]:
    """Преобразование указанного *.csv файла в список словарей"""

    with open(file_csv_path, encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=';')
    result = [row for row in reader]
    return result

def read_xlsx_transactions(file_xlsx_path: str) -> list[dict]:
    """Преобразование указанного *.xlsx файла в список словарей"""

    df = pd.read_excel(file_xlsx_path)
    return [dict(df.iloc[i]) for i in range(df.shape[0])]


if __name__ == '__main__':
    # url = "https://github.com/skypro-008/transactions/raw/refs/heads/main/transactions.csv"
    # file_path = "../data/transactions.csv"
    #
    # response = requests.get(url)
    # if response.status_code == 200:
    #     with open(file_path, "w", encoding="utf-8") as file:
    #         for line in response.text:
    #             file.write(line)
    #     print("Downloading successful")
    # else:
    #     print("Something went wrong")
    #
    # url = "https://github.com/skypro-008/transactions/raw/refs/heads/main/transactions_excel.xlsx"
    # file_path = "../data/transactions_excel.xlsx"
    #
    # response = requests.get(url)
    # if response.status_code == 200:
    #     with open(file_path, "w", encoding="utf-8") as file:
    #         for line in response.text:
    #             file.write(line)
    #     print("Downloading successful")
    # else:
    #     print("Something went wrong")
    print(read_csv_transactions('../data/transactions.csv'))