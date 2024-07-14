**Guess the Number - Python Project**
--------------------

Introduction

This Python project implements a fun and engaging "Guess the Number" game. The program generates a random number between 1 and 100, and you (the user) have to guess it within the least number of attempts.

Features

- Random number generation between 1 and 100 (inclusive).
- User input for guessing the number.
- Hints for guesses being too high or too low.
- Tracks the number of guesses.
- Saves a high score in a file (`highscore.txt`).
- Challenges the user to beat the high score.

**New Feature: Now Includes Executable File!**

This project now includes an executable file (`guess_the_number.exe`) for easy use on Windows. Simply download and run `guess_the_number.exe` to start playing immediately without needing Python installed.

Getting Started

1. **Download the Executable:**
   - Download `guess_the_number.exe` from the repository.
   
2. **Run the Executable:**
   - Double-click `guess_the_number.exe` to launch the game.

Gameplay

The program will greet you and ask you to enter your guesses. As you guess, the program will provide hints:

- "Your guess is too low. Try again." (if your guess is lower than the number)
- "Your guess is too high. Try again." (if your guess is higher than the number)

High Score

The game keeps track of the least number of guesses it took you to guess the number correctly. This becomes the new high score if it's lower than the previously saved high score.

Further Development

- **Difficulty Levels:** Implement different difficulty levels where the number range changes (e.g., Easy: 1-50, Medium: 1-100, Hard: 1-200).
- **Multiple Chances:** Allow a certain number of guesses per round before the game ends.
- **Number Range Customization:** Let users define the minimum and maximum values for the random number generation.
- **Graphical User Interface (GUI):** Consider creating a graphical interface for a more interactive experience.

Example Interaction

Enter your guess (between 1 and 100): 50  
Your guess is too low. Try again.  
Enter your guess (between 1 and 100): 75  
Your guess is too high. Try again.  
Enter your guess (between 1 and 100): 63  
You guessed it right in 3 tries! You have just broken the legal high score!

Thanks for playing!

---

This format should clearly indicate to users that they can now use the `.exe` file for a simpler and more accessible gameplay experience on Windows.
