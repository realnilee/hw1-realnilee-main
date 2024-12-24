import pytest
import import_ipynb
from hw1 import preprocess_text

def test_cleaning_simple_text():
    input_text = "Hello, World!   This is a test..."
    expected_output = "hello world! this is a test."
    assert preprocess_text(input_text) == expected_output

def test_cleaning_with_special_characters():
    input_text = "Python is fun!!! #coding"
    expected_output = "python is fun! coding"
    assert preprocess_text(input_text) == expected_output

def test_cleaning_extra_spaces():
    input_text = "  Spaces should be    removed."
    expected_output = "spaces should be removed."
    assert preprocess_text(input_text) == expected_output

def test_cleaning_multiple_punctuations():
    input_text = "Hello!!! Is this working? Yes!!!"
    expected_output = "hello! is this working? yes!"
    assert preprocess_text(input_text) == expected_output

def test_cleaning_no_punctuation():
    input_text = "This is a normal sentence"
    expected_output = "this is a normal sentence"
    assert preprocess_text(input_text) == expected_output
