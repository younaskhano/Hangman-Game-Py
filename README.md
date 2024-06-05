# CodeAlpha_Hangman_Game
This Python-based Hangman game selects a random word and reveals three letters. Players guess the remaining letters one at a time, with up to 6 incorrect guesses allowed. 
The goal is to complete the word before running out of guesses.

## Guess the Number - Python Project
### Introduction ###
This Python project implements a fun and engaging "Guess the Number" game. The program generates a random number between 1 and 100, and you (the user) have to guess it within the least number of attempts.

### Features 
- Random number generation between 1 and 100 (inclusive).
- User input for guessing the number.
- Hints for guesses being too high or too low.
- Tracks the number of guesses.
- Saves a high score in a file (highscore.txt).
- Challenges the user to beat the high score.

### Getting Started
1. *Save the Code:* Copy and paste the provided code into a new Python file (e.g., guess_the_number.py).
2. *Run the Script:*
   - Open a terminal or command prompt and navigate to the directory where you saved the file.
   - Execute the Python script using: python guess_the_number.py

### Gameplay
The program will greet you and ask you to enter your guesses. As you guess, the program will provide hints:
- "Your guess is too low. Try again." (if your guess is lower than the number)
- "Your guess is too high. Try again." (if your guess is higher than the number)

### High Score
- The game keeps track of the least number of guesses it took you to guess the number correctly. This becomes the new high score if it's lower than the previously saved high score.
- The high score is stored in a file named highscore.txt in the same directory as your Python script.
- If there's no existing high score file, the game will create one and set your current score as the initial high score.

### Example Interaction
Enter your guess (between 1 and 100): 50
Your guess is too low. Try again.
Enter your guess (between 1 and 100): 75
Your guess is too high. Try again.
Enter your guess (between 1 and 100): 63
You guessed it right in 3 tries!
You have just broken the legal high score!

#### *Thanks for playing!*

### Further Development
- *Difficulty Levels: Implement different difficulty levels where the number range changes (e.g., Easy: 1-50, Medium: 1-100, Hard: 1-200).*
- *Multiple Chances: Allow a certain number of guesses per round before the game ends.*
- *Number Range Customization: Let users define the minimum and maximum values for the random number generation.*
- *Graphical User Interface (GUI): Create a graphical interface for a more interactive experience.*
