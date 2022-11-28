# Step 5
#from replit import clear
import random

# TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
word_list = []
from hangman_words import word_list
from hangman_art import stages

# Delete this line: word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

# TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
from hangman_art import logo

print(logo)

# Testing code
print("")
print(f"Welcome to game HANGMAN!\nYou have total {lives} lives.\nGood luck!")
# Create blanks
display = []
for _ in range(word_length):
    display += "_"
print(" ")
print(*display)
while not end_of_game:
    guess = input("\nGuess a letter: \n").lower()
  #  clear()
    # TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(" ")
        print(f"You've already guessed {guess}")
    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #        print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    # Check if user is wrong.
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        # TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose. Bhahahahhauahuahau\n")

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("Nice! You win.\n")

    # TODO-2: - Import the stages from hangman_art.py and make this error go away.
    print(stages[lives])
