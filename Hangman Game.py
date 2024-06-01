import random

def play_guessing_game():
  randomNumber = random.randint(1, 100)
  userGuess = None
  guesses = 0

  while userGuess != randomNumber:
    userGuess = int(input("Enter your guess (between 1 and 100): "))
    guesses += 1

    if userGuess == randomNumber:
      print(f"You guessed it right in {guesses} tries!")
    elif userGuess < randomNumber:
      print("Your guess is too low. Try again.")
    else:
      print("Your guess is too high. Try again.")

  return guesses  


guesses = play_guessing_game()


try:
  with open("highscore.txt", "r") as f:
    highscore = int(f.read())
except FileNotFoundError:
  print("No high score file found. You're setting the new high score!")
  highscore = 0  


if guesses < highscore:
  print("You have just broken the legal high score!")
  
  with open("highscore.txt", "w") as f:
    f.write(str(guesses))  
else:
  print(f"Your score of {guesses} is not enough to beat the high score of {highscore}.")

print("Thanks for playing!")

  