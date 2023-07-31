import pytest
from lib.check_todo import *

def test_check_includes_todo():
    result = check_todo("This is a #TODO list.")
    assert result == True

def test_check_does_not_include_todo():
    result = check_todo("This is a list.")
    assert result == False

def test_check_includes_lowercase_todo():
    result = check_todo("This is a #todo list.")
    assert result == True

def test_check_is_empty():
    result = check_todo("")
    assert result == False