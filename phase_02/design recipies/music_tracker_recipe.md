# Music Tracker Class Design Recipe

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class MusicTracker:
    # User-facing properties:
    #   None

    def __init__(self):
        self.tracks = []
        pass # No code here yet

    def add_track(self, track_name):
        # Parameters:
        #   track_name: string representing a track
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the track to the tracks list
        pass # No code here yet

    def display_tracklist(self):
        # Returns:
        #   A list of the tracks
        # Return a message if no tracks exist in list
        pass # No code here yet
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Given a trackname, add the track to the list
"""
track_list = MusicTracker()
track_list.add('Three little birds')
track_list.tracks = ['Three little birds']

"""
Given a trackname that already exists
raise an exception saying 'Track already exists in list'
"""
track_list = MusicTracker()
track_list.add('Three little birds')
track_list.add('Three little birds') -> Exception('Track already exists in list')

"""
When display_tracklist is called
Return list of tracks
"""
track_list = MusicTracker()
track_list.add('Three little birds')
track_list.add('Billie Jean')
track_list.display_tracklist() -> ['Three little birds', 'Billie Jean']
```

"""
When display_tracklist is called on an empty list
return message saying 'Tracklist is empty'

track_list = MusicTracker()
track_list.display_tracklist() -> 'Tracklist is empty'

When an empty string is added through add method
Raise exception saying 'Please enter a trackname'

track_list = MusicTracker()
track_list.add('') -> Exception('Please enter a trackname')
