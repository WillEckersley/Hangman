# Hangman
My build of the classic game "Hangman".

### Description
Hangman is a classic game where the player tries to discover a mystery word using a mixture of guesswork and deduction. The game begins with the player being presented with a series of dashes:

Each dash represents a letter in the unknown word. The player then has a predetermined number of chances (lives) to suggest letters that might be in the word.  In this version of the game, the player has 10 lives. 

If the player suggests a letter that appears in the word, two things happen. First, a message of congratulation is printed. Second, the position(s) occupied by the letters in the word are updated from '_' to the successful suggestion. 

If the player guesses a letter that appears more than once in the word, e.g. 'apple' where the letter 'p' appears twice, then every position occupied by that letter in the word is filled in. The player does not have to guess the same letter more than once to confirm that it does not reappeaer in the word.   

 If the player suggests a letter that is not in the word, a message of comiseration is printed. 

 If the player successfuly discovers every letter that appears in the word 
