"""
Validation Exercises

These functions return ``True`` or ``False`` depending on whether the
string passes a condition.

"""
import re

def has_vowel(sentence : str) -> bool:
    """Return True iff the string contains one or more vowels."""
    vowel_regex = re.compile(r'[aeiou]', re.I)
    return vowel_regex.search(sentence) != None


def is_integer(text: str):
    """Return True iif the string is an integer"""
    '''
    Broker apart...

    ^(-|\+)? - starts with zero or one instances of either '-' or '+'
    \d+$ - ends with one or more digit

    '''
    integer_regex = re.compile(r'^(-|\+)?\d+$')
    integer_regex = re.compile(r'^(-)?\d+$')

    return integer_regex.search(text) != None

def is_fraction(string):
    """Return True iff the string represents a valid fraction."""


def is_valid_date(string):
    """Return True iff the string represents a valid YYYY-MM-DD date."""


def is_number(string):
    """Return True iff the string represents a decimal number."""


def is_hex_color(string):
    """Return True iff the string represents an RGB hex color code."""
