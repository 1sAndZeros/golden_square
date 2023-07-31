from lib.diary_entry_class_system import DiaryEntry
from lib.diary import Diary
import pytest

# Test that diary is initialised correctly with a valid entry
def test_add_one_diary_entry():
    my_diary = Diary()
    entry_1 = DiaryEntry('My Title', 'These are the contents of my diary entry...')
    my_diary.add(entry_1)
    assert my_diary.entries == [entry_1]

# Test that multiple diary entries are added correctly
def test_add_multiple_entries():
    my_diary = Diary()
    entry_1 = DiaryEntry('My Title', 'These are the contents of my diary entry...')
    entry_2 = DiaryEntry('My Sequel', 'These are the contents of my second diary entry.')
    my_diary.add(entry_1)
    my_diary.add(entry_2)
    assert my_diary.entries == [entry_1, entry_2]

# Test that when diary entries are added they are returned when calling all
def test_display_all():
    my_diary = Diary()
    entry_1 = DiaryEntry('My Title', 'These are the contents of my diary entry...')
    entry_2 = DiaryEntry('My Sequel', 'These are the contents of my second diary entry.')
    my_diary.add(entry_1)
    my_diary.add(entry_2)
    assert my_diary.all() == [entry_1, entry_2]

'''
Test when there are no entires, a message indicates
this when the all method is called
'''
def test_no_entries_when_calling_all():
    my_diary = Diary()
    assert my_diary.all() == 'There are no entries in this diary'

'''
When count words is called,
method should return total number of words
in all diary entries
'''
def test_count_words():
    my_diary = Diary()
    entry_1 = DiaryEntry('My Title', 'These are the contents of my diary entry...')
    entry_2 = DiaryEntry('My Sequel', 'These are the contents of my second diary entry.')
    my_diary.add(entry_1)
    my_diary.add(entry_2)
    assert my_diary.count_words() == 17

'''
Test count words method when there are no entires
should return zero
'''
def test_count_words_with_no_entries():
    my_diary = Diary()
    assert my_diary.count_words() == 0

'''
Check reading time works as expected
Calculates how long to read all entries when given wpm
'''
def test_reading_time():
    my_diary = Diary()
    entry_1 = DiaryEntry('My Title', 'These are the contents of my diary entry...')
    entry_2 = DiaryEntry('My Sequel', 'These are the contents of my second diary entry.')
    my_diary.add(entry_1)
    my_diary.add(entry_2)
    assert my_diary.reading_time(17) == 1

# Test reading time rounds correctly, both up and down
def test_reading_time_rounding():
    my_diary = Diary()
    entry_1 = DiaryEntry('My Title', 'These are the contents of my diary entry...')
    entry_2 = DiaryEntry('My Sequel', 'These are the contents of my second diary entry.')
    my_diary.add(entry_1)
    my_diary.add(entry_2)
    assert my_diary.reading_time(8) == 2
    assert my_diary.reading_time(10) == 2
    assert my_diary.reading_time(100) == 1

'''
If there are no entries,
reading time should return an Exception
'''
def test_reading_time_with_no_entries():
    my_diary = Diary()
    with pytest.raises(Exception) as e:
        assert my_diary.reading_time(8)
    error_message = str(e.value)
    assert error_message == 'Cannot calculate reading time without any entries'

'''
Check that the single entry in the diary
is returned when find best entry is called
'''
def test_find_best_entry_one_entry():
    my_diary = Diary()
    entry_1 = DiaryEntry('My Title', 'These are the contents of my diary entry...')
    my_diary.add(entry_1)
    assert my_diary.find_best_entry_for_reading_time(20, 50) == entry_1

# Find best entry to read when given multiple entries
def test_find_best_entry_two_entries():
    my_diary = Diary()
    entry_1 = DiaryEntry('My Title', 'These are the contents of my diary entry...')
    entry_2 = DiaryEntry('My Sequel', 'These are the contents of my second diary entry. This entry has more words than entry one')
    my_diary.add(entry_1)
    my_diary.add(entry_2)
    assert my_diary.find_best_entry_for_reading_time(20, 50) == entry_2

# Find best entry to read when given,
# same entries above but swapped
def test_find_best_entry_two_entries_swapped():
    my_diary = Diary()
    entry_2 = DiaryEntry('My Sequel', 'These are the contents of my second diary entry. This entry has more words than entry one')
    entry_1 = DiaryEntry('My Title', 'These are the contents of my diary entry...')
    my_diary.add(entry_2)
    my_diary.add(entry_1)
    assert my_diary.find_best_entry_for_reading_time(20, 50) == entry_2

'''
Add multiple entries with various lengths
Return the entry closest to the time you have to read
without the entry word count going over
This means you can read the entire entry within the timeframe
'''
def test_find_best_entry_multiple_entries():
    my_diary = Diary()
    entry_1 = DiaryEntry('My Title', 'These are the contents of my diary entry...')
    entry_2 = DiaryEntry('Longest Entry', 'These are the contents of my diary entry. This entry has more words than every other entry in my diary')
    entry_3 = DiaryEntry('Short Entry', 'Entry contents here')
    entry_4 = DiaryEntry('Another Entry', 'Another entry added to the diary')
    my_diary.add(entry_1)
    my_diary.add(entry_2)
    my_diary.add(entry_3)
    my_diary.add(entry_4)
    assert my_diary.find_best_entry_for_reading_time(20, 50) == entry_2

'''
If the reading time is not long enough to read any entry
return a message indicating this
'''
def test_find_best_entry_short_reading_time():
    my_diary = Diary()
    entry_1 = DiaryEntry('My Title', 'These are the contents of my diary entry...')
    entry_2 = DiaryEntry('Longest Entry', 'These are the contents of my diary entry. This entry has more words than every other entry in my diary')
    entry_3 = DiaryEntry('Short Entry', 'Entry contents here')
    entry_4 = DiaryEntry('Another Entry', 'Another entry added to the diary')
    my_diary.add(entry_1)
    my_diary.add(entry_2)
    my_diary.add(entry_3)
    my_diary.add(entry_4)
    assert my_diary.find_best_entry_for_reading_time(1, 2) == 'There are no entries short enough for you to read'

# Test best entry method when no entries exist
def test_find_best_entry_with_no_entries():
    my_diary = Diary()
    with pytest.raises(Exception) as e:
        assert my_diary.find_best_entry_for_reading_time(10, 20)
    error_message = str(e.value)
    assert error_message == 'Cannot find entry to read without any entries'
