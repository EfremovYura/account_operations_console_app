import json
from datetime import datetime
from operation import Operation
from pydantic import ValidationError
from config import JSON_DATE_FORMAT, PRINT_DATE_FORMAT


def load_json(filename):
    """Загружает список из файла json"""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)


def validate_data(data: list[dict]) -> list[Operation]:
    """Проверяет наличие полей операции при преобразовании"""
    operations = []
    for operation_data in data:
        try:
            operation_data['from_'] = operation_data['from']
            operation = Operation(**operation_data)
            operations.append(operation)
        except (ValidationError, KeyError):
            continue
    return operations


def remove_not_executed_operations(operations: list[Operation]) -> None:
    """Удаляет операции не EXECUTED"""
    for operation in operations:
        if operation.state != 'EXECUTED':
            operations.remove(operation)


def hide_numbers(from_to_data: str) -> str:
    """Маскирует номера карт и счетов в строке"""

    card, number = from_to_data.rsplit(" ", maxsplit=1)

    if "Счет" in card:
        formatted_data = f'{card} **{number[-4:]}'
    else:
        formatted_data = f'{card} {number[:4]} {number[4:6]}** **** {number[-4:]}'

    return formatted_data


def change_date_type(operations: list[Operation]) -> None:
    """Изменяет формат date с str на datetime"""

    for operation in operations:
        operation.date = datetime.strptime(operation.date, JSON_DATE_FORMAT)


def get_formatted_str(operation: Operation) -> str:
    """Формирует информацию по операции в заданном формате"""

    formatted_date = operation.date.strftime(PRINT_DATE_FORMAT)

    description = operation.description

    from_data = operation.from_
    formatted_from_data = hide_numbers(from_data)

    to_data = operation.to
    formatted_to_data = hide_numbers(to_data)

    money_amount = operation.operationAmount.amount
    currency_name = operation.operationAmount.currency.name

    operation_info = f"{formatted_date} {description} \n" \
                     f"{formatted_from_data} -> {formatted_to_data} \n" \
                     f"{money_amount} {currency_name} \n"

    return operation_info


def print_operations(operations: list[Operation]) -> None:
    """Выводит на экран список операций в заданном формате"""
    for operation in operations:
        operation_info = get_formatted_str(operation)

        print(operation_info)
        print()
