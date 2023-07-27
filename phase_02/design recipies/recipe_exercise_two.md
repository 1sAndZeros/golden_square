# Grammar Check Function Design Recipe

## 1. Describe the Problem

As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

## 2. Design the Function Signature

```python
def check_grammar(text):
    """
    Given some test, calculate how many minutes it would take to read based on 200 words per minute

    Parameters:
        text: a string containing words (e.g. "This is a sentence, please work out how long it would take me to read it")

    Returns:
        a float, representing time in minutes (e.g. 0.08)

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass
```

## 3. Create Examples as Tests

```python
"""
Given an empty string, return 0
"""
estimate_reading_time("") => 0

"""
Given some short text (under 200 words), return float representing the fraction of a minute it would take to read
"""
estimate_reading_time("This is a very short sentence that contains ten words") => 0.05

"""
Given a piece of text containing exactly 200 words, return float of 1 representing the minutes it would take to read. The example text below has been truncated!
"""

estimate_reading_time("Lorem ipsum dolor sit amet, consectetur adipiscing elit ... Quisque quis risus dapibus, pretium mi ut, mollis mi. Aliquam erat volutpat.") => 1.0

"""
Given a longer piece of text (300 words), return float of 1.5 representing the minutes it would take to read. The example text below has been truncated!
"""

estimate_reading_time("Lorem ipsum dolor sit amet, consectetur adipiscing elit ... Quisque quis risus dapibus, pretium mi ut, mollis mi. Aliquam erat volutpat.") => 1.5

"""
Given a None value
It throws an error
"""
estimate_reading_time(None) throws an error
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

```python

from lib.estimate_reading_time import *

"""
Given some short text (under 200 words), return float representing the fraction of a minute it would take to read
"""
def test_short_text():
    result = calculate_reading_time("This is a very short sentence that contains ten words")
    assert result == 0.05

"""
Given a piece of text containing exactly 200 words, return float of 1 representing the minutes it would take to read. The example text below has been truncated!
"""
def test_text_with_200_words():
    result = calculate_reading_time("Lorem ipsum dolor sit amet, consectetur adipiscing elit ... Quisque quis risus dapibus, pretium mi ut, mollis mi. Aliquam erat volutpat.")
    assert result == 1

"""
Given a longer piece of text (300 words), return float of 1.5 representing the minutes it would take to read. The example text below has been truncated!
"""
def test_text_with_300_words():
    result = calculate_reading_time("Lorem ipsum dolor sit amet, consectetur adipiscing elit ... Quisque quis risus dapibus, pretium mi ut, mollis mi. Aliquam erat volutpat.")
    assert result == 1.5

"""
Given an empty string, return 0
"""
def test_empty_string():
    result = calculate_reading_time("")
    assert result == 0

"""
Given a None value
It throws an error
"""
def test_none_input():
    with pytest.raises(Exception) as e:
        estimate_reading_time(None)
    error_message = str(e.value)
    assert error_message == 'No text was given. Cannot estimate reading time.'

```

Ensure all test function names are unique and begin with test, otherwise pytest will ignore them!
