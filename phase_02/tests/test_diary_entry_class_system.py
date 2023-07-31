from lib.diary_entry_class_system import DiaryEntry
import pytest


"""
Test that diary entry when initialised has a title and a contents
"""

def test_adds_title_and_contents_when_initialised():
    diary_entry1 = DiaryEntry("Title", "Contents.....")
    assert diary_entry1.title == "Title"
    assert diary_entry1.contents == "Contents....."

"""
Test Count Words
"""

def test_count_words():
    diary_entry1 = DiaryEntry("Title", "Contents.....")
    assert diary_entry1.count_words() == 1

def test_count_words_for_multiple_words():
    diary_entry1 = DiaryEntry("Title", "This is my diary entry number 1")
    assert diary_entry1.count_words() == 7

"""
Test empty title should raise an error
"""

def test_empty_title_raises_error():
    with pytest.raises(Exception) as e:
        diary_entry1 = DiaryEntry("", "This is my diary entry number 1")
    assert str(e.value) == "No Title Given"

def test_empty_contents_raises_error(): 
    with pytest.raises(Exception) as e:
        diary_entry2 = DiaryEntry("Title", "")
    assert str(e.value) == "No Contents Given" 

"""
Test for if reading_time wpm argument is 0, raise an Exception
"""       

def test_reading_time_wpm_0_raises_error():
    diary_entry1 = DiaryEntry("My Title", "This is a diary entry that is longer to test the wpm count for this method")
    with pytest.raises(Exception) as e:
        diary_entry1.reading_time(0)
    assert str(e.value) == "Wpm cannot be 0"

#16

"""
Test Reading time works as expected
"""

def test_reading_time_works_as_expected():
    diary_entry1 = DiaryEntry("My Title", "This is a diary entry that is longer to test the wpm count for this method")
    assert diary_entry1.reading_time(16) == 1
    assert diary_entry1.reading_time(8) == 2


"""
Test Read
"""

def test_read_entry_in_one():
    diary_entry1 = DiaryEntry("My Title", "This is a diary entry that is longer to test the wpm count for this method")
    assert diary_entry1.reading_chunk(8, 2) == "This is a diary entry that is longer to test the wpm count for this method"

"""
Test where we cannot read whole contents in one go
"""

def test_read_entry_in_two_chunks():
    diary_entry1 = DiaryEntry("My Title", "This is a diary entry that is longer to test the wpm count for this method")
    assert diary_entry1.reading_chunk(4, 2) == "This is a diary entry that is longer"
    assert diary_entry1.reading_chunk(4, 2) == "to test the wpm count for this method"

"""
Test that after second chunk providing contents is fully read, goes back to beginning
"""

def test_read_from_beginning():
    diary_entry1 = DiaryEntry("My Title", "This is a diary entry that is longer to test the wpm count for this method")
    diary_entry1.reading_chunk(4, 2)
    diary_entry1.reading_chunk(4, 2)
    assert diary_entry1.reading_chunk(4, 2) == "This is a diary entry that is longer"