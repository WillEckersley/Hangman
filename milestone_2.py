import random

words_list = ["apple", "banana", "cherry", "damson", "melon"]
print(words_list)

word = random.choice(words_list)
print(word)

guess = input("Please guess a character:")

if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else: 
    print("Oops! That is not a valid input. Please enter a single character.")
