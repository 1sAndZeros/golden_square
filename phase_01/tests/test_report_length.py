from lib.report_length import *

def test_correct_length():
    result = report_length('hello')
    assert result == 'This string was 5 characters long.'