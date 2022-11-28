from art import logo
from random import randint
import clear

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thing of a number between 1 and 100.")
computer_number = randint(0, 100)

gamewin = False
lives = 0
level = input("Choose a difficulty. Type 'easy' or 'hard': ")


def levels():
    if level == "easy":
        global lives
        lives = 10
        return lives
    elif level == "hard":
        lives = 5
        return lives


levels()
while not gamewin:
    if lives <= 0:
        print("You run out of all attempts. You lose.")
        gamewin = True
    else:
        def game():
            global lives
            global gamewin
            print(f"You have {lives} attempts remaining to guess the number.")
            user_number = int(input("Make a guess: "))
            if user_number == computer_number:
                print("You guessed right number! You win!")
                gamewin = True
                return gamewin
            elif user_number < computer_number:
                print("\n   Too low.\n")
                # global lives
                lives = lives - 1
                return lives
            elif user_number > computer_number:
                print("\n   Too high.\n")
                lives = lives - 1
                return lives
            return


        game()

# Include an ASCII art logo.
# Allow the player to submit a guess for a number bhetween 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
