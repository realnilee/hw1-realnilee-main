import pytest
import import_ipynb
from hw1 import visualize_word_frequency

def test_visualize_word_frequency(capsys):
    word_frequencies = {
        "hello": 5,
        "world": 3,
        "python": 4,
        "coding": 2
    }

    visualize_word_frequency(word_frequencies)

    captured = capsys.readouterr()

    # Get the output and split by lines
    output_lines = captured.out.strip().split("\n")

    # Check that each word in the dictionary appears on its own line
    for word in word_frequencies.keys():
        assert any(word in line for line in output_lines), f"Word '{word}' not found in output"


def test_visualize_max_threshold(capsys):
    word_frequencies = {
        "hello": 10,
        "world": 8,
        "python": 7,
        "coding": 5,
        "fun": 3
    }

    # Set a max_threshold of 3
    visualize_word_frequency(word_frequencies, max_threshold=3)
    captured = capsys.readouterr()
    output = captured.out.strip().split("\n")

    # Check that only the top 3 words are in the output
    top_words = ["hello", "world", "python"]
    for word in top_words:
        assert any(word in line for line in output)

    # Ensure no other words are present
    for word in ["coding", "fun"]:
        assert not any(word in line for line in output)
