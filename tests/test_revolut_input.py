import pytest
from pathlib import Path


@pytest.fixture
def example():
    return Path(__file__).resolve().parent.parent / "example.txt"


@pytest.fixture
def example2():
    return Path(__file__).resolve().parent / "example_android_2019-10.csv"


def test_example_import(example, capsys):
    from main import main

    main(example)
    captured = capsys.readouterr()
    first_entry = captured.out.split("\n")[:3]
    assert first_entry == [
        '2017/05/31 Kenzo Ramen Sheppard',
        '    Expenses:Kenzo Ramen Sheppard              30.24',
        '    Assets:Revolut:Euro                       -30.24'
    ]


def test_example2_import(example2, capsys):
    from main import main

    main(example2)
    captured = capsys.readouterr()
    first_entry = captured.out.split("\n")[:3]
    assert first_entry == [
        '2019/10/20 some description (a note)',
        '    Assets:Revolut:Euro                         1,00',
        '    Income:some description (a note)           -1,00',
    ]


def test_example2_import_replace_comma(example2, capsys):
    from main import main

    main(example2, replace_comma=True)
    captured = capsys.readouterr()
    first_entry = captured.out.split("\n")[:3]
    assert first_entry == [
        '2019/10/20 some description (a note)',
        '    Assets:Revolut:Euro                         1.00',
        '    Income:some description (a note)           -1.00',
    ]
