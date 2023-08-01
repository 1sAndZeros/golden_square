class GrammarStats:
    def __init__(self):
        self.num_good = 0
        self.num_bad = 0

    def check(self, text):
        if text == "":
            self.num_bad += 1
            return False
        else:
            if text[0].isupper() and (text[-1] == "." or text[-1] == "!"):
                self.num_good += 1
                return True
            else:
                self.num_bad += 1
                return False

    def percentage_good(self):
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
        return int((self.num_good / (self.num_good + self.num_bad))*100)
        