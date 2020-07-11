# Write your code here
import random
from string import ascii_lowercase


class HangmanGame:
    def __init__(self):
        self.tries = 8
        self.words = ['python', 'java', 'kotlin', 'javascript']
        self.word = ''
        self.letters = set()
        self.i_letters = set()
        self.win = False

    def get_word(self, words_list):
        random.seed()
        self.word = words_list[random.randint(0, len(words_list) - 1)]

    def get_letter(self):
        while True:
            inp = input('Input a letter: ')
            if len(inp) != 1:
                print('You should input a single letter\n')
            elif inp not in ascii_lowercase:
                print('It is not an ASCII lowercase letter\n')
            elif inp in self.i_letters:
                print('You already typed this letter\n')
            else:
                break
            print(self.secret_word())
        return inp

    def check_letter(self):
        letter = self.get_letter()
        if letter not in self.i_letters:
            self.i_letters.update(letter)
            if letter not in self.letters:
                print('No such letter in the word')
                return False
            return True

    def secret_word(self):
        str_ = ''
        for w in self.word:
            if w in self.i_letters:
                str_ += w
            else:
                str_ += '-'
        return str_

    def start_game(self):
        print('H A N G M A N')
        while True:
            u_input = input('Type "play" to play the game, "exit" to quit: ')
            if u_input == 'play':
                self.restart()
                self.game()
            elif u_input == 'exit':
                break

    def restart(self):
        self.word = ''
        self.letters = set()
        self.i_letters = set()
        self.win = False

    def game(self):
        self.get_word(self.words)
        self.letters = set(self.word)
        n = 0

        while n < self.tries:
            print('\n' + self.secret_word())
            if not self.check_letter():
                n += 1
            if self.secret_word() == self.word:
                self.win = True
                break
        if self.win:
            print('You guessed the word {}!'.format(self.word))
            print('You survived!\n')
        else:
            print('You are hanged!\n')


hangman = HangmanGame()
hangman.start_game()
