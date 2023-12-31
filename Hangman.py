from wonderwords import RandomWord # Library that randomly generates words using .word() function. See line 60-1 for implementation. 


class Hangman:
    

    def __init__(self, word, num_lives=10): 
        self.num_lives = num_lives
        self.word = word
        self.word_guessed = ["_" for letter in self.word]
        self.list_of_guesses = []
        self.word_guessed_string = ""
    
    def check_guess(self, guess):
        """Checks the guess made by the player.

        Args:
            guess (str): a letter inputted by the player. 

        Returns:
            none
        """
        guess.lower()
        if guess in self.word:
            self.list_of_guesses.append(guess)
            for index, letter in enumerate(self.word): # allows iteration through indexes, facilitating the addition of repeated letters to the guessed list. 
                if letter == guess:
                    self.word_guessed[index] = guess # if guessed letter is in input word, match the value of that letter to the index it has in the original input word in the guessed list. 
                    self.word_guessed_string = "".join([str(char) for char in self.word_guessed]) # string version of the guessed list to compare against original word. Used to trigger win condition when equal to input word in line 53. 
            print(f"\nGood guess! {guess} is in the word.") 
            print(f"Word:{self.word_guessed}") 
        else:
            self.num_lives -= 1
            self.list_of_guesses.append(guess)
            print(f"\nSorry, {guess} is not in the word.") 
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self): 
        """Requests input and checks input validity.

        Args:
            none
        
        Returns: 
            none
        """
        while True:
            guess = input("\nPlease enter a letter:")
            if not guess.isalpha() or len(guess) != 1: # if the guess is a non-aphabetical character or longer than one charchter, retrun the error message in line 32.
                print("\nInvalid character. Please enter a single aphabetical character.")
                break
            elif guess in self.list_of_guesses:
                print("\nYou already tried that letter!")
                break
            else:
                self.check_guess(guess)
                break


def play_game(word):
    num_lives = 10
    game = Hangman(word, num_lives)
    count = 1
    while count >= 1:
        print(f"\nWord:{game.word_guessed}")
        count -= 1
    while True:
        if game.num_lives == 0:
            print("\nYou lost!")
            print(f"The word was: {game.word}")
            break
        elif game.num_lives > 0 and game.word != game.word_guessed_string: # alternative conditionals to previous versions checks input word against developing string version of input word created at line 20.
            game.ask_for_input()
        elif game.word == game.word_guessed_string:
            print("\nCongratulations, you've won!")
            print(f"The word was: {game.word_guessed_string}")
            break

random_word = RandomWord() # code used to generate any random word from wonderwords library.
word = random_word.word()

play_game(word)