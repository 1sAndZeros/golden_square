from lib.diary_entry_class_system import DiaryEntry

class Diary:
    # Public properties:
    #   entries: a list of DiaryEntry instances representing entries
    def __init__(self):
        self.entries = []

    def add(self, entry: DiaryEntry):
        # Parameters:
        #   entry: an instance of DiaryEntry
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the entry to the entries list
        self.entries.append(entry)

    def all(self):
        # Returns:
        #   A list of instances of DiaryEntry
        if len(self.entries) == 0:
            return 'There are no entries in this diary'
        return self.entries

    def count_words(self):
        # Returns:
        #   An integer representing the number of words in all diary entries
        # HINT:
        #   This method should make use of the `count_words` method on DiaryEntry.
        return sum([entry.count_words() for entry in self.entries])

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   if the user were to read all entries in the diary.
        if len(self.entries) == 0:
            raise Exception('Cannot calculate reading time without any entries')
        reading_time = round(self.count_words() / wpm)
        return 1 if reading_time == 0 else reading_time

    def find_best_entry_for_reading_time(self, wpm, minutes):
        # Parameters:
        #   wpm:     an integer representing the number of words the user can
        #            read per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   An instance of DiaryEntry representing the entry that is closest to,
        #   but not over, the length that the user could read in the minutes
        #   they have available given their reading speed.
        words_that_can_be_read = wpm * minutes
        if self.entries == []:
            raise Exception('Cannot find entry to read without any entries')
        entry_to_read = self.entries[0]
        for entry in self.entries:
            if entry.count_words() <= words_that_can_be_read:
                if entry.count_words() > entry_to_read.count_words():
                    entry_to_read = entry
        if entry_to_read.count_words() > words_that_can_be_read:
            return 'There are no entries short enough for you to read'
        else:
            return entry_to_read