import json
from datetime import datetime


def load_json(file):
    """Загружает список из файла json"""
    with open(file, 'r', encoding='utf-8') as f:
        return json.load(f)


def has_empty_fields(operation):
    """Проверяет поля для вывода на наличие в данных """
    has_empty = (not operation.get('state') or
                 not operation.get('date') or
                 not operation.get('description') or
                 not operation.get('from') or
                 not operation.get('to') or
                 not operation.get('operationAmount') or
                 not operation.get('operationAmount').get("amount") or
                 not operation.get('operationAmount').get("currency") or
                 not operation.get('operationAmount').get("currency").get('name')
                 )
    return has_empty


def get_invalid_operations_index(data):
    """Составляет список индексов операций с незаполненными полями или не EXECUTED"""
    operations_index_to_del = []
    for index, operation in enumerate(data):
        if has_empty_fields(operation):
            operations_index_to_del.append(index)
            continue

        if operation.get('state') != 'EXECUTED':
            operations_index_to_del.append(index)
            continue

    return operations_index_to_del


def hide_numbers(from_to_data):
    """Маскирует номера карт и счетов в строке"""
    card, number = from_to_data.rsplit(" ", maxsplit=1)

    if "Счет" in card:
        formatted_data = f'{card} **{number[-4:]}'
    else:
        formatted_data = f'{card} {number[:4]} {number[4:6]}** **** {number[-4:]}'

    return formatted_data


def get_formatted_str(operation):
    """Формирует информацию по операции в заданном формате"""
    datetime_object = datetime.strptime(operation.get('date'), '%Y-%m-%dT%H:%M:%S.%f')
    formatted_date = datetime_object.strftime('%d.%m.%Y')

    description = operation.get('description')

    from_data = operation.get('from')
    formatted_from_data = hide_numbers(from_data)

    to_data = operation.get('to')
    formatted_to_data = hide_numbers(to_data)

    money_amount = operation.get('operationAmount').get("amount")
    currency_name = operation.get('operationAmount').get("currency").get('name')

    operation_info = f"{formatted_date} {description} \n" \
                     f"{formatted_from_data} -> {formatted_to_data} \n" \
                     f"{money_amount} {currency_name} \n"

    return operation_info


def print_operations(operations):
    """Выводит на экран список операций в заданном формате"""
    for operation in operations:
        operation_info = get_formatted_str(operation)

        print(operation_info)
        print()
