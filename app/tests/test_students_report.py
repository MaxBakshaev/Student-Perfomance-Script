from app.students import (
    collect_grades,
    calculate_avg_grades,
    get_students_average_marks_table,
    sort_and_number,
)


def test_collect_grades():
    rows_list = [
        ["Максимов Кирилл", "Физика", "Белова Светлана", "2023-09-02", "3"],
        ["Калинина Ольга", "Математика", "Орлов Сергей", "2023-09-01", "5"],
        ["Калинина Ольга", "Физика", "Белова Светлана", "2023-09-01", "4"],
    ]

    result = collect_grades(rows_list)

    expected = {
        "Максимов Кирилл": [3],
        "Калинина Ольга": [5, 4],
    }

    assert dict(result) == expected


def test_calculate_avg_grades():
    grades_dict = {
        "Максимов Кирилл": [3],
        "Калинина Ольга": [5, 4],
    }

    result = calculate_avg_grades(grades_dict)

    expected = [
        ("Максимов Кирилл", 3.0),
        ("Калинина Ольга", 4.5),
    ]

    assert sorted(result) == sorted(expected)


def test_sort_and_number():
    avg_grades = [
        ("Максимов Кирилл", 3.0),
        ("Калинина Ольга", 4.5),
    ]

    result = sort_and_number(avg_grades)

    expected = [
        (1, "Калинина Ольга", 4.5),
        (2, "Максимов Кирилл", 3.0),
    ]

    assert result == expected


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
