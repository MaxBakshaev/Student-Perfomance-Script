from abc import ABC
from tabulate import tabulate
from typing import List, Tuple


class BaseTable(ABC):
    """
    Документация tabulate: https://github.com/astanin/python-tabulate

    Настройки таблицы
    """

    headers: List[str]
    tablefmt: str
    colalign: Tuple[str, ...]

    def __init__(self, table: List[Tuple]):
        self.table = table

    def print(self):
        """Выводит таблицу в консоль"""
        print(
            tabulate(
                self.table,
                headers=self.headers,
                tablefmt=self.tablefmt,
                colalign=self.colalign,
            )
        )


class StudentsTable(BaseTable):
    headers = [" ", "student_name", "grade"]
    tablefmt = "pretty"
    colalign = ("right", "left", "right")


# class TeachersTable(BaseTable):
    # headers = ...
    # tablefmt = ...
    # colalign = ...
