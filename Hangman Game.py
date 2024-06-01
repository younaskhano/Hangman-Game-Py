import random # Here we use "import random" and this module is use for selecting a random word in the given program.

def get_random_word():
    words = ['python', 'hangman', 'programming', 'computer', 'developer', 'algorithm'] # This is the list of possible words to be selected by the computer to be guess. 
    return random.choice(words) # And then return a randomly choosen word from the above given list.

def display_current_state(word, guessed_letters):
    display_word = ''.join([letter if letter in guessed_letters else '_' for letter in word]) # Create a string showing guessed letters in their correct positions and underscores for remaining letters
    print("Current word: ", display_word)

def hangman():
    word = get_random_word() # This will select a random word for the game
    guessed_letters = set() # This line of code will initialize an empty set to store guessed letters
    incorrect_guesses = 0 # This will act as a counter for incorrect guesses
    max_incorrect_guesses = 6 # Maximum number of allowed incorrect guesses
    
    print("Welcome to the Hangman Game!")
    print("Guess the word by picking one letter at a time.")
    print(f"You can make {max_incorrect_guesses} incorrect guesses.")
    
    while incorrect_guesses < max_incorrect_guesses: # This is the Loop until the player runs out of guesses
        display_current_state(word, guessed_letters) # Here we can display the current state of the word
        guess = input("Guess a letter: ").lower() # Here the player to guess a letter and itself it will convert it to lowercase
        
        if guess in guessed_letters: # This will check if the letter has already been guessed
            print("You guessed that already. Try a different letter.")   # This will inform the player and continue the loop
            continue
        
        guessed_letters.add(guess) # This will add the guessed letter to the set of guessed letters
        
        if guess in word: # This line of code will check if the guessed letter is in the word
            print(f"Good guess! '{guess}' is in the word.")
        else:
            incorrect_guesses += 1 # This will increase the incorrect guess counter
            print(f"Sorry, '{guess}' is not in the word.")
            print(f"Incorrect guesses left: {max_incorrect_guesses - incorrect_guesses}") # This will display remaining incorrect guesses
        
        if all(letter in guessed_letters for letter in word): # This will check if all letters have been guessed
            print(f"Congratulations! You guessed the word '{word}' correctly.")
            break
    else:
        print(f"Game Over! You ran out of guesses. The word was '{word}'.")

if __name__ == "__main__":
    hangman() # Run the hangman game if the script is executed directly
