import json

import requests


def data_from_json(path_to_file: str = '../data/operations.json') -> list[dict]:
    """
    Преобразование файла в формате *.json в список словарей
    """
    try:
        with open(path_to_file) as f:
            data = json.load(f)
    except Exception:
        data = None
    if not data or type(data) != list:
        data = []
    return data


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
