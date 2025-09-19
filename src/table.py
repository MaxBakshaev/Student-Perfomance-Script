from tabulate import tabulate
from typing import List, Tuple


class Table:
    """
    Документация tabulate: https://github.com/astanin/python-tabulate

    Настройки таблицы
    """

    headers: List[str] = [" ", "student_name", "grade"]
    tablefmt: str = "pretty"
    colalign: Tuple[str, str, str] = ("right", "left", "right")

    @classmethod
    def print_table(cls, table: List[Tuple[int, str, int]]) -> None:
        """Выводит таблицу в консоль"""

        print(
            tabulate(
                table,
                headers=cls.headers,
                tablefmt=cls.tablefmt,
                colalign=cls.colalign,
            )
        )
