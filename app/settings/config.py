import argparse


class Config:
    """Настройки скрипта"""

    def __init__(self):
        self.prog: str = "students-performance"
        self.description: str = "Скрипт для анализа успеваемости студентов"

        # добавление отчетов
        self.allowed_reports = [
            "students-performance",
            # "teachers-performance",
        ]

    def parsed_args(self):
        """
        Документация argparse: https://docs.python.org/3/library/argparse.html

        Парсит аргументы командной строки
        """

        parser = argparse.ArgumentParser(
            prog=self.prog,
            description=self.description,
        )
        parser.add_argument(
            "--files",
            nargs="+",
            required=True,
            help="Файл или файлы с оценками",
        )
        parser.add_argument(
            "--report",
            choices=self.allowed_reports,
            required=True,
            help="Название отчета",
        )

        return parser.parse_args()


config = Config()
