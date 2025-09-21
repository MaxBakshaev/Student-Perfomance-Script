from app.students import get_students_average_marks_table


def test_get_students_average_marks_table():
    rows_list = [
        ["Калинина Ольга", "Математика", "Орлов Сергей", "2023-09-01", "5"],
        ["Калинина Ольга", "Физика", "Белова Светлана", "2023-09-01", "5"],
        ["Максимов Кирилл", "Физика", "Белова Светлана", "2023-09-02", "4"],
    ]

    report_table = get_students_average_marks_table(rows_list)

    isinstance(report_table, list)
    assert isinstance(report_table[0], tuple)
    assert len(report_table) == 2
    assert report_table[0][0] == 1
    assert report_table[0][1] == "Калинина Ольга"
    assert report_table[0][2] == 5
    assert report_table[1][0] == 2
    assert report_table[1][1] == "Максимов Кирилл"
    assert report_table[1][2] == 4
