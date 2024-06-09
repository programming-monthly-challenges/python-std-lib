import pytest

import main


def test_example_answer():

    answer = main.example_answer()
    assert answer == "Hello, world!"
    
    
def test_templating_introduction_answer():
    
    answer = main.Templating().question_introduction()
    assert answer == "Hello, world! My name is Jimmy and I am 6 years old. My favorite food is ice cream. I am really scared of clowns."
    
    
def test_regex_single_line_answer():

    answer = main.Regex().question_regex_single_line()
    assert answer == ("John", 2)
    
    
def test_regex_janes_score():

    answer = main.Regex().question_janes_score()
    assert answer == 60