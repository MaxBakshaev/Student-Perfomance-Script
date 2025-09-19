"""
Документация:
- tabulate: https://github.com/astanin/python-tabulate
- argparse: https://docs.python.org/3/library/argparse.html
"""

import csv
import argparse
from operator import itemgetter
from typing import List, Tuple

from tabulate import tabulate


def parsed_args():
    """Парсит аргументы командной строки"""

    parser = argparse.ArgumentParser(
        prog="students-performance",
        description="Скрипт для отслеживания успеваемости учеников",
    )
    parser.add_argument(
        "-f",
        "--filename",
        default="students1.csv",
        help="Путь к CSV файлу с данными студентов",
    )

    return parser.parse_args()


def get_csv_rows(filename: str) -> List[List[str]]:
    """Читает CSV-файл и возвращает список его строк"""

    with open(filename, "r", encoding="utf-8", newline="") as file:
        row = csv.reader(file)
        next(row)

        return list(row)


def convert_marks_to_int(rows_list: List[List[str]]) -> None:
    """Преобразует оценки в столбце с индексом 4 в int"""

    for row in rows_list:
        row[4] = int(row[4])


def sort_rows_by_marks(rows_list: List[List[str]]) -> List[List[str]]:
    """Возвращает список, отсортированный по оценкам в порядке убывания"""

    convert_marks_to_int(rows_list)

    sorted_rows = sorted(rows_list, key=itemgetter(4), reverse=True)

    return sorted_rows


def get_table(sorted_rows: List[List[str]]) -> List[Tuple[int, str, int]]:
    """
    Возвращает список кортежей (номер, имя, оценка),
    отсортированный по оценкам с номерами по порядку
    """

    table: List[Tuple[int, str, int]] = [
        (number, row[0], row[4])
        for number, row in enumerate(
            sorted_rows,
            start=1,
        )
    ]

    return table


def print_table(table: List[List[str]]) -> None:
    """Выводит таблицу в консоль"""

    print(
        tabulate(
            table,
            headers=[" ", "student_name", "grade"],
            tablefmt="pretty",
            colalign=("right", "left", "right"),
        )
    )


def main():

    # Аргументы командной строки
    args = parsed_args()
    filename = args.filename

    # Список строк из CSV-файла
    rows_list = get_csv_rows(filename)

    # Список, отсортированный по оценкам в порядке убывания
    sorted_rows = sort_rows_by_marks(rows_list)

    # Cписок кортежей (номер, имя, оценка),
    # отсортированный по оценкам с номерами по порядку
    table = get_table(sorted_rows)

    # Вывод таблицы в консоль
    print_table(table)


if __name__ == "__main__":
    main()
