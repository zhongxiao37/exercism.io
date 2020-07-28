# Game status categories
# Change the values as you see fit
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman(object):
    def __init__(self, word):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.word = list(word)
        self.masked_word = list(map(lambda x: '_', list(self.word)))

    def guess(self, char):
        if self.remaining_guesses < 0 or self.status == STATUS_WIN:
            raise ValueError('No remaining guesses')
        
        guess_result = False
        for i in range(len(self.word)):
            if char == self.word[i] and self.masked_word[i] == '_':
                self.masked_word[i] = char
                guess_result = True
        
        if not any(x == '_' for x in self.masked_word):
            self.status = STATUS_WIN

        if not guess_result:
            self.remaining_guesses -= 1

        if self.remaining_guesses == 0 and self.status == STATUS_ONGOING:
            self.status = STATUS_LOSE
        pass

    def get_masked_word(self):
        return ''.join(self.masked_word)

    def get_status(self):
        return self.status
