from typing import Callable, Any
from unittest.mock import Mock, patch

import pytest
import requests

from src.utils import data_from_json, transaction_amount_rub


@patch('builtins.open', create=True)
def test_data_from_json(mock_open):
    mock_file = mock_open.return_value.__enter__.return_value
    mock_file.read.return_value = '''[
  {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  },
  {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    }
  }]'''
    assert data_from_json() == [
  {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  },
  {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    }
  }]
    mock_open.assert_called_once_with('../data/operations.json', 'r')

@pytest.mark.parametrize(
  'transaction, response, result',
  [(
   {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    }
   }, '''
  {
    "date": "2019-07-03",
    "historical": true,
    "info": {
      "rate": 63.315897,
      "timestamp": 1562198399
    },
    "query": {
      "amount": 8221.37,
      "from": "USD",
      "to": "RUB"
    },
    "result": 520543.416119,
    "success": true
  }
 ''', 520543.416119
  )]
)
def test_transaction_amount_rub(transaction: dict, response:str, result: float) -> None:
  mock_request = Mock(return_value=response)
  requests.request = mock_request
  assert transaction_amount_rub(transaction) == result
