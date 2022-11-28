############### Blackjack Project #####################
import random
from art import logo

# from replit import clear

print(logo)


def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(computer_score, user_score):
    if user_score > 21 and computer_score > 21:
        return "\nYou went over. You lost"
    elif computer_score == user_score:
        return "\nIts a draw!"
    elif computer_score == 0:
        return "\nYou lost! Computer have blackjack"
    elif user_score == 0:
        return "\nYou won with blackjack!"
    elif user_score > 21:
        return f"\nToo many cards! You lost your score is {user_score}"
    elif computer_score > 21:
        return f"\nYou win with {user_score} against computer: {computer_score}"
    elif user_score > computer_score:
        return f"\nYou win with {user_score} against computer: {computer_score}"
    else:
        return f"\nYou lost with {user_score} against computer: {computer_score}"


def play():
    print(logo)
    user_cards = []
    computer_cards = []
    gameover = False
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    print(f"YOUR CARDS: {user_cards}")
    print(f"COMPUTER CARDS: {computer_cards[_]}")

    while not gameover:

        #  print(f"SHOW WITH HIDDEN USER CARDS: {user_cards}")
        #  print(f"SHOW WITH HIDDEN COMPUTER CARDS: {computer_cards}")

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"\n   Your cards: {user_cards}, current score: {user_score}\n")
        #   print(f"   Computer first card: {computer_card[_]}\n")
        # Look up the sum() function to help you do this.
        if user_score == 0 or computer_score == 0 or user_score > 21:
            gameover = True
        else:

            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                gameover = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    #   print(f"\nYour current score: {user_score}\n")
    #   print(f"Computer current score: {computer_score}\n")
    #  clear()
    # print(logo)
    print(f"    Your final hand: {user_cards}, final score: {user_score}")
    print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(computer_score, user_score))
    # Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.


while input("\nDo you want to play a game of Blackjack? Type 'y' or 'n'") == "y":
    # clear()
    play()
# Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
