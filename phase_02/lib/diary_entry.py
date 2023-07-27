class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        self.words_read = 0
    def format(self):
        return f"{self.title}: {self.contents}"
    def count_words(self):
        words = self.contents.split(" ")
        return len(words)
    def reading_time(self, wpm):
        return int(self.count_words() / wpm)

    def reading_chunk(self, wpm, minutes):
        no_of_words_we_can_read = wpm * minutes
        chunk = self.contents.split()[self.words_read:self.words_read + no_of_words_we_can_read]
        self.words_read += no_of_words_we_can_read
        if self.words_read > self.count_words():
            self.words_read = 0
        return ' '.join(chunk)

