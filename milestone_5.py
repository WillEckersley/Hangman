import random

class Hangman:
    
    def __init__(self, word_list, num_lives=5): # instance attributes of the Hangman game class. 
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list)
        self.word_guessed = ["_" for letter in self.word]
        self.list_of_guesses = []
        self.word_guessed_string = ""
    
    def check_guess(self, guess): # method checks input 
        guess.lower()
        if guess in self.word:
            self.list_of_guesses.append(guess)
            for index, letter in enumerate(self.word): # allows iteration through indexes, facilitating the addition of repeated letters to the guessed list. 
                if letter == guess:
                    self.word_guessed[index] = guess # if guessed letter is in input word, match the value of that letter to the index it has in the original input word in the guessed list. 
                    self.word_guessed_string.join([str(char) for char in self.word_guessed]) # string version of the guessed list to compare against original word. Used to trigger win condition when equal to input word. 
                    print(f"\nGood guess! {guess} is in the word.") # use of '\n' to facilitated better output formatting. 
                    print(f"Word:{self.word_guessed}")
                    print(f"Letters tried: {self.list_of_guesses}")
        else:
            self.num_lives -= 1
            self.list_of_guesses.append(guess)
            print(f"\nSorry, {guess} is not in the word.") # use of '\n' to facilitated better output formatting. 
            print(f"Letters tried: {self.list_of_guesses}")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self): # method requests input and checks validity.
        while True:
            guess = input("Please enter a letter:")
            if not guess.isalpha() or len(guess) != 1:
                print("Invalid character. Please enter a single aphabetical character.")
                break
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
                break
            else:
                self.check_guess(guess)
                break

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print("\nYou lost!")
            print(f"The word was: {game.word}")
            break
        elif game.num_lives > 0 and game.word != game.word_guessed_string: # alternative conditionals to previous versions checks input word against developing string version of input word created at line 20.
            game.ask_for_input()
        elif game.word == game.word_guessed_string:
            print("Congratulations, you've won!")
            break

play_game(["apple", "banana", "cherry", "damson", "tangerine", "blueberry", "strawberry", "grape", "melon", "lemon", "blackcurrent", "redcurrent", "orange", "blackberry", "lychee"]) # test the code multiple words.