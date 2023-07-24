from lib.gratitudes import *

def test_empty_list():
    gratitudes = Gratitudes()
    assert gratitudes.gratitudes == []

def test_add_gratitude():
    gratitudes = Gratitudes()
    gratitudes.add('family')
    gratitudes.add('friends')
    gratitudes.add('food')
    assert gratitudes.gratitudes == ['family', 'friends', 'food']

def test_format():
    gratitudes = Gratitudes()
    gratitudes.add('family')
    gratitudes.add('friends')
    gratitudes.add('food')
    assert gratitudes.format() == 'Be grateful for: family, friends, food'