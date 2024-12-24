import pytest
import import_ipynb
from hw1 import apply_analysis, word_frequency, analyze_sentiment


def test_apply_single_function():
    input_text = "i love python! it's amazing and fun."

    # Test with just the word frequency function
    result = apply_analysis(input_text, [word_frequency])

    # Check that the result is a dictionary and contains the expected keys
    assert isinstance(result, dict)
    assert "word_frequency" in result

    # Verify that word frequency results are correct
    assert result["word_frequency"] == {
        "love": 1,
        "python": 1,
        "amazing": 1,
        "fun": 1,
        "it's": 1
    }

def test_apply_multiple_functions():
    input_text = "i love python! it's amazing and fun."

    # Test with both word frequency and sentiment analysis functions
    result = apply_analysis(input_text, [word_frequency, analyze_sentiment])

    # Check that the result is a dictionary and contains the expected keys
    assert isinstance(result, dict)
    assert "word_frequency" in result
    assert "analyze_sentiment" in result

    # Verify that word frequency results are correct
    assert result["word_frequency"] == {
        "love": 1,
        "python": 1,
        "amazing": 1,
        "fun": 1,
        "it's": 1
    }

    # Verify that sentiment score is calculated correctly
    assert result["analyze_sentiment"] == 3  # Adjust based on the sentiment words provided

def test_apply_no_functions():
    input_text = "this is a neutral sentence."

    # Test with an empty list of functions
    result = apply_analysis(input_text, [])

    # Check that the result is an empty dictionary
    assert isinstance(result, dict)
    assert len(result) == 0
