from config import JSON_FILE, LIMIT_OPERATIONS
from utils import load_json, remove_not_executed_operations, validate_data, print_operations, change_date_type

if __name__ == "__main__":
    # Загрузить данные из файла
    data = load_json(JSON_FILE)

    # Валидация данных
    validated_data = validate_data(data)

    # Удалить из данных операции не EXECUTED
    remove_not_executed_operations(validated_data)

    # Изменить тип даты
    change_date_type(validated_data)

    # Отсортировать данные по убыванию даты
    validated_data.sort(key=lambda operation: operation.date, reverse=True)

    # Вывод на экран в заданном формате
    print_operations(validated_data[:LIMIT_OPERATIONS])
