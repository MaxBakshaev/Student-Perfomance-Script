from app.settings import StudentsTable


def test_print_students_table(capsys):

    table = [
        (1, "Семенова Елена", 4.5),
        (2, "Титов Владислав", 4.0),
    ]

    report_table = StudentsTable(table)
    report_table.print()

    captured = capsys.readouterr()
    output = captured.out

    table_output = (
        "+---+-----------------+-------+\n"
        "|   | student_name    | grade |\n"
        "+---+-----------------+-------+\n"
        "| 1 | Семенова Елена  |   4.5 |\n"
        "| 2 | Титов Владислав |   4.0 |\n"
        "+---+-----------------+-------+\n"
    )

    assert table_output in output
