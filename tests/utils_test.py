from datetime import datetime
import pytest

from utils import load_json, hide_numbers, get_formatted_str, validate_data, remove_not_executed_operations, \
    change_date_type

from config import JSON_FILE, JSON_DATE_FORMAT


def test_load_json():
    assert isinstance(load_json(JSON_FILE), list)


def test_validate_data(good_operations_data, bad_operations_data):
    assert len(validate_data(good_operations_data)) == len(good_operations_data)
    assert len(validate_data(bad_operations_data)) == 0


def test_remove_not_executed_operations(canceled_operation_data, good_card_to_card_operation_data):
    validated_data = validate_data([canceled_operation_data, good_card_to_card_operation_data])
    assert len(validated_data) == 2

    remove_not_executed_operations(validated_data)

    assert len(validated_data) == 1


def test_change_date_type(good_card_to_bill_operation):
    assert isinstance(good_card_to_bill_operation.date, str)

    change_date_type([good_card_to_bill_operation])

    assert isinstance(good_card_to_bill_operation.date, datetime)


hide_from_to_data = [
    ("Счет 48894435694657014368", "Счет **4368"),
    ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
    ("МИР 8201420097886664", "МИР 8201 42** **** 6664")
]


@pytest.mark.parametrize('plain_data, formatted_data', hide_from_to_data)
def test_hide_numbers(plain_data, formatted_data):
    assert hide_numbers(plain_data) == formatted_data


def test_get_formatted_str(good_card_to_bill_operation, good_card_to_bill_operation_formatted_str):
    good_card_to_bill_operation.date = datetime.strptime(good_card_to_bill_operation.date, JSON_DATE_FORMAT)

    assert get_formatted_str(good_card_to_bill_operation) == good_card_to_bill_operation_formatted_str
