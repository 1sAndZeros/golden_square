from lib.count_words import *

def test_count_words():
    count = count_words('This sentence has five words')
    assert count == 5