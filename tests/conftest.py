import pytest


@pytest.fixture()
def good_card_to_bill_operation():
    return {'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041',
            'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}},
            'description': 'Перевод организации', 'from': 'Maestro 1596837868705199', 'to': 'Счет 64686473678894779589'}


@pytest.fixture()
def good_card_to_bill_operation_formatted_str():
    return f"26.08.2019 Перевод организации \n" \
           f"Maestro 1596 83** **** 5199 -> Счет **9589 \n" \
           f"31957.58 руб. \n"


@pytest.fixture()
def good_bill_to_card_operation():
    return {'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041',
            'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}},
            'description': 'Перевод со счета на карту', 'from': 'Счет 64686473678894779589',
            'to': 'Maestro 1596837868705199'}


@pytest.fixture()
def good_bill_to_bill_operation():
    return {'id': 142264268, 'state': 'EXECUTED', 'date': '2019-04-04T23:20:05.206878',
            'operationAmount': {'amount': '79114.93', 'currency': {'name': 'USD', 'code': 'USD'}},
            'description': 'Перевод со счета на счет', 'from': 'Счет 19708645243227258542',
            'to': 'Счет 75651667383060284188'}


@pytest.fixture()
def good_card_to_card_operation():
    return {'id': 895315941, 'state': 'EXECUTED', 'date': '2018-08-19T04:27:37.904916',
            'operationAmount': {'amount': '56883.54', 'currency': {'name': 'USD', 'code': 'USD'}},
            'description': 'Перевод с карты на карту', 'from': 'Visa Classic 6831982476737658',
            'to': 'Visa Platinum 8990922113665229'}


@pytest.fixture()
def canceled_operation():
    return {'id': 441945886, 'state': 'CANCELED', 'date': '2019-08-26T10:50:58.294041',
            'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}},
            'description': 'Перевод организации', 'from': 'Maestro 1596837868705199', 'to': 'Счет 64686473678894779589'}


@pytest.fixture()
def bad_empty_operation():
    return {}


@pytest.fixture()
def bad_without_from_operation():
    return {'id': 587085106, 'state': 'EXECUTED', 'date': '2018-03-23T10:45:06.972075',
            'operationAmount': {'amount': '48223.05', 'currency': {'name': 'руб.', 'code': 'RUB'}},
            'description': 'Открытие вклада', 'to': 'Счет 41421565395219882431'}


@pytest.fixture()
def bad_without_to_operation():
    return {'id': 142264268, 'state': 'EXECUTED', 'date': '2019-04-04T23:20:05.206878',
            'operationAmount': {'amount': '79114.93', 'currency': {'name': 'USD', 'code': 'USD'}},
            'description': 'Перевод со счета на счет', 'from': 'Счет 19708645243227258542'}


@pytest.fixture()
def bad_without_date_operation():
    return {'id': 895315941, 'state': 'EXECUTED',
            'operationAmount': {'amount': '56883.54', 'currency': {'name': 'USD', 'code': 'USD'}},
            'description': 'Перевод с карты на карту', 'from': 'Visa Classic 6831982476737658',
            'to': 'Visa Platinum 8990922113665229'}


@pytest.fixture()
def bad_without_amount_operation():
    return {'id': 895315941, 'state': 'EXECUTED', 'date': '2018-08-19T04:27:37.904916',
            'operationAmount': {'currency': {'name': 'USD', 'code': 'USD'}},
            'description': 'Перевод с карты на карту', 'from': 'Visa Classic 6831982476737658',
            'to': 'Visa Platinum 8990922113665229'}


@pytest.fixture()
def bad_without_currency_name_operation():
    return {'id': 895315941, 'state': 'EXECUTED', 'date': '2018-08-19T04:27:37.904916',
            'operationAmount': {'amount': '56883.54', 'currency': {'code': 'USD'}},
            'description': 'Перевод с карты на карту', 'from': 'Visa Classic 6831982476737658',
            'to': 'Visa Platinum 8990922113665229'}


@pytest.fixture()
def bad_without_description_operation():
    return {'id': 895315941, 'state': 'EXECUTED', 'date': '2018-08-19T04:27:37.904916',
            'operationAmount': {'amount': '56883.54', 'currency': {'name': 'USD', 'code': 'USD'}},
            'from': 'Visa Classic 6831982476737658', 'to': 'Visa Platinum 8990922113665229'}


@pytest.fixture()
def good_operations(good_card_to_bill_operation, good_bill_to_card_operation, good_bill_to_bill_operation,
                    good_card_to_card_operation):
    return [good_card_to_bill_operation, good_bill_to_card_operation, good_bill_to_bill_operation,
            good_card_to_card_operation]


@pytest.fixture()
def bad_operations(bad_empty_operation, bad_without_from_operation, bad_without_to_operation,
                   bad_without_description_operation, bad_without_currency_name_operation, bad_without_amount_operation,
                   bad_without_date_operation):
    return [bad_empty_operation, bad_without_from_operation, bad_without_to_operation,
            bad_without_description_operation, bad_without_currency_name_operation, bad_without_amount_operation,
            bad_without_date_operation]
