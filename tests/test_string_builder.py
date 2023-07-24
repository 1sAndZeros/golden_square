from lib.string_builder import *

string_builder = StringBuilder()

def test_add_hello_world():
    string_builder.add('hello ')
    string_builder.add('world')
    assert string_builder.output() == 'hello world'

def test_length():
    assert string_builder.size() == 11