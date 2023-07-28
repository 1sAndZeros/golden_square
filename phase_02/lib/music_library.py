class MusicLibrary:
    def __init__(self) -> None:
        self.tracks = []

    def add(self, track) -> None:
        self.tracks.append(track)

    def all(self) -> list:
        return self.tracks

    def search_by_title(self, keyword):
        return [track for track in self.tracks if keyword in track.title]
        res = []
        for track in self.tracks:
            if keyword in track.title:
                res.append(track)
        return res


class Track:
    def __init__(self, title, artist) -> None:
        self.title = title
        self.artist = artist
    
    def format(self):
        return f"{self.title} by {self.artist}"
    