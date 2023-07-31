from lib.make_snippet import *

def test_truncated_snippet():
    result = make_snippet('This is a sentence longer than five words')
    assert result == 'This is a sentence longer...'

def test_snippet_under_five_words():
    result = make_snippet('This is a sentence')
    assert result == 'This is a sentence'
