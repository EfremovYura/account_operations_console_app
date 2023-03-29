import pytest


from utils import load_json, has_empty_fields, get_invalid_operations_index, hide_numbers, get_formatted_str

from config import JSON_FILE


def test_load_json():
    assert isinstance(load_json(JSON_FILE), list)


def test_has_empty_fields(good_operations, bad_operations):
    for operation in good_operations:
        assert has_empty_fields(operation) is False

    for operation in bad_operations:
        assert has_empty_fields(operation) is True


def test_get_invalid_operations_index(good_operations, bad_operations, canceled_operation):
    assert get_invalid_operations_index(bad_operations) == list(range(len(bad_operations)))
    assert get_invalid_operations_index([canceled_operation]) == [0]
    assert get_invalid_operations_index(good_operations) == []


hide_from_to_data = [
    ("Счет 48894435694657014368", "Счет **4368"),
    ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
    ("МИР 8201420097886664", "МИР 8201 42** **** 6664")
]


@pytest.mark.parametrize('plain_data, formatted_data', hide_from_to_data)
def test_hide_numbers(plain_data, formatted_data):
    assert hide_numbers(plain_data) == formatted_data


def test_get_formatted_str(good_card_to_bill_operation, good_card_to_bill_operation_formatted_str):
    assert get_formatted_str(good_card_to_bill_operation) == good_card_to_bill_operation_formatted_str
