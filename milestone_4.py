import random

class Hangman:
    
    def __init__(self, word_list, num_lives=5): # instance attributes of the Hangman game class
        self.word_list = word_list
        self.num_lives = num_lives
    
    word = random.choice(word_list) # class attributes of the Hangman game class
    word_guessed = ["_" for letter in word]
    num_letters = len(word)
    list_of_guesses = []
    
    def check_guess(self, guess): # method checks input 
        guess.lower()
        if guess in word:
            print(f"Good guess! {guess} is in the word.")
            for letter in word:
                if letter == guess:
                    self.word_guessed[word.index(letter)] = guess
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
            elif guess in list_of_guesses:
                print("You already tried that letter!")
            else:
                check_guess(guess)
                list_of_guesses.append(guess)