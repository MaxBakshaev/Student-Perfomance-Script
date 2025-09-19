from src.config import config
from src.csv_reader import get_csv_rows
from src.students_report import get_students_average_table
from src.table import Table


def generate_report():
    """Создает отчет и выводит в консоль"""

    # Аргументы командной строки
    args = config.parsed_args()

    if args.report == "students-performance":
        generate_students_report(args)

    elif args.report == "teachers-perfomance":
        generate_teachers_report(args)


def generate_students_report(args):
    rows_list = []

    # Добавление строк из CSV-файлов
    for filename in args.files:
        rows_list.extend(get_csv_rows(filename))

    # Преобразование списка строк в таблицу со средними оценками студентов
    table = get_students_average_table(rows_list)

    # Вывод таблицы в консоль
    Table.print_table(table)


def generate_teachers_report(args):  # <- Точка расширения
    pass
