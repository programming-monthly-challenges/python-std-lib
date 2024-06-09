import pytest

import main


def test_example_answer():

    answer = main.example_answer()
    assert answer == "Hello, world!"