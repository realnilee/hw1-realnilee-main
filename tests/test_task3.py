import pytest
import import_ipynb
from hw1 import extract_information

def test_extract_information_basic():
    input_text = "Contact me at john.doe@example.com or call +123 456 7890. Meeting on 10/05/2024."
    expected_output = {
        "emails": ["john.doe@example.com"],
        "phone_numbers": ["+123 456 7890"],
        "dates": ["10/05/2024"],
        "times": [],
        "prices": []
    }
    assert extract_information(input_text) == expected_output

def test_extract_information_with_custom_patterns():
    input_text = "The price is $19.99 and my number is 555-1234."
    custom_patterns = {
        "price_pattern": r'\$\d+(?:\.\d{2})?',
        "phone_pattern": r'\d{3}-\d{4}'
    }
    expected_output = {
        "emails": [],
        "phone_numbers": ["555-1234"],
        "dates": [],
        "times": [],
        "prices": ["$19.99"]
    }
    assert extract_information(input_text, **custom_patterns) == expected_output

def test_extract_information_no_matches():
    input_text = "There are no emails, phone numbers, or prices here."
    expected_output = {
        "emails": [],
        "phone_numbers": [],
        "dates": [],
        "times": [],
        "prices": []
    }
    assert extract_information(input_text) == expected_output

def test_extract_information_multiple_matches():
    input_text = "Emails: test@example.com, info@domain.com. Prices: $10, $20. Date: 12/31/2024."
    expected_output = {
        "emails": ["test@example.com", "info@domain.com"],
        "phone_numbers": [],
        "dates": ["12/31/2024"],
        "times": [],
        "prices": ["$10", "$20"]
    }
    assert extract_information(input_text) == expected_output

def test_extract_information_special_characters():
    input_text = "Contact me at john.doe@example.com, call me at (555) 123-4567, or visit 01-01-2024."
    expected_output = {
        "emails": ["john.doe@example.com"],
        "phone_numbers": ["(555) 123-4567"],
        "dates": ["01-01-2024"],
        "times": [],
        "prices": []
    }
    assert extract_information(input_text) == expected_output

def test_extract_information_custom_username_pattern():
    input_text = "Here are some usernames: @user1, @example_user, and @john_doe."
    custom_patterns = {
        "usernames": r'@[\w]+'
    }
    expected_output = {
        "emails": [],
        "phone_numbers": [],
        "dates": [],
        "times": [],
        "prices": [],
        "usernames": ["@user1", "@example_user", "@john_doe"]
    }
    assert extract_information(input_text, **custom_patterns) == expected_output
