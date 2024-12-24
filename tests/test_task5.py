import pytest
import import_ipynb
import re
from hw1 import summarize_text

def count_sentences(text):
    return len(re.split(r'(?<=[.!?])\s+', text))


def test_summarize_text_basic_compression():
    input_text = (
        "I love this product! It's fantastic and makes me very happy. "
        "This is the worst experience I've ever had. "
        "Great service but the food was bad. "
        "The atmosphere was amazing, and the location is perfect."
    )
    compression_ratio = 0.5
    result = summarize_text(input_text, compression_ratio=compression_ratio)
    # Ensure the summary is about half the length
    assert count_sentences(result) <= count_sentences(input_text) * compression_ratio

def test_summarize_text_min_threshold():
    input_text = (
        "I love this product! It's fantastic and makes me very happy. "
        "This is the worst experience I've ever had."
    )
    compression_ratio = 0.1
    min_threshold = 2
    result = summarize_text(input_text, compression_ratio=compression_ratio, min_threshold=min_threshold)
    # Even with a low compression ratio, the output should have at least min_threshold sentences
    assert count_sentences(result) >= min_threshold

def test_summarize_text_high_compression_ratio():
    input_text = (
        "Great product! Easy to use. Quick setup. Fantastic performance. "
        "Affordable and reliable. Highly recommend."
    )
    compression_ratio = 0.8
    result = summarize_text(input_text, compression_ratio=compression_ratio)
    # Ensure the summary retains 80% of the original content
    assert count_sentences(result) >= count_sentences(input_text) * (1 - compression_ratio)

def test_summarize_text_single_sentence():
    input_text = "This is the only sentence in the text."
    compression_ratio = 0.5
    result = summarize_text(input_text, compression_ratio=compression_ratio)
    # If there's only one sentence, it should be retained regardless of the compression ratio
    assert result == input_text

def test_summarize_text_empty_input():
    input_text = ""
    compression_ratio = 0.6
    result = summarize_text(input_text, compression_ratio=compression_ratio)
    # An empty input should return an empty output
    assert result == ""
