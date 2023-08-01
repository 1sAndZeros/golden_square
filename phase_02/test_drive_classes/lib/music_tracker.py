class MusicTracker:
    def __init__(self):
        self.tracks = []
    
    def add(self, track_name):
        if track_name in self.tracks:
            raise Exception('Track already exists in list')
        elif track_name == '':
            raise Exception('Please enter a trackname')
        self.tracks.append(track_name)
    
    def display_tracklist(self):
        if len(self.tracks) == 0:
            return 'Tracklist is empty'
        return self.tracks