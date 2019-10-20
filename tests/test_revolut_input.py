import pytest
from pathlib import Path


@pytest.fixture
def example():
    return Path(__file__).resolve().parent.parent / "example.txt"


@pytest.fixture
def example2():
    return Path(__file__).resolve().parent / "example_android_2019-10.csv"


def test_example_import(example):
    from main import main

    main(example)


def test_example2_import(example2):
    from main import main

    main(example2)
