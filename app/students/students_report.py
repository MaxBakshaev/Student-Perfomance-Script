from collections import defaultdict
from typing import Dict, List, Tuple


def collect_grades(rows_list: List[List[str]]) -> Dict[str, List[float]]:
    """Добавляет в словарь имя и оценки"""

    grades = defaultdict(list)
    for row in rows_list:
        name = row[0]  # имя студента
        grade = int(row[4])  # оценка int
        grades[name].append(grade)
    return grades


def calculate_avg_grades(
    grades_dict: Dict[str, List[float]],
) -> List[Tuple[str, float]]:
    """Считает среднюю оценку для каждого студента"""

    return [
        (name, round(sum(grades) / len(grades), 2))
        for name, grades in grades_dict.items()
    ]


def sort_and_number(
    avg_grades: List[Tuple[str, float]],
) -> List[Tuple[int, str, float]]:
    """Cортирует и нумерует строки"""

    sorted_ = sorted(avg_grades, key=lambda x: x[1], reverse=True)

    return [(i + 1, name, avg) for i, (name, avg) in enumerate(sorted_)]


def get_students_average_marks_table(
    rows_list: List[List[str]],
) -> List[Tuple[int, str, float]]:
    """
    Возвращает список кортежей (номер, имя, средняя оценка)
    в порядке в порядке успеваемости студентов

    Пример возвращаемого значения:
    table = [
        (1, 'Калинина Ольга', 4.8),
        (2, 'Максимов Кирилл', 4.4),
        (3, 'Семенова Елена', 4.0),
        ...
    ]

    """

    # добавление в словарь имени и оценки
    grades_dict = collect_grades(rows_list)

    # подсчет средней оценки для каждого студента
    avg_grades = calculate_avg_grades(grades_dict)

    # сортировка и нумерация
    table = sort_and_number(avg_grades)

    return table
