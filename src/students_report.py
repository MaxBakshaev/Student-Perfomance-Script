from collections import defaultdict
from typing import Dict, List, Tuple

from src.table import StudentsTable


def get_students_average_marks_table(
    rows_list: List[List[str]],
) -> List[Tuple[int, str, float]]:
    """
    Считает среднюю оценку по каждому студенту

    Возвращает объект StudentsTable, в который передается
    table: список кортежей (номер, имя, средняя оценка)

    Пример:
    table = [
        (1, 'Калинина Ольга', 4.8),
        (2, 'Максимов Кирилл', 4.4),
        (3, 'Семенова Елена', 4.0),
        ...
    ]

    """

    # добавление в словарь имени и оценки
    student_grades: Dict[str, list[float]] = defaultdict(list)
    for row in rows_list:
        name = row[0]  # имя студента
        grade = int(row[4])  # оценка int
        student_grades[name].append(grade)

    # подсчет средней оценки для каждого студента
    avg_grades = [
        (name, round(sum(grades) / len(grades), 2))
        for name, grades in student_grades.items()
    ]

    # сортировка по убыванию средней оценки
    avg_grades_sorted = sorted(avg_grades, key=lambda x: x[1], reverse=True)

    # добавление нумерации
    table = [
        (i + 1, name, avg)
        for i, (name, avg)
        in enumerate(avg_grades_sorted)
    ]

    return StudentsTable(table)
