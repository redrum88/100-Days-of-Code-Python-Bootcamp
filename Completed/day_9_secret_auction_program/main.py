#from replit import clear
from art import logo

print(logo)
print("Welcome to the secret auction program.")

bids = {}
finish = False


def max_bidder(bid_record):
    max_bid = 0
    winner = ""
    for bidder in bid_record:
        bid_amount = bid_record[bidder]
        if bid_amount > max_bid:
            max_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with bid of £{max_bid}")


while not finish:
    name = input("What is your name? ")
    price = int(input("What's your bid? £"))
    bids[name] = price
    question = input("Are there any other bidders? Type 'yes' or 'no'\n")
    if question == "no":
        finish = True
        max_bidder(bids)
    elif question == "yes":
        pass
        #clear()