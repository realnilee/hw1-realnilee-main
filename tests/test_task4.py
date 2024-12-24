import pytest
import import_ipynb
from hw1 import analyze_sentiment

positive_words = ["good", "great", "happy", "joy", "excellent", "fantastic", "love", "best"]
negative_words = ["bad", "sad", "hate", "terrible", "awful", "poor", "worst"]

def test_analyze_sentiment_positive_words():
    input_text = "I love this product! It's fantastic and makes me very happy."
    expected_output = 3  # 3 positive words - 0 negative word
    assert analyze_sentiment(input_text, positive_words=positive_words, negative_words=negative_words) == expected_output

def test_analyze_sentiment_negative_words():
    input_text = "This is the worst experience I've ever had."
    expected_output = -1  # 0 positive words - 1 negative words
    assert analyze_sentiment(input_text, positive_words=positive_words, negative_words=negative_words) == expected_output

def test_analyze_sentiment_mixed_words():
    input_text = "Great service but the food was bad."
    expected_output = 0  # 1 positive word - 1 negative word
    assert analyze_sentiment(input_text, positive_words=positive_words, negative_words=negative_words) == expected_output

def test_analyze_sentiment_with_custom_words():
    input_text = "This is a terrible product."
    custom_positive_words = ["great", "awesome"]
    custom_negative_words = ["terrible", "bad", "awful"]
    expected_output = -1  # 0 positive words - 1 negative words
    assert analyze_sentiment(input_text, positive_words=custom_positive_words, negative_words=custom_negative_words) == expected_output

def test_analyze_sentiment_no_words():
    input_text = "Nothing special about this."
    expected_output = 0  # 0 positive words - 0 negative words
    assert analyze_sentiment(input_text, positive_words=positive_words, negative_words=negative_words) == expected_output
