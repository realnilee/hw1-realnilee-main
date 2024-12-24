import pytest
import import_ipynb
from hw1 import word_frequency

def test_word_frequency_basic():
    input_text = "hello world this is a test"
    expected_output = {
        "hello": 1,
        "world": 1,
        "test": 1
    }
    assert word_frequency(input_text) == expected_output

def test_word_frequency_with_stop_words():
    input_text = "hello world this is a test and this is fun"
    stop_words = ["is", "a", "and"]
    expected_output = {
        "hello": 1,
        "world": 1,
        "this": 2,
        "test": 1,
        "fun": 1
    }
    assert word_frequency(input_text, stop_words=stop_words) == expected_output

def test_word_frequency_case_insensitive():
    input_text = "Hello hello world"
    expected_output = {
        "hello": 2,
        "world": 1
    }
    assert word_frequency(input_text) == expected_output

def test_word_frequency_empty_text():
    input_text = ""
    expected_output = {}
    assert word_frequency(input_text) == expected_output

def test_word_frequency_special_characters():
    input_text = "Hello, world! This is a test."
    expected_output = {
        "hello": 1,
        "world": 1,
        "test": 1
    }
    assert word_frequency(input_text) == expected_output
