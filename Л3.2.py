# TODO Напишите функцию find_common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"


def find_common_participants(group1, group2, separator=','):
    """
    Находит общих участников в двух группах.

    Параметры:
    group1 (str): строка с участниками первой группы
    group2 (str): строка с участниками второй группы
    separator (str): разделитель (по умолчанию ',')

    Возвращает:
    list: отсортированный список общих участников
    """
    # Разделяем строки на списки участников
    participants1 = group1.split(separator)
    participants2 = group2.split(separator)

    # Находим пересечение множеств для поиска общих участников
    common = set(participants1) & set(participants2)

    # Возвращаем отсортированный список
    return sorted(common)

participants1_default = "Иванов,Петров,Сидоров"
participants2_default = "Петров,Сидоров,Смирнов"
print("Тест с разделителем-запятой:")
print(find_common_participants(participants1_default, participants2_default))

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print("\nТест с разделителем '|':")
result = find_common_participants(participants_first_group, participants_second_group, separator='|')
print(result)

print("\nДополнительные тесты:")
print(find_common_participants("Иванов,Петров", "Сидоров,Смирнов"))  # Нет общих
print(find_common_participants("Иванов", "Иванов,Петров"))  # Общий: Иванов
print(find_common_participants("", "Петров"))  # Пустая первая группа
# TODO Провеьте работу функции с разделителем отличным от запятой
