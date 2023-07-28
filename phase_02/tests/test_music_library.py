from lib.music_library import *

# These are the unit tests, which test the individual classes, functions, methods etc.

# Test initially there are no tracks
def test_initially_no_tracks():
    music_library = MusicLibrary()
    assert music_library.all() == []

# Search by title with no results gets an empty list
def test_initial_search_returns_empty():
    music_library = MusicLibrary()
    assert music_library.search_by_title('hello') == []

def test_formats_title_and_artist():
    song = Track('Opus', 'Eric Prydz')
    assert song.format() == 'Opus by Eric Prydz'

# These are integration tests that check the class systems works together

# Given I add 2 tracks, I can see them represented in the list
def test_adds_multiple_tracks_and_lists_them():
    music_library = MusicLibrary()
    song1 = Track('Sun and Moon', 'Above and Beyond')
    song2 = Track('Opus', 'Eric Prydz')
    music_library.add(song1)
    music_library.add(song2)
    assert music_library.all() == [song1, song2]

# Given I add 2 tracks, if I search for a title, I get the tracks returned
def test_searches_by_title():
    music_library = MusicLibrary()
    song1 = Track('Sun and Moon', 'Above and Beyond')
    song2 = Track('Opus', 'Eric Prydz')
    music_library.add(song1)
    music_library.add(song2)
    assert music_library.search_by_title('Opus') == [song2]

# Given I add two tracks, if I search for part of title, I get back list of matching tracks
def test_searches_by__part_of_title():
    music_library = MusicLibrary()
    song1 = Track('Sun and Moon', 'Above and Beyond')
    song2 = Track('Opus', 'Eric Prydz')
    music_library.add(song1)
    music_library.add(song2)
    assert music_library.search_by_title('Moon') == [song1]