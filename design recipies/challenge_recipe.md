# TODO List Function Design Recipe

## 1. Describe the Problem

As a user
So that I can keep track of my tasks
I want to check if a text includes the string #TODO.

## 2. Design the Function Signature

```python

def check_todo(text):
   """: Parameters:
        Text which is a string of text to check.

    Returns:
        A boolen of True, if it includes #TODO
"""
    pass
```

## 3. Create Examples as Tests

```python

"""
Check if the text includes #TODO.
"""
check_todo("This is a #TODO list.") => True

"""
Check if the text does not include #TODO.
"""
check_todo("This is a list.") => False

"""
Check if the text includes #todo.
"""
check_todo("This is a #todo list.") => True

"""
Check if the text is an empty string.
"""
check_todo("") => False


```
