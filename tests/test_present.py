import pytest
from lib.present import *

def test_contents():
    present = Present()
    present.wrap('chocolate')
    assert present.unwrap() == 'chocolate'

def test_unwrap_error():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    error_message = str(e.value)
    assert error_message == 'No contents have been wrapped.'

def test_wrap_error():
    present = Present()
    with pytest.raises(Exception) as e:
        present.wrap('item1')
        present.wrap('item2')
    error_message = str(e.value)
    assert error_message == 'A contents has already been wrapped.'