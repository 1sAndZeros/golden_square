from lib.check_codeword import *

def test_horse_returns_correct():
    result = check_codeword("horse")
    assert result == "Correct! Come in."

def test_hurdle_returns_close():
    result = check_codeword("hurdle")
    assert result == "Close, but nope."

def test_highway_returns_wrong():
    result = check_codeword("highway")
    assert result == "WRONG!"

def test_capital_horse_returns_wrong():
    result = check_codeword("HORSE")
    assert result == 'WRONG!'