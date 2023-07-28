class VowelRemover:
    def __init__(self, text):
        self.text = text
        self.vowels = ["a", "e", "i", "o", "u"]
        self.vowels_removed = ''

    def remove_vowels(self):
        i = 0
        while i < len(self.text):
            if self.text[i].lower() not in self.vowels:
                self.vowels_removed += self.text[i]
            i += 1
        return self.vowels_removed