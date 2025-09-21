import csv
from app.csv import get_csv_rows


def test_get_csv_rows(tmp_path):
    filename = tmp_path / "test.csv"
    csv_content = [
        ["student", "subject", "teacher", "date", "grade"],
        ["Семенова Елена", "Химия", "Ковалева Анна", "2023-01-10", "5"],
        ["Белов Станислав", "Физика", "Ткач Наталья", "2023-01-11", "4"],
    ]

    with filename.open(mode="w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(csv_content)

    result = get_csv_rows(filename)

    rows_list = [
        ["Семенова Елена", "Химия", "Ковалева Анна", "2023-01-10", "5"],
        ["Белов Станислав", "Физика", "Ткач Наталья", "2023-01-11", "4"],
    ]

    assert result == rows_list
