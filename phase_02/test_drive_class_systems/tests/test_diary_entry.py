from lib.diary_entry import *

def test_create_object():
    diary_entry = DiaryEntry("title", "contents")
    assert diary_entry.title == "title"
    assert diary_entry.contents == "contents"
def test_format():
    diary_entry = DiaryEntry("title", "contents")
    assert diary_entry.format() == "title: contents"
def test_count_words():
    diary_entry = DiaryEntry("title", "contents")
    num_words = diary_entry.count_words()
    assert num_words == 1
def test_reading_time():
    words_200 = " ".join(['hello' for word in range(0, 200)])
    diary_entry = DiaryEntry("title", words_200)
    result = diary_entry.reading_time(200)
    assert result == 1
def test_reading_whole_chunk():
    diary_entry = DiaryEntry("title", "these are the contents of the book")
    chunk = diary_entry.reading_chunk(2, 5)
    assert chunk == "these are the contents of the book"

def test_reading_two_chunks():
    diary_entry = DiaryEntry("title", "these are the contents of the book")
    chunk = diary_entry.reading_chunk(1, 2)
    assert chunk == "these are"
    chunk2 = diary_entry.reading_chunk(1, 2)
    assert chunk2 == "the contents"

def test_reading_entire_contents_in_chunks():
    diary_entry = DiaryEntry("title", "these are the contents of the book")
    chunk = diary_entry.reading_chunk(1, 4)
    assert chunk == "these are the contents"
    chunk2 = diary_entry.reading_chunk(1, 100)
    assert chunk2 == "of the book"

def test_reading_contents_again():
    diary_entry = DiaryEntry("title", "these are the contents of the book")
    chunk = diary_entry.reading_chunk(1, 4)
    assert chunk == "these are the contents"
    chunk2 = diary_entry.reading_chunk(1, 1000000)
    assert chunk2 == "of the book"
    chunk3 = diary_entry.reading_chunk(1, 5)
    assert chunk3 == "these are the contents of"