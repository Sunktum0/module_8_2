def personal_sum(numbers):
    result = 0
    incorrect_data = 0

    for number in numbers:
        # Проверяем, является ли элемент пустой строкой или символом
        if isinstance(number, (int, float)):
            result += number
        elif isinstance(number, str) and not number.strip():  # Пустая строка
            print(f'Некорректный тип данных для подсчёта суммы - {number}')
            incorrect_data += 1
        else:
            print(f'Некорректный тип данных для подсчёта суммы - {number}')
            incorrect_data += 1

    return result, incorrect_data

def calculate_average(numbers):
    try:
        if not isinstance(numbers, (list, tuple, set)):
            raise TypeError("В numbers записан некорректный тип данных")

        total_sum, incorrect_data_count = personal_sum(numbers)
        count = len(numbers) - incorrect_data_count

        return total_sum / count if count > 0 else 0

    except ZeroDivisionError:
        return 0
    except TypeError as te:
        print(te)
        return None

# Примеры выполнения программы
print(f'Результат 1: {calculate_average(["1", "", "2", "", "3"])}')  # Проверка строки с пустыми элементами
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать