from lib.music_tracker import *
import pytest

def test_add_track():
    track_list = MusicTracker()
    track_list.add('Three little birds')
    assert track_list.tracks == ['Three little birds']

def test_add_existing_track():
    track_list = MusicTracker()
    track_list.add('Three little birds')
    with pytest.raises(Exception) as error:
        track_list.add('Three little birds')
    error_message = str(error.value)
    assert error_message == 'Track already exists in list'

def test_display_tracklist():
    track_list = MusicTracker()
    track_list.add('Three little birds')
    track_list.add('Billie Jean')
    assert track_list.display_tracklist() == ['Three little birds', 'Billie Jean']

def test_display_empty_tracklist():
    track_list = MusicTracker()
    assert track_list.display_tracklist() == 'Tracklist is empty'

def test_adding_empty_trackname():
    track_list = MusicTracker()
    with pytest.raises(Exception) as error:
        track_list.add('')
    error_message = str(error.value)
    assert error_message == 'Please enter a trackname'