import pytest
from lib.password_checker import *

def test_valid():
    pwd_chkr = PasswordChecker()
    result = pwd_chkr.check('thisisalongpassword')
    assert result == True

def test_invalid():
    pwd_chkr = PasswordChecker()
    with pytest.raises(Exception) as e:
        pwd_chkr.check('short')
    assert str(e.value) == "Invalid password, must be 8+ characters."