import sys
from unittest import mock
from app.settings import config


def test_parsed_args():
    test_args = [
        "students-performance",
        "--files",
        "file1.csv",
        "file2.csv",
        "--report",
        "students-performance",
    ]

    with mock.patch.object(sys, "argv", test_args):
        args = config.parsed_args()
        assert args.files == ["file1.csv", "file2.csv"]
        assert args.report == "students-performance"
