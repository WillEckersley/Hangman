import random

class Hangman:
    
    def __init__(self, word_list, num_lives=5): # instance attributes of the Hangman game class
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list) 
        self.word_guessed = ["_" for letter in self.word]
        self.num_letters = len(self.word)
        self.list_of_guesses = []
    
    
    def check_guess(self, guess): # method checks input 
        guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for letter in self.word:
                if letter == guess:
                    self.word_guessed[self.word.index(letter)] = guess
            self.num_letters -= 1 
        else:
            num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self): # method requests input and checks validity
        while True:
            guess = input("Please enter a letter:")
            if not guess.isalpha() and len(guess) == 1:
                print("Invalid character. Please enter a single aphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if num_lives == 0:
            print("You lost!")
        elif num_lives > 0:
            game.ask_for_input()
        elif num_lives > 0 and not game.num_letters > 0:
            print("Congratulations, you've won!")

play_game(["apple"])



