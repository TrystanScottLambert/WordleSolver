"""Wordle Solver."""
import string
import numpy as np



def generate_all_words():
    """Get the all the 5 letter words of the english language."""

    with open("word.txt") as file:
        words = [
            line.lower().split('\n')[0]  for line in file if len(line) == 6 and "'" not in line]
    return np.array(words)

def _evaluate_guess(guess_word, target_word):
    """Compare the guess to the known word.

    This will be down by the website itself
    """
    results = np.zeros(5)
    for i, letter in enumerate(guess_word):
        result = target_word.find(letter)
        if result == -1:
            results[i] = 0
        elif result == i:
            results[i] = 2
        else:
            results[i] = 1
    return results

def find_letter_pattern(letters, wordlist):
    """Return words that only have those letters."""
    new_wordlist = []
    for word in wordlist:
        in_word = True
        for letter in letters:
            if letter not in word:
                in_word = False
        if in_word is True:
            new_wordlist.append(word)

    return np.array(new_wordlist)


class CurrentGuess():
    """Main class of the program."""
    available_words = generate_all_words()
    must_use_letters = []

    permutations = {
    1: list(string.ascii_lowercase),
    2: list(string.ascii_lowercase),
    3: list(string.ascii_lowercase),
    4: list(string.ascii_lowercase),
    5: list(string.ascii_lowercase)
    }

    def __init__(self, word, result):
        self.word = word
        self.result = result
        self.update_permutations()
        self.remove_permutations()
        self.find_must_use()
        self.make_new_guess()

    def update_permutations(self):
        """Update each possible letter for each position."""
        for i, feedback in enumerate(self.result):
            if feedback == 0:
                for j in range(1,6):
                    try:
                        CurrentGuess.permutations[j].remove(self.word[i])
                    except ValueError:
                        pass

            if feedback == 1:
                try:
                    CurrentGuess.must_use_letters.append(self.word[i])
                    CurrentGuess.permutations[i+1].remove(self.word[i])
                except ValueError:
                    pass

            if feedback == 2:
                CurrentGuess.must_use_letters.append(self.word[i])
                CurrentGuess.permutations[i+1] = [self.word[i]]


    def find_must_use(self):
        """Find all words which have all of the must use letters in them."""
        CurrentGuess.available_words = find_letter_pattern(
            CurrentGuess.must_use_letters, CurrentGuess.available_words)

    def remove_permutations(self):
        """Find all words which are within the allowable permutations"""
        new_words = []
        for word in CurrentGuess.available_words:
            good_word = True
            for i in range(5):
                if word[i] not in CurrentGuess.permutations[i+1]:
                    good_word = False
            if good_word is True:
                new_words.append(word)
        CurrentGuess.available_words = np.array(new_words)


    def make_new_guess(self):
        """Make the new guess"""
        print(CurrentGuess.available_words)
        new_guess = np.random.choice(CurrentGuess.available_words)
        self.new_guess = new_guess

if __name__ == '__main__':
    TARGET = 'float'
    WORD = 'crate'
    result = _evaluate_guess(WORD, TARGET)
    for i in range(5):
        guess = CurrentGuess(WORD, result)
        WORD = guess.new_guess
        result = _evaluate_guess(WORD, TARGET)
