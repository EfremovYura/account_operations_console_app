from datetime import datetime
from config import JSON_FILE, LIMIT_OPERATIONS
from utils import load_json, get_invalid_operations_index, print_operations


if __name__ == "__main__":
    # Загрузить данные из файла
    data = load_json(JSON_FILE)

    # Удалить из данных операции с пустыми полями и не EXECUTED
    operations_index_to_del = get_invalid_operations_index(data)
    for index in operations_index_to_del[::-1]:
        del data[index]

    # Отсортировать данные по убыванию даты
    sorted_by_date_data = sorted(data,
                                 key=lambda operation: datetime.strptime(operation.get('date'), '%Y-%m-%dT%H:%M:%S.%f'),
                                 reverse=True)

    # Вывод на экран в заданном формате
    print_operations(sorted_by_date_data[:LIMIT_OPERATIONS])
