from abc import ABC, abstractmethod

from app.settings import config, StudentsTable
from app.csv import get_csv_rows
from app.students import get_students_average_marks_table


class BaseReport(ABC):

    def generate_report(self):
        # Добавление строк из CSV-файлов
        rows_list = []
        for filename in config.parsed_args().files:
            rows_list.extend(get_csv_rows(filename))

        # Создание таблицы отчета
        report_table = self.build_table(rows_list)
        # Вывод в консоль
        report_table.print()

    @abstractmethod
    def build_table(self, rows_list):
        """Преобразование списка строк в таблицу с кастомными параметрами"""
        pass


class StudentsPerformanceReport(BaseReport):
    def build_table(self, rows_list):
        """Создание отчета о средних оценках студентов"""

        table = get_students_average_marks_table(rows_list)
        return StudentsTable(table)


# class TeachersPerformanceReport(BaseReport):
#     def build_table(self, rows_list):
#         table = get_teachers_some_params_table(rows_list)
#         return TeachersTable(table)


class ReportGenerator:
    def report_generator(self):
        """Создает отчет и выводит в консоль"""

        if config.parsed_args().report == "students-performance":
            rg = StudentsPerformanceReport()

        # elif config.parsed_args().report == "teachers-performance":
        #     rg = TeachersPerformanceReport()

        rg.generate_report()


report = ReportGenerator()
