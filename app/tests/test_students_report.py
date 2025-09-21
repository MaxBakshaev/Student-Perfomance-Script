from app.students import get_students_average_marks_table


def test_get_students_average_marks_table():
    rows_list = [
        ["Максимов Кирилл", "Физика", "Белова Светлана", "2023-09-02", "4"],
        ["Калинина Ольга", "Математика", "Орлов Сергей", "2023-09-01", "5"],
        ["Калинина Ольга", "Физика", "Белова Светлана", "2023-09-01", "5"],
    ]

    report_table = get_students_average_marks_table(rows_list)

    assert report_table == [
        (1, "Калинина Ольга", 5),
        (2, "Максимов Кирилл", 4),
    ]
