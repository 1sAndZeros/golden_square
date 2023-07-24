from lib.greet import *

def test_greet_rikie_returns_hello_rikie():
    result = greet('Rikie')
    assert result == 'Hello, Rikie!'