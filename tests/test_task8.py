import pytest
import import_ipynb
from hw1 import TextAnalyzer, word_frequency, analyze_sentiment


def test_initialization():
    text = "This is a test. Testing initialization!"
    analyzer = TextAnalyzer(text)

    # Check that the original text is stored correctly
    assert analyzer.original_text == text

    # Check that the cleaned text is correctly processed
    assert analyzer.cleaned_text == "this is a test. testing initialization!"

def test_word_frequency_method():
    text = "Hello, hello world! Python is fun. Python!"
    analyzer = TextAnalyzer(text)
    result = analyzer.word_frequency()

    # Check the word frequencies are calculated correctly
    expected = {"hello": 2, "world": 1, "python": 2, "fun": 1}
    assert result == expected

def test_extract_information_method():
    text = "Email me at john.doe@example.com. Call me at +123 456 7890."
    analyzer = TextAnalyzer(text)
    result = analyzer.extract_information()

    # Check if emails and phone numbers are extracted correctly
    assert result["emails"] == ["john.doe@example.com"]
    assert result["phone_numbers"] == ["+123 456 7890"]

def test_analyze_sentiment_method():
    text = "I love Python, but I hate bugs."
    analyzer = TextAnalyzer(text)
    result = analyzer.analyze_sentiment()

    # Check if the sentiment score is calculated correctly
    assert result == 0  # Adjust based on your predefined positive and negative words

def test_summarize_text_method():
    text = (
        "I love this product! It's fantastic and makes me very happy. "
        "This is the worst experience I've ever had. "
        "Great service but the food was bad. "
        "The atmosphere was amazing, and the location is perfect."
    )
    analyzer = TextAnalyzer(text)
    summary = analyzer.summarize_text(compression_ratio=0.5)

    # Check if the summary is a string and has a reduced number of sentences
    assert isinstance(summary, str)
    assert len(summary.split('. ')) <= len(text.split('. ')) * 0.5

def test_visualize_word_frequency_method(capsys):
    text = "Hello world! Hello again, world!"
    analyzer = TextAnalyzer(text)
    analyzer.visualize_word_frequency()

    # Capture the output
    captured = capsys.readouterr().out

    # Check that words appear in the output, each on its own line
    assert "hello" in captured
    assert "world" in captured

def test_apply_analysis_method():
    text = "I love Python! It's amazing and fun."
    analyzer = TextAnalyzer(text)
    result = analyzer.apply_analysis([word_frequency, analyze_sentiment])

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
