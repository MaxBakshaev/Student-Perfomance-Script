from abc import ABC, abstractmethod
from src.config import parced_args
from src.csv_reader import get_csv_rows
from src.students_report import get_students_average_table
from src.table import Table


class BaseReport(ABC):

    @abstractmethod
    def generate_report(self):
        pass


class StudentsPerformanceReport(BaseReport):
    def generate_report(self):
        """Создает отчет о средних оценках студентов"""

        # Добавление строк из CSV-файлов
        rows_list = []
        for filename in parced_args.files:
            rows_list.extend(get_csv_rows(filename))

        # Преобразование списка строк в таблицу со средними оценками студентов
        table = get_students_average_table(rows_list)

        # Вывод таблицы в консоль
        Table.print_table(table)


class TeachersPerformanceReport(BaseReport):
    def generate_report(self):

        pass  # <- Точка расширения


class ReportGenerator:
    def report_generator(self):
        """Создает отчет и выводит в консоль"""

        if parced_args.report == "students-performance":
            rg = StudentsPerformanceReport()

        elif parced_args.report == "teachers-performance":
            rg = TeachersPerformanceReport()

        rg.generate_report()


report = ReportGenerator()
