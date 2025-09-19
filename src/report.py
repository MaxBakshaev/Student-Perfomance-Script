from abc import ABC
from src.config import config
from src.csv_reader import get_csv_rows
from src.students_report import get_students_average_table
from src.table import Table


class BaseReport(ABC):
    def __init__(self):
        """Аргументы командной строки"""

        self.args = config.parsed_args()


class StudentsPerfomanceReport(BaseReport):
    def generate_report(self):
        """Создает отчет о средних оценках студентов"""

        # Добавление строк из CSV-файлов
        rows_list = []
        for filename in self.args.files:
            rows_list.extend(get_csv_rows(filename))

        # Преобразование списка строк в таблицу со средними оценками студентов
        table = get_students_average_table(rows_list)

        # Вывод таблицы в консоль
        Table.print_table(table)


class TeachersPerfomanceReport(BaseReport):
    def generate_report(self):

        pass   # <- Точка расширения


class ReportGenerator(BaseReport):
    def generate_report(self):
        """Создает отчет и выводит в консоль"""

        if self.args.report == "students-performance":
            rg = StudentsPerfomanceReport()

        elif self.args.report == "teachers-performance":
            rg = TeachersPerfomanceReport()

        rg.generate_report()


report = ReportGenerator()
