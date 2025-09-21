from abc import ABC, abstractmethod
from src.config import parced_args
from src.csv_reader import get_csv_rows
from src.students_report import get_students_average_marks_table


class BaseReport(ABC):

    def generate_report(self):
        # Добавление строк из CSV-файлов
        rows_list = []
        for filename in parced_args.files:
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

        return get_students_average_marks_table(rows_list)


# class TeachersPerformanceReport(BaseReport):
#     def build_table(self, rows_list):
#         return get_teachers_some_params_table(rows_list)


class ReportGenerator:
    def report_generator(self):
        """Создает отчет и выводит в консоль"""

        if parced_args.report == "students-performance":
            rg = StudentsPerformanceReport()

        # elif parced_args.report == "teachers-performance":
        #     rg = TeachersPerformanceReport()

        rg.generate_report()


report = ReportGenerator()
