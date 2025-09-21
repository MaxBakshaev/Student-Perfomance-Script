from unittest.mock import patch, MagicMock

from app.report import ReportGenerator


def test_report_generator_students_performance():
    rows_list = [
        ["Семенова Елена", "Химия", "Ковалева Анна", "2023-01-10", "5"],
        ["Семенова Елена", "Физика", "Ткач Наталья", "2023-01-11", "4"],
    ]

    table = [
        (1, "Семенова Елена", 4.5),
    ]

    mock_students_table = MagicMock()
    mock_students_table.print = MagicMock()

    with (
        patch("app.report.config") as mock_config,
        patch(
            "app.report.get_csv_rows",
            return_value=rows_list,
        ) as mock_get_csv_rows,
        patch(
            "app.report.get_students_average_marks_table",
            return_value=table,
        ) as mock_get_avg_table,
        patch("app.report.StudentsTable", return_value=mock_students_table),
    ):

        mock_config.parsed_args.return_value.files = ["students1.csv"]
        mock_config.parsed_args.return_value.report = "students-performance"

        report = ReportGenerator()
        report.report_generator()

        mock_get_csv_rows.assert_called_once_with("students1.csv")
        mock_get_avg_table.assert_called_once_with(rows_list)
        mock_students_table.print.assert_called_once()
