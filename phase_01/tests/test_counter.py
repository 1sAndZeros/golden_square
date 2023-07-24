from lib.counter import *

def test_counter_once():
    counter = Counter()
    counter.add(5)
    result = counter.report()
    assert result == 'Counted to 5 so far.'

def test_counter_twice():
    counter = Counter()
    counter.add(10)
    counter.add(6)
    result = counter.report()
    assert result == 'Counted to 16 so far.'