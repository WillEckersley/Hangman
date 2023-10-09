word = "Strawberries" # using a temporary variable to test output. 

def ask_for_input(): # checking the input is a single aphabetical character.
    while True:
        guess = input("Please enter a letter:")
        if len(guess) == 1 and guess.isalpha():
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(guess) 

def check_guess(guess): # checking if the character entered is in the word. 
    guess.lower()
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

ask_for_input()